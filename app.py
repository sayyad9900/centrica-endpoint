from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive-data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("Data received:", data)
    return jsonify({"message": "Data received successfully"}), 200

if __name__ == '__main__':
    app.run()
