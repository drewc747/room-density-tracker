# laser_out_states.py

import sys
sys.path.insert(1, '../')

from state import State

# Start of laser out states

'''
The state which indicated that a laser package is in dual laser mode
'''
class DualOutState(State):
    '''
    Fuction to return state based on input event
    '''
    def on_event(self, event):
        if event == 'powerDown':
            return SingleOutState()
        
        return self

'''
The state which indicated that a laser package is in single laser mode
'''
class SingleOutState(State):
    '''
    Fuction to return state based on input event
    '''
    def on_event(self, event):
        if event == 'powerUp':
            return DualOutState()
            
        return self
