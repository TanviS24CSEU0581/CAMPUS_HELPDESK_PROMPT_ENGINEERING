# Tests

Test data and results used to compare the prompt versions.

## Question types
- **answerable:** the answer is in `policy.txt`.
- **tricky:** looks answerable but is not in the documents, or has conflicting rules.
- **unanswerable:** not in the documents. The expected answer is a refusal.

## How the tests were run
Each prompt was pasted into a fresh ChatGPT chat once, and the reply was pasted unedited into the scoring sheet. A teammate who did not run that version scored it.
