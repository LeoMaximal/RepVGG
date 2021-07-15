import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.size']=20

epochs=52
loss=np.zeros(epochs)
acc=np.zeros((2,epochs))
count=0
f=open('/Users/leoma/Programming/Python/RepVGG/analysis/log_A0.txt')
for i in range(1374):
    if (i-149)%24==0 and i>=149:
        if (i-149)/24 < 10:
            loss[count]=float(str[83:93])
            acc[0,count]=float(str[110:115])
            acc[1,count]=float(str[132:137])
            print(float(str[83:93]))
            print(float(str[110:115]))
            print(float(str[132:137]))
        else:
            loss[count]=float(str[84:94])
            acc[0,count]=float(str[111:116])
            acc[1,count]=float(str[133:138])
            print(float(str[84:94]))
            print(float(str[111:116]))
            print(float(str[133:138]))
        count+=1
    str=f.readline()
f.close()

fig,ax=plt.subplots(figsize=(8,8))
ax.plot(loss)
ax.set(xlabel='epoch',ylabel='loss')
plt.savefig('loss.png')

fig,ax=plt.subplots(figsize=(8,8))
ax.plot(acc[0],label='Top 1')
ax.plot(acc[1],label='Top 5')
ax.set(xlabel='epoch',ylabel='accuracy(%)')
ax.legend()
plt.savefig('acc.png')