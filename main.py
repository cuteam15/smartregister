from kivy.lang import Builder
from kivymd.app import MDApp
import FakeRPi.GPIO as GPIO
from kivy.uix.button import Button 
 

#Disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 23 as output
beepPin=17 
GPIO.setup(beepPin,GPIO.OUT)


def buzzer_off(dt):
    GPIO.output(beepPin,GPIO.Low)


class POSApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "DeepPurple"
		return Builder.load_file('POS.kv')
	
	
POSApp().run()


