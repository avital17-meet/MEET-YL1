from meet import *
import random
cells=[]
cells_num=0
while(cells_num<20):
	ball1= {"radius":random.randint(1,100), "x":random.randint(-10,10), "y":random.randint(-10,10), "dx":random.randint(-10,10), "dy":random.randint(-10,10)}
	circle1 = create_cell(ball1)
	cells.append(circle1)
	cells_num=cells_num+1

for cell in cells:
	width = get_screen_width()
	height = get_screen_height()
	x = cell.xcor()
	y = cell.ycor()
	if (-width<x<width)
	elif(-height<y<height)
		


while(True):
	move_cells(cells)
 
