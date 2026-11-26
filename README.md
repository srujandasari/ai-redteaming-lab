# Automated AI Red-Teaming Lab

Repeatable security testing of a fictional LLM customer-support chatbot ("Aria" for Northwind Retail), running locally on Ollama (llama3.2). The loop is: attack, fix, retest, keep the evidence.

> Everything here is fictional and runs against a system I own. The chatbot's secret was a fake API key planted as a leak target.

## What I built
- `app/chatbot.py`: the chatbot, with a hidden system prompt.
- `app/aria_generator.py`: adapter so Garak attacks the chatbot, not the bare model.
- `app/promptfoo_provider.py` and `promptfooconfig.yaml`: Promptfoo tests aimed at leaking the key and the system prompt.
- `results_before.json` / `results_after.json`: raw Promptfoo results before and after the fix.

## Tools
Ollama, Garak (NVIDIA), Promptfoo. PyRIT (Microsoft) is installed but not used yet planning for version 2 of this project.

## Findings

| # | Finding | OWASP LLM | Result |

| 1 | A "developer debugging" request made the bot print its system prompt | LLM07 System Prompt Leakage | Confirmed (before fix) |
| 2 | Fake API key extraction (direct, poem, completion, translation, base64) | LLM02 Sensitive Information Disclosure | Not leaked in any run |

## Fix and retest
- Removed the secret from the system prompt entirely.
- Added a rule to refuse requests to repeat, translate or reveal the instructions.
- Reran the same 6 tests.

| Run | Passed | Failed |

| Before fix | 5 | 1 |
| After fix | 6 | 0 |

## Limitations
- 6 tests on a small 3B model, so results vary between runs. One clean run is not proof.
- Garak's `promptinject` scan against the chatbot, with 0 key leaks.
