import socket
import struct
import time
import argparse
import numpy as np
import cv2
import csv
import os

def init_csv_logging(filename):
    file_exists = os.path.exists(filename)
    csv_file = open(filename, 'a', newline='')
    csv_writer = csv.writer(csv_file)
    if not file_exists:
        # Write header if file doesn't exist
        csv_writer.writerow(["measurement_time", "frame_timestamp", "latency_ms"])
    return csv_file, csv_writer

def run_receiver(listen_port, log_filename):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', listen_port))
    
    print("Receiver is listening on port", listen_port)
    
    # Initialize CSV logging
    csv_file, csv_writer = init_csv_logging(log_filename)

    try:
        while True:
            # Increase buffer size as needed
            packet, addr = sock.recvfrom(65536)
            if len(packet) < 8:
                continue

            # Unpack timestamp (first 8 bytes) and extract frame data
            frame_timestamp = struct.unpack("d", packet[:8])[0]
            frame_data = packet[8:]
            
            # Calculate latency (in milliseconds)
            measurement_time = time.time()
            latency = (measurement_time - frame_timestamp) * 1000
            print(f"Latency: {latency:.2f} ms")

            # Log the result to CSV
            csv_writer.writerow([measurement_time, frame_timestamp, latency])
            csv_file.flush()  # Ensure data is written immediately

            # Optionally decode and display the frame
            frame = cv2.imdecode(np.frombuffer(frame_data, np.uint8), cv2.IMREAD_COLOR)
            if frame is not None:
                cv2.imshow("Received Frame", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    finally:
        sock.close()
        csv_file.close()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate video receiver.")
    parser.add_argument("--listen_port", type=int, required=True, help="Port number to listen on.")
    parser.add_argument("--log_file", type=str, default="latency_log.csv", help="CSV file to log results.")
    args = parser.parse_args()
    run_receiver(args.listen_port, args.log_file)
