FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY web_app.py .

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["web_app.py"]
