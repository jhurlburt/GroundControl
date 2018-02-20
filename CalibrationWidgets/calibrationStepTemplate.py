'''

A template for creating a new calibration step widget

'''
from   kivy.uix.gridlayout							import   GridLayout
from   kivy.properties								import   ObjectProperty

class CalibrationStepTemplate(GridLayout):
    done   = ObjectProperty(None)
    
    
    def onEnter(self):
		'''
		
		This function runs when the step is entered
		
		'''
	
	def onExit(self):
		'''
		
		This function run when the step is completed
		
		'''