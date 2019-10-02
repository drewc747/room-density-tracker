# lasers.py

from laser_states import OffState, SingleState, DualState
from laser_out_states import SingleOutState, DualOutState

''' A state machine for the laser package between bathroom1 and the hallway '''
class Bat1Hal(object):
    ''' Method to initilize the laser package '''
    def __init__(self):
        self.state = OffState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)

''' A state machine for the laser package between bathroom2 and bedroom2 '''
class Bat2Bed2(object):
    ''' Method to initilize the laser package '''
    def __init__(self):
        self.state = OffState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)

''' A state machine for the laser package between bedroom1 and bedroom2 '''
class Bed1Bed2(object):
    ''' Method to initilize the laser package '''
    def __init__(self):
        self.state = OffState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)

''' A state machine for the laser package between bedroom1 and the hallway '''
class Bed1Hal(object):
    ''' Method to initilize the laser package '''
    def __init__(self):
        self.state = OffState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)

''' A state machine for the laser package between bedroom1 and outside '''
class Bed1Out(object):
    ''' Method to initilize the laser package '''
    def __init__(self):
        self.state = SingleOutState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)

''' A state machine for the laser package between bedroom2 and the hallway '''
class Bed2Hal(object):
    ''' Method to initilize the laser package '''
    def __init__(self):
        self.state = OffState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)

''' A state machine for the laser package between the hallway and living room '''
class HalLiv(object):
    ''' Method to initilize the laser package '''
    def __init__(self):
        self.state = SingleState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)

''' A state machine for the laser package between the hallway and utility room '''
class HalUtl(object):
    ''' Method to initilize the laser package '''
    def __init__(self):
        self.state = OffState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)

''' A state machine for the laser package between the kitchen and living room '''
class KitLiv(object):
    ''' Method to initilize the laser package '''
    def __init__(self):
        self.state = SingleState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)

''' A state machine for the laser package between the kitchen and utility room '''
class KitUtl(object):
    ''' Method to initilize the laser package '''
    def __init__(self):
        self.state = OffState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)


''' A state machine for front door laser package (between outside and living room) '''
class LivOut(object):
    ''' Method to initilize the laser package '''
    def __init__(self):
        self.state = DualOutState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)

''' A state machine for the laser package between outside and the utility room '''
class OutUtl(object):
    ''' Method to initilize the laser package '''
    def __init__(self):
        self.state = SingleOutState()

    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state = self.state.on_event(event)


