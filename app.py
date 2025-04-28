from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive_centric_data', methods=['POST'])
def receive_data():
    data = request.json  # Assuming Centrica sends data as JSON
    print("Received Data:", data)  # Log the data for testing
    return jsonify({"status": "success", "message": "Data received successfully"}), 200

if __name__ == '__main__':
    print("Starting the Flask app...")  # Add a print statement here
    app.run(debug=True, host="0.0.0.0", port=5000)  # Use 0.0.0.0 to allow external access if needed

