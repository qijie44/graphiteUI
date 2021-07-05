from flask import Flask, render_template, jsonify, request
# import RPI.GPIO as GPIO

app = Flask(__name__)
# GPIO.setmode(GPIO.BCM)

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)