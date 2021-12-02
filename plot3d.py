#
# python3 plot3d.py
#
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import glob

def fig_init(col1,col2,col3):
   # Figureを追加
   fig = plt.figure(figsize = (8, 8))
   # 3DAxesを追加
   ax = fig.add_subplot(111, projection='3d')
   #
   #ax.set_title("Helix", size = 20)
   #
   ax.set_xlabel(col1, size = 14)
   ax.set_ylabel(col2, size = 14)
   ax.set_zlabel(col3, size = 14)
   # 
   #ax.set_xticks([-1.0, -0.5, 0.0, 0.5, 1.0])
   #ax.set_yticks([-1.0, -0.5, 0.0, 0.5, 1.0])
   ax.view_init(azim=-80, elev=20)
   return ax

def fig_plot(ax, x, y, z, lstyle, col):
   ax.plot(x, y, z, linestyle=lstyle, linewidth=2, color = col)
   
###########
Xidx=4
Yidx=6
Zidx=7
filesSS = glob.glob('./Branch-S-S-*.csv')
filesSU = glob.glob('./Branch-S-U-*.csv')
filesPS = glob.glob('./Branch-P-S-*.csv')
filesPU = glob.glob('./Branch-P-U-*.csv')

print("fileSS=", filesSS)
print("fileSU=", filesSU)
print("filePS=", filesPS)
print("filePU=", filesPU)
# axis name
df = pd.read_csv(filesSS[0], index_col=0)
col=df.columns.values
ax=fig_init(col[Xidx],col[Yidx],col[6])
# Steady-Stable
for fname in filesSS:
  df = pd.read_csv(fname, index_col=0)
  col=df.columns.values
  #print(col[Xidx])
  #print(df[col[Xidx]])
  fig_plot(ax,df[col[Xidx]].values,df[col[Yidx]].values,df[col[Zidx]].values,'-', "black")
# Steady-Unstable
for fname in filesSU:
  df = pd.read_csv(fname, index_col=0)
  col=df.columns.values
  fig_plot(ax,df[col[Xidx]].values,df[col[Yidx]].values,df[col[Zidx]].values,':',"black")
# Periodic-Stable  
for fname in filesPS:
  df = pd.read_csv(fname, index_col=0)
  col=df.columns.values
  fig_plot(ax,df[col[Xidx]].values,df[col[Yidx]].values,df[col[Zidx]].values,'-',"red")
# Periodic-Unstable
for fname in filesPU:
  df = pd.read_csv(fname, index_col=0)
  col=df.columns.values
  fig_plot(ax,df[col[Xidx]].values,df[col[Yidx]].values,df[col[Zidx]].values,':',"red")
  
plt.savefig("bif-3d.png")
plt.show()
