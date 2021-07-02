from flask import Flask, render_template
import RPI.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

#don't forget to set GPIO as input/output
# e.g. GPIO.setup(1, GPIO.OUT)

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/Up")
def Up():
    # your code here
    print("up was pressed")
    return render_template("index.html")

@app.route("/Down")
def Down():
    # your code here
    print("down was pressed")
    return render_template("index.html")

@app.route("/Left")
def Left():
    # your code here
    print("left was pressed")
    return render_template("index.html")

@app.route("/Right")
def Right():
    # your code here
    print("right was pressed")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)