# Guizero documentation https://lawsie.github.io/guizero/

from guizero import App
from guizero import Combo
from guizero import Text
from guizero import CheckBox
from guizero import ButtonGroup 
from guizero import PushButton
from guizero import info

def do_booking():
    info('Booking', 'Thank you For Booking')
    print(film_choice.value)
    print(vip_seat.value)
    print(row_choice.value)

app = App(title='My second app', width=300,
height= 200, layout='grid')



film_choice = Combo(app, options=['Star war', 'Froze', 'Lion King'], grid=[1,0], align='left')

film_description = Text(app, text='Which Film', grid=[0,0], align='left')

vip_seat = CheckBox(app, text='VIP seat?', grid=[1,1], align='left')

seat_type =  Text (app, text='Seat Type', grid=[0,1], align='left')


row_choice = ButtonGroup(app, options = [['Front', 'F'], ['Middle', 'M'], ['Back', 'B']],  #for example if you choose Front, F will be saved in row_choice.value
grid=[1,2], align='left', selected='M', horizontal=True)

Text(app, text='Seat location', grid=[0,2], align='left')
book_seats = PushButton(app, command=do_booking, text='Book Now', grid=[1,3], align='left')



app.display()
