# 
# AUTOdatb.py
#  ver. 0.0.1
#  by T.Takaishi (2021-11-28)
#
# $ python3 AUTOdatb.py < b.XXX
#
import matplotlib.pyplot as plt
import pandas as pd


def msave(dd):
   n=len(dd)
   for idx in range(n):
     df1=dd[idx]
     if(len(df1) > 2):
       nb=int(df1.iat[1,0]) # 2nd data (The last data of previous one may be set at 1st data)
       pt=int(df1.iat[1,1]) # 2nd data
       if(pt < 0): # Unstable
          stability='U'
       else: # Stable
          stability='S'
       if(nb < 0): # Periodic solution
          sol='P'
       else: # Steady solution
          sol='S'
       df1.to_csv('Branch-%s-%s-%d.csv' % (sol, stability, idx))

def mplot(dd, col1, col2):
   n=len(dd)
   for idx in range(n):
     df1=dd[idx]
     #print(df1)
     if(len(df1) > 2):
       nb=int(df1.iat[1,0]) # 2nd data (The last data of previous one may be set at 1st data)
       pt=int(df1.iat[1,1]) # 2nd data
       if(nb < 0): # Periodic solution
         if(pt < 0): # P-Unstable
           ls='-.'
         else: # P-Stable
           ls='--'
       else: # Steady solution
         if(pt < 0): # S-Unstable
           ls=':'
         else: # S-Stable
           ls='-'
       plt.plot(df1[col1], df1[col2],label=nb, linestyle=ls, linewidth=2)
   plt.xlabel(col1)
   plt.ylabel(col2)
   plt.legend()
   plt.savefig("bif.png")
   plt.show()

######################
BRoutput = False
nfile = 0
pPT=0
label=[]
branch=[]
col=[]
while True:
   try:
      line = input()
   except EOFError:
       print("End of a branch #{}".format(nBR))
       #print(df)
       branch.append(df)
       break
   except:
       print ("Error:")
       break
   #print ("line:"+line)
   s = line.split() # 'a b c' -> ['a','b','c']
   nval = len(s)
   #print ("nval={}".format(nval))
   if(nval == 0):
      break;
   else:
      IBR=int(s[0])   # idx of BRANCH
      if(IBR == 0): # No data
         if (BRoutput==True): # Stop BR output
            print("End of a branch #{}".format(nBR))
            #print(df)
            branch.append(df) # append branch data
            BRoutput = False # turned off
            nPT=0
            #bplot(df,col[4],col[5],nBR)
            #plt.show()
      else:
         #   DUMMY,IBR,MTOT,ITP,LAB,PAR = s[0], s[1], s[2], s[3], s[4], s[5]	
         snum=list(map(float, s)) # strings -> float
         LAB=int(s[3])   # idx of LABEL
         PT=int(s[1])   # idx of POINT
         print("IBR=%d, LAB=%d" % (IBR,LAB))
         # Write LABEL data
         if (LAB > 0):
            label.append([LAB,[snum]])
         # 
         if (BRoutput==False): # Start BR output
            nfile=nfile+1
            nBR=IBR
            BRoutput = True   # Swith to output
            col=s1.copy()
            print("IBR=%d" % IBR)
            print("col=%s" % col)
            print("s=%s" % s)
            df=pd.DataFrame([snum], columns=col) # start branch data
            #print(df)
         else: # Write BR data
            if(PT * pPT < 0): # change stability
               print("Stability is changed")
               #print(df)
               branch.append(df) # append branch data
               nfile=nfile+1
               snum1=df.iloc[-1] # last data -> 1st data
               df=pd.DataFrame([snum1], columns=col) # start branch data
            # Wite point data
            df=df.append(pd.DataFrame([snum], columns=col))
            #print(df)
         pPT = PT # store Point number
      s1=line.replace('MAX ', 'MAX-').split() # store current line with replacing
      
#
#print(branch)
mplot(branch,col[4],col[5])
msave(branch)

#print(branch[0])
#print(label)
