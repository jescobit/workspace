'''
PARTICLE space.py 

creates a 3d space for a simulation and allows the creation of potentials
Can create an object in space and update the field. 

in it, it describes the potentials of all 4 forces, 
and by sectioning the scale,
    we can go from quantum, to fluid, to statics


workflow: 
    when called, create a Rn space, with potential values for em, strong, weak, 
    and gravitational forces in each. 

create class object, which has a position, mass, charge, and momentum
    when created it updates the field with its potential values.

### for now, make it a static universe, as in, nothing changes, but adding stuff changes things


'''

import numpy as np
import constants as k


class Space: 
    def __init__(self, dimensions=3, size=10, type = 'particle'):
        self.dimensions = dimensions
        self.size = size
        self.objects = []
        #self.e_field = np.zeros((size, size, size))
        #self.potential_field = np.zeros((size, size, size))
        #self.gravity_field = np.zeros((size, size, size))
        #self.update_field() = 

    def add_object(self, obj):
        self.objects.append(obj)
        self.update_field()





