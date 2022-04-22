from flask import Flask
from flask import request
from flask import render_template
import tracker
import location

ipapi = Flask(__name__)

@ipapi.route("/", methods = ['GET','POST'])
def main():
    if request.method == 'GET':
        return render_template("index.html")
    
    search = request.form.get('ipaddress')
    result = tracker.ipaddressinfo(ip = search)
    location_result = location.ipaddressloc(ip = search)
    return render_template("result.html",result=result,location_result=location_result)

if __name__ == "__main__":
    ipapi.run(host="0.0.0.0", port=5050)
