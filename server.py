import pyenttec as pyenttec
import time
dmx = pyenttec.select_port()

red_value = int(raw_input('red: '))
green_value = int(raw_input('green: '))
blue_value = int(raw_input('blue: '))

dmx.dmx_frame[144] = red_value
dmx.dmx_frame[145] = green_value
dmx.dmx_frame[146] = blue_value

dmx.render()

time.sleep(0.1)
