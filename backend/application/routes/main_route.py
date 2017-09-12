from application import app
# ==============================================================================================
# FUNCTION TO SHUTDOWN SERVER
# ==============================================================================================
from flask import request

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['GET', 'POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

# ===============================================================================================================
# HOMEPAGE
# ===============================================================================================================
#@app.route('/')
#def index():
#    return app.send_static_file('index.html')

@app.route('/')
def index():
    return 'Hello World'
