import sys
sys.path.insert(0, 'pyenttec/')
import pyenttec
import time

dmx = pyenttec.select_port()

red_value = int(input('red: '))
green_value = int(input('green: '))
blue_value = int(input('blue: '))

dmx.dmx_frame[144] = red_value
dmx.dmx_frame[145] = green_value
dmx.dmx_frame[146] = blue_value

dmx.render()

time.sleep(0.1)
