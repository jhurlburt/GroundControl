'''

A template for creating a new calibration step widget

'''
from   kivy.uix.gridlayout							import   GridLayout
from   kivy.properties								import   ObjectProperty

class DistBetweenChainBrackets(GridLayout):
    done   = ObjectProperty(None)
    
    
    