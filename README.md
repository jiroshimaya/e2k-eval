# e2k-eval

英語とカタカナの変換精度を評価するためのツールです。
[e2k](https://github.com/Patchethium/e2k)、[english2kana](https://github.com/m7142yosuke/english2kana)というライブラリについて、[bep-eng.dic](https://fastapi.metacpan.org/source/MASH/Lingua-JA-Yomi-0.01/lib/Lingua/JA)を正解としたときの精度や速度を算出します。

# 使い方

## 評価データのダウンロード

```
# local/bep-eng.dicが作成されます。
sh scripts/download_dict.sh
```

## e2k評価の実行

誤り事例と評価値が出力されます。

```
uv run src/e2k_eval/core/evaluate_e2k.py
```

```
...
('PRACTICABILITY', 'プラクティカビリティー', 'プラクチキャビリティー')
('ANTIBODY', 'アンティボディー', 'アンチボディー')
Accuracy: 36.00%
Average Edit Distance: 0.220
Average Kana Distance: 1.465
Time: 0.036 seconds / per item
```

## english2kana評価の実行

誤り事例と評価値が出力されます。

```
uv run src/e2k_eval/core/evaluate_english2kana.py
```

```
...
('PRACTICABILITY', 'プラクティカビリティー', 'プラクティカビリティ')
('ANTIBODY', 'アンティボディー', 'アンティボディ')
Accuracy: 25.00%
Average Edit Distance: 0.371
Average Kana Distance: 2.356
Time: 0.436 seconds / per item
```

# 評価指標について
- Accuracy: 変換結果と正解結果が完全一致した割合
- Average Edit Distance: 変換結果と正解結果の相対編集距離の平均値
- Average Kana Distance: 変換結果と正解結果の子音や母音の類似度を考慮した相対編集距離の平均。子音、母音の類似度は[kanasim](https://github.com/jiroshimaya/kanasim)を用いて計算されます。

## 📄 ライセンス

本リポジトリはMITライセンスで提供されます。

本ツールで評価データに用いるbep-eng.dicはGPLv2ライセンスですが、本リポジトリではダウンロードスクリプトのみを提供し、再配布は行っていため、本リポジトリのライセンスはMITライセンスに保たれます。