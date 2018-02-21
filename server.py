import sys
sys.path.insert(0, 'pyenttec/')
import pyenttec
import time
from flask import Flask, render_template, Response

app = Flask(__name__)
dmx = pyenttec.select_port()

# sequence = [
#     {'red': 138, 'green': 104, 'blue': 185},
#     {'red': 255, 'green': 0, 'blue': 255},
#     {'red': 107, 'green': 109, 'blue': 179},
#     {'red': 0, 'green': 255, 'blue': 255}
# ]

# while True:
#     for frame in sequence:
#         dmx.dmx_frame[144] = frame['red']
#         dmx.dmx_frame[145] = frame['green']
#         dmx.dmx_frame[146] = frame['blue']

#         dmx.render()

#         time.sleep(0.5)

@app.route('/')
def index():
    return render_template('light.html')

def make_color(color):
    dmx.dmx_frame[144] = color['red']
    dmx.dmx_frame[145] = color['green']
    dmx.dmx_frame[146] = color['blue']

    dmx.render()


@app.route('/white')
def white():
    color = {'red': 255, 'green': 255, 'blue': 255}

    make_color(color)

    return render_template('light.html')


@app.route('/red')
def red():
    color = {'red': 255, 'green': 0, 'blue': 0}

    make_color(color)

    return render_template('light.html')

@app.route('/green')
def green():
    color = {'red': 0, 'green': 255, 'blue': 0}

    make_color(color)

    return render_template('light.html')

@app.route('/blue')
def blue():
    color = {'red': 0, 'green': 0, 'blue': 255}

    make_color(color)

    return render_template('light.html')

@app.route('/purple')
def purple():
    color = {'red': 255, 'green': 0, 'blue': 255}

    make_color(color)

    return render_template('light.html')


@app.route('/teal')
def teal():
    color = {'red': 0, 'green': 255, 'blue': 255}

    make_color(color)

    return render_template('light.html')

@app.route('/yellow')
def yellow():
    color = {'red': 255, 'green': 255, 'blue': 0}

    make_color(color)

    return render_template('light.html')

@app.route('/off')
def off():
    color = {'red': 0, 'green': 0, 'blue': 0}

    make_color(color)

    return render_template('light.html')


