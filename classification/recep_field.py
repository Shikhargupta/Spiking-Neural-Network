import numpy as np
import cv2

def rf(inp):
	w = [[-0.5,-0.125,  0.25,  -0.125, -0.5  ],
	 [-0.125 , 0.25  , 0.625 , 0.25 , -0.125],
	 [ 0.25   ,0.625 , 1. ,    0.625 , 0.25 ],
	 [-0.125 , 0.25  , 0.625 , 0.25,  -0.125],
	 [-0.5  , -0.125 , 0.25 , -0.125 ,-0.5  ]]
	pot = np.zeros([16,16])
	ran = [-2,-1,0,1,2]
	ox = 2
	oy = 2


	for i in range(16):
		for j in range(16):
			summ = 0
			for m in ran:
				for n in ran:
					if (i+m)>=0 and (i+m)<=15 and (j+n)>=0 and (j+n)<=15:
						summ = summ + w[ox+m][oy+n]*inp[i+m][j+n]/255
			pot[i][j] = summ
	return pot		

# if __name__ == '__main__':

# 	maxx = -1000
# 	minn = 1000

# 	for j in range(1,1500):
# 		img = cv2.imread("images/" + str(j) + ".png", 0)
# 		pot = rf(img)
# 		for c in pot:
# 			if max(c)>maxx:
# 				maxx=  max(c)
# 			if min(c)<minn:
# 				minn = min(c)

# 	print maxx, minn				