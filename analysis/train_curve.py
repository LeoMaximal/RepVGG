import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.size']=20

epochs=52
loss=np.zeros(epochs)
acc=np.zeros((2,epochs))
lr=np.zeros(epochs*11)
count1=0
count2=0
f=open('/Users/leoma/Programming/Python/RepVGG/analysis/log_A0.txt')
for i in range(1374):
    if (i-149)%24==0 and i>=149:
        if (i-149)/24 < 10:
            loss[count1]=float(str[83:93])
            acc[0,count1]=float(str[110:115])
            acc[1,count1]=float(str[132:137])
        else:
            loss[count1]=float(str[84:94])
            acc[0,count1]=float(str[111:116])
            acc[1,count1]=float(str[133:138])
        count1+=1
    str=f.readline()
    if str.find('cur lr') != -1 and count2 <= epochs*11:
        lr[count2]=float(str[9:21])
        count2+=1
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

x=np.linspace(0,epochs,epochs*11)
fig,ax=plt.subplots(figsize=(8,8))
ax.plot(x,lr)
ax.set(xlabel='epoch',ylabel='learning rate')
plt.savefig('lr.png')