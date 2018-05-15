
import numpy as np  
import random
from math import*

def con(x):
	px = x[0]
	py = x[1]
	
	d = sqrt(np.power(px,2)+np.power(py,2))
	a = atan2(py, px)

	y = np.transpose(np.array([d, a]))

	C = np.array([[px/d, py/d, 0, 0],
		         [-py/(np.power(px,2)*(np.power(py,2)/np.power(px,2) + 1)), 1/(px*(np.power(py,2)/np.power(px,2) + 1)), 0, 0]])

	return(y, C)

def main(x):
	[y, C] = con(x)
	return(y, C)

if __name__=='__main__':
 	import sys
 	main(sys.argv[1:])