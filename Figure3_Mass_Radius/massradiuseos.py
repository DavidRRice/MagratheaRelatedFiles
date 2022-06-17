#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:42:36 2020

@author: davidr
"""

from matplotlib import pyplot as plt
import re
from astropy import constants as const
import numpy as np

plt.rcParams['font.family'] = 'Times New Roman'
params = {'text.usetex': False, 'mathtext.fontset': 'stixsans'}
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 13

earthrad=const.R_earth.si.value/1000

corefiles=['default','default2000','seager','bouch','dor','wicks7si','wicks15si']
mantfiles=['default','default2000','seager','prem','oganov','shimpv']
waterfiles=['defaultbez','seager','zeng','frank','grande','herm']

clabels=['CD','CD-2000','CS','C1','C2','CW1','CW2']
mlabels=['MD','MD-2000','MS','MP','M1','M2']
wlabels=['WD','WS','W1','W2','W3','W4']

mass=np.arange(0.5,10.1,0.1)
corerad=[]
mantrad=[]
waterrad=[]

for i in corefiles:
    inf=open('out'+i+'core.txt')
    lines=inf.readlines()
    temp=[]
    for line in lines[1:]:
        div=re.split('\s+',line)
        temp.append(float(div[7]))
    corerad.append(temp)
    inf.close()
    
for i in mantfiles:
    inf=open('out'+i+'mant.txt')
    lines=inf.readlines()
    temp=[]
    for line in lines[1:]:
        div=re.split('\s+',line)
        temp.append(float(div[7]))
    mantrad.append(temp)
    inf.close()
    
for i in waterfiles:
    inf=open('out'+i+'water.txt')
    lines=inf.readlines()
    temp=[]
    for line in lines[1:]:
        div=re.split('\s+',line)
        temp.append(float(div[7]))
    waterrad.append(temp)
    inf.close()

plt.figure(figsize=(8,6))
grid = plt.GridSpec(3, 3, wspace=0.45, hspace=0.3)
plt.subplot(grid[:3,:2])

ls=['solid','dashed','dotted',(0,(3,1,1,1)),(0,(5,1,1,1,1,1)),(0,(5,1)),'dashdot']
ws=['solid','dotted',(0,(3,1,1,1)),(0,(5,1,1,1,1,1)),(0,(5,1)),'dashdot']
lw=1.8
zo=[0,7,6,5,4,3,2,1]
colors = plt.cm.tab20((np.arange(20)).astype(int)) 
np.random.seed(82020)
cshuffle=np.random.shuffle(colors)
cc=['xkcd:mahogany','tab:orange','red','xkcd:raspberry','xkcd:coral','xkcd:cinnamon','firebrick'] 
cma=['k','tab:orange','xkcd:kermit green','xkcd:muddy yellow','xkcd:raw sienna','xkcd:olive'] 
cw=['darkslategray','b','xkcd:azure','rebeccapurple','xkcd:turquoise','violet']
 
for i in range(len(corerad)):
    plt.plot(mass,corerad[i],lw=lw,ls=ls[i],label=clabels[i],c=cc[i],zorder=zo[i])
    
for i in range(len(mantrad)):
    plt.plot(mass,mantrad[i],lw=lw,ls=ls[i],label=mlabels[i],c=cma[i],zorder=zo[i])

for i in range(len(waterrad)):
    plt.plot(mass,waterrad[i],lw=lw,ls=ws[i],label=wlabels[i],c=cw[i],zorder=zo[i])

plt.text(6,1.1,'100% core',color='dimgrey',fontsize=16)    
plt.text(6,1.62,'100% mantle',color='dimgrey',fontsize=16) 
plt.text(6,2.55,'100% water',color='dimgrey',fontsize=16) 
plt.tick_params(labelsize=18)
plt.xticks([2,4,6,8,10])
plt.xlabel(u'M$_\oplus$',fontsize=20)
plt.ylabel(u'R$_\oplus$',fontsize=20)
#plt.savefig('massradall.pdf',bbox_inches='tight')
#plt.show()  
#plt.close() 

corediff=[np.zeros(len(corerad[0]))]
mantdiff=[np.zeros(len(mantrad[0]))]
waterdiff=[np.zeros(len(waterrad[0]))]
for i in corerad[1:]:
    corediff.append((np.array(i)-np.array(corerad[0]))/np.array(corerad[0])*100)
for i in mantrad[1:]:
    mantdiff.append((np.array(i)-np.array(mantrad[0]))/np.array(mantrad[0])*100)
for i in waterrad[1:]:
    waterdiff.append((np.array(i)-np.array(waterrad[0]))/np.array(waterrad[0])*100)  

plt.subplot(grid[0,2])    
for i in range(len(waterdiff)):    
    plt.plot(mass,waterdiff[i],lw=lw,ls=ws[i],label=wlabels[i],c=cw[i],zorder=zo[i])
plt.plot(np.zeros(1), np.zeros([1,1]), color='w', alpha=0, label=' ')
plt.plot(np.zeros(1), np.zeros([1,1]), color='w', alpha=0, label=' ')
plt.axis([0,10.5,-8.0,6.0])
plt.xticks([2,4,6,8,10])  
plt.yticks([-5,0,5])
plt.tick_params(labelsize=16)
plt.legend(bbox_to_anchor=(0.8, 2.1, -2.70, -0.1), ncol=2, borderaxespad=0.,frameon=False,fontsize=15)

plt.subplot(grid[1,2])
plt.plot(np.zeros(1), np.zeros([1,1]), color='w', alpha=0, label=' ')     
plt.plot(np.zeros(1), np.zeros([1,1]), color='w', alpha=0, label=' ') 
for i in range(len(mantdiff)):    
    plt.plot(mass,mantdiff[i],lw=lw,ls=ls[i],label=mlabels[i],c=cma[i],zorder=zo[i])
plt.tick_params(labelsize=16)
plt.legend(bbox_to_anchor=(0., 3.4, -0.83, -0.1), ncol=2, borderaxespad=0.,frameon=False,fontsize=15,columnspacing=1.4)
plt.ylabel(u'$\Delta$R/R$_{D}$ (%)',fontsize=20)
plt.axis([0,10.5,-8.0,6.0])
plt.xticks([2,4,6,8,10])    
plt.yticks([-5,0,5])  


plt.subplot(grid[2,2])
for i in range(len(corediff)):    
    plt.plot(mass,corediff[i],lw=lw,ls=ls[i],label=clabels[i],c=cc[i],zorder=zo[i])

plt.axis([0,10.5,-8.0,6.0])
plt.xticks([2,4,6,8,10])
plt.yticks([-5,0,5])  

plt.xlabel(u'M$_\oplus$',fontsize=20)  

plt.legend(bbox_to_anchor=(0., 4.7, 1.05, -0.1), ncol=2, borderaxespad=0.,frameon=False,fontsize=15,columnspacing=1.5)
plt.tick_params(labelsize=16)

plt.savefig('eosall3.pdf',bbox_inches='tight')    
plt.show()
plt.close()    
    
    
    
    
    