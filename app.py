from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Server is up and running", 200

@app.route('/data', methods=['POST'])
def handle_data():
    # Check if the request contains JSON data
    if not request.is_json:
        return jsonify({"error": "Request must contain JSON data"}), 400

    data = request.json

    # Define required fields and their expected types
    required_fields = {
        "timestamp": str,
        "energy": (int, float),
        "current": (int, float),
        "voltage": (int, float),
        "power": (int, float)
    }

    # Validate the presence and type of required fields
    for field, expected_type in required_fields.items():
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400
        if not isinstance(data[field], expected_type):
            return jsonify({"error": f"Field '{field}' must be of type {expected_type.__name__}"}), 400

    # Log the received data
    print(f"Data received: {data}")

    # Return success response
    return jsonify({"message": "Data received", "data": data}), 200

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
