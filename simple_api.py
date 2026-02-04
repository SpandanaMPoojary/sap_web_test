# simple_api.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/sales')
def get_sales():
    return jsonify({
        "d": {
            "results": [
                {"id": "SO001", "customer": "ABC Corp", "amount": 1000},
                {"id": "SO002", "customer": "XYZ Ltd", "amount": 2000}
            ]
        }
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)