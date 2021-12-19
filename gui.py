import tkinter as tk
import os
import numpy as np
import threading
from time import sleep
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# class screen:
# 	"""docstring for screen"""
# 	def __init__(self, x_pix,y_pix):
# 		super(screen, self).__init__()
# 		self.x_pix = x_pix
# 		self.y_pix = y_pix

# 		self.pixels = []
# 		for x in self.x_pix:
# 			temp = []
# 			for y in self.y_pix:
# 				temp.append()
		
class jumpy:
	"""docstring for jumpy"""

	#states:
	#	0	black
	#	1 	white (player)
	#   2	red (floor)

	def __init__(self,maxx,maxy):
		super(jumpy, self).__init__()
		self.max_x = maxx
		self.max_y = maxy
		self.game_running = False

		self.player_pos = [3,self.max_y-5] #[x,y] starting player position
		self.floors = [[0,self.max_y-4,self.max_x],[self.max_x,self.max_y-5,self.max_x]]#[[x0,y0,len0],[x1,y1,len1]] starting floor state
		
		self.jump_sequence = [[0,-1],[0,0],[0,0],[0,0],[0,1]] #[[change in x,change in y],...]
		# self.raise_floors_sequence = [[0,1]]

	# 	self.state_array = np.zeros((self.max_x*10,self.max_y))
	# 	self.state_array[self.player_pos[0]][self.player_pos[1]] = 1
	# 	self.state_array[self.player_pos[0]][self.player_pos[1]] = 1
	
	# def move_player(self):
		

	# def step(self):


	

	

