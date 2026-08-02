# Supporting proof evidence — P1-02

Verified: 2026-08-02

## Scope

This record supports three secondary recruiter-facing cases:

1. SPINE freshness reconciliation;
2. Adaptive MCP Orchestrator Blueprint freshness and lifecycle reconciliation;
3. Broker Lane Sandbox source-first evidence card.

The four primary flagships remain unchanged.

## SPINE

### Pins

- private source: `fbratten/spine@8fa62c1ebfc0c7b65680ef2d89b9953a519e4138`
- public showcase before refresh: `fbratten/spine-showcase@bb2c265252d0caaa634b12ab0254273b26640da7`
- recruiter-proof publication merge: `22233862a208ac32ab61997b37ef57675e78a812`
- current proof route: `https://fbratten.github.io/spine-showcase/recruiter-proof/`

### Supported framing

- SPINE is a RunContext-governed orchestration runtime and multi-agent backbone.
- The adopted compiled path is `SkillCompiler -> PlanArtifact -> PlanExecutor` through `execute_compiled_plan(...)`.
- The adopted transports are CLI and `POST /api/orchestrator/execute`.
- AgenticLoop, OODA, scenarios, review, fan-out and pipeline remain peer/reference surfaces unless separately adopted.
- The source README reports `3650+` tests; they were not re-run by the static proof publication.
- The larger public showcase remains a point-in-time projection with seven interactive demos.

### Non-claims

- not every implemented surface is on the adopted compiled path;
- not every optional memory backend is active in one environment;
- the public showcase is not asserted byte-current with all later private-source work;
- no test or runtime execution was performed in the publication PR.

## Adaptive MCP Orchestrator Blueprint

### Pins

- private source: `fbratten/ai-projects-and-management-example@e86fefcac3f3b06d5afd01caeb5cdce8660a19e4`
- public showcase before refresh: `fbratten/Adaptive-MCP-Orchestrator-Blueprint-Showcase@417fa071575e546bd3ef48e2e07d3da7491546d4`
- recruiter-proof publication merge: `bef828ad953a71bd5d14025e2ea4f892cc5c4d36`
- current proof route: `https://fbratten.github.io/Adaptive-MCP-Orchestrator-Blueprint-Showcase/recruiter-proof/`
- private security follow-up: source issue #21

### Supported framing

- private teaching/reference implementation of capability-based routing, provider fallback, observability and optional learning;
- six core modules and ten extended modules;
- FastAPI, MCP, LanceDB, Neo4j, Prometheus, Grafana and Loki surfaces;
- source README records 951 passing tests;
- separate deep inspection counted approximately 1,038 test functions across 52 files, which is not a passing-run receipt;
- SPINE contains an implemented MCPOrchestratorExecutor seam and fallback path.

### Lifecycle reconciliation

This project is not presented as:

- an active production service;
- the estate's current universal MCP router;
- a public source repository;
- a current ranking of provider models or prices.

The current proof uses generic candidates to explain the routing model and leaves the historical demos intact.

### Security boundary

Private source issue #21 tracks rotation and removal of provider credentials previously found committed in configuration history. No value is repeated in public documentation. The showcase refresh does not close that issue.

## Broker Lane Sandbox

### Pins

- public source: `fbratten/broker-lane-sandbox@aae50e2d5b3bb3445561396d7cf80cef978bff24`
- implementation/test receipt named by the source README: `19091b1`
- source-reported test receipt: 286 passing tests on 2026-07-23
- evidence-card publication merge: `316dbbd65d6301dd99b668f637b04f93182186aa`
- evidence-card route: `https://fbratten.github.io/broker-lane-sandbox/`

### Supported framing

- public, dependency-free, default-deny process execution boundary;
- allow-listed bare command names;
- child environment built from empty;
- secret-shaped environment names filtered unless explicitly permitted;
- wall-clock timeout, process-group cleanup and optional POSIX resource limits;
- structured JSON and additive JSONL streaming;
- local llama.cpp-family inference using operator-fetched, size- and checksum-verified weights;
- model-weight exclusion enforced by repository guards.

### Non-claims

- not a kernel, VM or container sandbox;
- no filesystem jail;
- no network namespace;
- no executable hash pinning;
- not hostile multi-tenant security;
- no test rerun during evidence-card publication.

The public source repository remains canonical. The evidence card is orientation only.

## Publication and privacy rule

All three public routes contain architecture summaries, synthetic interaction or public-source facts only. They publish no private prompts, operational logs, memory records, credentials, provider accounts, private paths, model weights or customer-like data.
