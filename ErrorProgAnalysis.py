## Nathan Morrow AFIT 
# Python program to estimate the error propagation of a S.S. INS system

# Import libraries
from matplotlib import pyplot as plt
import numpy as np

# Define Constants
Re = 6.3781e6       # Radius of the earth
u = 3.986006752e14  # Mass and Gravitational constant combined
Wie = 7.2921159e-5  # Earth rotation speed in (rad/sec)
dt1 = 0.01
dur = 12*3600
K = int(dur/dt1) + 1

# Define State Space arrays
r_t = np.zeros([K,3])       # Truth trajectory (Xi,Yi,Zi)
rc_t = np.zeros([K,3])      # Calculated trajectory (Xi,Yi,Zi)


def latlongToXYZ (r,lat,astlong):
    x = r*np.cos(lat)*np.cos(astlong)
    y = r*np.cos(lat)*np.sin(astlong)
    z = r*np.sin(lat)
    return np.array([x,y,z])

## Case 1: South-North Flight Path
ldot = 0
Ldot = (1/360)*(1/60)       # (rad/sec)
r = Re                      # Vehichle is on earths surface
lat = 0
astlong = 0
for k in range(K):
    lat += Ldot*k*dt1
    astlong += (ldot+Wie)*k*dt1
    r_t[k] = latlongToXYZ(r,lat,astlong)
plt.figure()
plt.plot(r_t[:,0],r_t[:,1])
plt.grid()
plt.savefig('Case1_Truth.pdf')


## Case 2: West-East Flight Path
ldot = (1/360)*(1/60)       # (rad/sec)
Ldot = 0
r = Re                      # Vehichle is on earths surface
lat = 0
astlong = 0
for k in range(K):
    lat += Ldot*k*dt1
    astlong += (ldot+Wie)*k*dt1
    r_t[k] = latlongToXYZ(r,lat,astlong)
plt.figure()
plt.plot(r_t[:,0],r_t[:,1])
plt.grid()
plt.savefig('Case2_Truth.pdf')




## Case 3: Vertical Rocket Launch
ldot = 0
Ldot = 0
r = Re                      # Vehichle is on earths surface
lat = 0
astlong = 0
for k in range(K):
    lat += Ldot*k*dt1
    astlong += (ldot+Wie)*k*dt1
    r+=20*(k*dt1)**2
    r_t[k] = latlongToXYZ(r,lat,astlong)
plt.figure()
plt.plot(np.arange(K)*dt1,r_t[:,2])
plt.grid()
plt.savefig('Case3_Truth.pdf')


