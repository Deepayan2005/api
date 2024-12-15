from flask import Flask,request
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

@app.route('/')
def func():
    name = str(request.args.get("name"))
    with ThreadPoolExecutor(max_workers=1000) as p:
        p.map(func)
        return f"Hello {name}, Your api is working....."
