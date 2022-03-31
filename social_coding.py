from flask import Flask
from flask import request
from flask import render_template
import tracker

ipapi = Flask(__name__)

@ipapi.route("/", methods = ['GET','POST'])
def main():
    if request.method == 'GET':
        return render_template("index.html")
    
    search = request.form.get('ipaddress')
    result = tracker.ipaddressinfo(ip = search)
    return render_template("result.html",result=result)

if __name__ == "__main__":
    ipapi.run(host="0.0.0.0", port=8080)
