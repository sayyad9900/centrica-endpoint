from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Centrica Flask App!'

@app.route('/receive_centric_data', methods=['POST'])
def receive_data():
    data = request.json
    print("Received Data:", data)
    return jsonify({"status": "success", "message": "Data received successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
