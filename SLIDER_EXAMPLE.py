import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


# def get_current_value():
#     return '{: .2f}'.format(slider.get())


def slider_changed(event):
    distance_label.configure(text=f"Distance from screen: {D.get()}")
    laser.place(x=600+(D.get() * 1.6), y=300)

def height_changed(event):
    height_label.configure(text=f"Height: {h.get()}")
    laser.place(x=600, y=300+(h.get()*1.6))


#creating elements
main_win = tk.Tk()
main_win.title("He Ne Laser")
main_win.geometry("1024x768")
main_win.configure(background='white')



style = ttk.Style()


#btn = ttk.Button(main_win, text="Button", style="TButton")

# creating image
laser = tk.Canvas(main_win, height=96, width=177)
laser.configure(borderwidth=0,highlightthickness=0,background='white')
pic = ImageTk.PhotoImage(Image.open('laser.png'))
laser.create_image(10,10, anchor='nw', image=pic)

#creating elements

D = tk.IntVar()
h = tk.IntVar()

distance = ttk.Scale(main_win, from_=0, to=100, style="Horizontal.TScale", command=slider_changed, variable=D)
distance_label = ttk.Label(main_win, text="Distance from screen: ", style="TLabel")

height = ttk.Scale(main_win, from_=-20, to=20, style="Horizontal.TScale", command=height_changed, variable=h)
height_label = ttk.Label(main_win, text="Height: ", style="TLabel")


#configuring elements
style.configure('TButton', font=(None, 15), foreground='black')
style.configure('Horizontal.TScale', background='white')
style.configure('TLabel', background='white', font=("Helvetical Bold", 10))


#placing elements

#btn.place(x=50,y=50)
laser.place(x=600,y=300)
distance.place(x=880, y=270)
distance_label.place(x=870, y=300)

height.place(x=880, y=200)
height_label.place(x=880, y=230)



main_win.mainloop()
