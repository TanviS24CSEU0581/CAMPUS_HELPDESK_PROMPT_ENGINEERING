# CAMPUS_HELPDESK_PROMPT_ENGINEERING

**Team:** Promptors | **Team ID:** PE-B37-02 | **Course:** SCSE4041 Prompt Engineering

## What this project does
A prompt-engineering project that tests how to make a language model answer student questions about **fees, exams, attendance and hostel** using **only official policy text**. The assistant should:
1. answer from the retrieved policy sections,
2. quote the exact source sentence with its section ID, and
3. refuse, and name the right office, when the answer is not in the documents.

It gives information only. The official office has the final word.

## How it works
Question -> keyword retrieval (TF-IDF) -> top 3 policy sections -> prompt template (`{ctx}`, `{q}`) -> ChatGPT -> answer with source and quote, or a refusal -> scored in a Google Sheet.

- **Knowledge base:** 104 policy sections with IDs (for example EXAM-1.2)
- **Model:** ChatGPT (GPT-6), used through the chat interface. No API key is used anywhere in this repo.
- **Retrieval:** Python and scikit-learn (Google Colab script and the dashboard).
- **Dashboard:** Streamlit page that retrieves sections, builds the prompt for a chosen version, and checks a pasted reply (quotes and section IDs must appear in the retrieved text).

## Prototype link
https://campusappdeskpromptengineering-99vagx6iupqbsfxtxd5wjj.streamlit.app/<img width="468" height="22" alt="image" src="https://github.com/user-attachments/assets/b79bae14-8acd-4077-b700-d6cdec78980b" />

**How to try it** (no login needed):
1. Open the link and choose a prompt version in the sidebar (v5 is the final one).
2. Ask a question, for example "How long are end term exams?".
3. Copy the generated prompt into a new ChatGPT chat.
4. Paste ChatGPT's reply back into the page to see the automatic quote and source checks.

Answers are produced by ChatGPT manually. The page does not call a model. If the app shows a "wake up" button, click it and wait a minute.

## Folder structure
| Folder or file | What is inside |
|---|---|
| `DOCS/` | `policy.txt` (policy sections with IDs) and the sources list |
| `prompts/` | Prompt versions `v1.txt` to `v5.txt` |
| `tests/` | The 40 test questions, generated prompts and scored results |
| `code/` | Streamlit dashboard (`app.py`) and the Colab retrieval script |
| `requirements.txt` | Libraries for the dashboard |
| `CHANGELOG.md` | Dated list of changes since Milestone 1 |

## Prompt versions
| Version | Idea | Owner | Score (out of 40) |
|---|---|---|---|
| v1 | Baseline: answer only from the text, fixed format | Tanvi | 35 |
| v2 | Strict numbered rules, injection rule | Yashika | 34 |
| v3 | Few-shot examples and a verify-the-quote step | Suhani | 35 |
| v4a | Topic classifier and a refusal that names the office | Samriddhi | 36 |
| v4b | Rewriting of messy questions, plain-language answers | Kratika | 36 |
| v5 | Built on v4a, plus rules for advice, completeness and no unrelated sections | Tanvi | 37 |

## How to reproduce the tests
1. Run the Colab script with `policy.txt`, `questions.csv` and a prompt file. It creates `ready_vX.csv` with a finished prompt for each question.
2. Paste each prompt into a **new ChatGPT chat**, and paste the reply unedited into the scoring sheet.
3. Score each reply (0 or 1): correct, citation right, refusal right.

## Results
- Best earlier versions scored 37/40; one-question differences are within run-to-run variation (one run per question).
- Q13, Q24 and Q34 failed in every version because the needed policy section was not retrieved. Q40 (advice stated as a requirement) was fixed only in v5.

## Known limitations
- Keyword retrieval can miss the right section.
- One manual run per question, scored by team members.
- v5 rules were written after seeing results on the same 40 questions.

## Team
| Name | Enrollment no. | Main task |
|---|---|---|
| Tanvi Chauhan | S24CSEU0581 | Lead, Colab retrieval script, v1 and v5, error analysis |
| Suhani Singh | S24CSEU0566 | Policy documents, v3 |
| Samriddhi Vishnoi | S24CSEU0455 | Questions Q1-Q20, v4a, scoring |
| Kratika Gupta | S24CSEU1860 | Questions Q21-Q40, v4b, results table |
| Yashika Mann | S24CSEU1888 | v2, Streamlit dashboard, robustness tests |

## Notes
- No personal data or API keys are stored in this repo.
- Policy sources and collection dates are in `DOCS/README.md`.
