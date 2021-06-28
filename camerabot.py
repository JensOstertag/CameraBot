import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
from picamera import PiCamera
from time import sleep
from tkinter import *

screen_width = 1024
screen_height = 600

# Motor1 for Left/Right Movement
motor1_dir = 29
motor1_stp = 31
motor1_ena = 32
GPIO.setup(motor1_dir, GPIO.OUT)
GPIO.setup(motor1_stp, GPIO.OUT)
GPIO.setup(motor1_ena, GPIO.OUT)

# Motor1 for Up/Down Movement
motor2_dir = 33
motor2_stp = 35
motor2_ena = 36
GPIO.setup(motor2_dir, GPIO.OUT)
GPIO.setup(motor2_stp, GPIO.OUT)
GPIO.setup(motor2_ena, GPIO.OUT)

# Motors Steps Per Revolution
motor_spr = 200

def driveMotor1(invert, speed, steps):
	delay = 60*1000*1000 / motor_spr / speed
	
	if invert:
		GPIO.output(motor1_dir, GPIO.HIGH)
		
		for x in range(steps):
			GPIO.output(motor1_stp, GPIO.HIGH)
			sleep(delay / 1000000)
			GPIO.output(motor1_stp, GPIO.LOW)
			sleep(delay / 1000000)
	else:
		GPIO.output(motor1_dir, GPIO.LOW)
		
		for x in range(steps):
			GPIO.output(motor1_stp, GPIO.HIGH)
			sleep(delay / 1000000)
			GPIO.output(motor1_stp, GPIO.LOW)
			sleep(delay / 1000000)
	
def driveMotor2(invert, speed, steps):
	delay = 60*1000*1000 / motor_spr / speed
	
	if invert:
		GPIO.output(motor2_dir, GPIO.HIGH)
		
		for x in range(steps):
			GPIO.output(motor2_stp, GPIO.HIGH)
			sleep(delay / 1000000)
			GPIO.output(motor2_stp, GPIO.LOW)
			sleep(delay / 1000000)
	else:
		GPIO.output(motor2_dir, GPIO.LOW)
		
		for x in range(steps):
			GPIO.output(motor2_stp, GPIO.HIGH)
			sleep(delay / 1000000)
			GPIO.output(motor2_stp, GPIO.LOW)
			sleep(delay / 1000000)
			
def updateEnableState1(enable):
	if enable:
		GPIO.output(motor1_ena, GPIO.LOW)
	else:
		GPIO.output(motor1_ena, GPIO.HIGH);

def updateEnableState2(enable):
	if enable:
		GPIO.output(motor2_ena, GPIO.LOW)
	else:
		GPIO.output(motor2_ena, GPIO.HIGH);
			
def move_left():
  print("MOVE LEFT")
  driveMotor1(False, 1000, 25)

def move_right():
  print("MOVE RIGHT")
  driveMotor1(True, 1000, 25)
  
def move_up():
  print("MOVE UP")
  driveMotor2(False, 1000, 25)

def move_down():
  print("MOVE DOWN")
  driveMotor2(True, 1000, 25)

updateEnableState1(True)
updateEnableState2(True)

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
