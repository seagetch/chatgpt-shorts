---
name: mystery-reviser
description: Use this skill when applying a mystery review to an existing mystery story, detective story, whodunit, clue puzzle, or locked-room plot. It is for tasks where Codex should update the reconstructed information tables and logic chain from reviewer findings, then revise the prose so the story matches the repaired mystery structure, fairness, and clue design.
---

# Mystery Reviser

## Overview

Revise mysteries by treating review findings as structural input, not as vague editorial notes. Update the written-out information first, then revise the prose to match the repaired design, then run a post-revision check.

When the failure is "I do not believe this person would act this way" or "this trick does not feel real enough," treat that as structural breakage, not as a cosmetic note.

This skill assumes the story has already been examined with `mystery-reviewer`, or that equivalent findings exist. If no review exists, do not jump straight to prose edits. Build at least a compact review first.

## Revision Principle

Separate three layers throughout revision:

- fact: what actually happened
- recognition: who knows or misunderstands what
- presentation order: what the reader sees, and when

Do not patch only the prose when the failure is structural. If the truth table, clue table, suspect field, or logic chain changes, update the information layer first and treat prose edits as propagation.

In this repository, default to:

- `idea.md` for updated tables, review findings, and revision policy
- `doc.md` for revised prose

This order is mandatory unless the user explicitly asks for prose-only emergency patching:

1. update `idea.md`
2. confirm the changed logic and change map there
3. only then edit `doc.md`

Do not use `doc.md` as a scratchpad for unresolved structural thinking.

## Revision Workflow

Follow this order unless the user explicitly asks for a narrower edit.

1. Read the review result.
   - Extract findings, reconstructed elements, verdict, and repair guidance.
   - Separate:
     - confirmed breakage
     - motivation-legibility failure
     - reality-sense failure
     - uncertain inference
     - optional improvement

2. Decide the repair scope.
   - Prefer the smallest set of changes that makes the mystery function.
   - Preserve the story's identity unless the user asks for deeper replacement.
   - Choose one of:
     - `local fix`: clue, scene, testimony, or logic patch
     - `mid-level fix`: suspect rebalance, motive repair, scene reorder
     - `case rewrite`: truth-table or culprit-plan replacement

3. Update the structured information.
   - Rewrite the extracted six tables to reflect the repaired version, not the broken one.
   - Update:
     - truth table
     - recognition table
     - clue table
     - motive-opportunity-means table
     - scene table
     - verification table
   - For each key action, rewrite the local reason it happens when it happens.
   - Rewrite the detective logic chain in explicit steps.
   - Do not edit `doc.md` before this step is materially complete.

4. Propagate the change map.
   - For every changed fact, list which scenes, clues, testimonies, and suspect impressions must change.
   - If one repair affects multiple scenes, treat it as a dependency graph, not isolated line edits.
   - Treat this as the gate between `idea.md` work and `doc.md` work.

5. Revise the prose.
   - Edit scenes in the order that preserves causal consistency.
   - Keep clue placement, misreading, and reveal timing aligned with the updated tables.
   - Remove or rewrite prose that still points to the broken version.
   - If prose edits reveal a new structural change, stop and update `idea.md` again before continuing.

6. Run a post-revision check.
   - Re-test physical, psychological, informational, and structural integrity.
   - Confirm that the revised prose matches the revised tables.
   - If not, update the tables again before making further prose edits.

## What To Update First

When a review identifies a problem, repair the underlying table before the prose.

1. `truth problem`
   - Fix the truth table and solution logic first.
   - Then update all affected clues, testimony, and reveal scenes.

2. `knowledge problem`
   - Fix the recognition table first.
   - Then update dialogue, omissions, lies, and detective deductions.

3. `clue problem`
   - Fix the clue table first.
   - Ensure each clue has both a first-read meaning and a solved meaning.
   - Then update first appearance, misreading, and recovery scenes.

4. `suspect-field problem`
   - Fix the motive-opportunity-means table first.
   - Then rebalance suspicion on the page.

5. `scene-stall problem`
   - Fix the scene table first.
   - Give each weak scene a concrete information role.

6. `motive legibility problem`
   - Fix the truth table and motive-opportunity-means table first.
   - Give each important action a clear local trigger, not only an abstract motive in summary form.

7. `reality-sense problem`
   - Fix the truth table and verification table first.
   - If the trick depends on implausible hearing, memory, inaction, confusion, or handling of objects, replace the mechanism or plant stronger support.

## Repair Rules

Apply these rules by default.

1. Prefer structural repair over cosmetic smoothing.
   - If a clue is unfair, do not merely soften the explanation scene. Plant or reshape the clue.

2. Prefer minimal stable fixes.
   - Do not replace the culprit or trick unless smaller repairs cannot solve the failure.

3. Do not leave orphaned information.
   - Every changed clue, lie, alibi, and deduction must still connect cleanly to the new version.

4. Do not reverse the repository order.
   - In this repo, structural mystery revision flows from `idea.md` to `doc.md`.
   - If you catch yourself patching prose first for a structural issue, stop, move the change into `idea.md`, then return to prose.

5. Do not add decisive late information unless the user accepts a non-fair-play solution.
   - Reinterpretation is better than invention.

6. After every major repair, re-check the suspect field.
   - A stronger clue or cleaner logic may accidentally collapse all false alternatives.

7. Keep the detective logic explicit.
   - If the revised answer still depends on hidden premises, the repair is incomplete.

8. Do not preserve a trick only because it is already drafted.
   - If the event reads as implausible after a plain-language explanation, redesign it.

9. Do not leave author-forced behavior in place.
   - If a witness withholds, misremembers, or speaks oddly only because the case needs it, either give that behavior a visible reason or change the case.

## Revision Output

When asked to revise, use this sequence unless the user asks for prose only.

1. `Applied findings`
   - State which review findings are being fixed now.

2. `Updated information`
   - Show the revised six-table summary and the revised logic chain.
   - Highlight what changed from the previous version.
   - Make clear that `idea.md` has been brought up to date before prose revision.

3. `Change map`
   - List the scenes, clues, testimonies, or suspect impressions that must be rewritten.

4. `Revised prose`
   - Provide the changed scenes or full revised draft, depending on scope.

5. `Post-revision check`
   - State whether the repaired version now works as a fair mystery, works with remaining weaknesses, or still fails.

Use [revision-template.md](references/revision-template.md) when a structured repair memo is needed.

## Review Loop

If the revision is substantial, run a short internal loop:

1. compare revised prose against revised tables
2. compare revised logic against clue placement
3. compare each key action against its local motive
4. compare the trick against ordinary reality-sense objections
5. compare suspect field against final fairness
6. note remaining weaknesses
7. revise again if the mystery still breaks

Do not stop at a polished sentence-level pass if the information design remains inconsistent.
