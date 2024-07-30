import sys
import matplotlib.pyplot as plt
from datetime import datetime

def read_file(filename):
    """Read the file and parse its contents into a list of tuples."""
    data = []
    with open(filename, 'r') as file:
        for line in file:
            epoch_time, duration = line.strip().split()
            epoch_time = int(epoch_time)
            duration = int(duration)
            data.append((epoch_time, duration))
    return data

def plot_data(data):
    """Plot the parsed data with time on the x-axis and duration on the y-axis."""
    times = [datetime.fromtimestamp(epoch) for epoch, duration in data]
    durations = [duration for epoch, duration in data]

    plt.figure(figsize=(10, 5))
    plt.plot(times, durations, marker='o')
    plt.xlabel('Time')
    plt.ylabel('Duration (ms)')
    plt.title('Duration over Time')
    plt.grid(True)
    plt.gcf().autofmt_xdate()  # Rotate date labels
    plt.show()

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    data = read_file(filename)
    plot_data(data)

if __name__ == "__main__":
    main()

