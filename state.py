# state.py

class State(object)
    def __init__(self):
        print(f'Processing current state: {str(self)}')
    
    '''
    Function to handle events delegated to state:
        Parameters:
            event: Event to be handled
    '''
    def on_event(self, event):
        pass
        
    '''
    Fuction to return description of state
        Returns:
            self.__str__(): Leverages __str__ method to describe the state
    '''
    def __repr__(self):
        return self.__str__()
    
    '''
    Functin to return the name of the state
        Returns:
            self.__class__.__name__: Name of the state
    '''
    def __str__(self):
        return self.__class__.__name__
