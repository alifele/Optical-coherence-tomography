from guizero import App
from guizero import Text
from guizero import TextBox
from guizero import PushButton
from guizero import Slider
from guizero import Picture 

def say_my_name():
    welcome_message.value  = my_name.value
    
def change_text_size(slider_value):
    welcome_message.size = slider_value

app = App(title='Hello World')
welcome_message = Text(app,
 text = 'hi there. Well come to my app',
 size = 15,
 font='Times New Roman',
 color='blue')

my_name = TextBox(app, width=25)

update_text = PushButton(app, command=say_my_name,
text = 'display my name')

text_size = Slider(app, command = change_text_size, start=10, end=80)

my_cat = Picture(app, image='MIT.gif')

app.display()
