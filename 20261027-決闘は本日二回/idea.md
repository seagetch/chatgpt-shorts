# 決闘は本日二回 — 制作メモ

## 本文前の設計
- ジャンル：時代活劇喜劇／興行ファルス。SFではない。時代・町・人物・興行は創作。江戸末期を思わせる架空の港町の影絵小屋。史実を再現した作品ではない。
- 視点・語り：三人称。算盤勘定と大げさな武士言葉の衝突。会話、足運び、影の大小、観客の反応で加速する。第一人称の内省、自己受容、手放し、終幕の小さな家事動作を使わない。
- 対立：ともに「天下無双」を掲げる二人の道場主が、看板を賭けて木刀で勝負する。雨で場所を失い、影絵小屋へ。小屋の女将は修理費と入場料を取り、主人は勝負を影芝居に仕立てる。どの人物も自分の利益を追い続ける。
- 局所的な行動理由：剣士は客の前で逃げたと言われたくない／小屋を借りるため物損弁償と木刀使用に同意／女将は雨の日の売上を取り戻したい／影絵師は大きな影と筋立てで客を沸かせたい。
- 段階：雨宿りと場所貸し交渉→物損価格により足場が狭くなる→影の大きさと悪役呼ばわりに反応して相互妨害→一本の決着より客の要求が強くなる→双方の看板と出演料を賭けた次の興行へ。
- 結末方針：二人は和解しない。相手が欠けると興行と再戦が成り立たないため、敵を風邪から守って同じ傘を奪い合う。意地を捨てるのでなく意地の用途が増える、声と動きのある喜劇的決着。
- 評価軸：各行動の因果20／掛け合いと身体的笑い20／時代喜劇の声と可読性20／直近作との差異20／結末の回収20。初稿後と独立読解後に改稿する。
- 謎解きではなく全員の意図を見せるファルス。mystery-writer/reviewer/reviserは確認したが、犯人・トリック・探偵構造を設けないため六表によるフェアプレイ設計は適用しない。shorts-reader-maintainerとimagegenを適用。

