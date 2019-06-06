from tkinter import *
import time

tk = Tk()

class Car:
	def __init__(self, x, y, vx, vy):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.car_c = canvas.create_oval(self.x,self.y,self.x+30,self.y+30,fill="black")


	def movecar(self, stop):
		pos = canvas.coords(self.car_c)
		
		if stop == False and self.vx == 0:
			if pos[3] < 0:
				return canvas.coords(self.car_c,self.x,self.y,self.x+30,self.y+30)

			return canvas.move(self.car_c, self.vx, self.vy)

		if self.vy == 0:
			if pos[2] > 800:
				return canvas.coords(self.car_c,self.x,self.y,self.x+30,self.y+30)

			return canvas.move(self.car_c, self.vx, self.vy)

		else:
			pass


	def stopcar(self, color, stop):
		pos = canvas.coords(self.car_c)

		#vertical
		if self.vx == 0:
			if (color == "red" and pos[3]>344 and pos[3]<345) or (color == "yellow" and pos[3]>344 and pos[3]<345):
				stop = True
				return stop
			else:
				stop = False
				return stop

		if self.vy == 0:
			if (color == "red" and pos[2]>354 and pos[2]<355) or (color == "yellow" and pos[2]>354 and pos[2]<355):
				print(pos[2])
				stop = True
				return stop
			else:
				stop = False
				return stop

		return stop


start_time = time.time()
color1 = "green"
color2 = "green"
stop = False
stoph = False

#canvas
canvas = Canvas(tk, width = 800, height=600)
canvas.grid()

#car
carro = Car(405, 570, 0, -0.07)
hcarlist = []
hcarlist.append(Car(2, 275, 0.07, 0))


#vertical traffic light
canvas.create_rectangle(448, 328, 472, 396)
red1 = canvas.create_oval(450,330,470,350,fill="grey")
yellow1 = canvas.create_oval(450,352,470,372,fill="grey")
green1 = canvas.create_oval(450,374,470,394,fill="green")

#vertical lane
canvas.create_line(360, 0, 360, 600, fill="black", width=2)
canvas.create_line(440, 0, 440, 600, fill="black", width=2)
#horizontal line in vertical lane
canvas.create_line(360, 330, 440, 330, fill="black", width=2)

#horizontal traffic light
canvas.create_rectangle(316, 154, 340, 222)
red2 = canvas.create_oval(318,156,338,176,fill="red")
yellow2 = canvas.create_oval(318,178,338,198,fill="grey")
green2 = canvas.create_oval(318,200,338,220,fill="grey")

#horizontal lane
canvas.create_line(0, 230, 800, 230, fill="black", width=2)
canvas.create_line(0, 310, 800, 310, fill="black", width=2)
#vertical line in horizontal lane
canvas.create_line(340, 230, 340, 310, fill="black", width=2)



tk.update()



def colorsem (greencolor, yellowcolor, redcolor):
	if greencolor == "green":
		sem_active="green"

	if yellowcolor == "yellow":
		sem_active="yellow"

	if redcolor == "red":
		sem_active="red"

	return sem_active




def traffic (color, sem_active, timesem, start_time):
	#green to yellow
	if sem_active == "green" and timesem > 3:
		#vert traffic
		canvas.itemconfig(green1, fill='grey')
		canvas.itemconfig(yellow1, fill='yellow')
		#hor traffic
		#canvas.itemconfig(green2, fill='grey')
		#canvas.itemconfig(yellow2, fill='yellow')

		start_time = time.time()
		color = "yellow"

		return color, start_time



	#yellow to red
	if sem_active == "yellow" and timesem > 1:
		#vert traffic
		canvas.itemconfig(yellow1, fill='grey')
		canvas.itemconfig(red1, fill='red')
		#hor traffic
		canvas.itemconfig(red2, fill='grey')
		canvas.itemconfig(green2, fill='green')

		start_time = time.time()
		color = "red"

		return color, start_time

	
	if sem_active == "red" and timesem > 2 and timesem < 3:
		canvas.itemconfig(yellow2, fill='yellow')
		canvas.itemconfig(green2, fill='grey')

		return color, start_time

	#red to green
	if sem_active == "red" and timesem > 3:
		#vert traffic
		canvas.itemconfig(red1, fill='grey')
		canvas.itemconfig(green1, fill='green')
		#hor traffic
		canvas.itemconfig(yellow2, fill='grey')
		canvas.itemconfig(red2, fill='red')

		start_time = time.time()
		color = "green"

		return color, start_time
	

	return color, start_time



while True:
	timesem = time.time() - start_time
	#print(timesem)

	sem_active = colorsem(canvas.itemcget(green1, 'fill'), canvas.itemcget(yellow1, 'fill'), canvas.itemcget(red1, 'fill'))	

	color1, start_time = traffic(color1, sem_active, timesem, start_time)
	color2 = colorsem(canvas.itemcget(green2, 'fill'), canvas.itemcget(yellow2, 'fill'), canvas.itemcget(red2, 'fill'))


	if (color2 != "red" or stoph != True) and (color2 != "yellow" or stoph != True):
		hcarlist[0].movecar(stop)
		stoph = hcarlist[0].stopcar(color2, stoph)
	else:
		pass


	if (color1 == "red" and stop == True) or (color1 == "yellow" and stop == True):
		pass
	else:
		carro.movecar(stop)
		stop = carro.stopcar(color1, stop)
	


	tk.update()
#	time.sleep(0.001)