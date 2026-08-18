# Evidence Trail

The reconstruction is grounded in the private historical archive `ChrisCanadian/Nexus-Historic`, primarily the imported `setup_chrisai/Nexus_synapse` tree.

## Primary anchors

### August 26, 2025 settings

`setup_chrisai/Nexus_synapse/engine2_1/config/settings.py`

Surviving settings define:

- `PERSONAS_DIR`
- `MEMORY_DIR`
- `SYSTEM_PERSONA = PERSONAS_DIR / "system_persona.txt"`
- `USER_PERSONA = PERSONAS_DIR / "user_persona.txt"`
- `MEMORY_FILE = MEMORY_DIR / "memory.json"`
- `LEARNING_DATA = DATA_DIR / "learning_data.json"`
- local application paths and a Stable Diffusion path
- learning and vocabulary settings

This is the strongest surviving direct description of the flat-file layout.

### Persona migration code

`setup_chrisai/Nexus_synapse/engine2_1/persona/personality_manager.py`

Later code retains migration paths that:

- read `user_persona.txt`;
- read `system_persona.txt`;
- extract structured preferences/traits from the text;
- save into `personality_bank.json` and an evolution-history file.

That migration trail proves the text personas preceded the structured PersonalityBank representation.

### Surviving early persona update test

`setup_chrisai/persona_update_test.py`

This preserved test records the flat persona update surface as:

- `helpful_persona.txt`;
- `jarvis_persona.txt`;
- `user_persona.txt`;
- `persona_history.json`;
- `learning_data.json`.

It also records update/append operations, AI-suggested changes with user confirmation, explicit user updates, and interaction-driven learning. The exact original implementation is not preserved in the curated tree, so this reconstruction implements only the directly supportable flat-file update/append + history behavior rather than inventing the missing suggestion pipeline.

### Legacy JSON removal record

`setup_chrisai/Nexus_synapse/LEGACY_JSON_REMOVAL_COMPLETE.md`

This October 29 migration record documents later JSON stores (`medium_term.json`, `knowledge_base/base.json`) being removed in favor of SQL-backed state. Those files belong to a later transition stage and are therefore not treated as the earliest ChrisAI core.

### Pre-migration feature snapshot

`setup_chrisai/Nexus_synapse/tests/pre_migration_snapshots/unique_features_report.json`

The October 4 snapshot preserves several earlier behaviors, including:

- simple case-insensitive first-match emotion mapping;
- a short-term RAM memory tier;
- later medium-term JSON / SQLite / JSON-knowledge tiers;
- project JSON persistence.

The reconstruction uses the preserved simple emotion mapping but does not import the later multi-tier database architecture.

### August vocabulary manager

`setup_chrisai/Nexus_synapse/vocabulary_manager.py`

This file is timestamped August 26 and preserves the word-complexity simplification logic and technical-term allowlist used as the basis for the reconstructed vocabulary adapter.

## Important limitation

The archive was imported from a local source tree whose original Git history was not recoverable. Dates embedded in source/configuration and migration records are useful evidence, but the reconstruction cannot claim a byte-for-byte historical checkout.
