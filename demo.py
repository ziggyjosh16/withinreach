import os
import kivy
import random
kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.garden.mapview import MapView, MapMarker
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Color, Rectangle, Line
#all options
class optionsLayout(BoxLayout):
	def __init__(self, **kwargs):
		super(optionsLayout, self).__init__(**kwargs)
		self.size_hint = (0.3 , 1)
		self.spacing = 15
		self.orientation = 'vertical'

		#label
		self.add_widget(Label(text = '[b]Parameters:[/b]', font_size = 20 ,  font_name = 'gothic',  markup = True))
		#options
		self.add_widget(option('Sex', sexToggle()))
		self.add_widget(option('Age', dropdownSelection(['0 - 5', '6 - 15', '16 - 25', '25 - 40', '41 - 65', '66+'])))
		self.add_widget(option('Social Media', yesOrNoBox('1')))
		self.add_widget(option('Last Seen (Hours)', dropdownSelection(['<1', '1-2', '2-3', '4-12', '12-24', '>24'])))
		self.add_widget(option('Mental State', dropdownSelection(['Autism', 'Dementia', 'Depression', 'Disability', 'Drug Abuse', 'Mental Illness'])))
		self.add_widget(option('Abducted', yesOrNoBox('2')))
		self.add_widget(option('Vehicle', yesOrNoBox('3')))
		self.add_widget(option('Outdoor Activity', dropdownSelection(['Fishing', 'Camping', 'Hiking', 'Working', 'Climbing', 'Snowboarding', 'Hunting' ])))
		self.add_widget(option('Temperature (F)', dropdownSelection(['<0','1-20','21-32','33-45','46-65','66-75','76-85','86-95', '96+' ])))
		self.add_widget(option('Weather', dropdownSelection(['Clear','Cloudy','Partly Cloudy','Rainy','Thunderstorm','Tornado','Hail','Sleet','Fog','Mist'])))
		self.submitbtn = Button(text = "LOCATE")
		self.add_widget(self.submitbtn)
		#image
		self.add_widget(Image(allow_stretch = True, source='logo.png', size_hint = (1, 1)))
		self.add_widget(Label(text = "[sub][i]Created by: Joshua Sharkey[/i][/sub]", markup=True ))
#for simplification of options
class option(BoxLayout):
	def __init__(self, labeltext, widget):
		super(option, self).__init__()
		self.orientation = 'horizontal'
		self.spacing = 10
		self.add_widget(Label(font_name= 'gothic', text = labeltext))
		self.add_widget(widget)

#gridlayout for yes or no selections
class yesOrNoBox(GridLayout):
	def __init__(self, groupt):
		super(yesOrNoBox, self).__init__()
		self.cols = 2
		self.rows = 2
		self.add_widget(Label(text ="Y"))
		self.add_widget(Label(text ="N"))
		self.add_widget(CheckBox(group = groupt))
		self.add_widget(CheckBox(group = groupt))

#togglesex
class sexToggle(BoxLayout):

	def __init__(self, **kwargs):
		super(sexToggle, self).__init__(**kwargs)
		self.orientation = 'horizontal'
		#self.size_Hint = (None, None)
		male = ToggleButton(text = 'Male', group = 'sex', state = 'normal')
		female = ToggleButton(text = 'Female', group = 'sex', state = 'down')
		self.add_widget(male)
		self.add_widget(female)
#map
class Map(MapView):
	def __init__(self, ilat = 43.0342389 , ilon = -87.9130591, update = False):	
		super(Map, self).__init__()
		self.size_hint = (0.7 , 1)
		self.zoom=15
		self.lat= 43.0399016
		self.lon= -88.4013728
		#randomize
		if update is True:
			self.add_coordinates()
			
	#takes current lat and lon and does a proximity based coordinate dump
	def add_coordinates(self):
		newlat = self.lat
		newlon = self.lon
		for i in range(5):
			newlat = self.lat+(random.uniform(-100,100)*.0001)
			newlon = self.lon+(random.uniform(-100,100)*.0001)
			self.add_marker(MapMarker(lat = newlat ,lon = newlon))
		

#dropdown menu
class dropdownSelection(Button):
	def __init__(self, opts = []):
		super(dropdownSelection, self).__init__()
		self.text = 'select'
		self.dropdown = DropDown()
		for option in opts:
			#consider resizing
			btn = Button(text = option, size_hint=(None, None), size=(100,30), shorten = True)
			btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
			self.dropdown.add_widget(btn)

		self.bind(on_release=self.dropdown.open)
		self.dropdown.bind(on_select=lambda instance, x: setattr(self, 'text', x))

class MainScreen(GridLayout):

	def __init__(self, **kwargs):
		super(MainScreen, self).__init__(**kwargs)
		self.cols = 2
		self.padding = 10
		self.spacing = 20
		self.map = Map()
		self.options = optionsLayout()
		self.options.submitbtn.bind(on_press = lambda x: self.updateMap())
		self.add_widget(self.options)
		self.add_widget(self.map)

	def updateMap(self):
		self.remove_widget(self.map)
		self.map = Map(ilat = self.map.lat, ilon = self.map.lon, update = True)
		self.add_widget(self.map)

class MyApp(App):

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    MyApp().run()