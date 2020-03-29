#Name: Vibhu Agrawal
#Roll No: 2018116
#Section: A
#Group: 4

"""This is the support file for hw4_main_2018116"""

import math

def matrix_multiplication(m1,m2):

	"""Multiplies matrix m1 with matrix m2
	m1 and m2 are matrices passed as nested list,
	each list containing elements row-wise."""

	#print (m1,m2)
	if len(m1[0])!=len(m2):
		return "Invalid dimensions"

	ans=[]
	for i in range(len(m1)):
		temp=[]
		for j in range(len(m2[0])):
			pro=0
			for k in range(len(m2)):
				pro=pro+(m1[i][k]*m2[k][j])
			temp.append(pro)
		ans.append(temp)
		temp=[]

	return ans

def transpose(matrix):
	"""Returns transpose of a given matrix.
	Matrix as nested list with each list containing 
	row vector."""

	matnew=[]
	s=len(matrix[0])
	# matnew=[[] for i in range(s)]
	

	temp=[]
	for j in range(len(matrix[0])):
		for i in range(len(matrix)):
			temp.append(matrix[i][j])
		matnew.append(temp)
		temp=[]

	return(matnew)

def printing(m):
	"""For proper printing of coordinates of a polygon"""
	print ()
	s1=""
	for i in range((len(m[0]))-1):
		s1=s1+str(round(m[0][i],2)) + " "
	print (s1[:-1])

	s2=""
	for j in range ((len(m[1]))-1):
		s2=s2+str(round(m[1][j],2)) + " "
	print (s2[:-1])
	print()



def scaling(sx,sy,mat2):
	""""To scale a figure by sx in x-axis and sy in y-axis. 
	mat2 is the matrix containing the defining coordinates of figure"""

	mat1=[[sx,0,0],[0,sy,0],[0,0,1]]
	scaled=matrix_multiplication(mat1,mat2)
	return scaled


def rotate(theta,mat2):
	"""To rotate a figure by theta angle.
	mat2 is the matrix containing the defining coordinates of figure"""
	the_rad=math.radians(theta)
	s=math.sin(the_rad)
	c=math.cos(the_rad)
	
	mat1=[[c,-s,0],[s,c,0],[0,0,1]]

	rotated=matrix_multiplication(mat1,mat2)

	return rotated


def translate(dx,dy,mat2):
	"""To translate a figure by dx in x-axis and dy in y-axis.
	mat2 is the matrix containing the defining coordinates of figure"""
	mat1=[[1,0,dx],[0,1,dy],[0,0,1]]
	translated=matrix_multiplication(mat1,mat2)
	return translated


def four_coor(a,b,major,minor,theta):
	"""Finds four extreme coordinates of the ellipse.
	(a, b) are the coordinates of center.
	major, minor are lengths of major and minor axes
	theta is the angle by which it has been rotated"""
	m1 = major/2
	m2 = minor/2
	c0 = [a, b, 1]
	c1 = [a+m1, b, 1]
	c2 = [a, b+m2, 1]
	c3 = [a-m1, b, 1]
	c4 = [a, b-m2, 1]
	mat=transpose([c1,c2,c3,c4])

	if theta!=0:
		mat=rotate(theta,mat)

	mat[0].insert(0,a)
	mat[1].insert(0,b)
	mat[2].insert(0,1)

	return mat 									#has center and four extreme coordinates
