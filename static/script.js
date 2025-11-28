function sendTest() {
    const data = {
        "start_ts": 1764344393,
        "heart": {
            "bpm": 0,
            "rr_ms": 0,
            "ecg_data": [0,0,0,0,0,0]
        },
        "chest_movement": {
            "ax": [0.03, 0.05],
            "ay": [-0.2, -0.3],
            "az": [12.3, 12.4],
            "gx": [0.01],
            "gy": [-0.03],
            "gz": [-0.03]
        }
    };

    fetch("/api/data", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(out => {
        document.getElementById("output").textContent = JSON.stringify(out, null, 4);
    });
}