# laser_states.py

import sys
sys.path.insert(1, '../')

from state import State

# Start of laser states

'''
The state which indicated that a laser package is in dual laser mode
'''
class DualState(State):
    '''
    Fuction to return state based on input event
    '''
    def on_event(self, event):
        if event == 'single':
            return SingleState()
        
        return self

'''
The state which indicated that a laser package is in single laser mode
'''
class SingleState(State):
    '''
    Fuction to return state based on input event
    '''
    def on_event(self, event):
        if event == 'off':
            return OffState()
        elif event == 'dual':
            return DualState()
            
        return self

'''
The state which indicates that a laser package is off
'''
class OffState(State):
    '''
    Fuction to return state based on input event
    '''
    def on_event(self, event):
        if event == 'single':
            return SingleState()
        
        return self
