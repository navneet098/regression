import math
# import matplotlib.pyplot as plt
def sigmaAll(x,y):
	if len(x)!=len(y):
		return None
	print(x,y)
	sx,sy,sx2,sxy,sy2=0,0,0,0,0
	n=len(x)
	for i in range(n):
		currentx,currenty=x[i],y[i]
		sx+=currentx
		sy+=currenty
		sx2+=currentx*currentx
		sy2+=currenty*currenty
		sxy+=currentx*currenty
	return sx,sy,sx2,sy2,sxy,n
def linearRegression(x,y):
	sx,sy,sx2,sy2,sxy,n=sigmaAll(x,y)
	print(f"sx={sx}, sy={sy},sx2={sx2},sxy={sxy}")
	m=(sx*sy-n*sxy)/(sx*sx -n*sx2)
	c=(sy-m*sx)/n
	r=(n*sxy-sx*sy)/math.sqrt((n*sx2-sx*sx)*(n*sy2-sy*sy))
	return r,m,c
def predict(x,m,c):
	y=m*x+c
	return y
a=[1,2,3,4,5,6]
b=[5,4,3,2,1,0]
r,m,c=linearRegression(a,b)
print(f"M={m}, C ={c}, predict(9)={predict(9,m,c)},correlation={r}")
# x=9
# //plt.scatter(a,b,color="green")
# plt.plot(a,b)
# plt.show()
