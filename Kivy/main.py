from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.scatter import Scatter 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout


class TareaKivyApp(App):
  def build(self):
    boxlayout = BoxLayout()

    def mensaje(instance,value):
      print('¡Excelente, pasaste el semestre')

    def callback(instance, value):
      print('Estado del switch', instance, ': ', value)

    slide = Slider(orientation='vertical',min=-10, max=10, value=5,value_track=True,value_track_color=(1,1,0,1))

    button = Button(text='¡Pasa el semestre!',
    background_color=(1,1,41,50))
    button.bind(state=mensaje)

    switch = Switch(active=True)
    switch.bind(active=callback)

    boxlayout.add_widget(slide)
    boxlayout.add_widget(button)
    boxlayout.add_widget(switch)
    
    return boxlayout

  

if __name__ == "__main__":
  TareaKivyApp().run()