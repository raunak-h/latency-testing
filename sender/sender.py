import socket
import struct
import time
import argparse
import cv2

def run_sender(dest_ip, dest_port, video_source):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    cap = cv2.VideoCapture(video_source)
    if not cap.isOpened():
        print(f"❌ Failed to open video source: {video_source}")
        return

    print(f"🚀 Streaming video from '{video_source}' to {dest_ip}:{dest_port}")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("✅ Video stream ended or frame unavailable.")
            break

        # Encode frame
        ret, encoded_frame = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        # Prepend timestamp
        timestamp = struct.pack("d", time.time())
        packet = timestamp + encoded_frame.tobytes()

        # Send packet
        sock.sendto(packet, (dest_ip, dest_port))

        # Simulate frame rate
        time.sleep(1 / 30.0)  # 30 FPS

    cap.release()
    sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate video sender.")
    parser.add_argument("--dest_ip", type=str, required=True, help="Destination IP address.")
    parser.add_argument("--dest_port", type=int, required=True, help="Destination port number.")
    parser.add_argument("--video_source", type=str, required=True, help="Path to input video file.")
    args = parser.parse_args()

    run_sender(args.dest_ip, args.dest_port, args.video_source)
