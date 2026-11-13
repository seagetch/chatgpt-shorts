// Pagination invariant checks, with a deterministic measure stub. Real geometry
// is checked separately by reader-pagination.html in four browser sizes.
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const assert = require('node:assert/strict');
const html = fs.readFileSync('book.html', 'utf8');
const parser = html.slice(html.indexOf('    function parseMarkdown'), html.indexOf('    async function waitForFonts'));
const pagination = html.slice(html.indexOf('    function paginateWork'), html.indexOf('    function fitsBlocksInPage'));
const splitting = html.slice(html.indexOf('    function splitParagraphAcrossPages'), html.indexOf('  </script>'));
const cases = [
 ['no final newline', '# 題\n\n最終文。'],
 ['one final newline', '# 題\n\n最終文。\n'],
 ['many final newlines', '# 題\n\n最終文。\n\n\n'],
 ['split final paragraph', '# 題\n\n' + '長い最終文。'.repeat(70) + '\n'],
 ['interior blank lines', '# 題\n\n第一段。\n\n\n\n第二段。\n'],
 ['spacers only', '\n\n\n'],
 ['heading only', '# 見出し\n\n'],
];
for (const dir of fs.readdirSync('.').filter(name => /^\d{8}-/.test(name))) {
 const filename = path.join(dir, 'doc.md');
 if (fs.existsSync(filename)) cases.push([dir, fs.readFileSync(filename, 'utf8')]);
}
let checked = 0;
for (const capacity of [1, 4, 9, 30, 71, 200]) {
 const node = () => ({ append() {}, remove() {} });
 const context = vm.createContext({
  Intl, Array, Error, document: { createElement: node, body: { append() {} } },
  fitsBlocksInPage: (_, blocks) => blocks.reduce((sum, b) => sum + (b.kind === 'spacer' ? 1 : b.text.length), 0) <= capacity,
 });
 vm.runInContext(parser + pagination + splitting, context);
 for (const [name, markdown] of cases) {
  const blocks = context.parseMarkdown(markdown);
  const pages = context.paginateWork({ blocks });
  assert.equal(pages[0].type, 'cover', name);
  const textPages = pages.slice(1);
  assert(textPages.every(p => p.blocks.some(b => b.kind !== 'spacer')), name + ': orphan space page');
  assert.equal(textPages.flatMap(p => p.blocks).map(b => b.text).join(''), blocks.map(b => b.text).join(''), name + ': changed text');
  for (const p of textPages) assert(context.fitsBlocksInPage(null, p.blocks), name + ': exceeds stub capacity');
  checked++;
 }
 // A final paragraph exactly filling its page used to leave a spacer-only page.
 const exact = context.paginateWork({ blocks: [{ kind: 'p', text: 'あ'.repeat(capacity) }, { kind: 'spacer', text: '' }] });
 assert.equal(exact.length, 2);
 checked++;
}
console.log(`PASS: ${checked} pagination cases, including all ${cases.length - 7} published stories; exact text and no spacer-only pages`);
