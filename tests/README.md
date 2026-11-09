# Reader regression checks

- `node tests/reader-text-integrity.cjs`: verifies that splitting retains the exact source text, including punctuation, newlines and Unicode, under multiple simulated capacities.
- Serve the repository over HTTP and open `tests/reader-pagination.html`, then click **Run tests**. It tests the actual shared runtime in 390×844, 775×1205, 1366×768 and 1920×1080 frames, with the reported novella, long prose, unpunctuated Japanese, punctuation/newlines, Latin, Unicode and long headings. It checks text reconstruction and the rendered line rectangles of every generated text page. The frames remain available for visual/navigation inspection.

The HTML suite does not modify stored stories. It checks actual geometry, not only scrollWidth: vertical-rl overflow can extend to negative x, and clipping can conceal it from an ancestor's scroll dimensions. Keep measurement and visible text-box styles identical. Do not append punctuation after a prefix has been measured; shorten a split boundary instead.

The first regression commit intentionally runs against the old reader to demonstrate the reported failure. The runtime fix also refreshes all generated wrapper/cache versions, without changing story text, cover images or the catalog's editorial order and descriptions.
