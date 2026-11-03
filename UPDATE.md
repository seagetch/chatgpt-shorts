# 更新環境

作業対象は `seagetch/chatgpt-shorts` の `main`。作品本文は各フォルダの `doc.md`、一覧と作品別 `index.html` は `generate_reader.py` が生成する。

## セットアップ

```sh
git clone --branch main https://github.com/seagetch/chatgpt-shorts.git
cd chatgpt-shorts
git lfs install --local
git lfs pull
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Windowsでは `.venv/bin/python` を `.venv/Scripts/python.exe` に読み替える。PNG変換はmacOSのsips、WindowsのPowerShell、その他の環境ではPillowを使用する。Git LFS管理のPNGを追加する場合はLFSの認証・アップロードも必要。

## 物語制作のスキル順序

新規短編の企画・執筆は `AGENTS.md` と `.codex/skills/shorts-production-orchestrator/SKILL.md` を入口とする。

1. `shorts-concept-planner` で幅広いジャンルと物語構造を独立に発案し、過去作はその後で重複検出・設定整合に使う。
2. 久条麗華シリーズなら、同じ企画段階で `reika-series-planner` を併用する（候補出しを二重にしない）。
3. 企画決定と `idea.md` 記録の後に、選んだ物語機構に応じ `mystery-writer` / `horror-writer` / `sf-short-writer` 等へ引き継ぐ。専門スキルがないジャンルを無理にミステリ化しない。
   - 小噺・落語風掌編、ライトノベル、異世界転生・転移、悪役令嬢も明示的な企画候補とし、純文学的な落ち着いた形式へ一律に寄せない。
4. 完成稿 `doc.md` を批判的に検証・改稿してから、`shorts-reader-maintainer` による表紙・reader・公開作業へ進む。表紙は作品内容への忠実性とジャンルらしさの両方を必須検証し、どちらかが不合格・未確認なら公開完了扱いにしない。

既存作の小修正、批評、reader保守は統括スキルの該当工程のみ適用する。完成・公開の状態は実際の検証結果に基づいて記録する。

## 編集・生成・検証

先に `AGENTS.md` と `.codex/skills/shorts-reader-maintainer/SKILL.md` を読む。既存の未コミット変更は保全する。新作には `doc.md` と表紙を置く。公開readerは `title.jpg` を読み込むのでJPEGを必ずコミットする。`title.png` は通常ignoreされている。

```sh
git pull --ff-only origin main
.venv/bin/python -m py_compile generate_reader.py
.venv/bin/python generate_reader.py
.venv/bin/python scripts/check_site.py
.venv/bin/python -m http.server 8000 --bind 127.0.0.1
```

HTTPで一覧、作品別ページ、共通readerの表紙・本文・ページ送りを確認する。サーバはCtrl+Cで終了する。

表紙を差し替えた場合も生成器を実行する。JPEGのSHA-256から表紙URLの `?v=` を生成し、一覧・SNSメタデータ・`cover-versions.json` に反映する。共通readerはこのJSONを毎回再検証して最新の表紙URLを取得する。作品ページと共通readerへのリンクも内容ハッシュでバージョン管理する。画像と生成されたHTML・JSONを一緒にコミットする。

## mainへの反映

```sh
git diff --check
git status --short
git add <変更したファイル>
git commit -m '<変更内容>'
git push origin HEAD:main
git ls-remote origin refs/heads/main
```

pushにはGitHub書き込み認証が必要。トークンをソースやログへ保存しない。このWorkでCLI認証がない場合は、接続済みGitHubコネクタの `create_blob` → `create_tree`（現在のmainのtreeを基点）→ `create_commit`（現在のmainを親）→ `update_ref`（branch_name=main、expected_sha=確認したmain、force=false）で同じ変更を反映できる。バイナリはbase64でblobを作成する。最後にmainを取得し、ローカルをfast-forwardしてSHA一致を確認する。競合時はmainを再取得して差分を見直す。

GitHub Pagesの公開状態はpushとは別に確認する。公開先: https://seagetch.github.io/chatgpt-shorts/
