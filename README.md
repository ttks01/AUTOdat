# AUTOdat
AUTOdatb, AUTOdats は分岐解析ツール AUTO の b.XXX や s.XXXX という出力ファイルから個別のデータを切り出す script です。
## AUTOdatb
b.XXX ファイルからブランチデータとラベルデータをファイルに書き出します。

`$ python3 AUTOdatb.py < b.XXX`

- Branch-X-Y-n.csv : ブランチデータ (ただし n はブランチ番号ではありません。）
  - X=S(steady solution),P(periodic solution)
  - Y=S(stable), U(unstable)
- LABEL-n.csv  : ラベル番号 n のデータ
