import tingbot
from tingbot import *
import time

def loop():
    current_date = time.strftime("%d %B %Y")
    current_time = time.strftime("%H:%M:%S")
    
    screen.fill(
        color='black'
    )
    screen.text(
        current_time, 
        xy=(160, 110),
        color='white',
        font_size=50,
    )
    screen.text(
        current_date,
        xy=(160, 180),
        color='white',
        font_size=24,
    )

tingbot.run(loop)
