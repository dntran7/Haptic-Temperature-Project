######################################################
#    This file is an example of how to use the LRHD 
#    The motors are fired sequentially 
#    and displayed on the screen visually
######################################################

from lrhd import lrhd
import numpy as np
import time

# Create an instance of the LRHD
hap_disp = lrhd()

# Get the dimension of the display
dims = (hap_disp.y_dim, hap_disp.x_dim)

# Clear the display
hap_disp.clear_display()

# Warms up the display
hap_disp.warmup()

# Scans the display by firing each motor sequentially
'''for i in range(dims[0]*dims[1]):
    # Create a blank haptic image 
    image = np.zeros(dims, np.uint8)
    # Lights up one motor
    image.flat[i] = 255
    # Sends the haptic image to the LRHD
    hap_disp.draw(image)
    # Delay so it can be felt
    time.sleep(0.4)'''
def alternateleftright(pulsewidth,gap):
    for x in range(0,3):
        image = np.zeros(dims, np.uint8)
        image[0,3] = 255
        image[1,3] = 255
        image[2,3] = 255
        image[3,3] = 255
        hap_disp.draw(image)
        time.sleep(pulsewidth)
        hap_disp.clear_display()
        time.sleep(gap)
        image = np.zeros(dims, np.uint8)
        image[0,0] = 255
        image[1,0] = 255
        image[2,0] = 255
        image[3,0] = 255
        hap_disp.draw(image)
        time.sleep(pulsewidth)
        hap_disp.clear_display()
        time.sleep(gap)
    time.sleep(5)
    
def alternatetopbottom(pulsewidth,gap):
    for x in range(0,3):
        image = np.zeros(dims, np.uint8)
        image[0,0] = 255
        image[0,1] = 255
        image[0,2] = 255
        image[0,3] = 255
        hap_disp.draw(image)
        time.sleep(pulsewidth)
        hap_disp.clear_display()
        time.sleep(gap)
        image = np.zeros(dims, np.uint8)
        image[3,0] = 255
        image[3,1] = 255
        image[3,2] = 255
        image[3,3] = 255
        hap_disp.draw(image)
        time.sleep(pulsewidth)
        hap_disp.clear_display()
        time.sleep(gap)
    time.sleep(5)
    
    
def explode(pulsewidth,gap):
    image = np.zeros(dims, np.uint8)
    image[1,1] = 255
    image[1,2] = 255
    image[2,1] = 255
    image[2,2] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap) 
    image = np.zeros(dims, np.uint8)
    image[1,1] = 255
    image[1,2] = 255
    image[2,1] = 255
    image[2,2] = 255
    image[0,0] = 255
    image[0,3] = 255
    image[3,0] = 255
    image[3,3] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    image = np.zeros(dims, np.uint8)
    image[0,0] = 255
    image[0,3] = 255
    image[3,0] = 255
    image[3,3] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth + 0.1) #arbitrary  value to emphasize on the explode pattern
    hap_disp.clear_display()
    time.sleep(gap)
    time.sleep(5)

def rain(pulsewidth,gap):
    image = np.zeros(dims, np.uint8)
    image[0,3] = 255
    image[0,1] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display() 
    time.sleep(gap)
    image = np.zeros(dims, np.uint8)
    image[1,1] = 255
    image[1,3] = 255
    image[0,0] = 255
    image[0,2] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    image = np.zeros(dims, np.uint8)
    image[1,0] = 255
    image[1,2] = 255
    image[2,3] = 255
    image[2,1] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    image = np.zeros(dims, np.uint8)
    image[3,1] = 255
    image[3,3] = 255
    image[2,0] = 255
    image[2,2] = 255
    image[0,3] = 255
    image[0,1] = 255        
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)
    time.sleep(5)
    
def shouldertap(pulsewidth,gap):
    for x in range(0,3):
        image = np.zeros(dims, np.uint8)
        image[0,3] = 255
        image[1,3] = 255
        image[0,2] = 255
        image[1,2] = 255
        hap_disp.draw(image)
        time.sleep(pulsewidth)
        hap_disp.clear_display()
        time.sleep(gap)
    time.sleep(5)
    
