
''' One dimensional kalman filter example 
SYSTEM :
x_next = x + u*dt + w
y = x + v

'''

import numpy as np 
import matplotlib.pyplot as plt 
import random 


N = 100
dt = 1

# simulated variables
u = 1
X = 7

# estimated variables
x = 0
P = 1e4

# Matrices and Vectors
A = 1
B = dt
C = 1
W = 1

Q = 0.01
R = 100


# trajectories 
tt = np.linspace(0,N, num = N + 1)



XX = np.zeros(N + 1, dtype = float)
xx = np.zeros(N + 1, dtype = float)
yy = np.zeros(N + 1, dtype = float)
PP = np.zeros(N + 1, dtype = float)


# perturbation levels
q = np.sqrt(Q);
r = np.sqrt(R);

# start loop
i = 0
for t in tt:

	# simulate 
	w = q * np.random.randn()
	X = A * X + B * u + W * w
	v = r * np.random.randn()
	y = C * X + v

	# estimate - prediction
	x = A * x + B * u
	P = A * P * np.transpose(A) + W * Q * np.transpose(W)

	# correction 
	e = C * x
	E = C * P * np.transpose(C)

	z = y - e
	Z = R + E

	K = P * np.transpose(C) * np.power(Z, -1)
	x = x + K * z
	P = P - K * C * P

	# collect data 
	XX[:][i] = X
	xx[:][i] = x
	yy[:][i] = y
	PP[:][i] = P #np.diag(P)

    # update index
	i =i+1


plt.plot(tt,XX,'r', label = 'Truth')
plt.plot(tt,xx,'c', label = 'Estimate')
plt.plot(tt,yy,'b', label = 'Measurement' )
plt.plot(tt,XX+3*np.sqrt(PP), 'g', label = '+3 Sigma')
plt.plot(tt,XX-3*np.sqrt(PP), 'g', label = '-3 Sigma')
plt.show()