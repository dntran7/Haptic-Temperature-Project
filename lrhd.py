'''from pynput.mouse import Button, Controller, Listener'''
import numpy as np
import cv2
from numpy import interp
import struct
import serial
from threading import Lock
import time
import socket
import os
import sys
import glob

def serial_ports():
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
 
        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result    
    
def find_comm_port():
        comm_port = []
        if os.name == 'posix':
            comm_port = glob.glob('/dev/tty.*')
            comm_port.extend( glob.glob('/dev/ttyACM*'))
            comm_port.extend( glob.glob('/dev/ttyUSB*'))
        elif os.name == 'nt':
            available = []
            for i in range(256):
                try:
                    s = serial.Serial(str(i))
                    available.append('COM'+str(i + 1))
                    s.close()
                except serial.SerialException:
                    pass
            comm_port.extend(available)
        print("Printing current available comm ports.\n")
        print(serial_ports())
        if len(comm_port) == 1:
            return comm_port[0]
        for i in comm_port:
            print(i)
        comm_choice = input("\nPlease choose the full path to the comm port that the haptic controller is connected to:")
        return comm_choice





class lrhd():
    def __init__(self, verbose=False):
        self.x_dim = 4
        self.y_dim = 4
        self.fast_rate = 0.60
        self.slow_rate = 1.40
        self.verbose = verbose
        s = socket.socket()
        
        # Open Serial Connection w/ Arudiono
        #port = '/dev/ttyACM0'
        
        
        port = find_comm_port()
        print('Attempting to connect to: ', port)
        try:
            self.ser = serial.Serial(port, 115200, write_timeout=0.1)             # open serial port
            print('Connected to: ', self.ser.name)           # check which port was really used
        except serial.serialutil.SerialException:
            print('Could not connect to: ', port)
        # Locking Mechanism for Threading
        self.lock = Lock()

    def warmup(self, times=4):
        ' Warms up the serial connection ' 

        for i in range(times):
            img = np.ones((self.y_dim, self.x_dim), np.uint8)
            self.draw(img)
            time.sleep(0.4)
            print('warming up')

        self.clear_display()

        print('Done warming up')

    def ltr_procedure(self, delay=0.25, speed_str=None):
        if(speed_str == 'fast'):
            delay = delay*self.fast_rate
        if(speed_str == 'slow'):
            delay = delay*self.slow_rate
        for x in range(self.x_dim):
            img = np.zeros((self.y_dim, self.x_dim), dtype=np.uint8)
            img[:,x] = 255
            self.draw(img)
            time.sleep(delay)
        self.clear_display()

    def rtl_procedure(self, delay=0.25, speed_str=None):
        if(speed_str == 'fast'):
            delay = delay*self.fast_rate
        if(speed_str == 'slow'):
            delay = delay*self.slow_rate
        for x in reversed(range(self.x_dim)):
            img = np.zeros((self.y_dim, self.x_dim), dtype=np.uint8)
            img[:,x] = 255
            self.draw(img)
            time.sleep(delay)
        self.clear_display()

    def utd_procedure(self, delay=0.25, speed_str=None):
        if(speed_str == 'fast'):
            delay = delay*self.fast_rate
        if(speed_str == 'slow'):
            delay = delay*self.slow_rate
        for y in range(self.y_dim):
            img = np.zeros((self.y_dim, self.x_dim), dtype=np.uint8)
            img[y,:] = 255
            self.draw(img)
            time.sleep(delay)
        self.clear_display()

    def dtu_procedure(self, delay=0.25, speed_str=None):
        if(speed_str == 'fast'):
            delay = delay*self.fast_rate
        if(speed_str == 'slow'):
            delay = delay*self.slow_rate
        for y in reversed(range(self.y_dim)):
            img = np.zeros((self.y_dim, self.x_dim), dtype=np.uint8)
            img[y,:] = 255
            self.draw(img)
            time.sleep(delay)
        self.clear_display()

    def oti_procedure(self, delay=0.5, speed_str=None):
        ' Out to in ' 
        if(speed_str == 'fast'):
            delay = delay*self.fast_rate
        if(speed_str == 'slow'):
            delay = delay*self.slow_rate
        img = np.zeros((self.y_dim, self.x_dim), dtype=np.uint8)
        img[0,0] = 255
        img[3,3] = 255
        img[3,0] = 255
        img[0,3] = 255
        self.draw(img)
        time.sleep(delay)
        self.clear_display()
        img = np.zeros((self.y_dim, self.x_dim), dtype=np.uint8)
        img[1,1] = 255
        img[1,2] = 255
        img[2,1] = 255
        img[2,2] = 255
        self.draw(img)
        time.sleep(delay)
        self.clear_display()

    def ito_procedure(self, delay=0.5, speed_str=None):
        ' In to out ' 
        if(speed_str == 'fast'):
            delay = delay*self.fast_rate
        if(speed_str == 'slow'):
            delay = delay*self.slow_rate
        img = np.zeros((self.y_dim, self.x_dim), dtype=np.uint8)
        img[1,1] = 255
        img[1,2] = 255
        img[2,1] = 255
        img[2,2] = 255
        self.draw(img)
        time.sleep(delay)
        self.clear_display()
        img = np.zeros((self.y_dim, self.x_dim), dtype=np.uint8)
        img[0,0] = 255
        img[0,3] = 255
        img[3,0] = 255
        img[3,3] = 255
        self.draw(img)
        time.sleep(delay)
        self.clear_display()

    def space_procedure(self, area, delay=1.0, speed_str=None):
        ' Gives patterns in the corners and centers given the input ' 
        if(speed_str == 'fast'):
            delay = delay*self.fast_rate
        if(speed_str == 'slow'):
            delay = delay*self.slow_rate
        img = np.zeros((self.y_dim, self.x_dim), dtype=np.uint8)
        if(area == 'TL'):
            img[0,0] = 255
        elif(area == 'TR'):
            img[0,3] = 255
        elif(area == 'BR'):
            img[3,3] = 255
        elif(area == 'BL'):
            img[3,0] = 255
        elif(area == 'OU'):
            img[0,0] = 255
            img[0,3] = 255
            img[3,0] = 255
            img[3,3] = 255
        elif(area == 'IN'):
            img[1,1] = 255
            img[1,2] = 255
            img[2,1] = 255
            img[2,2] = 255
        else:
            print('Error: INCORRECT AREA CODE')
            return 

        self.draw(img)
        time.sleep(delay)
        self.clear_display()

    def clear_display(self):
        img = np.ones((self.y_dim, self.x_dim), dtype=np.uint8)
        self.draw(img)
        img = np.zeros((self.y_dim, self.x_dim), dtype=np.uint8)
        self.draw(img)

            

    #def draw(self, hw_img):
    #    'Draws the various image version to screen and hardware'
    #    # Make sure hw_img is a uint8
    #    if(hw_img.dtype != np.uint8):
    #        print('Wrong format - must be np.uint8')
    #        return 0

    #    # Scale and reverse image for hardware
    #    hw_img_scaled = interp(hw_img, [0,255], [0, 254])


    #    # Send the image to hardware!
    #    #print('Sending Image to Hardware: ')
    #    for x in range(self.x_dim):
    #        for y in range(self.y_dim):
    #            #print('Sending: ', str(x), str(y), str(int(hw_img_scaled[x,y])))
    #            if(not self.lock.locked()):
    #                self.lock.acquire()
    #                try:
    #                    self.ser.write(struct.pack('>B', int(hw_img_scaled[x,y])))
    #                except serial.serialutil.SerialTimeoutException:
    #                    if(self.verbose):
    #                        print('Send Failure!')
    #                        print('Flushing')
    #                    self.ser.flushInput()
    #                self.lock.release()
    #            else:
    #                print("LOCK ALREADY ACQUIRED!")
    #    try:
    #        self.ser.write(struct.pack('>B', int(255)))
    #    except serial.serialutil.SerialTimeoutException:
    #        if(self.verbose):
    #            print('Send Failure!')
    #            print('Flushing')
    #        self.ser.flushInput()
    #            
    #    # Wait so images open
    #    cv2.waitKey(1)

    def draw(self, img):
        'Draws the various image version to screen and hardware'

        # Draw rectangle on original image to screen
        big_img = img.copy()
        cv2.imshow('image', big_img)

        # Scale and reverse image for hardware
        hw_img_scaled = interp(img, [0,255], [0, 254])

        # Send the image to hardware!
        print('Sending Image to Hardware: ')
        for x in range(self.x_dim):
            for y in range(self.y_dim):
                print('Sending: ', str(x), str(y), str(int(hw_img_scaled[x,y])))
                if(not self.lock.locked()):
                    self.lock.acquire()
                    try:
                        self.ser.write(struct.pack('>B', int(hw_img_scaled[x,y])))
                    except serial.serialutil.SerialTimeoutException:
                        print('Send Failure!')
                        self.ser.flushInput()
                        print('Flushed()')
                    self.lock.release()
                else:
                    print("LOCK ALREADY ACQUIRED!")
        try:
            self.ser.write(struct.pack('>B', int(255)))
            print("RESTART at 0")
        except serial.serialutil.SerialTimeoutException:
            print('Send Failure!')
            self.ser.flushInput()
            print('Flushed()')
                
        # Wait so images open
        cv2.waitKey(1)
    