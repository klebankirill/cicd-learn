from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
PrometheusMetrics(app)

@app.route("/")
def hello():
	return "Hello, CI/CD with monitiring!"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)