## 時事の入口（2026-10-26 UTC調査）
第39回東京国際映画祭が10月26日に開幕したという公式の当日レポートを確認。雨のレッドカーペットを透明傘の列が進む風景から、「雨で屋外の催しが屋内へ押し寄せる」「観客が出来事を興行に変える」という動きを取り出した。現実の映画祭を描いた作品ではなく、影絵興行の時代喜劇へ大きく転換する。実在人物の言動・不祥事は創作しない。
- [TIFF公式・2026年10月26日開幕レポート](https://2026.tiff-jp.net/news/en/?p=20984)：当日付検索取得で本文確認。直接openは取得エラーだったため、その事実も記録。映画祭の開始日、雨、透明傘のみを発想に利用し、記事の台詞や場面を転載しない。
- [第39回TIFF公式トップ](https://2026.tiff-jp.net/en/)：10月26日〜11月4日の開催期間、同日ニュースを確認。

## 継続・重複確認
- 着手時main：7c56c6d7ad489238191044f3fcfb192ff9dad714。最新2026-10-26『急がない部屋』。既存22作品。10月27日作品は未登録。
- 久条麗華シリーズ最新：2026-10-18『獅子は席を外す』。次回期限2026-11-01を維持。今日は非シリーズ。
- 最近10作のSF偏重だけでなく、第一人称と静かな心理決着の反復を避ける。10月21日の現代の芸人喜劇とも、歴史風の舞台、対等な二人の喧嘩、肉体的競争、未解消のライバル関係を軸に区別する。

## 初稿・自己点検
- 初稿3,764文字（空白込み）。自己評価85/100：因果16、笑い18、声18、差異17、結末16。
- 長所：看板の四文字という卑小な発端が、雨、修理代、観客、弟子、収入によって大きくなる。二人の意地は解消しない。影の大きさは光源との距離で一貫。
- 弱点：身体の絡まりを説明する言葉が不足。初稿の額への木刀打ちが喜劇の軽さより負傷を連想させる。人物の動きと台詞が主なので情景を増やしすぎない。

## 独立レビュー・改稿方針
独立レビュアーfarce_plotが本文と10月21日『王様の昼休み』を実読。初稿88/100（因果16/20、笑い18/20、声18/20、差異18/20、結末18/20）。「意図しない行動が観客に芸と取られる」という共通項はあるが、前作の一人の休憩・サービス欲・最後に隠れる構造と、本作の四者の利害・ライバルの継続・興行の増殖は別と判定。

修正を先に確定：
1. 幕へ平行に走れば衝突しないため、「幕の中央へ」を争うと限定。
2. 立ったまま袖を踏めないため、相手の「袴の裾」へ変更。
3. 額への本気の木刀打ちをやめ、双方が手首を絞った制御した肩への接触に変更。後段も額を押さえる絵でなく、互いの肩に木刀を載せる形へ。
4. 「合体！」の現代的な語感は時代ファルスの誇張として残す。史実の台詞再現ではない。

上記をdoc.mdに適用し、因果と身体配置を再読する。独立の初稿評を改稿後の採点と混同しない。

## 表紙制作・実画素レビュー
- built-in image_genで新規生成→限定編集。採用PNGは1086×1448、縦3:4。本文を読んだうえで、中盤以前の「壊せない小屋で木刀を振る二人と算盤の女将」を選択。結末の相打ち、二頭の合体影、相合傘は見せない。文字・題名・ロゴなし。
- 構図：狭い木組みの舞台を斜め上から見る三者配置、誇張した止めの動作と幕の大小の影。木版画風の輪郭、木地の茶、藍、錆朱。日常の静物や孤独な背中ではなく、競争と身振りを正面に置く。
- 初版の欠点：幕と人物の間に光源があり、影の投影方向と矛盾。右の影に目鼻が残っていた。独立レビュアーも同じ問題を指摘。image_genでその灯籠だけ除去し、前景画面外からの光源に変更、両影を内部描写のない平坦なシルエットへ修正。人物・画風・配色は維持。修正版実画素で修正を確認。
- 原寸と縮小で確認：木刀であって金属刀ではない。手足に致命的破綻なし。右人物の長い腕は戯画的な誇張。女将の算盤、二者の対抗姿勢、雨景が縮小でも読める。木版風の密度は高いが、大きな明るい幕と黒い影が焦点を作る。
- 実画素を直近5枚と並べて比較：10/26の駅で向かい合う母娘（柔らかな描画と昼光）、10/25の宇宙の斜めアクション、10/21の黄色地の正面座像、10/20の暗い廊下の奥行き、10/19の空中気球の淡彩。今回の舞台の切り取り、三者の戯画的身振り、木版調の黒い輪郭と影は明確に別。10/26とは茶系部分が共通しても、構図・光・表情・線の性格が異なる。独立レビューも差別化とネタバレなしを確認。
- 初版生成物は制作資料として保持。採用PNGをtitle.pngへコピーし、リポジトリ標準ジェネレーターで公開用title.jpgへ変換。

### 初回生成プロンプト
Use case: illustration-story. Create a finished portrait 3:4 literary book cover illustration with NO TEXT for a Japanese period slapstick short story, set in a fictional late-Edo-like port town's small shadow-puppet theatre on a rainy festival day. Scene is early in the story, NOT its ending. Two fiercely proud rival Japanese swordsmen in modest kimono and hakama, one stocky with a broad face in indigo, the other tall and lean with a long face in russet brown, holding WOODEN practice swords, are absurdly trying to duel in a cramped backstage space without damaging the posts or low ceiling. One is arrested mid-step in a low wide defensive stance, the other has suddenly drawn his wooden sword back just before a timber post, expressive comic indignation, anatomically coherent. A shrewd middle-aged Japanese theatre proprietress in a striped charcoal kimono stands safely at lower side of the scene, holding a wooden abacus and surveying them sternly. A broad translucent ivory theatre screen occupies the upper background; the men's enlarged black shadows fall onto it. Protected stage lamp behind a low wooden guardrail, sparse timber stage geometry, one glimpse of slanting rain outside the open side doorway. No spectators must be crowded onto the stage. Viewpoint: bold elevated three-quarter cutaway into the cramped backstage, a diagonally arranged triangular composition of three figures, full bodies and clear separation. Style: sophisticated lively Japanese woodcut-inspired editorial illustration, strong carved sumi-black contour marks, flat warm-ivory paper ground, restrained indigo and vermilion accent blocks, visible fine paper texture, humorous angular movements, not photoreal, not glossy anime, not a still life. Crisp graphic contrast and silhouettes legible as a small thumbnail. The image should feel boisterous and competitive, not sentimental or threatening. NO blood, NO metal blades, NO injuries, NO joined two-headed shadow, NO final shared umbrella, NO text, NO lettering, NO calligraphy, NO logo, NO watermark. Portrait 3:4 full bleed.

### 光源・影の限定編集プロンプト
Edit this existing book cover with ONLY two targeted optical corrections, preserving its portrait 3:4 composition, all three characters, facial expressions, body poses, wooden swords, timber stage, rainy exterior, palette, paper texture, and woodblock-inspired drawing style exactly. Correction 1: remove the glowing lantern currently BETWEEN the swordsmen and the rear ivory screen (at the center-right behind the stocky man's right side). There must be no lamp there. Instead establish the projection illumination as coming from a single low stage light off-canvas in the foreground, on the viewer's side of BOTH men, shining past them onto the rear screen. Do not add another visible object or move the characters. Correction 2: make the two cast shadows on the rear ivory screen physically coherent, FLAT uniform dark silhouettes of these two men and their raised wooden swords. Remove ALL internal facial features, eyes, nose lines, kimono details, pale holes, and highlights from within the shadows. Their outer silhouette contours may be preserved as much as feasible. A shadow is only an opaque silhouette, not a second drawing of a person. Preserve separate shadows, no joined monster. Keep everything else unchanged. No text, no logo, no watermark.

## 改稿後点検
- 「幕の中央」を取り合う動線、踏む対象を袴の裾へ変更、木刀は互いの肩へ制御した接触に変更。影の大小・灯りの位置・観客と舞台の分離・金銭配分・未決着の看板条件を再確認した。
- 源八が濡れた足袋を脱いでから試合する準備を一文補った。前半の水滴と、乾いた舞台／裸足の表紙の動作がつながる。
- 最終自己評価90/100（因果18、笑い18、声18、差異18、結末18）。独立初稿88点とは区別する。

## リーダー生成・公開前検査（2026-10-26 UTC）
- Pythonコンパイル、標準generate_reader.pyによる23作品生成、scripts/check_site.pyのHTTPリソース・キャッシュ版検査23作品、共有readerのJavaScript構文検査、git diff --checkを通過。
- 公開対象は新作doc.md、idea.md、title.jpg、index.html、およびルートindex.html、cover-versions.jsonの6ファイル。title.pngは生成元として別保存し、既定の.gitignoreに従い公開コミットへ含めない。
- 標準generatorは3月13日『綴じ穴は三つある』の既存短い紹介文も本文から再生成した。今回の範囲外のため、その旧wrapperとcatalog内の旧カードをHEADの内容へ戻した。その他既存作品の変更なし。復元後に23作品HTTP検査を再実行し通過。
- 公開前の実Chromium検査は未完了：sandbox起動はsocket作成拒否で起動前終了。正規の承認付き再実行はbwrapのread-only mountエラーで実行前終了。既存CUAクラウドブラウザは利用可能だが、隔離されたローカルHTTPには接続できなかった。アクセス制限を迂回せず、この段階で画面・操作・実ページ数が通過したとは記録しない。
- 公開担当へ、凍結した6ファイルと検証記録を引き渡す。実機の表紙／全本文／ページ送り／最終頁／再読込等の検証は、担当者が公開後の正規GitHub Pagesで行う。本文の都合でページ数を固定しない。

## 独立再レビュー（改稿後）
- 改稿後本文90/100（各軸18/20）、修正後表紙とも採用可。3点の本文修正、不要な灯籠の撤去、両影から目鼻を除いたことを実読・実画素で再確認。新たな重大欠陥なし。
- レビュアーは構想候補を提示した後、完成本文を別途独立読解した。本文・画像の編集は担当していない。評価範囲は物語と表紙であり、未完了のブラウザ検査の合格を意味しない。
