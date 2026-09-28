# simulate
''' 
creates a simulation, saved as a video file using manim, of a physical system. 
Either of : 
    QM / particle physics
    fluid dynamics
    statics
    electrical 
    chemical 

In each there is a seperate file detailing the objects in the file
ideally, this will eventually be used in a virutal environment that contains the ability to superimpose 
the file onto a video and create a real interactive screen from which to create the simulation objects. 
okay now: 

'''

import PyQt6 as qt
import manimations as m
import numpy as np
import matplotlib.pyplot as plt
import space as s
import constants as k 

class Screen: 
    '''
    Digital Space where simulation is run. 
    It is defined with dimensions, sizes, and calls control pad to know what objects are being manipulated and in what way.
    It also calls the render function to create a video of the simulation.
        Calling out the size of the render and an estimate of the amount of time it will take to render the simulation. 
    '''
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.space = s.Space(dimensions=3, size=10)
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)
        self.space.add_object(obj)

    def render(self):
        # Render the simulation using manim
        m.render_simulation(self.space, self.objects)
        if m.render_successful():
            return print("Simulation rendered successfully.")
        else: 
            return print("Simulation rendering failed.")



class ControlPad: 
    '''' 
    An interactive control pad for manipulating the simulation objects on the screen.
    
    '''
    def __init__(self, screen):
        self.screen = screen



if __name__ == "__main__":
    # Create a screen for the simulation
    screen = Screen(width=10, height=10)

    # Create a control pad for the simulation
    control_pad = ControlPad(screen)

    # Add objects to the screen (example objects)
    # obj1 = SomeObject(parameters)
    # obj2 = AnotherObject(parameters)
    # screen.add_object(obj1)
    # screen.add_object(obj2)

    # Render the simulation
    screen.render()