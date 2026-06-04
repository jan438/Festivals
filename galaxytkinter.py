
import math
import tkinter as tk
from random import randint, uniform, random

# Set scaling factor for galaxy:
SCALE = 225

# set-up tkinter display canvas:
root = tk.Tk()
root.title("A Spiral Galaxy")
c = tk.Canvas(root, width=1000, height=800, bg='black')
c.configure(scrollregion=(-500, -400, 500, 400))

c.grid()

# Define function to build an individual spiral arm:
def build_spiral(b, r, rot_fac, fuz_fac, arm):
    """Build spiral arms for tkinter display using Logarithmic spiral formula.
    b = constant for spiral direction and "openess"
    r = scaled galactic disc radius
    rot_fac = factor to rotate each spiral arm
    fuz_fac = random shift in star position in arm, applied to 'fuzz' variable
    arm = spiral arm (0 = leading edge, 1 = trailing stars)
    """
    spiral_stars = []
    fuzz = int(0.030 * abs(r))  # Scalable initial amount to shift locations.
    for i in range(0, 800, 2):
        theta = math.radians(-i)
        x = r * math.exp(b*theta) * math.cos(theta - math.pi * rot_fac)\
            - randint(-fuzz, fuzz) * fuz_fac
        y = r * math.exp(b*theta) * math.sin(theta - math.pi * rot_fac)\
            - randint(-fuzz, fuzz) * fuz_fac
        spiral_stars.append((x, y))
        
    for x, y in spiral_stars:
        if arm == 0 and int(x % 2) == 0:
            c.create_text(x, y, 
                          fill='white', 
                          font=('Helvetica', '6'), 
                          text='*')
        elif arm == 0 and int(x % 2) != 0:
            c.create_text(x, y, 
                          fill='white', 
                          font=('Helvetica', '5'), 
                          text='*')
        elif arm == 1:
            c.create_text(x, y, 
                          fill='white', 
                          font=('Helvetica', '5'), 
                          text='.')

# Define functions to distribute star "haze" between spiral arms:
def random_polar_coordinates(scale_factor):
    """Generate uniform random x,y point within a disc for 2-D display."""
    n = random()
    theta = uniform(0, 2 * math.pi)
    x = round(math.sqrt(n) * math.cos(theta) * scale_factor)
    y = round(math.sqrt(n) * math.sin(theta) * scale_factor)
    return x, y

def star_haze(scale_factor, density):
    """Randomly distribute faint stars in galactic disc.
    SCALE = scaled galactic disc radius
    density = multiplier to vary number of stars posted
    """
    for _ in range(0, scale_factor * density):
        x, y = random_polar_coordinates(scale_factor)
        c.create_text(x, y, 
                      fill='white', 
                      font=('Helvetica', '3'), 
                      text='.')

def build_galaxy():
    """Generate the galaxy display with tkinter."""
    b=0.3
    fuz_fac=1.5
    
    # Build leading and trailing spiral arms:
    build_spiral(b=b, r=SCALE, rot_fac=2, fuz_fac=fuz_fac, arm=0)
    build_spiral(b=b, r=SCALE, rot_fac=1.91, fuz_fac=fuz_fac, arm=1)
 
    build_spiral(b=b, r=-SCALE, rot_fac=2, fuz_fac=fuz_fac, arm=0)
    build_spiral(b=b, r=-SCALE, rot_fac=-2.09, fuz_fac=fuz_fac, arm=1)
 
    build_spiral(b=b, r=-SCALE, rot_fac=0.5, fuz_fac=fuz_fac, arm=0)
    build_spiral(b=b, r=-SCALE, rot_fac=0.4, fuz_fac=fuz_fac, arm=1)
 
    build_spiral(b=b, r=-SCALE, rot_fac=-0.5, fuz_fac=fuz_fac, arm=0)
    build_spiral(b=b, r=-SCALE, rot_fac=-0.6, fuz_fac=fuz_fac, arm=1)
    
    # Distribute star haze:
    star_haze(SCALE, density=20)

    # run tkinter loop:
    root.mainloop()
    
build_galaxy()
