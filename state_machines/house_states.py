# house_states.py

from state import State

# Start of house states

'''
The state which indicated that a house is occupied by 2+ people
'''
class MultiOccupiedState(State):
    '''
    Fuction to return state based on input event
    '''
    def on_event(self, event):
        if event == 'exit':
            return SingleOccupiedState()
        
        return self

'''
The state which indicated that a house is occupied by 1 person
'''
class SingleOccupiedState(State):
    '''
    Fuction to return state based on input event
    '''
    def on_event(self, event):
        if event == 'exit':
            return UnoccupiedState()
        elif event == 'entry':
            return MultiOccupiedState()
            
        return self

'''
The state which indicates that a room is unoccupied
'''
class UnoccupiedState(State):
    '''
    Fuction to return state based on input event
    '''
    def on_event(self, event):
        if event == 'entry':
            return SingleOccupiedState()
        
        return self