def snakehorizontal(pulsewidth,gap):
    for r in range (0,3):
        if(r==1):
            for x in range(0,3):
                image = np.zeros(dims, np.uint8)
                image[r,x] = 255
                image[r,x+1] = 255
                hap_disp.draw(image)
                time.sleep(pulsewidth)
                hap_disp.clear_display()
                time.sleep(gap)
        else:
            for x in reversed(range(1,4)):
                image = np.zeros(dims, np.uint8)
                image[r,x] = 255
                image[r,x-1] = 255
                hap_disp.draw(image)
                time.sleep(pulsewidth)
                hap_disp.clear_display()
                time.sleep(gap)
        
    time.sleep(5)

def snakevertical(pulsewidth,gap):
    for c in reversed(range (1,4)):
        if(c==2):
            for r in reversed(range(1,4)):
                image = np.zeros(dims, np.uint8)
                image[r,c] = 255
                image[r-1,c] = 255
                hap_disp.draw(image)
                time.sleep(pulsewidth)
                hap_disp.clear_display()
                time.sleep(gap)
        else:
            for r in range(0,3):
                if(r==2 and c==1):
                    c=0
                    r=2
                image = np.zeros(dims, np.uint8)
                image[r,c] = 255
                image[r+1,c] = 255
                hap_disp.draw(image)
                time.sleep(pulsewidth)
                hap_disp.clear_display()
                time.sleep(gap)
        
    time.sleep(5)

def sixmotorburst(pulsewidth,gap):
    for x in range(0,3):
        image = np.zeros(dims, np.uint8)
        image[0,2] = 255
        image[1,3] = 255
        image[1,0] = 255
        image[2,1] = 255
        image[2,2] = 255
        image[3,2] = 255
        hap_disp.draw(image)
        time.sleep(pulsewidth)
        hap_disp.clear_display()
        time.sleep(gap)
    time.sleep(5)

def spinedown(pulsewidth,gap):
    for x in range(0,4):
        image = np.zeros(dims, np.uint8)
        image[x,1] = 255
        image[x,2] = 255
        hap_disp.draw(image)
        time.sleep(pulsewidth)
        hap_disp.clear_display()
        time.sleep(gap)
    time.sleep(5)
    
def spineup(pulsewidth,gap):
    for x in reversed(range(0,4)):
        image = np.zeros(dims, np.uint8)
        image[x,1] = 255
        image[x,2] = 255
        hap_disp.draw(image)
        time.sleep(pulsewidth)
        hap_disp.clear_display()
        time.sleep(gap)
    time.sleep(5)

def spiral(r,c,pulsewidth,gap):
    image = np.zeros(dims, np.uint8)
    image[r,c] = 255
    image[r+1,c] = 255
    image[r,c-1] = 255
    image[r+1,c-1] = 255
    hap_disp.draw(image)
    time.sleep(pulsewidth)
    hap_disp.clear_display()
    time.sleep(gap)

def spiralout(pulsewidth,gap):
    r=1
    c=2
    spiral(r,c,pulsewidth,gap)
        
    r=1
    c=3
    spiral(r,c,pulsewidth,gap)
        
    r=0
    c=3
    spiral(r,c,pulsewidth,gap)
        
    r=0
    c=2
    spiral(r,c,pulsewidth,gap)
          
    r=0
    c=1
    spiral(r,c,pulsewidth,gap)
    
    r=1
    c=1
    spiral(r,c,pulsewidth,gap)
    
    r=2
    c=1
    spiral(r,c,pulsewidth,gap)
    
    r=2
    c=2
    spiral(r,c,pulsewidth,gap)
    
    r=2
    c=3
    spiral(r,c,pulsewidth,gap)
    
    time.sleep(5)   

