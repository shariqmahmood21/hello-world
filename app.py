from flask import Flask
from flask import request
from datetime import datetime


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def hello_world():
    # Requirement : If the request header :  "Accept header" equals "application/json" , return JSON response
    if request.method == 'GET' and request.headers.get('X-accept-header') == "application/json":
        # Requirement: If Debug enabled, log timestamp and request URL"
        app.logger.debug(str(datetime.now()) + "\t" + request.url )
        return '{"message": "Hello, World"}'
    # Requirement : If the request header : "Accept header" NOT equals "application/json" , return string
    app.logger.debug(str(datetime.now()) + "\t" + request.url)
    return '<p>Hello, World</p>'

if __name__ == '__main__':
    app.run()

