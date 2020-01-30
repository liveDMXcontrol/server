import sys
from flask import abort, Flask, render_template, request, Response
from flask_cors import CORS
sys.path.insert(0, 'pyenttec/')
import pyenttec

app = Flask(__name__)
if __name__ == '__main__':
    app.run(host="0.0.0.0")
CORS(app)
dmx = pyenttec.select_port()

# {
#   "channels_list": [
#     {"channel": 50, "value": 255},
#     {"channel": 51, "value": 0},
#     {"channel": 52, "value": 0}
#   ]
# }

@app.route('/', methods=['POST'])
def jsonHandler():
    try:
        contents = request.get_json()['channels_list']
        print(contents)
        for content in contents:
            # print(content['channel'],': ',content['value'])
            dmx.dmx_frame[content['channel']] = content['value']

        dmx.render()
        return Response(status=204, mimetype='application/json')
    except TypeError:
        print('TypeError')
        abort(400)
    except:
        print('other error')
