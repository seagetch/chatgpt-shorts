---
name: shorts-production-orchestrator
description: Mandatory top-level workflow for creating, planning, drafting, reviewing, revising, or publishing a chatgpt-shorts story. Route concept planning through shorts-concept-planner and optional series planning, then dispatch to the correct genre specialists, quality checks, and reader maintenance without forcing a single genre formula.
---

# Shorts Production Orchestrator / 全体構成・工程統括

## Purpose

Own **the order, handoffs, and release gates** for chatgpt-shorts work. This is a routing and quality-control skill, NOT another genre or story-generation template. For a new story, invoke this skill first. It must route concept selection to `shorts-concept-planner`, then route the selected genre and story mechanism to the appropriate specialist(s). Do not directly start `sf-short-writer`, `mystery-writer`, or `horror-writer` for a new work before the common concept decision is recorded.

When users request only an idea, critique, limited revision, or reader repair, perform only the relevant phases and explicitly label skipped or unverified phases. Do not silently republish, overwrite unrelated work, or change a user's specified premise.

## Canonical pipeline

```text
User constraints / scope
  |
  v
SHORTS CONCEPT PLANNER (always for a new premise)
  |-- if 久条麗華 series: REIKA SERIES PLANNER adds canon and
  |   series-specific divergence + archive checks during planning
  v
Concept lock (idea.md: candidates, novelty audit, chosen engine, handoff)
  |
  v
Genre and mechanism router
  |-- fair-play puzzle / detective mystery -> mystery-writer
  |       review -> mystery-reviewer; changes -> mystery-reviser
  |-- horror / uncanny / supernatural danger -> horror-writer
  |-- SF from scientific/technological difference -> sf-short-writer
  |-- mixed works -> specialists for actual mechanisms, primary first
  |-- other genres -> common narrative craft checks; do not fabricate
  |                    missing specialist skills or force mystery tables
  v
Full draft in doc.md
  |
  v
Independent critical review, revision, verification
  |
  v
Cover, site generation, HTTP checks -> shorts-reader-maintainer
  |
  v
Commit/push and publication verification when authorized
```

## Phase 0: Scope and repo check

- Read `AGENTS.md`, `UPDATE.md`, the relevant skill files, and the target work's `idea.md`/`doc.md` if they exist.
- Identify one of: **new story**, **new concept only**, **revision of existing story**, **critique**, **publication**, **reader maintenance**.
- Preserve user constraints on series, topic, genre, length, viewpoint, deadlines and existing files. Check current `main` state before writing. Do not assume past conversation state is the live repo.
- For existing-story revision preserving the premise, do not rerun six new concepts automatically. Reopen concept planning only when the central premise or engine is being changed.

## Phase 1: Broad common concept planning

Read and apply `.codex/skills/shorts-concept-planner/SKILL.md`.

- Generate distinct candidates **before browsing old plot content**; use genre taxonomy and independent story engines as separate axes.
- Then check actual older texts and production notes to find structural repetition, not inspiration to replicate.
- For a series, perform its series-specific planning as a **substep of the common planning phase**, not as a competing earlier route. For 久条麗華, read `reika-series-planner` and preserve its canon/divergence/score rules; avoid duplicate six-candidate exercises by using one shared pool that satisfies both skills.
- Record in `idea.md`: candidate set, novelty audit, selected direction, rejected near-duplicates, genre/engine, requirements, and specialist routing.
- **STOP gate:** Do not draft `doc.md` if concept is FAIL or key genre/engine has not been selected. If user asks only for ideas, end after this phase.

## Phase 2: Specialist routing, not genre flattening

Pick on the basis of the **actual narrative mechanism**, not a superficial genre word or the author's previous skill:

