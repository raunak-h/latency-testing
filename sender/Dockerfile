FROM python:3.9-slim
WORKDIR /app
COPY sender.py .
COPY video/sample.mp4 video/
RUN apt-get update && apt-get install -y libgl1
RUN apt-get update && apt-get install -y libglib2.0-0
RUN pip install opencv-python
CMD ["python", "sender.py", "--dest_ip", "receiver", "--dest_port", "5000", "--video_source", "video/sample.mp4"]
