#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import signal
"""Initialize metrics"""
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

""" Function to handle keyboard interruption (CTRL + C)"""
def handle_interrupt(signal, frame):
    print("\nFile size: {}".format(total_file_size))
    for status_code, count in sorted(status_code_counts.items()):
        print("{}: {}".format(status_code, count))
    sys.exit(0)

"""Register the interrupt handler"""
signal.signal(signal.SIGINT, handle_interrupt)

"""Read input lines and process them"""
for line in sys.stdin:
    try:
        ip_address, date, request, status_code, file_size = line.strip().split()
        total_file_size += int(file_size)
        status_code_counts[int(status_code)] += 1
    except ValueError:
        pass

""" Print metrics after processing all lines"""
print("\nFile size: {}".format(total_file_size))
for status_code, count in sorted(status_code_counts.items()):
    print("{}: {}".format(status_code, count))
