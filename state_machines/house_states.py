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
    def on_event(self, event, count):
        if event == 'exit':
            count -= 1
            if count > 1:
                return MultiOccupiedState(), count
            else:
                return SingleOccupiedState(), count
        elif event == 'entry':
            return MultiOccupiedState(), count + 1
        
        return self

'''
The state which indicated that a house is occupied by 1 person
'''
class SingleOccupiedState(State):
    '''
    Fuction to return state based on input event
    '''
    def on_event(self, event, count):
        if event == 'exit':
            return UnoccupiedState(), count - 1
        elif event == 'entry':
            return MultiOccupiedState(), count + 1
            
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
            return SingleOccupiedState(), count + 1
        
        return self
