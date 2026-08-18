# ChrisAI Actual Component Inventory

This inventory separates what can be reconstructed confidently from what belongs to later Nexus/Engine2_1 eras.

| Component | Disposition | Evidence-supported reason |
|---|---|---|
| `system_persona.txt` | RECONSTRUCT | August 26 settings define `SYSTEM_PERSONA`; later migration code reads the text file. |
| `user_persona.txt` | RECONSTRUCT | August 26 settings define `USER_PERSONA`; later migration code reads and parses it. |
| `helpful_persona.txt` / `jarvis_persona.txt` | RECONSTRUCT AS OPTIONAL LAYERS | Surviving early persona-update test explicitly lists both files as update targets. Exact original contents/combination order are not preserved. |
| `persona_history.json` | RECONSTRUCT | Surviving early persona-update test explicitly identifies it as the persona change log. |
| `memory.json` | RECONSTRUCT | August 26 settings define `MEMORY_FILE = MEMORY_DIR / "memory.json"`. |
| `learning_data.json` | RECONSTRUCT | August 26 settings define `LEARNING_DATA = DATA_DIR / "learning_data.json"`. |
| JSON load/save helpers | KEEP / ADAPT | Surviving helpers implement JSON load/save and file backups. |
| Vocabulary simplification | KEEP / ADAPT | Surviving August 26 VocabularyManager contains explicit complexity mappings and preserved technical terms. Exact placement in the response hot path is not asserted. |
| Simple emotion mapping | RECONSTRUCT | October 4 pre-migration snapshot records the earlier hardcoded emotion map and first-match-wins behavior. |
| In-memory session state | RECONSTRUCT | Later migration snapshot records short-term RAM memory; dispatcher also maintains conversation history in process memory. |
| Direct prompt construction | RECONSTRUCT | Later prompt module says PromptBuilder logic migrated into ResponseEngine; pre-SSR architecture therefore constructed prompts directly rather than through SSR. |
| Local model call | RECONSTRUCT | Historical configuration and later model-dispatch material establish local-model inference as a runtime responsibility. |
| Stable Diffusion integration | DOCUMENT ONLY | August 26 settings contain `SD_PATH`, proving a local integration point existed, but not enough evidence is used here to reconstruct its exact early runtime contract. |
| Personal stream overlay | EXCLUDE | Personal precursor project; intentionally outside the ChrisAI runtime release scope. |
| Structured `personality_bank.json` | TOO LATE FOR CORE | Later PersonalityManager code explicitly migrates from `.txt` files into structured JSON. |
| `medium_term.json` / JSON knowledge base | TOO LATE FOR CORE | October migration docs describe these as legacy file stores removed during database consolidation. |
| Separate SQLite `memory.db` | TOO LATE FOR CORE | Pre-migration snapshot records this as a later multi-tier memory stage. |
| Central `memorybanks.db` / production DB | EXCLUDE | Database-era Nexus/Engine2_1 architecture. |
| RAG / Chroma / smart retrieval | EXCLUDE | Later memory architecture, not flat-file ChrisAI. |
| SSR | EXCLUDE | Explicitly later architecture. |
| Senate / Thinker / modern modes / gauges | EXCLUDE | Modern Nexus systems, not ChrisAI. |
| Modern tool orchestration | EXCLUDE | Later architecture; exact early ChrisAI tool boundary is not reconstructed here. |

## Reconstruction rule

A feature is included only when the surviving archive supports both:

1. that the responsibility existed in the target era; and
2. enough of its shape survives to implement a conservative executable representation.

If either condition is weak, the feature is documented rather than invented.
