# Recruiter-proof evidence record — 2026-08-02

This record supports the canonical recruiter-facing GitHub profile landing.

It distinguishes:

- source-backed implementation evidence;
- static public proof packages;
- independently observed HTTP accessibility;
- source-reported verification receipts that were not re-run during this profile-only change.

## Flagship evidence

| Project | Private source or public source | Current evidence pin | Public proof | Verification boundary |
|---|---|---|---|---|
| Intelligence Engine | Private source | `fbratten/intelligence-engine@3cdf7099c32c614a376a03324f545cfe8bc3a8b4` | `https://fbratten.github.io/intelligence-engine-showcase/` | Source README reports 3 domains, 8 source languages, 14 MCP tools, 46 REST endpoints and 1261+ tests. This profile change did not re-run the suite. The public showcase is independently discoverable over HTTP through its indexed documentation surface. |
| MADS | Private source | Current docs `c84698d91d20bde4771a813029c52e2dfa356827`; implementation receipt `dbd87c532bb01931b980ba2660a7f749b2e8a239` | `https://fbratten.github.io/mads/` | Implementation commit records typecheck, lint, 125 Vitest tests, production build and 13 Electron E2E scenarios. The public page is synthetic and performs no host mutation. Immediate independent HTTP verification remained unavailable from the execution environment. |
| Adaptivearts.ai | Private source, public deployed product | Current docs `adea33d6a2c193d67dcb0f5389fb7b17acf6954c`; implementation evidence `e31d085707dd98c86286e8368b0c4dc75b5ac9fa` | `https://fbratten.github.io/adaptivearts-ai/` and `https://adaptivearts.ai/` | Astro, React, Supabase Auth and the authenticated server-side Gemini proxy were inspected. The product site was externally reachable during the earlier review. No automated test-suite claim is made. Immediate independent HTTP verification of the new GitHub Pages case-study route remained unavailable from this execution environment. |
| Gate Monitor | Private source | Current docs `90f9845d6fde1b1ba902473afea2bb79dfab9877`; inspected runtime `193821edcacca87d286292e5f568c6aad9c808df`; report confinement `f3c30f4ce7e512cdd92615bd8fa82892843c9455` | `https://fbratten.github.io/gate-monitor/` | Source history reports 279 passing tests, one environment-dependent skip and three green dogfood scripts. The static demonstrator uses fictional values and does not run the Python engine. Immediate independent HTTP verification remained unavailable from the execution environment. |

## Public-proof policy

A private source project may be shown through a public-safe proof package when the package:

1. states that the source is private;
2. pins the source or implementation commit;
3. identifies which verification receipt supports the claim;
4. marks source-reported receipts that were not re-run;
5. uses synthetic fixtures where real logs, patches, prompts, paths or operational data are sensitive;
6. includes explicit non-claims;
7. does not imply customer production, Azure deployment or commercial scale unless separately evidenced.

## Route-verification status

### Repository-level verification

The following files were verified on the publication repository's `main` branch:

- `mads/index.html`
- `adaptivearts-ai/index.html`
- `gate-monitor/index.html`

The Intelligence Engine showcase repository was also refreshed and merged separately.

### HTTP-level verification

The Intelligence Engine documentation surface was independently discoverable and readable through the web search layer on 2026-08-02.

The execution environment could not resolve `fbratten.github.io` directly during the final route probe. Therefore the new MADS, Adaptivearts.ai case-study and Gate Monitor routes are classified as:

- repository-published: verified;
- HTTP-live: pending independent confirmation.

This is a verification limitation, not evidence of a deployment failure.

## Profile freshness rule

The profile should not repeat volatile counts unless they are pinned to an evidence date and source commit.

The first screen therefore uses capability summaries and bounded verification receipts. The wider catalogue below remains a navigation surface, not a claim that every linked project has equal maturity or freshness.

## Preserved predecessor

The pre-restructure profile README is preserved at:

`archived/README.pre-canonical-recruiter-landing-2026-08-02.md`
