## Skills

### Available skills

- `shorts-production-orchestrator`: Mandatory entrypoint for new shorts and substantial story work; coordinates common concept planning, series planning, genre specialists, verification, and publication. (file: `.codex/skills/shorts-production-orchestrator/SKILL.md`)
- `shorts-concept-planner`: Mandatory common first creative phase for new premises; diversifies genre and story engine, audits repetition, and chooses a concept before genre-specific writing. (file: `.codex/skills/shorts-concept-planner/SKILL.md`)

- `mystery-writer`: Use when planning, drafting, revising, or checking a mystery story through explicit truth, clue, suspect, and reveal design. (file: `.codex/skills/mystery-writer/SKILL.md`)
- `mystery-reviewer`: Use when reviewing an existing mystery to reconstruct its six tables and judge whether it functions as a fair and coherent mystery. (file: `.codex/skills/mystery-reviewer/SKILL.md`)
- `mystery-reviser`: Use when applying mystery review findings to update structured story information and revise the prose accordingly. (file: `.codex/skills/mystery-reviser/SKILL.md`)
- `shorts-reader-maintainer`: Use when working on this repository's shared reader, generator, root catalog, or per-work wrappers. (file: `.codex/skills/shorts-reader-maintainer/SKILL.md`)
- `sf-short-writer`: Use when planning or drafting a new SF short for this repository from a scientific world-change premise. (file: `.codex/skills/sf-short-writer/SKILL.md`)
- `horror-writer`: Use when planning, drafting, reviewing, or revising horror; verify observable events, physical staging, supernatural invariants, credible decisions, and first-read clarity before approval. (file: `.codex/skills/horror-writer/SKILL.md`)
- `reika-series-planner`: Use before proposing, drafting, or structurally revising any 久条麗華／冬月澄乃 series episode to develop cross-genre concepts independently of previous plots and audit the archive only for structural repetition and canon consistency. (file: `.codex/skills/reika-series-planner/SKILL.md`)

### How to use skills

- **Always enter through `shorts-production-orchestrator` for new stories, story concepts, substantial story revisions, reviews, or publication workflows.** It determines which phases apply; do not start with a genre writer for a new story.
- **For a new story, run `shorts-concept-planner` before any genre-specific writing skill.** Research current news, trends, public discussions, and deeper scientific/historical/cultural topics using dated sources before genre selection. Then create at least six substantially different independent concepts where the brief permits, and only afterward inspect previous stories for repetition detection and continuity. Record sources, verification limits, candidate comparison, and selection in `idea.md` before writing `doc.md`.
- For an existing story with unchanged premise, use the orchestrator's narrow review/revision route; do not force six new pitches. For other genres without a dedicated writer skill, use common concept and quality checks rather than forcing mystery mechanics.

- Use `mystery-writer` for planning or drafting a mystery, especially when the story should be managed through truth, recognition, clue, suspect, scene, and verification tables.
- Use `mystery-reviewer` for analyzing an existing mystery draft, extracting its underlying structure, and judging whether it works as a mystery.
- Use `mystery-reviser` after a mystery review, when the structured information should be updated first and the prose should then be revised to match.
- Use `shorts-reader-maintainer` for changes to `book.html`, `generate_reader.py`, root `index.html`, or any generated work `index.html`.
- Use `sf-short-writer` for planning and drafting new SF shorts, especially when the user wants the story built from premise `1`, human theme `2`, transformed theme `3`, and literary flavor `4`.
- Use `horror-writer` for all horror work, including supernatural, uncanny, psychological, and horror/SF or horror/mystery hybrids. Before changing `doc.md`, record the event model, spatial geometry, supernatural constraints, and reader-facing verification in `idea.md`. A failed clarity, spatial, rule, or behavioral gate blocks acceptance even when the prose is polished.
- Within the common concept phase, also use `reika-series-planner` for every new or substantially re-plotted 久条麗華／冬月澄乃 episode. One shared pool of at least six independent cross-genre concepts satisfies both planning skills; do not run two redundant candidate exercises. Consult prior episode plots only after independent candidates exist and use them for continuity and anti-repetition. Apply genre writer skills only **after** concept selection. Character notes preserve personality but do not mandate the same case type or dialogue beats.
- Prefer the shared reader flow over per-folder bespoke logic.
- Treat `doc.md` as the story source of truth.
- Before creating a work folder `index.html`, confirm `title.png` or `title.jpg` exists.
- If neither cover file exists after writing the story, create a story-appropriate cover image and save it as `title.png`.
