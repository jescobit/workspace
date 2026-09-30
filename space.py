'''
Creates an Rn dim space and defines all the objects that can exist in it. 
Then exports the space in a format that can be used later. 
    (format undecided, hash map??? or just object file?)

Objects: 
    points: 
    lines: 
    planes: 
    volumes: 
    tensors: 
    fields: 


'''
import numpy as np
import matplotlib.pyplot as plt
import PyQt6 as qt 
import constants as k

class momentum: 
    def __init__(self, magnitude, direction=()): 
        self.magnitude = magnitude
        self.direction = direction


class point: 
    def __init__(self, position= (0,0,0), mass=0, velocity=(0,0,0), charge=0):
        self.position = position
        self.mass = mass
        self.charge = charge
        self.velocity = velocity 

    def add_vels(self, velocity, others=[]):
        ''' turns velocity into momentum and runs a momentum sums for inelastic collisions.'''
        dummy = self.velocity * self.mass

        for vector in others:
            dummy += np.array(vector.velocity) * vector.mass

        #find velocity
        self.velocity = dummy / self.mass
        return self.velocity

    def move(self, dt): 
        ''' moves the point in space based on its velocity and time interval. '''
        self.position = tuple( np.array(self.position) + np.array(self.velocity) * dt)
        return self.position


class force: 
    def __init__(self, magnitude, direction=(0,0,0)):
        self.magnitude = magnitude
        self.direction = direction

    def apply(self, point, dt):
        ''' applies the force to a point, changing its velocity based on the force and time interval. '''
        acceleration = np.array(self.direction) * (self.magnitude / point.mass)
        point.velocity = tuple(np.array(point.velocity) + acceleration * dt)
        return point.velocity

    def sum(self, other= []): 
        ''' sums multiple forces together. '''
        total_magnitude = self.magnitude
        total_direction = np.array(self.direction) * self.magnitude

        for force in other:
            total_magnitude += force.magnitude
            total_direction += np.array(force.direction) * force.magnitude

        if total_magnitude != 0:
            total_direction /= total_magnitude 

        return force(total_magnitude, tuple(total_direction))
    

class line: 
    def __init__(self, start_point, end_point, mass=0, velocity=(0,0,0)):
        self.start_point = start_point
        self.end_point = end_point
        self.length = np.linalg.norm(np.array(end_point) - np.array(start_point))
        self.mass = mass
        self.density = mass / self.length if self.length > 0 else 0 
        self.velocity = velocity



class field: 
    ''''
    creates an origin point and defines how values vary in respect to it
    depends on the way that qt6 creates an image, as this will be the center piece of uig  
    '''
    def __init__(self, field_type, dimensions=3, size=10):
        self.field_type = field_type
        self.dimensions = dimensions
        self.size = size
        self.field = np.zeros((size, size, size))

class Space: 
    '''
    Space class creates an origin point and defines how many dimensions are in it. 
    '''
    def __init__(self, dimensions=3, size = 10):
        self.dimensions = dimensions
        self.size = size
        self.objects = []
        #self.e_field = np.zeros((size, size, size))
        #self.potential_field = np.zeros((size, size, size))
        #self.gravity_field = np.zeros((size, size, size))
        #self.update_field() =



if __name__ == "__main__":
    print( np.array((1, 1, 3))  + np.array((1, 1, 3)) )