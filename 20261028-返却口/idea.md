# 返却口 — 制作記録

## 執筆前の設計
- 第一ジャンル：現代怪奇ホラー。三人称・水野に限った視点。技術の外挿や病原体による説明を置かない。犯人当て・謎解きではなく、声と身体の居場所がずれる恐怖を描く。
- 舞台：架空の町の移動図書館。読書週間の追加巡回で工場の交替勤務者向けに夜の貸出を行う。実在する自治体・図書館・企業の事件を示唆しない。
- 人物：司書の水野、六年組んでいる運転手の関。水野は仕事を終えたいが、同行者の危険を確かめずに去れない。関の「はいよ」と運転前の膝叩きで、身体と声を別々に先出しする。
- 核：移動図書館の返却箱に、いるはずのない関の声が聞こえる。戻って来た関の身体と箱の返事が一致しない。水野は連絡、明るい車外への退避を試みるが、箱の中から出る生身の手を見捨てられず、触れた瞬間に場所を奪われる。
- 段階：いつもの夜間貸出→一人の客と返却の音→同行者不在・箱からの返事→同行者の姿だけが戻る→外部連絡と退避→箱の手を引く→返却される側に置かれた声で閉じる。
- 異変の起源や万能な対処法は説明しない。一方、人物の動線・箱の構造・声の聞こえる位置・連絡を取る試みは明示する。電話不通、電池切れ、車の故障、光で止まる怪物は使わない。
- 終幕：救出と癒やしで閉じない。水野は帰宅せず、物理的な拘束と自分の声を他人が使用する状態が残る。単純な「全部夢」「本人が最初から死者」にはしない。
- 表紙方針：冒頭の通常業務と最初の違和感まで。返却箱から伸びる手、人物の入れ替わり、終幕の状況は描かない。
- 評価軸：恐怖の段階20／行動の納得20／声と空間の一貫性20／文章・身体感覚20／直近作品との差異20。

## 適用した手順
- main の AGENTS.md、UPDATE.md、shorts-reader-maintainer/SKILL.md と references/repo-layout.md を読了。
- mystery-writer/reviewer/reviser は適用範囲を確認。今回は解ける事件や探偵・真相説明を約束しない超自然ホラーで、六表による犯人特定設計は適用しない。専用ホラースキルはリポジトリに存在しない。一般の企画→本文→独立批評→改稿→実画素表紙比較→生成・HTTP検証を行う。
- 画像は built-in image_gen を使用。画像生成スキル読了。

