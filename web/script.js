function sendData() {
    const deviceId = document.getElementById("deviceId").value;
    const message = document.getElementById("message").value;

    fetch("/send", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            device_id: deviceId,
            message: message
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").innerText =
            JSON.stringify(data, null, 2);
    })
    .catch(err => {
        document.getElementById("output").innerText =
            "Error sending data";
    });
}
