import cv2
import socket
import struct
import time
import argparse

def run_sender(dest_ip, dest_port, video_source=0):
    cap = cv2.VideoCapture(video_source)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    frame_interval = 1/30  # Targeting 30 FPS

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Capture current timestamp (in seconds with sub-second precision)
        timestamp = time.time()
        # Encode frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        # Create a packet: 8 bytes for timestamp + image data
        packet = struct.pack("d", timestamp) + buffer.tobytes()
        sock.sendto(packet, (dest_ip, dest_port))
        time.sleep(frame_interval)

    cap.release()
    sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate video sender.")
    parser.add_argument("--dest_ip", type=str, required=True, help="Destination IP address.")
    parser.add_argument("--dest_port", type=int, required=True, help="Destination port number.")
    parser.add_argument("--video_source", type=int, default=0, help="Video source (default webcam).")
    args = parser.parse_args()
    run_sender(args.dest_ip, args.dest_port, args.video_source)
