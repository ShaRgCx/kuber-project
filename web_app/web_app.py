from flask import Flask, jsonify
import datetime

app = Flask(__name__)

# Счетчик запросов к /time
time_requests_count = 0

@app.route("/time", methods=["GET"])
def get_time():
    """
    Обрабатывает GET-запрос к /time и возвращает текущее время.
    """
    global time_requests_count
    time_requests_count += 1

    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    return jsonify({"time": current_time})

@app.route("/statistics", methods=["GET"])
def get_statistics():
    """
    Обрабатывает GET-запрос к /statistics и возвращает количество запросов к /time.
    """
    global time_requests_count
    return jsonify({"requests_count": time_requests_count})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
