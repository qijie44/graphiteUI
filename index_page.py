from flask import Flask, render_template, jsonify, request
import time

app = Flask(__name__)
app.config["run"] = True
app.config["progress"] = 0

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route('/_command')
def command():
    sent_command = request.args.get('command')
    print(f"{sent_command} was pressed!")
    if sent_command == "Pause":
        app.config["run"] = False
        time.sleep(600)
    elif sent_command == "Run":
        app.config["run"] = True
    return jsonify(command=sent_command)

@app.route('/_tape-exfoliation')
def tape_exfoliation():
    print(f"Exfoliate Tape {request.args.get('times')} times")
    app.config["tape_exfoliate"] = request.args.get('times')
    return "200"

@app.route('/_substrate-exfoliation')
def substrate_exfoliation():
    print(f"Exfoliate Substrate {request.args.get('times')} times")
    app.config["substrate_exfoliate"] = request.args.get('times')
    return "200"

@app.route('/_substrate-no')
def set_substrate_no():
    print(f"Substrate no {request.args.get('value')} selected")
    app.config["substrate_no"] = request.args.get('value')
    return "200"

@app.route('/_movement-speed')
def set_movement_speed():
    print(f"Movement Speed set to {request.args.get('value')}")
    app.config["movement_speed"] = request.args.get('value')
    return "200"
    
@app.route('/_progress')
def get_progress():
    return jsonify(value=app.config["progress"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)