FROM python:3.11-slim
WORKDIR /app
COPY ../src/app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ../src/app/ .
EXPOSE 5000
CMD ["python", "app.py"]
