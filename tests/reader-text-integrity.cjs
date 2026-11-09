// Pure splitting checks: layout remains covered by reader-pagination.html.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const html = fs.readFileSync('book.html', 'utf8');
const code = html.slice(html.indexOf('    function splitParagraphAcrossPages'), html.indexOf('  </script>'));
for (const capacity of [4, 9, 30, 71]) {
 const context = vm.createContext({ Intl, Array, Error, fitsBlocksInPage: (_, blocks) => blocks[0].text.length <= capacity });
 vm.runInContext(code, context);
 for (const text of ['。\nあ。い。う。え。', '最初。次。'.repeat(100), '  空白\n\n改行。途中 の空白。\n末尾  ', '長い見出し'.repeat(100), '😀か\u3099'.repeat(100)]) {
  const chunks = context.splitParagraphAcrossPages(null, text, 'p');
  assert.equal(chunks.join(''), text);
  assert(chunks.every(c => c.length <= capacity));
 }
}
console.log('PASS: exact text and bounded chunks at 4 capacities');
