# ChrisAI Runtime v0.1.0 Release Acceptance

This file records the closure criteria for the public ChrisAI historical reconstruction.

The release is intentionally small. It is an executable historical reference for the flat-file ChrisAI era, not a lightweight modern Nexus Synapse runtime.

## Acceptance criteria

- [x] Installable Python package (`pip install -e .`).
- [x] Console entry point (`chrisai`).
- [x] Module entry point (`python -m chrisai_runtime`).
- [x] Deterministic dependency-free test model for first-run validation.
- [x] Ollama-compatible local model adapter.
- [x] Flat persona files and persona change history.
- [x] Bounded JSON conversation memory.
- [x] JSON interaction/learning persistence.
- [x] Historical rule-based emotion detector.
- [x] Historical vocabulary utility preserved without inventing an unsupported hot-path role.
- [x] Direct prompt assembly from persona, recent memory, detected emotion, and current input.
- [x] Automated tests for the reconstructed responsibilities.
- [x] CI across Python 3.10, 3.11, and 3.12.
- [x] Installed-package CLI smoke check in CI.
- [x] Scope and provenance boundaries documented.

## Optional live-model verification

A live Ollama server is deliberately not required for CI because the repository must remain reproducible without downloading a model. To exercise the real adapter locally:

```bash
ollama serve
ollama pull qwen2.5:3b

# macOS/Linux
export CHRISAI_MODEL_BACKEND=ollama
export CHRISAI_OLLAMA_URL=http://localhost:11434
export CHRISAI_MODEL=qwen2.5:3b
printf "Hello\n/quit\n" | python -m chrisai_runtime
```

PowerShell:

```powershell
$env:CHRISAI_MODEL_BACKEND="ollama"
$env:CHRISAI_OLLAMA_URL="http://localhost:11434"
$env:CHRISAI_MODEL="qwen2.5:3b"
"Hello`n/quit" | python -m chrisai_runtime
```

A successful live check demonstrates the transport adapter only. It does not change the historical-evidence classification of the reconstructed runtime.

## Freeze rule

After v0.1.0, the historical core should remain frozen except for:

1. bug fixes;
2. packaging or compatibility fixes;
3. corrections supported by newly recovered historical evidence; or
4. documentation/provenance clarification.

Modern Nexus features should not be backported into this repository merely to make ChrisAI more capable. Doing so would erase the architectural boundary this reconstruction exists to preserve.
