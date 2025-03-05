FROM python:3.9-slim
WORKDIR /app
COPY receiver.py .
RUN pip install opencv-python numpy
CMD ["python", "receiver.py", "--listen_port", "5000"]