## 時事の入口と日付確認（2026-10-28 05時台 JST）
- [FNNプライムオンライン「10月27日から『読書週間』がスタート！」](https://www.fnn.jp/articles/FNN/1140009)：公開は2026-10-27 06:00 JST。出来事は10月27日〜11月9日の読書週間開始。記事の本文を直接取得し日付を確認。
- [伊賀市「秋の読書週間」](https://www.city.iga.lg.jp/0000014464.html)：公開・更新は2026-10-23。行事期間10月27日〜11月9日、巡回車の案内を確認。実在の巡回車・名称・運行場所は小説へ移さず、「図書館が住民のところへ出向く」という文化活動のみを着想にした。
- 記事の文言・標語・人物を引用せず、読書週間と巡回図書館という一般的な事実から独立した怪奇小説を創作する。

## 重複・シリーズ・連作との差異
- 着手時 main は d7e8a2bfb07798cecf74dc18cff6c7c4869763c7。23作品、10月28日作品なし。作業フォルダもなし。新規 clone で既存未コミット作業を上書きしない。
- 実際の全 doc.md をシリーズ名で照合。麗華シリーズ最新は2026-10-18『獅子は席を外す』。同作本文・制作記録、および20260311-ポーは「通すな」と言わない/characters.mdを読んだ。10月28日は10日後で、14日以内条件の次回目安11月1日より前。今日は非シリーズ。
- 昨日『決闘は本日二回』の時代興行喜劇とは、時代・感情・人間関係・結末・画風を変える。
- 10/20『暗期』は実読。二人の労働者と超自然的な異変は共通するが、光と作業灯を利用した救助・救出後の日常という構造を採らない。今回は声と身体の分離、援助の判断の破綻、取り返せない閉塞を核にする。機器故障を障害の原因にしない。

## 設計の独立検討
- 独立の編集検討で「未完の一行を読むと発動」という呪物ルール、余白の手形、異様な客などの盛り込み過ぎを指摘された。読み上げによる発動・手形・呪いの解答は設計段階で削除。
- 残した助言：車は走れる、電話も使える。同行者を置き去りにできないという人の判断から危険へ進める。「声と身体の位置」の一点に絞る。

## 初稿の自己点検
- 初稿3122文字。自己評価85/100（恐怖18、行動16、声と空間17、文章17、差異17）。返却口へ取り込まれる場面は意図的超自然。それ以前の動線と、温かい手を見て救助へ戻る動機が成立するかを独立査読に依頼。
- 改稿予定：手の絆創膏を冒頭の通常動作で先に見せ、後段の救助の判断が都合のよい新情報に依存しないようにする。携帯を関へ渡す段で、手を握ったまま移動できるかの動線も確認する。本文変更前にここへ記録。

## 独立初稿批評と改稿指示
本文を執筆していない批評者が doc.md と idea.md、10/20『暗期』、10/27『決闘は本日二回』を読んだ。評価85/100：恐怖18、行動17、声と空間15、文章18、差異17。
1. 中：運転席の外から、後部の内扉に出る手を見る動線が抜けている。食堂へ戻る途中に車の後ろを回り、乗降口をのぞく動作を追加してから手を見せる。
2. 中：「主任には近い声のほうが聞こえる」という断定は水野限定視点を逸脱し、主任が異常を無視する保証にもなっている。説明を削り、箱内の声が本に遮られる感覚と、外の水野が受話口を耳へ当てる動作へ変更。主任が安全だと納得したとは書かない。
3. 小：反転の瞬間に「引き出そうとしていた」と解釈を説明し過ぎる。手首を握られる感触と頬に当たる本で位置の逆転を示す。
4. 『暗期』との労働者二人・救助・電話の共通骨格は残るため、電話対応を増やさず、声の居場所と身体の反転を中心にする。照明や機材による攻略・救助後の日常は導入しない。
以上を先に改稿方針として確定し、本文へ反映する。

## 改稿後の独立再批評
- 91/100：恐怖19、行動18、声と空間19、文章18、差異17。新たな重大問題なし、本文採用可。
- 後部への移動・手を見つける視線・携帯を渡す往復の補足で、通常空間と意図的な超自然の反転を区別できた。主任側の聴取断定を削り、接続があるのに救われない形を保った。
- 軽微な重複として、絆創膏を先出ししたあとの「朝、積み込みで切った」再説明を削る。水野自身が渡した絆創膏だという個人的な記憶は残す。

## 表紙制作と実画素比較
- built-in image_gen で新規生成。採用元 PNG は1086×1448、縦3:4。物語の冒頭付近、移動図書館の返却口で物音に顔を向ける水野を描いた。題字や文字は入れない。箱からの手、分身、取り込み、呼吸の終幕は示さない。
- 白とくすんだ緑の車体を大きく切り取り、冷色の衣服と青黒い夜、赤い尾灯を置く。左右非対称、人物の横顔・金属の投入口・開いた乗降口・背後の営業中の食堂を同一画面にした。油彩／ガッシュに似たマットな写実感で、温かな懐旧風にはしない。
- 元画像と公開JPEGの実画素を確認。指・腕・顔に明確な破綻なし、箱の収納と本棚が読める。人物の表情は絶叫でなく不審な物音への警戒。話の始まりに留める意図と一致する。
- 直近五枚の実画像を並べて比較。10/20の無人で対称的な暗い廊下、10/21の黄色い正面喜劇像、10/25の宇宙のアクション、10/26の明るい駅の母娘、10/27の木版調の舞台競争のいずれとも構図・色・人数・光が異なる。今回の白い車体と大きい現代女性の横顔、生活者のいる背景を中心に採用。
- 独立画像レビューも採用可。本文で外側投入口を「右側」と限定した箇所と、画面の後面らしい位置に軽微な差を指摘された。動線を変えず「返却口の前」として不要な方向限定を削除。車の本棚・貸出台・後部入口の関係は維持する。
- JPEGは同じ画像を1086×1448のままquality72/subsampling2で再符号化、174100bytes。原寸と縮小で顔・手・投入口・書棚の可読性を確認。絵の内容の加工ではない。元PNGは制作資料として保存し、通常ignoreされるため公開Gitには含めない。

### 画像生成プロンプト
Use case: illustration-story. Create a finished literary cover illustration for a contemporary Japanese supernatural horror short story titled '返却口', but put NO TEXT anywhere. Portrait 3:4 full bleed. Depict an EARLY scene only, before any explicit supernatural event: a Japanese woman librarian in her late thirties, short black hair, ordinary pale blouse and dark teal cardigan, has paused at the open rear passenger entrance of a modest white-and-muted-green mobile library minibus parked outside a factory cafeteria at night. She is seen in a close three-quarter SIDE view at the edge of the frame, her hand hovering above a low book return cabinet inside the rear doorway, head turning slightly as if she heard a sound she cannot locate. Her expression is alert and uneasy, not screaming. Clearly visible within the doorway are a small librarian's counter, low shelves holding books of different thickness, and the open rectangular inner door of the return compartment below the counter, containing only several normal books and ordinary dark space. Camera at waist height outside the bus, strong asymmetrical crop with the bus's large off-white body panel and a horizontal exterior book return slot taking up much of the left foreground; librarian and open rear doorway on the right, door and cabinet geography coherent. A sliver of blue-black night and distant brightly illuminated factory cafeteria windows behind, no ominous abandoned building. Style: sophisticated restrained cinematic gouache and charcoal editorial illustration, realistic anatomy, matte tactile painted surfaces, fine grain, subtly unsettling mundane realism rather than graphic novel or anime. Palette: pale mint, cold chalk white, ink navy, a single muted red rear taillight; cool fluorescent interior light. Make the white vehicle against night read clearly at thumbnail size; not an all-black image. No paper lettering, no readable book titles, no typography, no logo, no watermark. Absolutely NO monster, NO extra hands, NO hand emerging from box, NO body in box, NO duplicate person, NO blood, NO ending reveal, NO ghost face, NO mirror trick, NO magical glow. Just an ordinary working woman at a mobile library and an uneasy pause. Not a symmetrical corridor, not an isolated still life, not a warm nostalgic scene.

## 生成・公開前検証
- 最終本文3173文字（見出し・空白を含む）。元PNGと公開JPEGを保持。
- 標準generate_reader.pyで全24作品のwrapperとcatalog・cover-versions.jsonを生成。生成器の既存挙動により3/13『綴じ穴は三つある』の独自の短い紹介も変わるため、同作wrapperとcatalogの同作カードだけはmainの内容をbyte単位で保持した。本日の作品以外の本文・表紙・wrapperは変更しない。
- py_compile、scripts/check_site.pyによる24作品のHTTP読込・本文・JPEG署名・表紙SHA URL・wrapper/reader/catalog版整合、共有readerのJavaScript構文、git diff --checkを確認。
- 実ブラウザでのページ分割・ページ送り・公開URLの描画確認は公開後の担当者による検証待ち。ここでは合格したと主張しない。ローカルHTTPリソース取得検査と実画素表紙レビューは別々に実施済み。
- 公開対象6ファイル：新作doc.md、idea.md、title.jpg、index.html、およびroot index.html、cover-versions.json。mainへの通常の非force更新のみ。公開後remote SHA/全6ファイル一致とGitHub Pagesを別に検証する。
