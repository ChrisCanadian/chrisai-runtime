# ChrisAI Runtime — Historical Reconstruction

[![CI](https://github.com/ChrisCanadian/chrisai-runtime/actions/workflows/ci.yml/badge.svg)](https://github.com/ChrisCanadian/chrisai-runtime/actions/workflows/ci.yml)

This repository reconstructs the **flat-file ChrisAI runtime architecture that preceded Nexus Synapse**.

It is intentionally **pre-database** and **pre-SSR**. It is not a stripped version of modern Nexus Synapse, and it does not reproduce later database schemas, Structured State Reconstruction, Senate/Thinker systems, modern memory retrieval, production tool execution, or private Nexus internals.

The reconstruction is based on surviving historical code, dated configuration, migration code, and pre-migration snapshots preserved in `ChrisCanadian/Nexus-Historic`. The original early Git history was not recoverable, so this repository is a **historically grounded reconstruction**, not a byte-for-byte August 2025 checkout.

## What this reconstructs

The surviving August 26, 2025 settings identify the early storage layout as flat files, while a surviving early persona-update test records additional persona files and the persona change log:

```text
personas/
  system_persona.txt
  user_persona.txt
  helpful_persona.txt   # recorded by surviving early persona test
  jarvis_persona.txt    # recorded by surviving early persona test
  persona_history.json  # persona change log
memory/
  memory.json
data/
  learning_data.json
```

The early runtime shape reconstructed here is:

```text
User input
   ↓
Input handling
   ├─ simple emotion detection
   └─ vocabulary utility available to the runtime
   ↓
Flat persona files
   ├─ system_persona.txt
   ├─ user_persona.txt
   ├─ helpful_persona.txt
   └─ jarvis_persona.txt
   ↓
Recent conversation memory
   ↓
Direct prompt construction
   ↓
Local model adapter
   ↓
Response
   ├─ append memory.json
   └─ append learning_data.json
```

## Deliberate scope

Included:
- flat text persona files, including optional Helpful/Jarvis layers recorded by the surviving early persona test;
- persona file update/append operations with a JSON change log;
- JSON conversation memory;
- JSON learning/event persistence;
- simple rule-based emotion detection preserved from the historical pre-migration snapshot;
- the surviving August 2025 vocabulary simplification utility, exposed without claiming an exact hot-path placement that the archive no longer proves;
- direct prompt construction;
- configurable local Ollama-style HTTP inference;
- a deterministic test model for local testing.

Not included:
- the personal streaming-overlay project;
- centralized SQL personality or memory state;
- SSR;
- RAG / vector retrieval;
- later PersonalityBank database structures;
- Senate, Thinker, modes, gauges, or modern Nexus governance;
- production credentials, user data, logs, databases, or machine-specific paths;
- later multimodal/tool systems whose exact early ChrisAI form cannot be reconstructed confidently from the surviving evidence.

## Run locally

```bash
python -m venv .venv
# activate the environment
pip install -e .
python -m chrisai_runtime
```

By default the runtime uses a deterministic local test model so the reconstruction can be exercised without any external dependency.

To use an Ollama-compatible local endpoint:

```bash
export CHRISAI_MODEL_BACKEND=ollama
export CHRISAI_OLLAMA_URL=http://localhost:11434
export CHRISAI_MODEL=qwen2.5:3b
python -m chrisai_runtime
```

On PowerShell:

```powershell
$env:CHRISAI_MODEL_BACKEND="ollama"
$env:CHRISAI_OLLAMA_URL="http://localhost:11434"
$env:CHRISAI_MODEL="qwen2.5:3b"
python -m chrisai_runtime
```

## Persona files

The exact original early persona prose is not preserved in the curated archive. The files in `src/chrisai_runtime/defaults/` are therefore **safe reconstruction templates**, not claimed originals.

The historical migration code does establish that the old user persona text contained free-form descriptions that were later parsed for concepts such as step-by-step guidance, detail preference, task spiraling, warmth, curiosity, creativity, and philosophy. The old system persona was later parsed for traits such as empathy, professionalism, wit, directness, analytical style, supportiveness, adaptability, intelligence, and helpfulness.

The surviving early persona-update test separately records `helpful_persona.txt`, `jarvis_persona.txt`, `user_persona.txt`, `persona_history.json`, and `learning_data.json` as files involved in persona updates and learning. Because the exact original combination order is not preserved, the Helpful/Jarvis files are treated here as optional additive persona layers rather than claimed exact historical precedence rules.

## Evidence

See [`docs/ACTUAL_COMPONENT_INVENTORY.md`](docs/ACTUAL_COMPONENT_INVENTORY.md) and [`docs/EVIDENCE_TRAIL.md`](docs/EVIDENCE_TRAIL.md).

Historical claims should remain distinguishable as directly verified, configuration-supported, inferred, legacy-unknown, or unavailable rather than silently filling gaps in the surviving record. See [`ATTRIBUTION.md`](ATTRIBUTION.md) for the provenance labels and authorship policy used by this reconstruction.

## Authorship and attribution

**Christopher Campbell** is the human author and maintainer of ChrisAI and this historical reconstruction.

AI coding and review tools were used as development assistants during the project history and reconstruction work. They are not presented as authors, owners, or licensors of ChrisAI. External models, libraries, providers, services, and protocols remain subject to their own licenses and ownership.

Compatibility, citation, or collaboration with another project does **not** imply shared authorship, shared IP, ownership transfer, or reciprocal licensing.

See [`ATTRIBUTION.md`](ATTRIBUTION.md) and [`NOTICE`](NOTICE) for the full attribution and provenance boundary.

## License

Licensed under the **Apache License 2.0**. See [`LICENSE`](LICENSE).

The license applies to this public historical reconstruction. It does not imply publication or licensing of private Nexus Synapse runtime code that is outside this repository.

## Status

`v0.1.0-reconstruction-candidate`

The code is deliberately small so each reconstructed responsibility can be traced back to surviving historical evidence. It should be treated as an executable historical reference, not evidence that every line existed in exactly this form in August 2025.
