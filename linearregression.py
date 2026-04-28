import matplotlib.pyplot as plt
def sigmaAll(x,y):
	if len(x)!=len(y):
		return None
	print(x,y)
	sx,sy,sx2,sxy=0,0,0,0
	n=len(x)
	for i in range(n):
		currentx,currenty=x[i],y[i]
		sx+=currentx
		sy+=currenty
		sx2+=currentx*currentx
		sxy+=currentx*currenty

	return sx,sy,sx2,sxy,n
def linearRegression(x,y):
	sx,sy,sx2,sxy,n=sigmaAll(x,y)
	print(f"sx={sx}, sy={sy},sx2={sx2},sxy={sxy}")
	m=(sx*sy-n*sxy)/(sx*sx -n*sx2)
	c=(sy-m*sx)/n
	return m,c
def predict(x,m,c):
	y=m*x+c
	return y
	
a=[1,2,3,4]
b=[2+1,5,7,9]
m,c=linearRegression(a,b)
print(f"M={m}, C ={c}, predict(5)={predict(5,m,c)}")
x=5
plt.scatter(a,b,color="green")
plt.plot(a,b)
# plt.show()

