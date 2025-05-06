from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Server is up and running", 200

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'GET':
        return jsonify({
            "message": "Send a POST request with JSON data to this endpoint."
        }), 200

    # Log request headers and raw data
    print(f"Request headers: {request.headers}")
    print(f"Raw request data: {request.data}")

    try:
        data = request.get_json(force=True)
    except Exception as e:
        print(f"JSON decode error: {e}")
        return jsonify({
            "error": "Request must contain valid JSON data"
        }), 400

    # Validate presence of 'measurements'
    if 'measurements' not in data or not isinstance(data['measurements'], list):
        return jsonify({"error": "Missing or invalid 'measurements' list in payload"}), 400

    processed = []
    for i, m in enumerate(data['measurements']):
        try:
            processed_entry = {
                "site_name": m["site_name"],
                "energy": m["energy(Wh)"],
                "current": m["current(A)"],
                "voltage": m["voltage(V)"],
                "power": m["power(W)"]
            }
            processed.append(processed_entry)
        except KeyError as e:
            print(f"Validation error in measurement {i}: missing {e}")
            return jsonify({"error": f"Missing expected field in measurement {i}: {e}"}), 400
        except Exception as e:
            print(f"Unexpected error in measurement {i}: {e}")
            return jsonify({"error": f"Error processing measurement {i}: {e}"}), 400

    # Log processed data
    print(f"Processed data: {processed}")

    return jsonify({"message": "Measurements received", "data": processed}), 200

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

