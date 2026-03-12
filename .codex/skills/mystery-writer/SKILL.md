---
name: mystery-writer
description: Use this skill when planning, drafting, revising, or checking a mystery story, detective story, whodunit, clue puzzle, suspect structure, locked-room case, or fair-play reveal. It is for tasks where Codex should design the flow of truth, character knowledge, clue presentation, misdirection, and solution logic before or alongside prose.
---

# Mystery Writer

## Overview

Treat mystery writing as information design before prose. Separate three layers at all times:

- fact: what actually happened
- recognition: who knows or misunderstands what
- presentation order: what the reader sees, and when

Write and revise against explicit planning tables instead of relying on memory. Keep the planning memo outside the draft itself. In this repository, default to putting the planning memo in `idea.md` and the prose in `doc.md`.

In this repo, if the case design changes, update `idea.md` before touching `doc.md`.

## Core Method

Maintain these six tables while writing.

1. `truth table`
   - Record only what actually happened in the world.
   - Fix the culprit, motive, method, timeline, concealment, accident, mistake, and final deductive path.
   - For every crucial action, record the local reason it happened then: why this person acted now, why this way, and why they did not choose an easier alternative.
   - Write the event timeline at action-level granularity. Prefer minute-by-minute precision.

2. `recognition table`
   - Track each character's knowledge, misunderstanding, lies, hidden knowledge, testimony, blind spots, and what they would naturally notice, remember, or say.
   - Use it to prevent impossible testimony, convenient intelligence, or an unnaturally dull detective.

3. `clue table`
   - Track every clue, foreshadowing beat, and misdirection.
   - Give each clue two meanings: its first-read meaning and its solved meaning.
   - Record first appearance, apparent interpretation, true function, and recovery scene.

4. `motive-opportunity-means table`
   - Build plausible culprit paths for multiple suspects, not just the real culprit.
   - Record motive, visible motive, immediate trigger, opportunity, means, relationship to victim, reason to lie, and how suspicion is explained if the suspect is innocent.

5. `scene table`
   - Treat each scene as an information-delivery unit.
   - Record surface action, new reader knowledge, new detective knowledge, withheld information, emotional role, suspense role, planted clue, recovered clue, and the question that pushes to the next scene.

6. `verification table`
   - Continuously test physical plausibility, reality-sense, psychology, information fairness, and structural pacing.
   - Update it during drafting, not only at the end.

## Writing Order

Use this order unless the user explicitly wants a looser process.

1. Build one clean truth of the case.
2. Design the culprit's plan and the culprit's mistake.
3. Write one plain-language reason for each crucial action: `why this person did this now`.
4. Distribute suspicion across the suspect set.
5. Build the clue and misdirection table.
6. Reverse-engineer the detective's logic from the final answer backward.
7. Build the scene table.
8. Draft the prose and update the verification table as soon as new text exists.

## Always-Keep-Visible Notes

Keep these notes visible while drafting.

- `case timeline`: the truth timeline, ideally minute-by-minute
- `reader timeline`: what the reader learns in each chapter
- `character secrets`: what each character knows, hides, and lies about
- `clue index`: clue, misdirection, setup, recovery
- `suspect comparison`: motive, opportunity, means, irregularity
- `solution logic`: explicit chain such as `A therefore B, B therefore C, therefore culprit X`

Use [six-table-template.md](references/six-table-template.md) when a blank planning scaffold is needed.

## Fair-Play Rules

Apply these rules by default.

1. Separate truth from prose.
   - Do not silently change the case because a drafted scene drifted.
   - If the solution changes, update the truth table first, then propagate the change.

2. Give clues room for misreading.
   - Avoid clues that instantly solve the case.
   - Avoid clues so vague that the reveal feels imported from nowhere.

3. Avoid perfect-crime design.
   - The detective's foothold usually comes from the culprit's oversight, stress, vanity, haste, or bad assumption.

4. Do not confuse abstract motive with legible motive.
   - The reader should be able to say why each important actor chose this action at this moment, not merely why they broadly disliked the outcome.

5. Do not rely on author-forced behavior.
   - If the trick works only because people fail to react, notice, ask, or speak in ways ordinary readers find unnatural, redesign the event.

6. Avoid adding decisive new facts in the solution.
   - Prefer reinterpretation of planted information over late insertion.

7. Leave a live question at the end of each chapter or major scene.
   - Mystery propulsion comes from unresolved questions more than from event volume.

## Verification Pass

Check these five lines of failure repeatedly.

1. `physical`
   - Do timing, movement, tools, wounds, weather, sound, light, and visibility actually work?

2. `behavioral / reality-sense`
   - Would ordinary people in the scene interpret the event this way?
   - Does the trick survive casual checking, not just formal deduction?
   - Does it depend on implausible confusion of voices, objects, distances, wording, etiquette, or memory?
   - If a skeptical reader said "that would not happen like that," could you answer concretely?

3. `psychological`
   - Would the culprit really choose this plan?
   - Is each key action locally understandable, not just globally motivated?
   - Would a witness remember the event in this form?
   - Does the detective miss too much for too long?
   - Does the reader feel "they should have said that earlier"?

4. `informational`
   - Is every necessary fact available before the solution?
   - Is the case accidentally solvable too early?
   - Does each clue function, rather than merely exist?

5. `structural`
   - Does the middle stall?
   - As the truth gets closer, do the suspicious points change shape rather than simply disappear?
   - Is the explanation short enough and staged clearly enough?
   - Does the reader get a near-solution moment just before the answer?

## Output Expectations

When using this skill to create or revise a mystery, prefer this working sequence in the response:

1. state the case premise in one short paragraph
2. show the six-table planning summary
3. show the detective's final logic chain
4. draft or revise the prose
5. run a verification pass and list weak points

If the user asks only for planning, stop before prose. If the user asks for prose only, still build at least a compact version of the six tables internally and surface them if the story starts to wobble.
