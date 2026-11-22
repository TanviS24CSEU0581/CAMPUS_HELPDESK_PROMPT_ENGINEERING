# Changelog

Changes since Milestone 1 (submitted 9-11 October 2026).

## 2026-11-22
- Final checks: links tested in incognito window, PDFs prepared.
- Added content in README.md and this changelog. (Tanvi)

## 2026-11-21
- Added Streamlit dashboard (`code/app.py`) and `requirements.txt`: retrieves policy sections, builds the prompt for the chosen version, and checks the pasted reply. (Yashika)
- Deployed the dashboard for the prototype link.
- Added `prompts/v5.txt`: built on v4a, with rules that advice is not a requirement, that all stated conditions are included, that unrelated sections are not added, and that refusals contain only the refusal sentence. (Tanvi)
- Ran v5 on the 40 questions and scored it. (Tanvi)
  
## 2026-11-20/21
- Ran and scored v1 to v4b on the 40 questions. (all members)
- Failure analysis: Q13, Q24 and Q34 failed in every version due to retrieval misses; Q40 failed until v5. (Tanvi)

## 2026-11-13
- Added prompt versions: v4a (Samriddhi), v4b (Kratika).
  
## 2026-11-1
- Added prompt versions: v1 (Tanvi), v2 (Yashika), v3 (Suhani).
- Wrote the 40 test questions with expected answers, including tricky and not-in-the-documents cases. (Samriddhi: Q1-Q20, Kratika: Q21-Q40)
- Added the Colab retrieval script that fills each prompt with the top 3 policy sections. (Tanvi)

## 2026-10-30
- Added `policy.txt` with section IDs and `docs/README.md` with sources. (Suhani) [FILL: confirm date]
- Decided to use ChatGPT only for all test runs. (team)

## 2026-10-29
- Created the repository and the folders (docs, prompts, tests, code). (Tanvi)
- Created the shared Google Sheet for test results. (Tanvi)

## Earlier changes after faculty feedback
- Added tricky "not in the documents" questions and a disclaimer after feedback from Asst. Prof. Deepali Vishnoi (Asian Business School). 
