#Name: Vibhu Agrawal
#Roll No: 2018116
#Section: A
#Group: 4

"""This program depicts the miniature version of transformations that occur during image
processing in computer graphics. It supports scaling, rotation, traslation on a disc/ellipse 
and a polygon."""

import helper_func as func
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import pylab
import math
from random import random as rand

plt.ion()


shape = input("Enter the name of shape to be transformed (disc/polygon): ")
shape = shape.lower()
#print ([a1,b1,c1])

if shape == "disc":
	try:
		a,b,r = map(float,input("Enter three space separated numbers denoting center and radius: ").split())
		fig = pylab.figure()
		ax = fig.add_subplot(111)
		ax.add_patch(Ellipse((a,b), 2*r, 2*r, fill=None))
		ax.axis('equal')
		plt.show()									#to plot ellipse
		major = 2*r
		minor = 2*r
		angle = 0
		# pyEl((a,b),2*r,2*r)
		plt.show()

	except:
		print ("Invalid input")
		quit()


elif shape == "polygon":
	try:
		x_list = list(map(float,input("Enter the x coordinates: ").split()))
		y_list = list(map(float,input("Enter the y coordinates: ").split()))
		x_list.append(x_list[0])
		y_list.append(y_list[0])
		plt.plot(x_list,y_list)
		plt.show()									#To plot polygon

	except:
		print ("Invalid input")
		quit()

	if len(x_list) != len(y_list):
		print ("Invalid coordinates")
		exit()

	
else:
	print ("Invalid shape.")
	quit()

###Initial inputs

query_in = ""										#queries that will be performed

print ("Enter the transformations to be performed.")
print("\nS x y: to scale the object by a factor of x along the x-axis, and y​ along the y-axis.\
	\nR theta: to rotate the object by theta degrees in counter clockwise direction.\
	\nT dx dy: to translate the object by dx units along x x-axis, and by dy units along the y-axis.\
	\nEnter 'quit' to stop.")

while  query_in != "quit":

	a1 = float(rand())							# To generate random colors
	b1 = float(rand())
	c1 = float(rand())

	query_in = input()
	q_list = query_in.split()

	if shape == "polygon":
		to_pass = []								#matrix of coordinates of polygon
		for c in range(len(x_list)):
			to_pass.append([x_list[c],y_list[c],1])
		
		to_pass = func.transpose(to_pass)
		#print (to_pass)

	try:

		if q_list[0] == "S":							#Scaling operations
			sx = float(q_list[1])
			sy = float(q_list[2])
			if shape == "disc":

				mat = func.four_coor(a,b,major,minor,angle)			#matrix of ellipse
				z = func.scaling(sx, sy, mat)
				a = z[0][0]
				b = z[1][0]
				major = math.sqrt(((z[0][1]-z[0][3])**2)+((z[1][1]-z[1][3])**2))			#distance formula
				minor = math.sqrt(((z[0][2]-z[0][4])**2)+((z[1][2]-z[1][4])**2))

				print()

				if major != minor:									# Controlling print format
					print (round(a,2),round(b,2),round(major/2, 2),round(minor/2,2),"\n")
				else: 
					print (round(a,2),round(b,2),round(major/2, 2),"\n")

				#plt.close()
				#fig = pylab.figure()
				#ax = fig.add_subplot(111)
				ax.add_patch(Ellipse((a,b), major, minor,angle, fill=None, EdgeColor=[a1,b1,c1]))
				ax.axis('equal')
				plt.show()



			else:

				t = func.scaling(sx,sy,to_pass)					# Scaling polygon
				func.printing(t)
				x_list = t[0]
				y_list = t[1]
				plt.plot(x_list,y_list)
				plt.show()


		elif q_list[0] == "R":									#Rotation operations
			theta = float(q_list[1])
			if shape == "disc":
				mut_mat = func.four_coor(a,b,major,minor,angle)
				q=func.rotate(theta,mut_mat)
				a = q[0][0]
				b = q[1][0]
				angle += theta									#Angle control

				print()

				if major != minor:
					print (round(a,2),round(b,2),round(major/2, 2),round(minor/2,2),"\n")
				else: 
					print (round(a,2),round(b,2),round(major/2, 2),"\n")

				#print (angle)
				#plt.close()
				#fig = pylab.figure()
				#ax = fig.add_subplot(111)
				ax.add_patch(Ellipse((a,b), major, minor,angle, fill=None, EdgeColor=[a1,b1,c1]))
				ax.axis('equal')
				plt.show()



			else:
				g = func.rotate(theta,to_pass)					#Polygon rotation
				func.printing(g)
				x_list = g[0]
				y_list = g[1]
				plt.plot(x_list,y_list)
				plt.show()


		elif q_list[0] == "T":									#Translation operations						
			dx = float(q_list[1])
			dy = float(q_list[2])

			if shape == "disc":
				new_mat = [[a],[b],[1]]							#Center translation
				#new_mat = func.transpose(new_mat)
				p = func.translate(dx,dy,new_mat)
				#print (p, "c'est p")
				a = p[0][0]
				b = p[1][0]

				print()
				# print("major", major)
				# print("minor", minor)
				# print (major==minor)

				if major != minor:
					print (round(a,2),round(b,2),round(major/2, 2),round(minor/2,2),"\n")
				else: 
					print (round(a,2),round(b,2),round(major/2),"\n")

				#plt.close()
				#fig = pylab.figure()
				#ax = fig.add_subplot(111)
				ax.add_patch(Ellipse((a,b), major, minor,angle, fill=None, EdgeColor=[a1,b1,c1]))
				ax.axis('equal')
				plt.show()



			else:
				h = func.translate(dx,dy,to_pass)						#Polygon translation
				func.printing(h)
				x_list = h[0]
				y_list = h[1]
				plt.plot(x_list,y_list)
				plt.show()


		
		elif query_in != "quit":
			
			print("Invalid input")
			quit()


	except:
		print("Invalid input")
		quit()
