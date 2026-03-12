---
name: mystery-reviewer
description: Use this skill when reviewing an existing mystery story, detective story, whodunit, clue puzzle, suspect structure, or locked-room plot in order to reconstruct its truth, knowledge gaps, clues, suspects, scene information flow, and fairness. Use it when Codex should judge whether the work actually functions as a mystery, where it breaks, and which extracted elements are missing, weak, or unfounded.
---

# Mystery Reviewer

## Overview

Review mysteries by rebuilding the design that `mystery-writer` would have created before drafting. Start by extracting the six tables from the existing text, mark confidence for each extracted item, and only then judge whether the piece stands as a mystery.

Judge not only whether a trick exists on the page, but whether the characters' choices are understandable and the trick feels plausible to an ordinary reader's reality-sense.

Separate three layers during review:

- fact: what the work implies actually happened
- recognition: who knows or misunderstands what at each point
- presentation order: what the reader receives, in what sequence

Do not collapse these layers into one summary. A work can have crime, atmosphere, and a reveal while still failing as a mystery.

## Review Workflow

Follow this order unless the user explicitly asks for a lighter pass.

1. Establish the review scope.
   - Identify whether the work is complete, partial, synopsis-only, or prose-only.
   - Identify whether the ending or culprit is known, unknown, or intentionally withheld.
   - If the text is incomplete, continue, but downgrade confidence and mark open gaps.

2. Reconstruct the six tables.
   - Build compact versions of the truth, recognition, clue, motive-opportunity-means, scene, and verification tables from the text.
   - Use direct textual support where available.
   - Reconstruct local motives for key actions, not only abstract motives for the case.
   - Mark each line with one of:
     - `explicit`
     - `strong inference`
     - `weak inference`
     - `missing`

3. Extract the detective logic chain.
   - Write the implied solution path as explicit steps.
   - If the chain cannot be written without hidden premises, mark the exact breakpoints.

4. Test mystery viability.
   - Judge whether the work stands as a mystery, not merely as a dramatic incident.
   - Focus on solvability, fairness, suspect structure, clue function, and explanatory integrity.

5. Report findings in severity order.
   - Lead with concrete failures and risks.
   - Only after findings, give the overall verdict.

## Six-Table Reconstruction Standard

Use the same six-table model as `mystery-writer`, but in reverse.

1. `truth table`
   - Reconstruct what actually happened.
   - If timing, method, culprit, concealment, or the immediate reason a character took a crucial action are unclear, say so plainly.
   - A mystery is unstable if its truth table cannot be reconstructed after the intended solution.

2. `recognition table`
   - Reconstruct who knows what, who lies, who is mistaken, and what each person would naturally notice or fail to notice.
   - Flag scenes where testimony or silence appears to serve the author rather than the character.

3. `clue table`
   - List clues, misdirections, setup beats, and recoveries.
   - Judge whether each clue has both a first-read meaning and a solved meaning.
   - Flag clues that solve the case too early or clues that do nothing until the ending explains them.

4. `motive-opportunity-means table`
   - Reconstruct the suspect field.
   - Record not only broad motive but also the immediate trigger and the reason each suspect might act, lie, or stay silent now.
   - A culprit should not be the only person with motive, access, or narrative pressure unless the work is intentionally not a fair-play mystery.
   - Flag cases where other suspects exist only decoratively.

5. `scene table`
   - Review scenes as information units.
   - Identify what each scene actually contributes: clue placement, misreading, suspect shift, new constraint, or reversal of prior meaning.
   - Flag scenes that contribute mood only while the mystery stalls.

6. `verification table`
   - Run physical, behavioral, psychological, informational, and structural checks.
   - Distinguish between:
     - impossible but intentional genre premise
     - accidental inconsistency
     - unfair withholding
     - merely under-explained reasoning
     - event that is described but still not convincing

Use [review-template.md](references/review-template.md) when the user wants a structured review memo.

## Decision Rules

Judge the work against these questions.

1. `Can the truth be reconstructed?`
   - If the reviewer cannot write a coherent truth timeline after the solution, the case architecture is weak.

2. `Do character knowledge states make sense?`
   - If a witness lies for no character reason, or the detective ignores obvious implications without cost, the mystery weakens.

3. `Are key actions character-driven?`
   - If the culprit's plan, a witness's silence, or a suspect's risky move makes sense only because the author needs the trick, mark it as a structural weakness.

4. `Do clues function as clues?`
   - A clue should support both misreading and later reinterpretation.
   - If every clue is either obvious or irrelevant, the mystery fails at clue design.

5. `Is there a real suspect field?`
   - If only one person can realistically be the culprit, the work may still function as suspense, but not as a strong whodunit.

6. `Is the solution fair?`
   - The ending should not import decisive new facts.
   - Reinterpretation is acceptable; sudden invention is not.

7. `Would the trick survive a reality-sense check?`
   - Ask whether ordinary people would hear, remember, misread, or accept the event the way the solution requires.
   - If the reviewer keeps thinking "people do not act like that" or "that would be checked immediately," treat it as a real failure, not a taste issue.

8. `Does the structure keep generating questions?`
   - The middle should transform suspicion and uncertainty rather than merely delay the reveal.

## Review Output

When asked for a review, present findings first and keep the overview brief.

Use this sequence.

1. `Findings`
   - List concrete issues in severity order.
   - Cite the relevant table, character, clue, scene, or logic break.

2. `Reconstructed elements`
   - Summarize the extracted six tables.
   - Mark each important item with `explicit`, `strong inference`, `weak inference`, or `missing`.

3. `Mystery verdict`
   - State whether the work functions as:
     - `works as a fair mystery`
     - `works as a mystery but with fairness or logic weaknesses`
     - `works mainly as drama or suspense, not as a robust mystery`
     - `does not currently function as a mystery`

4. `Repair guidance`
   - Suggest the smallest structural changes that would strengthen the mystery.
   - Prefer fixes that repair the information design, local action motives, and realism rather than only the prose style.

## Review Tone

Be explicit and unsentimental. Do not flatter atmosphere if the clue logic is weak. Do not confuse "the text says this happened" with "this is convincing." If the text is incomplete, say what cannot yet be judged and why.
