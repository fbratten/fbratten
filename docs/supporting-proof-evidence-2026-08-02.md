# Supporting proof evidence — Vertex and Worktrace

Verified: 2026-08-02

This record supports two secondary recruiter-facing proof packages. They strengthen the current four-project flagship group but do not replace it.

## Vertex

- private source repository: `fbratten/vertex`
- source branch: `main`
- inspected source pin: `af879d6108a07b1ed816772e43f7fb5cde81c175`
- public proof: `https://fbratten.github.io/vertex/`
- publication merge: `fbratten/fbratten.github.io@cd1337e7281a170d47dd1ce99b433ddb8ff641e4`
- source-reported verification: 569 tests across 30 files

Supported evidence:

- React 18, Three.js 0.160, Vite and Vitest;
- canonical `GraphNode`, `GraphEdge`, `GraphEvent` and `SceneSnapshot` model;
- Agent Activity, Portfolio, Family and Workflows scenes;
- shared provenance, replay, focus, labels, export and URL-state surfaces;
- read-only source adapters;
- a bounded workflow-publication lane with positional node pseudonymisation and an 18/18 reverse-mutation gate for that surface.

Boundary:

- the public page is a synthetic Three.js demonstration;
- it does not publish private source, real agent messages, portfolio data, workflows, prompts, paths or credentials;
- the test receipt was not re-run during publication;
- the source explicitly says the live agent endpoint is development-only.

## Worktrace

- private source repository: `fbratten/worktrace`
- current source/documentation pin: `e09c10acfd7b3748054bb4b31beb6594d57136e2`
- implementation receipt: `84e03b312e36c66e4fdcac05a3ff800961c6fea5`
- public proof: `https://fbratten.github.io/worktrace/`
- publication merge: `fbratten/fbratten.github.io@1859dbb9db9abc288f7cbe98fe4c0ab66fe66406`
- source-reported verification: 962 passing tests, 0 skipped, CI on Python 3.10–3.13

Supported evidence:

- Python 3.10+ CLI with stdlib-only runtime apart from conditional Windows `tzdata`;
- local SQLite ledger and FTS5 search;
- ledger schema 6, event envelope 2 and producer 0.4.2;
- explicit temporal semantics for source-exact, collection-time, source-interval and order-only evidence;
- bounded metadata collection and privacy receipts;
- automatic Claude Code observation;
- Personal RAG outbox with status and bounded drain recovery;
- reports and JSONL export derived from the canonical ledger.

Boundary:

- the public page is a browser-memory simulation, not the Python or SQLite runtime;
- it contains no real ledger rows, shell history, transcripts, Personal RAG records, paths or credentials;
- `invoked` and `referenced` do not assert successful effect;
- native Windows execution is not claimed as verified;
- the test and CI receipts were not re-run during publication.

## Publication status

Both proof files and evidence manifests are verified on the GitHub Pages repository's `main` branch.

Direct independent HTTP confirmation is a separate verification class. Until a direct route probe succeeds, repository publication must not be restated as proof of HTTP availability.
