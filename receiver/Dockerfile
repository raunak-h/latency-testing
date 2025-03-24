FROM python:3.9-slim
WORKDIR /app
COPY receiver.py .
RUN apt-get update && apt-get install -y libgl1
RUN apt-get update && apt-get install -y libglib2.0-0
RUN pip install opencv-python numpy
CMD ["python", "receiver.py", "--listen_port", "5000"]
