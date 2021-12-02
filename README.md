# AUTOdat
AUTOdatb, AUTOdats は分岐解析ツール AUTO の b.XXX や s.XXXX という出力ファイルから個別のデータを切り出す script です．
## AUTOdatb.py
b.XXX ファイルからブランチデータとラベルデータをファイルに書き出します．

`$ python3 AUTOdatb.py < b.XXX`

- Branch-X-Y-n.csv : ブランチデータ (ただし n はブランチ番号ではありません．）
  - X=S(steady solution),P(periodic solution)
  - Y=S(stable), U(unstable)
- LABEL-n.csv  : ラベル番号 n のデータ
### plot3d.py
Branch-X-Y-n.csv ファイルから3次元分岐図を作成します．
### plot3dP.py
Branch-P-Y-n.csv ファイルから，PERIODを使って周期解の3次元分岐図を作成します．
### plot2dP.py
Branch-P-Y-n.csv ファイルから，周期解の2次元分岐図(y軸はPERIOD)を作成します．
