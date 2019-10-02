# house.py

from house_states import MultiOccupiedState, SingleOccupiedState, UnoccupiedState

''' A state machine for the house '''
class House(object):
    ''' Method to initilize the house '''
    def __init__(self):
        self.name = 'house'
        self.state = SingleOccupiedState()
        self.count = 1
        
    '''
    Method to handle events
        Parameters:
            event: Event passed from HUB
    '''
    def on_event(self, event):
        self.state, self.count = self.state.on_event(event, self.count)
              
