from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def handle_data():
    data = request.json  # Assuming the incoming data is in JSON format
    print(f"Data received: {data}")
    return "Data processed", 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # Ensure the server listens on all interfaces
