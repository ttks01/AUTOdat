#
# python3 plot2dP.py
#
import matplotlib.pyplot as plt
import pandas as pd
import glob

###########
Xidx=4
Yidx=9
filesPS = glob.glob('./Branch-P-S-*.csv')
filesPU = glob.glob('./Branch-P-U-*.csv')

print("filePS=", filesPS)
print("filePU=", filesPU)
# axis name
df = pd.read_csv(filesPS[0], index_col=0)
col=df.columns.values
plt.xlabel(col[Xidx])
plt.ylabel(col[Yidx])
# Periodic-Stable  
for fname in filesPS:
  df = pd.read_csv(fname, index_col=0)
  col=df.columns.values
  plt.plot(df[col[Xidx]].values,df[col[Yidx]].values,linestyle='-',color="red")
# Periodic-Untable
for fname in filesPU:
  df = pd.read_csv(fname, index_col=0)
  col=df.columns.values
  plt.plot(df[col[Xidx]].values,df[col[Yidx]].values,linestyle=':',color="red")
  
plt.legend()
plt.savefig("bif-PERIOD-2d.png")
plt.show()
