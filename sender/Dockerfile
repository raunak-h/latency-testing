FROM python:3.9-slim
WORKDIR /app
COPY sender.py .
RUN pip install opencv-python
CMD ["python", "sender.py", "--dest_ip", "receiver", "--dest_port", "5000", "--video_source", "0"]
