import matplotlib.pyplot as plt
import pandas
import numpy as np

df = pandas.read_excel('Book2.xlsx')
deformation =-1* df[df.columns[0]].values
force = df[df.columns[1]].values

YieldStress=26e+6
Flim=5.14*YieldStress/np.sqrt(3)

plt.figure(1)
plt.semilogy(deformation,force,'-o',color='b')
plt.axhline(y=Flim, color='r', linestyle='-')

plt.xlabel('Applied displacement (m)')
plt.ylabel('Total reaction (N)')
plt.legend(['ANSYS simulation results','Slip-line theory limit load: '+str(round(Flim/1e6, 2))+' MN'])

# plt.figure(2)
# right_edge = df[df.columns[2]].values
# symmetry = df[df.columns[3]].values
# total_reaction=force+right_edge+symmetry
# plt.semilogy(deformation,total_reaction,'-o',color='b')
# plt.axhline(y=Flim, color='r', linestyle='-')

error=0
biginds=[i for i,v in enumerate(force) if v > Flim]

for j in range(0,np.shape(biginds)[0]-1):
    error=error+abs((force[biginds[j]]-Flim)/ force[biginds[j]])  
    
print(round(error,2))
