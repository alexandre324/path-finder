# import libraries
import pygame, time, random
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image  


# when the form is submit
def submit_form():
        # set the variables (getting the entry data)
    # positions of the flags
    pos_1 = [0,0]
    pos_2 = [24,24]
    draw = 1
    # pos_1 = [int(pos_x_1.get())-1, int(pos_y_1.get())-1]
    # pos_2 = [int(pos_x_2.get())-1, int(pos_y_2.get())-1]
    # draw = var1.get()
    # close the form window
    # root.destroy()



        # functions
    # draw the gride
    def draw_gride():
        for i in range(0, 500, 20):
            for j in range(0, 500, 20):
                pygame.draw.line(window, (255,255,255), (0, j), (500, j), 1)
            pygame.draw.line(window, (255,255,255), (i, 0), (i, 500), 1)
    
    # draw the walls and the flags
    def draw_walls_flags(gride):
        for i in range(0, len(gride)):
            for j in range(0, len(gride[0])):
                if gride[i][j] == 1:
                    pygame.draw.rect(window,(255,255,255), (i*20,j*20,20,20))
                    pygame.display.update()
                elif gride[i][j] == 2:
                    pygame.draw.rect(window,(255,0,0), (i*20,j*20,20,20))
                    pygame.display.update()
                elif gride[i][j] == 3:
                    pygame.draw.rect(window,(255,255,0), (i*20,j*20,20,20))
                    pygame.display.update()
                elif gride[i][j] == 4:
                    pygame.draw.rect(window,(0,255,0), (i*20,j*20,20,20))
                    pygame.display.update()
                elif gride[i][j] == 5:
                    pygame.draw.rect(window,(0,0,255), (i*20,j*20,20,20))
                    pygame.display.update()
    
    # draw the new rectangle
    def new_rect(actual_pos_x, actual_pos_y):
        if gride[actual_pos_x][actual_pos_y] == 0 or gride[actual_pos_x][actual_pos_y] == 5:
            gride[actual_pos_x][actual_pos_y] = 4
            
        if gride[actual_pos_x+1][actual_pos_y] == 0 and gride[actual_pos_x+1][actual_pos_y] != 4:
            gride[actual_pos_x+1][actual_pos_y] = 5
        
        if gride[actual_pos_x-1][actual_pos_y] == 0 and gride[actual_pos_x-1][actual_pos_y] != 4:
            gride[actual_pos_x-1][actual_pos_y] = 5
            
        if gride[actual_pos_x+1][actual_pos_y+1] == 0 and gride[actual_pos_x+1][actual_pos_y+1] != 4:
            gride[actual_pos_x+1][actual_pos_y+1] = 5
            
        if gride[actual_pos_x][actual_pos_y-1] == 0 and gride[actual_pos_x][actual_pos_y-1] != 4:
            gride[actual_pos_x][actual_pos_y-1] = 5
        
        if gride[actual_pos_x][actual_pos_y+1] == 0 and gride[actual_pos_x][actual_pos_y+1] != 4:
            gride[actual_pos_x][actual_pos_y+1] = 5
            
        if gride[actual_pos_x -1][actual_pos_y+1] == 0 and gride[actual_pos_x -1][actual_pos_y+1] != 4:
            gride[actual_pos_x - 1][actual_pos_y+1] = 5
            
        if gride[actual_pos_x + 1][actual_pos_y-1] == 0 and gride[actual_pos_x + 1][actual_pos_y-1] != 4:
            gride[actual_pos_x + 1][actual_pos_y-1] = 5
            
        
        
    # find the path
    def find_path(pos_1, pos_2, draw, gride):
        print(draw)
        actual_pos_x = pos_1[0]
        actual_pos_y = pos_1[1]
        
        while actual_pos_x != pos_2[0] and actual_pos_y != pos_2[1]:
            if gride[actual_pos_x + 1][actual_pos_y + 1] != 1:
                actual_pos_x += 1
                actual_pos_y += 1
                if actual_pos_x <= 25:
                    new_rect(actual_pos_x, actual_pos_y)
                else:
                    actual_pos_y += 1
                    
                if actual_pos_y <= 25:
                    new_rect(actual_pos_x, actual_pos_y)
                else:
                    actual_pos_x += random.choice([-1, 1])
            else:
                actual_pos_x -= 1
                actual_pos_y += 1
                new_rect(actual_pos_x, actual_pos_y)
            draw_walls_flags(gride)
                
            print(actual_pos_x, actual_pos_y)
            
        return gride
    if pos_1[0] >= 0 and pos_1[0] <= 25 and  pos_1[1] >= 0 and pos_1[1] <= 25 and pos_2[0] >= 0 and pos_2[0] <= 25 and pos_2[1] >= 0 and pos_2[1] <= 25:
        # variables
        running = True
        draw_fences = True
        gride = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]
        # start the pygame window
        pygame.init()
        window = pygame.display.set_mode((500, 550))
        draw_gride()
        gride[pos_1[0]][pos_1[1]] = 2
        gride[pos_2[0]][pos_2[1]] = 3
        
        draw_walls_flags(gride)
        
        # write "press enter" on the bottom of the screen
        font = pygame.font.SysFont(None, 24)
        img = font.render('press enter (start)', True, (255,255,255))
        window.blit(img, (200, 510))

        while running:
            # get the mouse click and position
            pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]
            # display the pygame window
            pygame.display.update()
            # check events
            for event in pygame.event.get():
                # if draw
                if pressed1 and draw_fences and mouse_x < 500 and mouse_y < 500:
                    mouse_pos_x = mouse_x // 20
                    mouse_pos_y = mouse_y // 20
                    gride[mouse_pos_x][mouse_pos_y] = 1
                    draw_walls_flags(gride)
                # if window close
                elif event.type == pygame.QUIT:
                    running = False
                # if enter is pressed (start)
                elif event.type==pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_SPACE]:
                    # set the window size 
                    window = pygame.display.set_mode((500, 500))
                    # draw everthing back
                    draw_gride()
                    draw_walls_flags(gride)
                    # find the path
                    gride = find_path(pos_1, pos_2, draw, gride)
                    draw_walls_flags(gride)

