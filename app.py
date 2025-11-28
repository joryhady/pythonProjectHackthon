from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def analyze_data(data):
    heart = data.get("heart", {})
    chest = data.get("chest_movement", {})

    # the values
    bpm = heart.get("bpm", 0)
    rr_ms = heart.get("rr_ms", 0)
    ecg_data = heart.get("ecg_data", [])

    ax = chest.get("ax", [])
    ay = chest.get("ay", [])
    az = chest.get("az", [])

    # analyze
    chest_amplitude = max(az) - min(az) if len(az) > 0 else 0

    # the heart status
    heart_status = "NO ECG SIGNAL" if all(v == 0 for v in ecg_data) else "ACTIVE"

    return {
        "bpm": bpm,
        "rr_ms": rr_ms,
        "heart_status": heart_status,
        "chest_amplitude": chest_amplitude,
        "samples": len(az)
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/data", methods=["POST"])
def receive_data():
    data = request.json
    result = analyze_data(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)