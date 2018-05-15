''' Two dimensional system

SYSTEM:

x = [px py vx vy]'
y = [d a]'

u = [ux uy]'
w = [wx wy]'
r = [rd ra]'

d = sqrt(px^2 + py^2) + rd
a = atan2(py, px) + ra

'''
import numpy as np 
import matplotlib.pyplot as plt 
import random
import matrices
import controlability 
N = 4
dt = 0.1;

Q = np.diag(np.power(np.array([0.1, 0.1]),2))
R = np.diag(np.power(np.array([0.1, np.pi/180.0]),2))

# simulated variables
X = np.transpose([2, 1, -1, 1])

# estimated variables
x = np.transpose([3, 3, 0, 0])
P = np.diag(np.power(np.array([1, 1, 1, 1]),2))

# trajectories
tt = np.arange(0,N, dt)



XX = np.zeros((4,np.shape(tt)[0]), dtype = float)

xx = np.zeros((4,np.shape(tt)[0]), dtype = float)
yy = np.zeros((2,np.shape(tt)[0]), dtype = float)
PP = np.zeros((4,np.shape(tt)[0]), dtype = float)

# perturbation levels
q = np.sqrt(np.diag(Q))/2
r = np.sqrt(np.diag(R))/2

# start loop

i = 0

for t in tt:

	if t == 1:
		u = np.transpose([2, 0])/dt
	elif t == 2:
		u = np.transpose([-3, 0])/dt
	elif t == 3:
		u = np.transpose([1, -2])/dt
	else:
		u = np.transpose([0, 0])/dt

	# simulate
	w = q * np.random.randn()
	x0, A, B, W = matrices.main(X, u, w,dt)
	X = x0
	v = r * np.random.randn()
	e, C = controlability.main(X)
	y = e + v

	# estimate -prediction
	[x, A, B, W] = matrices.main(x, np.zeros((2,1),float),np.zeros((2,1),float),dt)
	
	P = np.dot(np.dot(A, P),np.transpose(A)) + np.dot(np.dot(W,Q),np.transpose(W))


	# correction 
	[e, C] = controlability.main(x)
	E = np.dot(np.dot(C,P),np.transpose(C))

	z = y - e
	Z = R + E
	

	K = np.dot(np.dot(P,np.transpose(C)),np.linalg.inv(Z))

	x = x + np.dot(K,z)
	P = P - np.dot(np.dot(K,C),P)


	# collect data 
	XX[:,i] = (X)
	xx[:,i] = x
	yy[:,i] = y
	PP[:,i] = np.diag(P)

	# upate index
	i =i+1

	print(X[0],X[1])
	print(x[0],x[1])

	# plt.plot(X[0],X[1],'r*', label = 'Truth')
	# plt.axis([-2, 4, 0, 6])
	# plt.plot(x[0],x[1],'c*', label = 'Estimate')
	# plt.show()
	# plt.pause(0.5)
	# plt.draw()



plt.plot(XX[0,:],XX[1,:],'r', label = 'Truth')
plt.axis([-2, 4, 0, 6])
plt.plot(xx[0,:],xx[1,:],'c', label = 'Estimate')
# # plt.plot(tt,yy,'b', label = 'Measurement' )
# # plt.plot(tt,XX+3*np.sqrt(PP), 'g', label = '+3 Sigma')
# # plt.plot(tt,XX-3*np.sqrt(PP), 'g', label = '-3 Sigma')
plt.show()