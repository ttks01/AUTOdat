#
# python3 plot3dP.py
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
Zidx=9
filesPS = glob.glob('./Branch-P-S-*.csv')
filesPU = glob.glob('./Branch-P-U-*.csv')

print("filePS=", filesPS)
print("filePU=", filesPU)
# axis name
df = pd.read_csv(filesPS[0], index_col=0)
col=df.columns.values
ax=fig_init(col[Xidx],col[Yidx],col[Zidx])
# Periodic-Stable  
for fname in filesPS:
  df = pd.read_csv(fname, index_col=0)
  col=df.columns.values
  fig_plot(ax,df[col[Xidx]].values,df[col[Yidx]].values,df[col[Zidx]].values,'-',"red")
# Periodic-Untable
for fname in filesPU:
  df = pd.read_csv(fname, index_col=0)
  col=df.columns.values
  fig_plot(ax,df[col[Xidx]].values,df[col[Yidx]].values,df[col[Zidx]].values,':',"red")
  
plt.savefig("bif-PERIOD-3d.png")
plt.show()