class gui:
	"""gui class contains all methods and variables needed for all GUIs.
		GUIs include the main GUI, delete data GUI, and select premade 
		initial conditions (not yet implimented)."""

	

	def __init__(self):
		super(gui, self).__init__()
		print("BENGIN")
		# ###Begin main window making###
		# if not os.path.isdir('data_dump'):
		# 	os.mkdir('data_dump')


		self.window = tk.Tk()
		self.window.title('Cannon Fodder')
		self.window.resizable(True, True)

		self.queue = []
		self.jump_on = False

		self.y_pix = 15 #number of pixels in vertical direction
		self.x_pix = int(self.y_pix*1.5) #number of pixels in horizontal direction
		self.dt = 0.1

		self.game = jumpy(self.x_pix,self.y_pix)
		self.game_on = False
		# self.display_screen = screen(self.x_pix,self.y_pix)

		self.w_width  = int(self.window.winfo_screenwidth()*2/3)
		self.w_height = int(self.window.winfo_screenwidth()*4/5)
		# self.w_height = int(self.window.winfo_screenheight()*4/5)
		self.window.geometry(f'{self.w_width}x{self.w_height}')

		#set up frames

		self.make_game_frame()
		self.make_info_frame()
		self.window.columnconfigure(0, weight=1)
		self.window.rowconfigure(0, weight=5)
		self.window.rowconfigure(1, weight=1)
 
		# self.pixels[0][1].update()
		# print(self.pixels)
		# self.game.game_loop()
		print("END")

		# for i in range(4):
		# 	self.frm_p_input.columnconfigure(i, weight=1)
		# 	self.frm_p_input.rowconfigure(i, weight=1)
		# for i in range(4):
		# 	self.frm_variable_input.columnconfigure(i, weight=1)
		# 	self.frm_variable_input.rowconfigure(i, weight=1)
		# for i in range(4):
		# 	self.existing_data_frame.columnconfigure(i, weight=1)
		# 	self.existing_data_frame.rowconfigure(i, weight=1)

	

	def make_pixels(self):
		self.pixels = []

		for x in range(self.x_pix):
			temp = []
			for y in range(self.y_pix):
				temp.append(tk.Frame(master=self.frm_screen, bg="black", \
					relief=tk.RAISED, borderwidth=0))
				temp[-1].grid(row=y,column=x,columnspan=1,rowspan=1,\
					padx=0,pady=0,sticky='NSEW')
				temp[-1].rowconfigure(0, weight=1)
				temp[-1].columnconfigure(0, weight=1)
				self.frm_screen.rowconfigure(y, weight=1)
				self.frm_screen.columnconfigure(x, weight=1)
			self.pixels.append(temp)

		#set starting position
		self.pixels[self.game.player_pos[0]][self.game.player_pos[1]].config(bg='white')
		
		for i in range(self.game.floors[0][0],self.game.floors[0][0]+self.game.floors[0][2]):
			self.pixels[i][self.game.floors[0][1]].config(bg='red',relief=tk.RAISED,borderwidth=8)
	
	#makes the frame the game will be displayed in
	def make_game_frame(self):
		self.frm_game = tk.Frame(master=self.window, bg="green", \
			relief=tk.RIDGE, borderwidth=5)
		self.frm_game.grid(row=0,column=0,columnspan=1,rowspan=1, \
			padx=0,pady=0,sticky='NSEW')
		self.frm_game.rowconfigure(0, weight=1)
		self.frm_game.columnconfigure(0, weight=1)

		self.make_screen_frame()
		#set up graph's frame
		# master_ = self.frm_game

		# self.fig = plt.Figure(figsize=(7*scale,5*scale),dpi=dpi_)
		# master_.get_tk_widget().grid(row=0,column=0,sticky='NSEW')
		
		# self.fg_width = self.frm_game.winfo_width()
		# self.fg_height = self.frm_game.winfo_height()
	def make_info_frame(self):
		self.frm_info = tk.Frame(master=self.window, bg="black",\
			relief=tk.RIDGE, borderwidth=5)
		self.frm_info.grid(row=1,column=0,columnspan=1,rowspan=1, \
			padx=0,pady=0,sticky='NSEW')
		self.frm_info.rowconfigure(0, weight=1)
		self.frm_info.columnconfigure(0, weight=1)
		
	def make_screen_frame(self):
		self.frm_screen = tk.Frame(master=self.frm_game,bg="black",\
			relief=tk.RAISED, borderwidth=5)
		self.frm_screen.grid(row=0,column=0,columnspan=1,rowspan=1,\
			padx=int(self.w_width)/20,pady=int(self.w_height)/20,sticky='NSEW')

		self.make_pixels()

	def move_floors(self,change):
		print("chnage {}".format(change))
		for ind,floor in enumerate(self.game.floors):
			for i in range(floor[0],floor[0]+floor[2]):
				if i < self.x_pix:
					print("start")
					print(len(self.pixels[0]))
					print(len(self.pixels[1]))
					print(floor[0])
					print(i)
					print(change[0])
					print(floor[1])
					print(change[1])
					self.pixels[i+change[0]][floor[1]+change[1]].config(bg='red',relief=tk.RAISED,borderwidth=8)
					self.pixels[i][floor[1]].config(bg='black',relief=tk.FLAT)

			self.game.floors[ind][0] += change[0]
			self.game.floors[ind][1] += change[1]
			# floor[0] += change[0]
			# floor[1] += change[1]


	def move_player(self,change):
		# print(change)
		posx = self.game.player_pos[0]
		posy = self.game.player_pos[1]
		start_frame = self.pixels[posx][posy]
		self.pixels[posx+change[0]][posy+change[1]].config(bg='white',relief=tk.FLAT)
		# self.pixels[posx][posy].config(bg='white')
		start_frame.config(bg='black',relief=tk.FLAT)
		self.game.player_pos[0] = posx + change[0]
		self.game.player_pos[1] = posy + change[1]
		self.window.update()
		# start_frame.update()
		# self.pixels[posx][posy-1].update()
		# for floor in self.game.floors:
		# 	print(floor[0],posx)
		# 	if floor[0] > posx:
		# 		continue
		# 	else:
		# 		for floor in self.game.floors:
		# 			floor[0]-=1
		# 			for i in range(floor[0],floor[0]+floor[2]):
		# 				if i >= self.x_pix:
		# 					break
		# 				self.pixels[i][floor[1]].config(bg="red",relief=tk.RIDGE)
		# 				self.pixels[i][floor[1]+1].config(bg="black",relief=tk.FLAT)


		# sleep(.1)
		# self.
		# self.pixels[posx][posy-1].config(bg='black')
		# start_frame.config(bg='white')

	def key_press(self,event):
		# print(self.game_onx)
		if not self.game_on:
			self.game_on = True
			self.game_loop()
			# clock_step_event = threading.Thread(target=self.game_loop)
			# clock_step_event.start()
			
		# if event.keysym == 'enter':
		# 	self.game_loop()
		else:
			if event.keysym == 'space':
				if self.jump_on == False:
					self.jump_on = True
				# jump_event = threading.Thread(target=self.jump)
				# jump_event.start()

	def game_loop(self):
		while self.game_on:
			if self.jump_on:
				# self.jump()
				for change in self.game.jump_sequence:
					if not (change[0] == 0 and change[1] == 0):
						self.move_player(change)
					self.step() 
				self.jump_on = False
			self.step()
			if len(self.game.floors) == 0:
					self.game_on = False

	def step(self):
		for floor in self.game.floors:
			# print("stepping")
			floorx = floor[0]
			floory = floor[1]
			floorlen = floor[2]
			print(floorx,floory,floorlen)
			# exit()
			if floorx == 0:
				if floorlen == 1:
					floorlen -= 1
					self.game.floors.remove(floor)
					print("Removed floor {}".format(floor))
					self.pixels[floorx+floorlen][floory].config(bg="black",relief=tk.FLAT)
				
				floorlen -= 1
				floor[2] = floorlen
			else:
				floorx-=1
				floor[0]=floorx
			# print("HERE {} {} {}".format(self.jump_on,self.game.player_pos[0],floorx))
			if self.jump_on and self.game.player_pos[0] == floorx:# and self.game.player_pos[y] == floory+1
				# print("MOVED")
				self.move_floors([0,1])
			if floorx < floorlen:
				self.pixels[floorx][floory].config(bg="red",relief=tk.RIDGE)
			if floorx + floorlen < self.x_pix:
				self.pixels[floorx+floorlen][floory].config(bg="black",relief=tk.FLAT)

			self.window.update()
		sleep(0.01)
			# floor[1] = floory+1
	


def main():
	game = gui()
	game.window.bind("<Key>",game.key_press)
	game.window.mainloop()

if __name__ == '__main__':
	main()