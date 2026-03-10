---
name: sf-short-writer
description: Use this skill when planning or drafting a new SF short story for this repository. It turns one scientific difference from the present world into a human theme, a changed value system, a literary flavor, and then a complete short.
---

# SF Short Writer

## Overview

This skill is for writing new SF shorts in the style of this repository. Treat the story as a sequence: first define the scientific difference from the present world, then define the human theme, then define how that theme changes under the SF premise, then choose the literary flavor, and only then draft the short.

## When To Use

Use this skill when the user asks for any of the following:

- a new SF short story
- an SF premise for a new work
- planning notes before drafting
- a rewrite of an idea into a repo-style SF short
- a somewhat longer short that should be planned before prose

## Core Planning Order

Always structure planning in this order.

1. Define `①`, the SF novelty.
   - Decide what is scientifically or technologically different from the present world.
   - Keep it concrete enough to change daily life, not just background lore.

2. Define `②`, the present-day human theme.
   - Decide what aspect of current human life, relationships, labor, memory, family, desire, loneliness, status, or morality the story is really about.

3. Define `③`, how `②` changes inside `①`.
   - State the dramatic question of the story: how does that human theme transform in the SF world?
   - This must be the center of the story, not a side note.

4. Define `④`, the literary flavor.
   - Decide the genre or seasoning as literature: romance, satire, mystery, twist ending, quiet melancholy, comic bureaucracy, family drama, and so on.

5. Write the short according to `①` through `④`.
   - The prose should clearly come from that planned combination.
   - Do not let the literary gimmick erase the SF premise.
   - Do not let the SF premise erase the human theme.

## Required Repo Workflow

When writing a managed short inside this repository, record the initial concept in `idea.md` before drafting `doc.md`.

- `idea.md` is the fixed working memo for the story.
- `doc.md` is the actual prose draft.
- Do not begin revising the prose without first writing down the initial direction in `idea.md`.

`idea.md` should hold at minimum:

- `① SF novelty`
- `② present-day human theme`
- `③ how ② changes in the world of ①`
- `④ literary flavor`
- the intended ending direction
- the current evaluation criteria for the draft

The purpose of `idea.md` is to keep the goal and the evaluation axis from drifting mid-process.

If the direction truly needs to change during revision, do not silently replace the plan. Append a note in `idea.md` explaining:

- what changed
- why it changed
- how the evaluation criteria changed

## Execution Loop

After drafting, do not stop immediately. Use this revision loop.

1. Critically self-score the draft out of 100.
   - Score the work harshly, not generously.
   - Judge at least these points:
     - strength of `①`
     - clarity and relevance of `②`
     - force of `③` as the actual story engine
     - effectiveness of `④`
     - ending quality
     - prose quality

2. Explain the weaknesses behind the score.
   - Identify what is thin, generic, overexplained, emotionally weak, structurally loose, or insufficiently SF.

3. Set a concrete revision policy from that critique.
   - State what must change in the next pass.
   - Prefer a short, operational policy, for example:
     - strengthen the everyday consequences of `①`
     - make `③` visible earlier
     - cut explanation and replace it with scene
     - sharpen the ending image

4. Record that revision policy in `idea.md`.
   - This keeps the revision target explicit.
   - It also prevents the scoring standard from changing unnoticed between passes.

5. Revise the actual story.

6. Repeat this loop until the score exceeds 70.
   - Do not stop at 70 exactly.
   - Keep looping while the score is 70 or below.

Unless the user asks otherwise, keep each loop visible in concise form:

- `Score`
- `Critique`
- `Revision policy`
- `Revised draft`

## Writing Rules

- `①` must be a genuine difference from the current world.
- `②` should be stated in present-human terms, not abstract doctrine.
- `③` should describe the change or distortion caused by `①`, not merely restate `②`.
- `④` should influence tone, structure, and reveal pattern.
- The ending should feel earned by the combination of `①` through `④`.

## Longer Works

If the user asks for something a little longer, write a memo before the story itself.

That memo belongs in `idea.md` and should include:

- `① SF novelty`
- `② present-day human theme`
- `③ transformed theme in the SF world`
- `④ literary flavor`
- optional supporting notes such as:
  - setting details
  - major character roles
  - reveal structure
  - ending image

Keep the memo short and functional. It is a working note, not an essay.

For longer works, run the same scoring and revision loop after the first full draft.

## Repo Fit

- New works in this repository live in their own dated folders.
- `idea.md` stores the plan and revision history.
- `doc.md` stores the story itself.
- If the user asks to create a new managed short in the repo, follow the existing dated-folder pattern already used by other works.
- If the task also involves generating reader pages or updating the catalog, use `shorts-reader-maintainer` as well.
- If you need a planning scaffold, read [references/planning-template.md](references/planning-template.md).
