from flask import Flask, request, jsonify
from functools import wraps
from markupsafe import escape
import pandas as pd

app = Flask(__name__)

# Track Time Decorator
def track_time_spent(name):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            import time
            start_time = time.time()

            ret_val = f(*args, **kwargs)
            print("--- %s seconds ---" % (time.time() - start_time))
            return ret_val
        return wrapped
    return decorator

@app.route("/")
@track_time_spent('hello_world')
# curl localhost
def hello():
    return "Hello, World!"

@app.route("/<name>")
@track_time_spent('hello_name')
# curl localhost/eric
def hello_name(name):
    return f"Hello, {escape(name)}!"

@app.route("/random/post", methods=['POST'])
@track_time_spent('test_post')
# curl localhost:8080/random/post -d '{"name": "Anthony", "location": "Japan", "randomlist": ["one", "random", "two"]}' --header "Content-Type: application/json"
def test_post():
    try:
        if request.method == 'POST':
            # return f"data:{request.form}"

            data = request.get_json()
            name = data['name']
            location = data['location']
            randomlist = data['randomlist']
            print(type(name))
            print(type(randomlist))


            return jsonify({
                'result': 'Success!',
                'name': name,
                'location': location,
                'randomkeyinlist': randomlist
            })
    except Exception as e:
        return f"Error: {e}"