from flask import Flask, request
import json
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def start():
    js = json.loads(request.data.decode('utf-8'))
    print(js)
    loc = "/Users/lee/Downloads/{}".format(js['link']) # put location here
    print(loc)
    try:
        os.system("python3 pose/src/run_video.py --model=mobilenet_thin --resolution=432x368 --video={}".format(loc))
    except:
        pass

if __name__ == "__main__":
    app.run(debug=True)