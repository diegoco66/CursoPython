
class Lamp:
    _LAMPS = ['''
            |   
         \ .-. /        
       -- (   ) --
           \ /
          _|=|_
         |_____|  
    ''', '''

           .-. 
          (   )
           \ /
          _|=|_
         |_____|  
    ''']

    def __init__(self, state):
        self._is_turned_on = state

    def turn_on(self):
        self._is_turned_on = True
        self._display_image()

    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])
