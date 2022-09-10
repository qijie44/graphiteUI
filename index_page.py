from flask import Flask, render_template, jsonify, request
import time
# import RPI.GPIO as GPIO

app = Flask(__name__)
# GPIO.setmode(GPIO.BCM)
app.config["run"] = True

#don't forget to set GPIO as input/output
# e.g. GPIO.setup(1, GPIO.OUT)

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route('/_command')
def command():
    # your code here
    print(request.args.get('command') + " was pressed!")
    return jsonify(command=request.args.get('command'))

@app.route("/Pause")
def pause():
    app.config["run"] = False
    time.sleep(600)
    return render_template("index.html")

@app.route("/Run")
def run():
    print(app.config["run"])
    app.config["run"] = True
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)