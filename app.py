from flask import Flask, request
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return "Server is up and running", 200
 
@app.route('/data', methods=['POST'])
def handle_data():
    data = request.json
    print(f"Data received: {data}")
    return "Data received", 200
 
if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
