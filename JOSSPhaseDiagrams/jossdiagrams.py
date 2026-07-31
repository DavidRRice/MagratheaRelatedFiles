# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 21:25:37 2025

@author: drice
"""


import numpy as np
import matplotlib.pyplot as plt
import re
import cmasher as cmr
from matplotlib.collections import LineCollection
plt.rcParams['font.family'] = 'Times New Roman'
params = {'text.usetex': False, 'mathtext.fontset': 'stixsans'}
plt.rcParams.update({'font.size': 20})



def lighten_color(color, amount=0.5):
    """
    Lightens the given color by multiplying (1-luminosity) by the given amount.
    Input can be matplotlib color string, hex string, or RGB tuple.

    Examples:
    >> lighten_color('g', 0.3)
    >> lighten_color('#F034A3', 0.6)
    >> lighten_color((.3,.55,.1), 0.5)
    """
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])

fig, axes = plt.subplots(1, 3, figsize=(15, 6.5), sharey=True, constrained_layout=True)
fig.set_constrained_layout_pads(wspace=0.0,w_pad=0.0)

ax = axes[0]
colors=['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:pink','tab:olive','tab:cyan','tab:gray']

lw=1.0
#inf=open('phaseline_ih_ii.txt','r')
a3 = 3.986300903e-09
a2 = -1.789026292e-06
a1 = 0.0009677787797
a0 = 0.02631882383


# Plot data and fitted curve
yp = np.linspace(0, 238.897, 5000)
xp = a3*yp**3+a2*yp**2+a1*yp+a0

ax.plot(xp, yp,color='k',lw=lw)


#print("Ice Ih to III, T-P")

a3 = 1.153769845e-08
a2 = -7.956399761e-06
a1 = 0.001642755909
a0 = 0.1140942871

# Plot data and fitted curve
yp = np.linspace(238.897, 251.126, 5000)
xp = a3*yp**3+a2*yp**2+a1*yp+a0

ax.plot(xp, yp,color='k',lw=lw)


#print("Ice Ih to water")
a3 = -32.26706488
a2 = -143.6159774
a1 = -74.97759097
a0 = 273.1683519

# Plot data and fitted curve
xp = np.linspace(0.0000001, 0.207592, 5000)
yp = a3*xp**3+a2*xp**2+a1*xp+a0

ax.plot(xp, yp,color='k',lw=lw)



#print("Ice II to III")
a3 = 10.6802119
a2 = -60.79880497
a1 = 108.5464607
a0 = 218.0347735

# Plot data and fitted curve
xp = np.linspace(0.209766, 0.355504, 5000)
yp = a3*xp**3+a2*xp**2+a1*xp+a0

ax.plot(xp, yp,color='k',lw=lw)



#print("Ice II to V")
a3 = 8.754511801
a2 = -42.36539788
a1 = -114.2410848
a0 = 294.9938885

# Plot data and fitted curve
xp = np.linspace(0.355504, 0.670843, 5000)
yp = a3*xp**3+a2*xp**2+a1*xp+a0


ax.plot(xp, yp,color='k',lw=lw)



#print("Ice III to V, T-P")
a3 = 2.669414392e-08
a2 = -1.786325179e-05
a1 = 0.003113786951
a0 = 0.2759414249

# Plot data and fitted curve
yp = np.linspace(249.419, 256.165, 5000)

xp = a3*yp**3+a2*yp**2+a1*yp+a0
ax.plot(xp, yp,color='k',lw=lw)



#print("Ice III to Water")
a3 = 99.49717929
a2 = -158.5333434
a1 = 100.0993404
a0 = 236.281993

# Plot data and fitted curve
xp = np.linspace(0.209766, 0.350109, 5000)
yp = a3*xp**3+a2*xp**2+a1*xp+a0

ax.plot(xp, yp,color='k',lw=lw)



#print("Ice V to VI Switch TP")
a3 = -1.970275298e-08
a2 = -1.858690183e-06
a1 = 0.003737731993
a0 = 0.1540994852

# Plot data and fitted curve
xt = np.linspace(201.933, 273.411, 5000)
yt = a3*xt**3+a2*xt**2+a1*xt+a0

ax.plot(yt, xt,color='k',lw=lw)


#print("Ice V to Water")
a3 = 47.24417282
a2 = -120.4230091
a1 = 143.9050041
a0 = 218.5209061

# Plot data and fitted curve
xp = np.linspace(0.350109, 0.634399, 5000)
yp = a3*xp**3+a2*xp**2+a1*xp+a0

ax.plot(xp, yp,color='k',lw=lw)


##VI Melting
a3 = 5.711742978
a2 = -39.67340784
a1 = 125.6893825
a0 = 208.5585936

# Plot data and fitted curve
xp = np.linspace(0.634399, 2.216, 5000)
yp = a3*xp**3+a2*xp**2+a1*xp+a0

ax.plot(xp, yp,color='k',lw=lw)


##II to VI
a3 = -3.607661344e-08
a2 = 1.032010899e-05
a1 = -0.002592049235
a0 = 1.070211316

# Plot data and fitted curve
yp = np.linspace(0, 201.933, 5000)
xp = a3*yp**3+a2*yp**2+a1*yp+a0

#ax.scatter(P_GPa, T_K, s=3,color=lighten_color(colors[0],0.5))
ax.plot(xp, yp,color='k',lw=lw)

##Ice VI-VII From AQUA
xp = np.linspace(0.5, 2.216, 5000)
yp = -1.4699e5+6.10791e-6*xp*1e9+8.1529e3*np.log(xp*1e9)-8.8439e-1*np.sqrt(xp*1e9)

ax.plot(xp, yp,color='k',lw=lw)


##New Ice VII Melting datchi
yt=np.linspace(355,1023,5000)
xp=2.17+1.253*(((yt/355)**3.0)-1)


ax.plot(xp, yt,color='k',lw=lw)


ax.hlines([700],11,30.9,ls='--',color='k',lw=lw)

##Ice X Melting
#yt=np.linspace(1634.6,2250,500)
yt=np.linspace(1280,2250,5000)
xp=10**(np.e**(1.7818*((yt/1634.6)**(0.2408))+0.8310*((yt/1634.6)**(-1))-0.1444*((yt/1634.6)**(-3)))-1)/1e9


ax.plot(xp, yt,color='k',lw=lw)

#Ice VII-X transition
ax.vlines([30.9],100,1280,linestyle='--',color='k',lw=lw)

#Water EOS transition
ax.hlines([490],0.0025,0.207592,linestyle='--',color='k',lw=lw)

#Supercritical transition
#ax.hlines([480],0.6343992,2.216,linestyle='--')

#Supercritical transition
#ax.vlines([30.9],350,1150,linestyle='--',color='k')
ax.vlines([0.20759],1150,25000,linestyle='--',color='k',lw=lw)
#ax.vlines([0.6343992],500,3000,linestyle='--')

ax.vlines([0.207592],250,1150,linestyle='--',color='k',lw=lw)

#IAPWS to Ideal Gas
ax.hlines([1000],0.000001,0.207592,linestyle='--',color='k',lw=lw)

ax.hlines([1280],0.207592,30.9,linestyle='--',color='k',lw=lw)
#Brown to Ideal
#ax.hlines([8000],0.207592,30.9,linestyle='--',color='k')

ax.hlines([2250],71.4289967,700,linestyle='--',color='k',lw=lw)



#Vapour Wagner, W. & Pruss, A. (1993).
a, b, c, d = -7.85951783, 1.84408259, -11.7866497, 22.6807411
Tc = 647.096  # K
Pc = 0.022064 # GPa
yt=np.linspace(100,647.096,500)
tau = 1 - yt/Tc
ln_term = (Tc/yt) * (a*tau + b*tau**1.5 + c*tau**3 + d*tau**6)
xp=(Pc * np.exp(ln_term))

ax.plot(xp, yt,color='k',lw=lw)


files=['200','300','400']

labels=files
markers=['o','s','^','*','.']
color=['tab:red','tab:blue','tab:green']


vmin = 0     # your global min density
vmax = 3.037     # your global max density
norm = plt.Normalize(vmin, vmax)
cmap = cmr.cosmic.reversed()

for i in range(len(files)):
    #inf=open('Hydro_03_07_1_1E5_'+files[i]+'.txt','r')
    inf=open('Hydro_1_'+files[i]+'.txt','r')
    lines=inf.readlines()
    magrad=[]
    magpress=[]
    magmass=[]
    magdens=[]
    magtemp=[]
    magphase=[]
    c=0
    for line in lines[1:-1]:
        div=re.split('\s{2,}',line)
        magphase.append(div[6])
        if "hcp" not in magphase[c] and "liquid" not in magphase[c] and "Si" not in magphase[c] and "Pv" not in magphase[c] and "Brg" not in magphase[c]:
            magrad.append(float(div[1]))
            magpress.append(float(div[2]))
            magmass.append(float(div[3]))
            magdens.append(float(div[4]))
            magtemp.append(float(div[5]))
        c=c+1
        inf.close()
    #ax.plot(magpress,magtemp,color='grey',lw=2.0,ls='-.',zorder=0) #,marker=markers[i%4],label=labels[i]
    #ax.scatter(magpress,magtemp,label=labels[i],c=magdens,cmap="cmr.lavender",marker=markers[i%4],s=80)
    points = np.array([magpress, magtemp]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, cmap=cmap, norm=norm,zorder=1)
    lc.set_array(magdens)
    lc.set_linewidth(4)
    ax.add_collection(lc)

    ax.plot([magpress[0]],[magtemp[0]],color='k',marker=markers[i],lw=0,ms=8,zorder=0,label=files[i]+" K\n"+str(round(magrad[-1],2))+r" R$_\oplus$")
    ax.plot([magpress[-1]],[magtemp[-1]],color='k',marker=markers[i],lw=0,ms=8,zorder=0)

ax.legend(frameon=False,fontsize=18,loc="upper center", bbox_to_anchor=(0.5, 1.2), ncol=3,handlelength=0.8,columnspacing=0.5,handletextpad=0.3)
cbar = plt.colorbar(
    lc,
    ax=ax,
    orientation='horizontal',
    pad=0.05,          # closer to the plot (default ~0.05–0.15)
    fraction=0.04,    # thinner bar
    aspect=25,        # longer and flatter
)
cbar.set_label('')  # no label directly on bar
fig.text(0.04, 0.11, r'$\rho$ (g cm$^{-3}$)', va='center', fontsize=18)
cbar.ax.tick_params(labelsize=18, length=4,direction='inout',)

ax.set_xlabel("P (GPa)")
ax.set_ylabel("T (K)")
ax.axis([0.000007,200,100,7000])
#ax.axis([0.07,150,100,7000])
#ax.axis([0.0007,80,200,1000])
#ax.axis([2.1,2.4,352,370])
ax.set_xscale("log")
ax.set_yscale("log")

#ax.text(0.001,110,'A')
ax.text(0.001,120,'A')
ax.text(4,120,'B')
ax.text(40,120,'C')
ax.text(0.001,600,'D')
#ax.text(0.001,600,'D')
ax.text(1.0,600,'E')
#ax.text(0.001,7000,'F')
ax.text(0.001,2500,'F')
ax.text(1,2000,'G')

#plt.legend()
#plt.tight_layout()
#plt.savefig('waterdiagram.pdf',bbox_inches='tight')
#plt.savefig('waterdiagram_allpress_05_1E8_360_420.pdf',bbox_inches='tight')
#plt.show()
#plt.clf()

ax = axes[1]
###Mantle
#fig = ax.figure(figsize=(5, 5))
lw=1.0
#PPV
yt=np.linspace(0,7000,5000)
xp=112.5+7E-3*yt

ax.plot(xp,yt,color='k',lw=lw)

#Melt
xp=np.linspace(0.000001,153.676,5000)
yt=1830*(1+xp/4.6)**0.33

ax.plot(xp,yt,color='k',lw=lw)

#Pv
yt=np.linspace(0,3185.87,5000)
xp=24.3-2.12E-4*yt-3.49E-7*yt**2

ax.plot(xp,yt,color='k',lw=lw)

#RWD
yt=np.linspace(0,2232.79,5000)
xp=8.69+6E-3*yt

ax.plot(xp,yt,color='k',lw=lw)

#WDS
yt=np.linspace(234.57,3094.08,5000)
xp=9.45+2.76E-3*yt

ax.plot(xp,yt,color='k',lw=lw)

vmin = 2.74     # your global min density
vmax = 6.0    # your global max density
norm = plt.Normalize(vmin, vmax)
cmap = cmr.ember.reversed()

files=['300','1000','2000']
labels=files
markers=['o','s','^','*','.']
color=['tab:red','tab:blue','tab:green']

for i in range(len(files)):
    inf=open('Structure_mant_1_'+files[i]+'.txt','r')
    lines=inf.readlines()
    magrad=[]
    magpress=[]
    magmass=[]
    magdens=[]
    magtemp=[]
    magphase=[]
    c=0
    for line in lines[1:-1]:
        div=re.split('\s{2,}',line)
        magphase.append(div[6])
        #if "hcp" not in magphase[c] and "liquid" not in magphase[c] and "Si" not in magphase[c] and "Pv" not in magphase[c] and "Brg" not in magphase[c]:
        magrad.append(float(div[1]))
        magpress.append(float(div[2]))
        magmass.append(float(div[3]))
        magdens.append(float(div[4]))
        magtemp.append(float(div[5]))
        c=c+1
        inf.close()

    #ax.plot(magpress,magtemp,label=labels[i],color=lighten_color(color[i%3],1-((i%4)/10*2)),lw=4.0,zorder=0) #,marker=markers[i%4]
    points = np.array([magpress, magtemp]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, cmap=cmap, norm=norm,zorder=1)
    lc.set_array(magdens)
    lc.set_linewidth(4)
    ax.add_collection(lc)

    ax.plot([magpress[0]],[magtemp[0]],color='k',marker=markers[i],lw=0,ms=8,zorder=0,label=files[i]+" K\n"+str(round(magrad[-1],2))+r" R$_\oplus$")
    ax.plot([magpress[-1]],[magtemp[-1]],color='k',marker=markers[i],lw=0,ms=8,zorder=0)

ax.legend(frameon=False,fontsize=18,loc="upper center", bbox_to_anchor=(0.5, 1.2), ncol=3,handlelength=0.8,columnspacing=0.5,handletextpad=0.3)
cbar = plt.colorbar(
    lc,
    ax=ax,
    orientation='horizontal',
    pad=0.05,          # closer to the plot (default ~0.05–0.15)
    fraction=0.04,    # thinner bar
    aspect=25,        # longer and flatter
)
cbar.set_label('')  # no label directly on bar
fig.text(0.36, 0.11, r'$\rho$ (g cm$^{-3}$)', va='center', fontsize=18)
cbar.ax.tick_params(labelsize=18, length=4,direction='inout',)


ax.axis([0.1,250,100,7000])
ax.set_xlabel("P (GPa)")
#ax.ylabel("T (K)")
ax.set_xscale("log")
ax.set_yscale("log")

ax.text(0.7,150,'Olv',fontsize=18)
ax.text(11,150,'Rwd',fontsize=18, rotation=-90)
ax.text(35,150, 'Bdm',fontsize=18, rotation=-90)
ax.text(115,150,'PPv',fontsize=18, rotation=-90)

ax.text(7.,1250,'Wds',fontsize=18,rotation=-90)
ax.annotate("", xytext=(14,1600), xy=(17,1600),
            arrowprops=dict(arrowstyle="->", lw=1))
ax.text(0.7,4000,'Melt',fontsize=18)

#plt.tight_layout()
#plt.show()

ax = axes[2]
###Carbon
#fig = plt.figure(figsize=(5, 5))
lw=1.0

#BC8
yt=np.linspace(0,7000,5000)
xp=970.679+(-1.52854E-2*yt)+(-5.72152E-7*yt**2)

ax.plot(xp,yt,color='k',lw=lw)

#Diamond
yt=np.linspace(0,7000,5000)
xp=1.949+(yt+273)/400

ax.plot(xp,yt,color='k',lw=lw)

#SiC
yt=np.linspace(0,7000,5000)
xp=69-0.001*(yt-300)

ax.plot(xp,yt,color='dimgrey',lw=lw,ls='--')

vmin = 2.25     # your global min density
vmax = 4.22    # your global max density
norm = plt.Normalize(vmin, vmax)
cmap = cmr.bubblegum.reversed()


files=['300','500','1000']
labels=files
markers=['o','s','^','*','.']
color=['tab:red','tab:blue','tab:green']

for i in range(len(files)):
    inf=open('Structure_carb_1_'+files[i]+'.txt','r')
    lines=inf.readlines()
    magrad=[]
    magpress=[]
    magmass=[]
    magdens=[]
    magtemp=[]
    magphase=[]
    c=0
    for line in lines[1:-1]:
        div=re.split('\s{2,}',line)
        magphase.append(div[6])
        #if "hcp" not in magphase[c] and "liquid" not in magphase[c] and "Si" not in magphase[c] and "Pv" not in magphase[c] and "Brg" not in magphase[c]:
        magrad.append(float(div[1]))
        magpress.append(float(div[2]))
        magmass.append(float(div[3]))
        magdens.append(float(div[4]))
        magtemp.append(float(div[5]))
        c=c+1
        inf.close()
    print(min(magdens))
    print(max(magdens))
    #ax.plot(magpress,magtemp,label=labels[i],color=lighten_color(color[i%3],1-((i%4)/10*2)),lw=4.0,zorder=0) #,marker=markers[i%4]
    points = np.array([magpress, magtemp]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, cmap=cmap, norm=norm,zorder=1)
    lc.set_array(magdens)
    lc.set_linewidth(4)
    ax.add_collection(lc)

    ax.plot([magpress[0]],[magtemp[0]],color='k',marker=markers[i],lw=0,ms=8,zorder=0,label=files[i]+" K\n"+str(round(magrad[-1],2))+r" R$_\oplus$")
    #ax.plot([0.1],[magtemp[-4]],color='k',marker=markers[i],lw=0,ms=8,zorder=0)

ax.legend(frameon=False,fontsize=18,loc="upper center", bbox_to_anchor=(0.5, 1.2), ncol=3,handlelength=0.8,columnspacing=0.5,handletextpad=0.3)
cbar = plt.colorbar(
    lc,
    ax=ax,
    orientation='horizontal',
    pad=0.05,          # closer to the plot (default ~0.05–0.15)
    fraction=0.04,    # thinner bar
    aspect=25,        # longer and flatter
)
cbar.set_label('')  # no label directly on bar
fig.text(0.68, 0.11, r'$\rho$ (g cm$^{-3}$)', va='center', fontsize=18)
cbar.ax.tick_params(labelsize=18, length=4,direction='inout',)

'''
files=['300','1000']
labels=files
markers=['o','s','^','*','.']
color=['tab:red','tab:blue','tab:green']

for i in range(len(files)):
    inf=open('Structure_sic_1_'+files[i]+'.txt','r')
    lines=inf.readlines()
    magrad=[]
    magpress=[]
    magmass=[]
    magdens=[]
    magtemp=[]
    magphase=[]
    c=0
    for line in lines[1:-1]:
        div=re.split('\s{2,}',line)
        magphase.append(div[6])
        #if "hcp" not in magphase[c] and "liquid" not in magphase[c] and "Si" not in magphase[c] and "Pv" not in magphase[c] and "Brg" not in magphase[c]:
        magrad.append(float(div[1]))
        magpress.append(float(div[2]))
        magmass.append(float(div[3]))
        magdens.append(float(div[4]))
        magtemp.append(float(div[5]))
        c=c+1
        inf.close()

    ax.plot(magpress,magtemp,label=labels[i],color=lighten_color(color[i%3],1-((i%4)/10*2)),lw=4.0,zorder=0,ls='--') #,marker=markers[i%4]

'''

#ax.legend(frameon=False,fontsize=18,loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=4,handlelength=1.5,columnspacing=0.5,handletextpad=0.3)

ax.axis([0.1,2000,100,7000])
ax.set_xlabel("P (GPa)")
#ax.ylabel("T (K)")
ax.set_xscale("log")
ax.set_yscale("log")


ax.text(0.3,150,'Grp')
ax.text(10,150, 'Dmd')
ax.text(880,150,'C-bc8',rotation=-90)

ax.text(14,1500,'SiC-\nB1',color='dimgrey',fontsize=18)
ax.text(90,1500,'SiC-\nB3',color='dimgrey',fontsize=18)

ax.text(0.15,4000,'Liquids\nNot Implemented',fontsize=16, fontstyle="italic")

# Make tick marks on all sides, both in and out
for ax in axes:
    ax.tick_params(
        direction='inout',   # ticks go both in and out
        length=6,            # tick length (points)
        width=1.0,           # tick width (points)
        top=True, bottom=True, left=True, right=True,  # show all sides
        which='both',        # apply to both major and minor ticks
        labeltop=False, labelright=False  # hide duplicate labels
    )
    # Optionally turn on minor ticks for more detail
    ax.minorticks_on()

fig.savefig("phase_panels.png", dpi=600, bbox_inches="tight")
plt.show()
