from flask import Flask, render_template, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/')
def home():
    logging.info("Home page accessed")
    return render_template('index.html')

@app.route('/api/status')
def status():
    logging.info("API status checked")
    return jsonify({"status": "success", "message": "Corporate-ready Flask app running!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
