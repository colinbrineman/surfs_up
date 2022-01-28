# import dependency
from flask import Flask

# create new app instance
app = Flask(__name__)

# create route
@app.route('/')
def hello_world():
    return 'Hello world'

# set host and port
if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)