if __name__ == "__main__":
    submit_form()
    # # load the Form window 
    # root = tk.Tk()
    # root.title("Form")
    # root.geometry('500x600')
    # var1 = tk.IntVar()

    # # picture gride 
    # canvas = Canvas(root, width = 400, height = 400)  
    # canvas.pack()  
    # img = ImageTk.PhotoImage(Image.open("gride.png"))  
    # canvas.create_image(10, 10, anchor=NW, image=img) 

    # # for the text (to hide when it's clicked)
    # class EntryWithPlaceholder(tk.Entry):
    #     def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
    #         super().__init__(master)

    #         self.placeholder = placeholder
    #         self.placeholder_color = color
    #         self.default_fg_color = self['fg']

    #         self.bind("<FocusIn>", self.foc_in)
    #         self.bind("<FocusOut>", self.foc_out)

    #         self.put_placeholder()

    #     def put_placeholder(self):
    #         self.insert(0, self.placeholder)
    #         self['fg'] = self.placeholder_color

    #     def foc_in(self, *args):
    #         if self['fg'] == self.placeholder_color:
    #             self.delete('0', 'end')
    #             self['fg'] = self.default_fg_color

    #     def foc_out(self, *args):
    #         if not self.get():
    #             self.put_placeholder() 
    
    # # entry 1 with text
    # label = Label( root, text="first position:")
    # label.pack()
    # pos_x_1 = EntryWithPlaceholder(root, "x:")
    # pos_y_1 = EntryWithPlaceholder(root, "y:")
    # pos_x_1.pack()
    # pos_y_1.pack()
    
    
    # # entry2 with text
    # label = Label( root, text="second position:")
    # label.pack()
    # pos_x_2 = EntryWithPlaceholder(root, "x:")
    # pos_y_2 = EntryWithPlaceholder(root, "y:")
    # pos_x_2.pack()
    # pos_y_2.pack()  

    # # check box
    # check = tk.Checkbutton(root, text='draw',variable=var1, onvalue=1, offvalue=0)
    # check.pack()

    # # subtmit button
    # button = Button(root, text="Valid", command=submit_form)
    # button.pack()

    # # show the window
    # root.mainloop()

