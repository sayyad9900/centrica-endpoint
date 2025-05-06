app = Flask(__name__)
 
stored_data = []
 
 
@app.route("/")
def index():
    return "Server is up and running", 200
 
@app.route("/data", methods=["POST", "GET"])
def handle_data():
    if request.method == "POST":
        data = request.json
        print(f"Data received: {data}")
        if data:
            stored_data.append(data)
        return "Data received", 200
    else:
        if stored_data:
            return jsonify(stored_data[-1])
        else:
            return jsonify({"message": "No data available yet. Send data via POST request first."}), 404
 
if __name__ == "__main__":
    import os
 
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
