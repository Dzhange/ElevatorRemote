from flask import Flask
from flask import request
import numpy as np
import cv2

app = Flask(__name__)

@app.route('/uploader', methods = ['POST'])
def uploader():

    if request.method == 'POST':
        filestr = request.files['file'].read()
        npimg = np.fromstring(filestr, np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        cv2.imwrite("./test_received.jpg",img)
        out = {"xy":(1,2)}
    
    return out


if __name__ == "__main__":
    app.run()