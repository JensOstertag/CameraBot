from picamera import PiCamera
from time import sleep
from tkinter import *

screen_width = 1920
screen_height = 1080

def move_left():
  print("MOVE LEFT")

def move_right():
  print("MOVE RIGHT")
  
def move_up():
  print("MOVE UP")

def move_down():
  print("MOVE DOWN")
  
camera = PiCamera()

camera.video_stabilization = True
camera.preview_fullscreen = False
camera.preview_window = (round(screen_width * 0.125), round(screen_height * 0.125), round(screen_width * 0.75), round(screen_height * 0.75))
camera.start_preview()

control_window = Tk()
control_window.title("CameraBot")

Button(control_window, text="Left", command=move_left).place(bordermode=INSIDE, relwidth=0.125, relheight=0.75, relx=0, rely=0.125)
Button(control_window, text="Right", command=move_left).place(bordermode=INSIDE, relwidth=0.125, relheight=0.75, relx=0.875, rely=0.125)
Button(control_window, text="Up", command=move_left).place(bordermode=INSIDE, relwidth=0.75, relheight=0.125, relx=0.125, rely=0)
Button(control_window, text="Down", command=move_left).place(bordermode=INSIDE, relwidth=0.75, relheight=0.125, relx=0.125, rely=0.875)

control_window.wm_attributes("-fullscreen", "True")
control_window.mainloop()