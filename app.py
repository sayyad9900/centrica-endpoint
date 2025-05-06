from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Server is up and running", 200

@app.route('/data', methods=['POST'])
def handle_data():
    # Log request headers and raw data for debugging
    print(f"Request headers: {request.headers}")
    print(f"Raw request data: {request.data}")

    # Check if the request contains JSON data
    if not request.is_json:
        try:
            # Attempt to parse raw data as JSON if Content-Type is missing
            if request.data:
                data = json.loads(request.data)
            else:
                return jsonify({
                    "error": "Request must contain JSON data",
                    "details": "No data received or Content-Type is not application/json"
                }), 400
        except json.JSONDecodeError:
            return jsonify({
                "error": "Request must contain valid JSON data",
                "details": "Invalid JSON format or missing Content-Type: application/json"
            }), 400
    else:
        data = request.json

    # Define required fields and their expected types
    required_fields = {
        "site_name": str,
        "energy": (int, float),
        "current": (int, float),
        "voltage": (int, float),
        "power": (int, float)
    }

    # Validate the presence and type of required fields
    for field, expected_type in required_fields.items():
        if field not in data:
            print(f"Validation error: Missing field {field}")
            return jsonify({"error": f"Missing required field: {field}"}), 400
        if not isinstance(data[field], expected_type):
            print(f"Validation error: Field {field} type mismatch, got {type(data[field])}, expected {expected_type}")
            return jsonify({"error": f"Field '{field}' must be of type {expected_type.__name__}"}), 400

    # Log the received data
    print(f"Data received: {data}")

    # Return success response
    return jsonify({"message": "Data received", "data": data}), 200

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
