# FP向きのディレクトリ構造.md

```text
app/
  core/
    combinators.py      # compose/pipe など高階関数
    types.py            # 型(alias)/プロトコル/データ構造（任意）
  domain/
    normalize.py        # 純粋変換（正規化）
    validate.py         # 純粋判定（検証）
    compute.py          # 純粋計算（集計/算出）
  pipeline/
    user_flow.py        # domain の関数を合成して “流れ” を作る
  io/
    repository.py       # DB/API/ファイルなどI/O
    presenter.py        # 表示/JSON化などI/O寄り
  main.py               # エントリーポイント

```
