# Attribution and Provenance

## Project authorship

**ChrisAI** was designed and built by **Christopher Campbell** as the early flat-file AI runtime that later evolved into Nexus Synapse.

This repository is a **historically grounded reconstruction** of that early runtime. It is not a claim that every line in this repository existed verbatim in August 2025. Reconstruction decisions are limited to what can be supported by surviving historical source files, dated configuration, migration code, tests, and pre-migration documentation preserved in `ChrisCanadian/Nexus-Historic`.

## AI-assisted development

Christopher Campbell is the project author and human maintainer. AI coding/review tools were used as development assistants during both the original project history and the preparation of this reconstruction. Those tools assisted with tasks such as code generation, review, explanation, and reconstruction from surviving artifacts; they are not represented as authors, owners, or licensors of ChrisAI.

Where historical evidence is incomplete, this repository prefers an explicit reconstruction note or an unknown state rather than inventing provenance.

## Historical provenance labels

When describing historical components, use the following evidence language where applicable:

- **VERIFIED** — directly supported by surviving source, tests, or dated artifacts.
- **CONFIGURED_ONLY** — configuration proves an integration point existed, but surviving evidence does not prove the full runtime path was exercised.
- **INFERRED_FROM_RUNTIME_CONFIG** — a limited architectural inference supported by runtime/configuration evidence, but not directly observed in preserved execution evidence.
- **LEGACY_UNKNOWN** — the artifact or behavior is known to have existed, but exact implementation/provenance is no longer recoverable.
- **NOT_AVAILABLE** — the surviving archive does not contain enough evidence to make the claim.

These labels are intended to keep the historical record inspectable without turning inference into fact.

## External models, libraries, and services

This repository does **not** claim authorship or ownership of third-party models, libraries, runtimes, services, or protocols used by or referenced by ChrisAI.

In particular, model names and provider/runtime names are descriptive interoperability references only. The configurable Ollama-compatible adapter in this reconstruction is an interface to external model infrastructure; no model weights are distributed by this repository.

Third-party dependencies remain subject to their own licenses and terms. The Apache-2.0 license in this repository applies only to material that Christopher Campbell has the right to license here.

## Nexus Synapse boundary

The Apache-2.0 license and attribution in this repository apply to the public **ChrisAI historical reconstruction only**.

They do **not** publish, relicense, transfer, or imply rights to private Nexus Synapse runtime code, production data, protected prompts, database schemas, private retrieval/context-selection logic, credentials, deployment configuration, or other material outside this repository.

ChrisAI is part of the historical lineage of Nexus Synapse, but this repository should not be described as the current Nexus runtime or as a complete implementation of modern Nexus architecture.

## Collaboration and third-party lineage

References to collaborators, external projects, research, or compatible systems do not imply shared authorship, shared ownership, merged intellectual property, or reciprocal licensing unless an explicit written contribution or license states otherwise.

Compatibility is not ownership, and citation is not transfer of authorship.

## Citation

For informal citation:

> Campbell, Christopher. *ChrisAI Runtime — Historical Reconstruction*. 2026. GitHub: `ChrisCanadian/chrisai-runtime`.

For technical claims about the reconstruction, cite the repository together with the relevant evidence document under `docs/` whenever possible.
