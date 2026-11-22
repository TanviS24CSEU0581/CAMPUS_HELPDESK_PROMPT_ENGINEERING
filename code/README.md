# Code

Code for the Campus Helpdesk Assistant.

| File | What it does |
|---|---|
| `app.py` | Streamlit dashboard. It finds the policy sections closest to a question (TF-IDF), builds the prompt for the chosen version, and checks that the quotes and section IDs in a pasted ChatGPT reply come from the retrieved text. |
| prompt_retrieval.py] | Colab script that reads `policy.txt` and `questions.csv`, retrieves the top 3 sections for each question, and creates a ready-to-paste prompt for every version (`ready_vX.csv`). |

## Run the dashboard
1. `pip install -r requirements.txt` (the file is in the top folder)
2. `python3 -m streamlit run code/app.py`

The dashboard does not call any model and uses no API key. Prompts are pasted into ChatGPT by hand.
