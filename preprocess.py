from token import LPAR
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Lp=np.zeros((10, 10, 3))
Ls=np.zeros((10, 10, 3))
Lp_short=np.zeros((10, 10, 3))
M=np.zeros((10, 10, 3))
k=np.zeros((10, 10, 3))

df = pd.read_csv('realInductances.CSV')

xloc=df['x_left'].unique()
yloc=df['y_left'].unique()
x_idx=['x_left', 'x_left.1', 'x_left.2']
y_idx=['y_left', 'y_left.1', 'y_left.2']
Lp_idx=['Lp', 'Lp.1', 'Lp.2']
Ls_idx=['Ls', 'Ls.1', 'Ls.2']
Lp_short_idx=['Lp(shrt)', 'Lp(shrt).1', 'Lp(shrt).2']
M_idx=['M', 'M.1', 'M.2']
k_idx=['k', 'k.1', 'k.2']

for z in range(0, 3):
    for y in range(0, 10):
        for x in range(0, 10):
            condition = (df[x_idx[z]] == xloc[x]) & (df[y_idx[z]] == yloc[y])
            Lp[x, y, z] = df.loc[condition, Lp_idx[z]].values[0]
            Ls[x, y, z] = df.loc[condition, Ls_idx[z]].values[0]
            Lp_short[x, y, z] = df.loc[condition, Lp_short_idx[z]].values[0]
            M[x, y, z] = df.loc[condition, M_idx[z]].values[0]
            k[x, y, z] = df.loc[condition, k_idx[z]].values[0]     
            print(f"{x}, {y}, {z}")
        
            
print(Lp[:,:,0])

X, Y = np.meshgrid(xloc, yloc)
fig = plt.figure()
for i in range(0, 3):
    ax = fig.add_subplot(3,5,5*i+1, projection='3d')
    ax.plot_surface(X, Y, Lp[:,:,i], cmap='viridis')  # 표면 플롯
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title('Lp', pad=10)


    ax = fig.add_subplot(3,5,5*i+2, projection='3d')
    ax.plot_surface(X, Y, Lp_short[:,:,i], cmap='viridis')  # 표면 플롯
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title('Lp_short', pad=10)

    ax = fig.add_subplot(3,5,5*i+3, projection='3d')
    ax.plot_surface(X, Y, Ls[:,:,i], cmap='viridis')  # 표면 플롯
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title('Ls', pad=10)

    ax = fig.add_subplot(3,5,5*i+4, projection='3d')
    ax.plot_surface(X, Y, M[:,:,i], cmap='viridis')  # 표면 플롯
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title('M', pad=10)   

    ax = fig.add_subplot(3,5,5*i+5, projection='3d')
    ax.plot_surface(X, Y, k[:,:,i], cmap='viridis')  # 표면 플롯
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title('k', pad=10)


plt.show()
