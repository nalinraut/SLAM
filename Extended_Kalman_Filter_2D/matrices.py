
import numpy as np  
import random

def jaco(x, u, w, dt):
	px = x[0]
	py = x[1]
	vx = x[2]
	vy = x[3]
	ax = u[0]
	ay = u[1]
	wx = w[0]
	wy = w[1]

	px = px + vx*dt
	py = py + vy*dt

	vx = vx + ax*dt + wx
	vy = vy + ay*dt + wy

	x0 = np.transpose(np.array([px, py, vx, vy]))

	A = np.array([[1.0,0.0,dt,0.0],
		 		  [0.0,1.0,0.0,dt],
		 		  [0.0,0.0,1.0,0.0],
		          [0.0,0.0,0.0,1.0]])
	
	B = np.array([[0.0, 0.0],
				  [0.0, 0.0],
				  [dt , 0.0],
				  [0.0, dt]])

	W = np.array([[0.0, 0.0],
				  [0.0, 0.0],
				  [1.0, 0.0],
				  [0.0, 1.0]])

	return(x0, A, B, W)

def main(x, u, w, dt):
	[x0, A, B, W] = jaco(x, u, w, dt)
	return(x0, A, B, W)

if __name__=='__main__':
 	import sys
 	main(sys.argv[1:])