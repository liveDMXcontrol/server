import pyenttec as pyenttec

dmx = pyenttec.select_port()


def make_4bar_red():
    dmx.dmx_frame[64] = 255
    dmx.dmx_frame[67] = 255
    dmx.dmx_frame[70] = 255
    dmx.dmx_frame[73] = 255

    dmx.render()


make_4bar_red()
