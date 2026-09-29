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
class Space: 
    '''
    A 
    '''
    def __init__(self, dimensions=3, size = 10):
        self.dimensions = dimensions
        self.size = size
        self.objects = []
        #self.e_field = np.zeros((size, size, size))
        #self.potential_field = np.zeros((size, size, size))
        #self.gravity_field = np.zeros((size, size, size))
        #self.update_field() =


class point: 
    def __init__(self, position, mass=0, charge=0, momentum=0):
        self.position = position
        self.mass = mass
        self.charge = charge
        self.momentum = momentum 

