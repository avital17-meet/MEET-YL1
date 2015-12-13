import meet
from meet import *
import random
cells=[]
user_cell={"x":0,"y":0,"radius":10,"dy":0,"dx":0,"color":"black"}
user_cell=meet.create_cell(user_cell)
cells.append(user_cell)
colors=["red","blue","pink","purple","black","orange","green","gray","gold", "yellow"]
for x in range (5):
	cell={"x":get_random_x(),"y":get_random_y(),"radius":random.randint(3,10),"dy":random.uniform(-1.00,2.00),"dx":random.uniform(-1.00,2.00),"color":random.choice(colors)}
	z=create_cell(cell)
	cells.append(z)


def Edge(cells):
	x,y=meet.get_user_direction(user_cell)
	user_cell.set_dx(x)
	user_cell.set_dy(y)
	for cell in cells:
		w=meet.get_screen_width()
		h=meet.get_screen_height()
		x=cell.xcor()
		y=cell.ycor()

		if (cell.xcor()>w):
			cell.set_dx(-cell.get_dx())
	
		elif (cell.xcor()<-w):
			cell.set_dx(-cell.get_dx())
		if (cell.ycor()>h):	
			cell.set_dy(-cell.get_dy())
		
		
		elif (cell.ycor()<-h):	
			cell.set_dy(-cell.get_dy())

def Collision(cells):
	for i in cells:
		for j in cells:
			if(abs(j.ycor()-i.ycor())<i.get_radius()/2):
				if(abs(j.xcor()-i.xcor())<i.get_radius()/2):
					if (i.get_radius()>j.get_radius()):
						i.set_radius(j.get_radius()/2+i.get_radius())
						j.set_radius(random.uniform(5,user_cell.get_radius()+10))
						j.goto(meet.get_random_x(),meet.get_random_y())
						j.set_dy(random.uniform(-1.00,2.00))
						j.set_dx(random.uniform(-1.00,2.00))
						meet.move_cell(j)
					elif(j.get_radius()>i.get_radius()):
						if(j['radius']==user_cell['radius'] and j['dx']==user_cell['dx'] and j['dy']==user_cell['dy']):
							turtle.write("Game Over!")
							turtle.mainloop()
						else:
							j.set_radius(i.get_radius()/2+j.get_radius())
							i.set_radius(random.uniform(5,user_cell.get_radius()+10))
							i.goto(meet.get_random_x(),meet.get_random_y())
							i.set_dy(random.uniform(-1.00,2.00))
							i.set_dx(random.uniform(-1.00,2.00))
							meet.move_cell(i)

while True :
	move_cells(cells)
	Edge(cells)
	Collision(cells)



meet.mainloop()
