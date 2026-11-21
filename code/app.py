import os
import re
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Campus Helpdesk Assistant", page_icon="🎓", layout="wide")
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# find files anywhere in the project
paths = {}
for root, dirs, fs in os.walk(base):
    if "venv" in root or ".git" in root:
        continue
    for f in fs:
        if f in ("policy.txt", "questions.csv") or (f.startswith("v") and f.endswith(".txt")):
            paths[f] = os.path.join(root, f)

vfiles = sorted(f for f in paths if f.startswith("v") and f.endswith(".txt"))
if "policy.txt" not in paths or not vfiles:
    st.error("policy.txt or the prompt files (v1.txt ... v5.txt) were not found in the project folder.")
    st.stop()

# load policy sections
ids, txt = [], []
for line in open(paths["policy.txt"], encoding="utf-8").read().splitlines():
    if " | " in line:
        a, b = line.split(" | ", 1)
        if "-" in a and " " not in a:
            ids.append(a.strip())
            txt.append(b.strip())
vec = TfidfVectorizer(stop_words="english").fit(txt)
mat = vec.transform(txt)

# sidebar
st.sidebar.title("🎓 Campus Helpdesk")
st.sidebar.caption("Prompt-engineering prototype")
start = vfiles.index("v5.txt") if "v5.txt" in vfiles else len(vfiles) - 1
ver = st.sidebar.selectbox("Prompt version", vfiles, index=start)
n = st.sidebar.slider("Policy sections to retrieve", 3, 5, 3)
st.sidebar.metric("Policy sections loaded", len(ids))
st.sidebar.info("Answers are written by ChatGPT. You copy the prompt into ChatGPT and paste the reply back here.")
st.sidebar.warning("Known limitation: keyword search can miss the right section, especially when the question uses different words from the policy.")
tmpl = open(paths[ver], encoding="utf-8").read()

st.title("🎓 Campus Helpdesk Assistant")
st.caption("Answers only from official policy text. Information only: the official office has the final word.")

tab1, tab2 = st.tabs(["Ask a question", "How it works"])

with tab1:
    if "q" not in st.session_state:
        st.session_state.q = ""
    st.write("Try an example:")
    ex = ["How long are end term exams?",
          "Can my parents come inside my hostel room?",
          "What is the supplementary exam fee?",
          "What is on the mess menu today?"]
    cols = st.columns(4)
    for c, e in zip(cols, ex):
        if c.button(e, use_container_width=True):
            st.session_state.q = e
    q = st.text_input("Your question", key="q", placeholder="Ask about fees, exams, attendance or hostel")

    if st.button("Find answer", type="primary") and q.strip():
        sc = cosine_similarity(vec.transform([q]), mat)[0]
        top = sc.argsort()[::-1][:n]
        st.session_state.top = [(ids[i], txt[i], float(sc[i])) for i in top]
        ctx = "\n".join("[" + ids[i] + "] " + txt[i] for i in top)
        st.session_state.prompt = tmpl.replace("{ctx}", ctx).replace("{q}", q)
        st.session_state.asked = q

    if "top" in st.session_state:
        st.divider()
        st.subheader("1. Policy sections found")
        st.caption("For: " + st.session_state.asked)
        if max(s for a, b, s in st.session_state.top) == 0:
            st.warning("No section matched the question. A good assistant should refuse here.")
        for sid, stxt, s in st.session_state.top:
            with st.expander(sid + "   |   match " + str(round(s, 2)), expanded=True):
                st.write(stxt)
                st.progress(min(max(s, 0.0), 1.0))

        st.subheader("2. Prompt for ChatGPT (" + ver + ")")
        st.caption("Use the copy icon on the box, then paste it into a new ChatGPT chat.")
        st.code(st.session_state.prompt, language=None)
        st.link_button("Open ChatGPT", "https://chatgpt.com")

        st.subheader("3. Paste ChatGPT's reply")
        reply = st.text_area("Reply", height=160, key="reply", label_visibility="collapsed")
        if reply.strip():
            if "could not find this in the official documents" in reply.lower():
                st.warning("The assistant refused:\n\n" + reply)
            else:
                st.success(reply)
                ctxn = re.sub(r"\s+", " ", " ".join(b for a, b, s in st.session_state.top).replace("’", "'")).lower()
                clean = reply.replace("“", '"').replace("”", '"')
                quotes = re.findall(r'"([^"]{15,}?)"', clean)
                st.write("**Automatic checks**")
                if not quotes:
                    st.error("No quoted sentence found in the reply.")
                for qt in quotes:
                    qn = re.sub(r"\s+", " ", qt.replace("’", "'")).lower()
                    if qn in ctxn:
                        st.success("✅ Quote found in the retrieved sections: " + qt[:70] + "...")
                    else:
                        st.error("⚠️ Quote NOT found in the retrieved sections (reworded or made up?): " + qt[:70] + "...")
                cited = set(re.findall(r"[A-Z]+-\d+\.\d+", reply))
                got = set(a for a, b, s in st.session_state.top)
                for sid in sorted(cited):
                    if sid in got:
                        st.success("✅ " + sid + " was retrieved")
                    else:
                        st.error("⚠️ " + sid + " was cited but not retrieved")


with tab2:
    st.subheader("How it works")
    st.markdown("""
1. **Retrieve:** a keyword search (TF-IDF) finds the policy sections closest to the question.
2. **Build the prompt:** the chosen prompt version is filled with those sections and the question.
3. **Answer:** ChatGPT answers only from those sections, quotes the source, or refuses.
4. **Check:** this page checks that every quote and section ID in the reply really came from the retrieved text.
5. **Evaluate:** we scored every prompt version on the same 40 questions.
""")
    st.warning("The checks only compare text. They do not prove that an answer is correct.")
