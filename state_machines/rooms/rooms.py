# rooms.py

from room_states import OccupiedState, UnoccupiedState

''' A state machine for bathroom 1 '''
class Bt1(object):
    ''' Method to initilize the room '''
    def __init__(self):
        self.name = 'bt1'
        self.state = UnoccupiedState()
        self.count = 0

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state, self.count = self.state.on_event(event, self.count)
        
        
''' A state machine for bathroom 2 '''
class Bt2(object):
    ''' Method to initilize the room '''
    def __init__(self):
        self.name = 'bt2'
        self.state = UnoccupiedState()
        self.count = 0
        
    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state, self.count = self.state.on_event(event, self.count)
       

''' A state machine for bedroom1 '''
class Bd1(object):
    ''' Method to initilize the room '''
    def __init__(self):
        self.name = 'bd1'
        self.state = UnoccupiedState()
        self.count = 0
        
    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state, self.count = self.state.on_event(event, self.count)
        
        
''' A state machine for bedroom2 '''
class Bd2(object):
    ''' Method to initilize the room '''
    def __init__(self):
        self.name = 'bd2'
        self.state = UnoccupiedState()
        self.count = 0
        
    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state, self.count = self.state.on_event(event, self.count)
        
        
''' A state machine for the hallway '''
class Hal(object):
    ''' Method to initilize the room '''
    def __init__(self):
        self.name = 'hal'
        self.state = UnoccupiedState()
        self.count = 0
        
    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state, self.count = self.state.on_event(event, self.count)
        
        
''' A state machine for the kitchen '''
class Kit(object):
    ''' Method to initilize the room '''
    def __init__(self):
        self.name = 'kit'
        self.state = UnoccupiedState()
        self.count = 0
        
    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state, self.count = self.state.on_event(event, self.count)
 
        
''' A state machine for the living room '''
class Liv(object):
    ''' Method to initilize the room '''
    def __init__(self):
        self.name = 'liv'
        self.state = OccupiedState()
        self.count = 1
    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state, self.count = self.state.on_event(event, self.count)
        
''' A state machine for the utility room '''
class Utl(object):
    ''' Method to initilize the room '''
    def __init__(self):
        self.name = 'utl'
        self.state = UnoccupiedState()
        self.count = 0
        
    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state, self.count = self.state.on_event(event, self.count)      
