# rooms.py

from room_states import OccupiedState, UnoccupiedState

''' A state machine for bathroom 1 '''
class Bat1(object):
    ''' Method to initilize the room '''
    def __init__(self):
        self.state = UnoccupiedState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)
        
        
''' A state machine for bathroom 2 '''
class Bat2(object):
    ''' Method to initilize the room '''
    def __init__(self):
        self.state = UnoccupiedState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)
        

''' A state machine for bedroom1 '''
class Bed1(object):
    ''' Method to initilize the room '''
    def __init__(self):
        self.state = UnoccupiedState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)
        
        
''' A state machine for bedroom2 '''
class Bed2(object):
    ''' Method to initilize the room '''
    def __init__(self):
        self.state = UnoccupiedState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)
        
        
''' A state machine for the hallway '''
class Hal(object):
    ''' Method to initilize the room '''
    def __init__(self):
        self.state = UnoccupiedState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)
        
        
''' A state machine for the kitchen '''
class Kit(object):
    ''' Method to initilize the room '''
    def __init__(self):
        self.state = UnoccupiedState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)
 
        
''' A state machine for the living room '''
class Liv(object):
    ''' Method to initilize the room '''
    def __init__(self):
        self.state = OccupiedState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)
        
''' A state machine for the utility room '''
class Utl(object):
    ''' Method to initilize the room '''
    def __init__(self):
        self.state = UnoccupiedState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)        
