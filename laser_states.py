# laser_states.py

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
        if event == 'powerDown':
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
        if event == 'powerDown':
            return OffState()
        elif event == 'powerUp':
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
        if event == 'powerUp':
            return SingleState()
        
        return self