def spiralin(pulsewidth,gap):
    r=2
    c=1
    spiral(r,c,pulsewidth,gap)
        
    r=2
    c=2
    spiral(r,c,pulsewidth,gap)
        
    r=2
    c=3
    spiral(r,c,pulsewidth,gap)
        
    r=1
    c=3
    spiral(r,c,pulsewidth,gap)
          
    r=0
    c=3
    spiral(r,c,pulsewidth,gap)
    
    r=0
    c=2
    spiral(r,c,pulsewidth,gap)
    
    r=0
    c=1
    spiral(r,c,pulsewidth,gap)
    
    r=1
    c=1
    spiral(r,c,pulsewidth,gap)
    
    r=1
    c=2
    spiral(r,c,pulsewidth,gap)
    
    time.sleep(5)    
    
def waveleft(pulsewidth,gap):
    for c in range (0,4):
        image = np.zeros(dims, np.uint8)
        image[0,c] = 255
        image[1,c] = 255
        image[2,c] = 255
        image[3,c] = 255
        hap_disp.draw(image)
        time.sleep(pulsewidth)
        hap_disp.clear_display()
        time.sleep(gap)
    time.sleep(5)
    
def waveright(pulsewidth,gap):
    for c in reversed(range (0,4)):
        image = np.zeros(dims, np.uint8)
        image[0,c] = 255
        image[1,c] = 255
        image[2,c] = 255
        image[3,c] = 255
        hap_disp.draw(image)
        time.sleep(pulsewidth)
        hap_disp.clear_display()
        time.sleep(gap)
    time.sleep(5) 
    
def waveup(pulsewidth,gap):
    for r in reversed(range (0,4)):
        image = np.zeros(dims, np.uint8)
        image[r,0] = 255
        image[r,1] = 255
        image[r,2] = 255
        image[r,3] = 255
        hap_disp.draw(image)
        time.sleep(pulsewidth)
        hap_disp.clear_display()
        time.sleep(gap)
    time.sleep(5)    
    
def wavedown(pulsewidth,gap):
    for r in range (0,4):
        image = np.zeros(dims, np.uint8)
        image[r,0] = 255
        image[r,1] = 255
        image[r,2] = 255
        image[r,3] = 255
        hap_disp.draw(image)
        time.sleep(pulsewidth)
        hap_disp.clear_display()
        time.sleep(gap)
    time.sleep(5)     
    

#start
'''time.sleep(5)
#wavedown(0.5)
#waveup(0.2)
alternateleftright(0.5)
alternatetopbottom(0.5)
shouldertap(0.5)
waveleft(0.3)
waveright(0.5)
spiralin(0.5)
spiralout(0.5)'''
#rain(0.3)
#shouldertap(0.2)
#snakevertical(0.5)
#snakehorizontal(0.5)
pattern = -1
interval = -1
gapped = 0.05
while (pattern != 0):
    print(pattern)
    print(interval)
    print(gapped)
    time.sleep(2)
    if pattern==1:
        alternateleftright(interval,gapped)
        print("here")
    elif pattern==2:
        alternatetopbottom(interval,gapped)
    elif pattern==3:
        explode(interval,gapped)
    elif pattern==4:
        rain(interval,gapped)
    elif pattern==5:
        shouldertap(interval,gapped)
    elif pattern==6:
        snakevertical(interval,gapped)
    elif pattern==7:
        snakehorizontal(interval,gapped)
    elif pattern==8:
        sixmotorburst(interval,gapped)
    elif pattern==9:
        spinedown(interval,gapped)
    elif pattern==10:
        spineup(interval,gapped)
    elif pattern==11:
        wavedown(interval,gapped)
    elif pattern==12:
        waveleft(interval,gapped)
    elif pattern==13:
        waveright(interval,gapped)
    elif pattern==14:
        waveup(interval,gapped)
    elif pattern==15:
        spiralin(interval,gapped)
    elif pattern==16:
        spiralout(interval,gapped)
    pattern = int(input("type on pattern number (0 to stop)"))
    interval =float(input("type in interval - 1 or 0.25"))