| Mechanism / need | Skill | Key constraints |
| --- | --- | --- |
| Fair-play detective puzzle | `mystery-writer` | Truth, recognition, clues, suspects, scene and verification tables; local causal logic |
| Existing mystery critique | `mystery-reviewer` | Reconstruct from prose, distinguish explicit facts from assumptions |
| Mystery structural revision | `mystery-reviser` | Fix `idea.md` information model before revising `doc.md` |
| Horror, uncanny, supernatural threat | `horror-writer` | Literal camera, spatial/body consistency, internal supernatural invariants and behavioral credibility |
| Science/technology-driven SF | `sf-short-writer` | SF difference, human theme, transformed theme, literary flavor; scoring/revision loop |
| 久条麗華 ongoing series | `reika-series-planner` | Canon and structural variety; does NOT require a mystery in every installment |
| Romance, comedy, fantasy, historical, action, work, sports, daily/literary, fable, philosophical, formal experiment and other genres without installed specialists | `shorts-concept-planner` + common verification below | Derive genre-relevant craft checks from chosen conflict, pacing and audience; record `specialist: none installed`; never misapply mystery/SF/horror rules just to fill a slot |

For cross-genre work, select a primary engine and apply other specialists only to their specific mechanisms. Example: SF horror uses SF world-change checks and horror geometry/fear checks; mystery romance uses fair-play logic only for the case and relationship stakes for the drama. Do not automatically label all stories science fiction or all detective-character episodes whodunits.

## Phase 3: Complete story draft and review

- Draft the **whole** `doc.md` from the concept lock and applicable skill. Do not publish a synopsis as a finished short.
- Verify event sequence, cause and effect, timing, physical space, objects, speech attribution, viewpoint and character decisions.
- Verify genre-specific execution: e.g. romance relationship development, action readable movement, comedy setup/escalation/payoff, drama consequential choice, sport understandable rules and stakes, horror observable effects, mystery fair evidence, SF world consequences.
- Check pacing at the specified length, distinctiveness, emotional effect, clarity of the climax, and ending payoff.
- Run a **skeptical first-reader pass** without relying on `idea.md`, past works, or familiar tropes to fill the gaps.
- Compare the actual `doc.md` with archive neighbors for repeated openings, conversational patterns, incident architecture, emotional resolution and endings. Novel premises can still produce formulaic prose.
- Record in `idea.md` a concrete pass/fail/not-tested matrix and repair decisions. Structural fail in causal/spatial/behavioral intelligibility or selected engine should block acceptance; rewrite, re-review, and retest until repaired. Never inflate a score to justify release.

## Phase 4: Publication when in scope

When authorized to produce/publish a managed story:
- Use `shorts-reader-maintainer` and `UPDATE.md`; `doc.md` remains text source of truth.
- Cover follows the actual story without giving away the climax; inspect similarity to recent actual covers, not just prompts. Ensure required JPEG exists for the current reader.
- Regenerate `index.html` wrappers and catalog with the repo's generator as appropriate, verify hashes and references, run documented static/HTTP tests and actual reader pagination/cover where possible.
- Preserve existing unrelated changes. Inspect staged scope and commit/push only within explicit user authorization.
- Distinguish code pushed, GitHub Pages deployed, and actual browser verified. Never claim the last two solely from a successful connector write.

## Route examples

- "Write a new short": orchestrator -> common concepts -> archive uniqueness -> appropriate specialist(s) -> draft/review -> publication as requested.
- "Next 久条麗華 installment": orchestrator -> common planning **with** reika-series-planner -> chosen engine -> possibly mystery, horror, SF, or none -> draft/review.
- "Review 『返却口』": orchestrator review route -> horror-writer literal staging / invariants -> critique; do not manufacture new premises.
- "Fix a missing line in an existing story": orchestrator narrow-revision route -> relevant specialist checks only -> preserve existing story.
- "Change the reader": orchestrator maintenance route -> shorts-reader-maintainer only.

## Mandatory handoff log

For substantial managed work record in `idea.md`:
1. scope and constraints;
2. concept skill completion and any series subskill;
3. primary genre and story engine, secondary genres if any;
4. invoked specialists **and why**; or why none applies;
5. design and first-reader verification, failed items and repairs;
6. publishing steps and verified vs unverified state.

An installed skill is only present if its SKILL.md exists and can be read. Do not claim that romance, fantasy, historical, comedy, etc. have specialized skills until those are added. The orchestration must still support them via the common craft verification rather than quietly biasing the publication list toward SF/mystery/horror.
