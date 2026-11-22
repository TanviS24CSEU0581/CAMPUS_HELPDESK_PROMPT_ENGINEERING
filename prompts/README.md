# Prompts

Prompt versions for the Campus Helpdesk Assistant. Each file has two placeholders: `{ctx}` (the retrieved policy sections) and `{q}` (the student's question). The Colab script fills them in.

| File | What changed | Owner | Score (out of 40) |
|---|---|---|---|
| `v1.txt` | Baseline: answer only from the text, Answer/Source/Quote format, fixed refusal sentence | Tanvi | 35 |
| `v2.txt` | Numbered strict rules, injection rule, multi-section rule | Yashika | 34 |
| `v3.txt` | Few-shot examples and a verify-the-quote step | Suhani | 35 |
| `v4a.txt` | Topic classifier and a refusal that names the right office | Samriddhi | 36 |
| `v4b.txt` | Rewriting of messy questions and plain-language answers | Kratika | 35 |
| `v5.txt` | Final prompt: built on v4a, plus rules for advice, completeness and no unrelated sections | Tanvi | 37 |


