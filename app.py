from flask import Flask
from flask import request
from datetime import datetime


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method == 'GET' and request.headers.get('X-accept-header') == "application/json":
        app.logger.debug(str(datetime.now()) + "\t" + request.url )
        return {"message": "Hello, World"}
    app.logger.debug(str(datetime.now()) + "\t" + request.url)
    return '<p>Hello, World</p>'


if __name__ == '__main__':
    app.run()
