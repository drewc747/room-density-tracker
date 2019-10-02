# laser_states.py

import sys
sys.path.insert(1, '../')

from state import State

# Start of laser states

'''
The state which indicated that a device is on
'''
class OnState(State):
    '''
    Fuction to return state based on input event
    '''
    def on_event(self, event):
        if event == 'off':
            return OffState()
        
        return self

'''
The state which indicates that a device is off
'''
class OffState(State):
    '''
    Fuction to return state based on input event
    '''
    def on_event(self, event):
        if event == 'On':
            return OnState()
        
        return self
