# room_states.py

import sys
sys.path.insert(1, '../')

from state import State

# Start of room states

'''
The state which indicated that a room is occupied
'''
class OccupiedState(State):
    '''
    Fuction to return state based on input event
    '''
    def on_event(self, event, count):
        if event == 'exit':
            count -= 1
            if count > 0:
                return OccupiedState(), count
            else:
                return UnoccupiedState(), count

        elif event == 'entry':
            return OccupiedState(), count + 1
        
        return self

'''
The state which indicates that a room is unoccupied
'''
class UnoccupiedState(State):
    '''
    Fuction to return state based on input event
    '''
    def on_event(self, event, count):
        if event == 'entry':
            return OccupiedState(), count + 1 
        
        return self
