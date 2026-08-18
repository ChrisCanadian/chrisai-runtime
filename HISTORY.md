# Historical Scope

ChrisAI was the early executable AI system that preceded the later Nexus Synapse architecture.

This reconstruction targets the **flat-file era** evidenced by the surviving August 26, 2025 configuration and later migration code. At that point, persona, memory, and learning state were represented through ordinary files rather than the centralized SQL-backed runtime state used later.

The repository deliberately stops before the later architecture became defined by database-backed state and Structured State Reconstruction.

## Evidence-supported progression

1. **Flat-file ChrisAI**
   - `system_persona.txt`
   - `user_persona.txt`
   - `memory.json`
   - `learning_data.json`
   - local model/runtime orchestration

2. **Structured file transition**
   - migration of text personas into structured JSON PersonalityBank data;
   - medium-term JSON and JSON knowledge-base state;
   - increasingly elaborate memory and learning systems.

3. **Database consolidation**
   - personality, memory, projects, tasks, and interaction history moved toward SQL-backed stores.

4. **Later Nexus Synapse**
   - runtime-owned structured state reconstruction and the modern architecture.

This repository reconstructs stage 1 only, while documenting later evidence only where it helps establish what stage 1 actually contained.
