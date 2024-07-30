import sys
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

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

def plot_duration(data):
    """Plot the duration data with time on the x-axis and duration on the y-axis."""
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

def plot_entry_counts(data, period):
    """Plot the number of entries over the specified time period."""
    df = pd.DataFrame(data, columns=['epoch_time', 'duration'])
    df['datetime'] = pd.to_datetime(df['epoch_time'], unit='s')
    
    if period == 'hourly':
        df['period'] = df['datetime'].dt.to_period('H')
    elif period == 'daily':
        df['period'] = df['datetime'].dt.to_period('D')
    else:
        print(f"Unsupported period: {period}")
        sys.exit(1)

    count_series = df['period'].value_counts().sort_index()
    count_series.index = count_series.index.to_timestamp()

    plt.figure(figsize=(10, 5))
    count_series.plot(marker='o')
    plt.xlabel('Time')
    plt.ylabel('Number of Entries')
    plt.title(f'Number of Entries per {period.capitalize()}')
    plt.grid(True)
    plt.gcf().autofmt_xdate()  # Rotate date labels
    plt.show()

def main():
    if len(sys.argv) not in [2, 3]:
        print("Usage: python script.py <filename> [period]")
        print("Period can be 'hourly' or 'daily'")
        sys.exit(1)

    filename = sys.argv[1]
    period = sys.argv[2] if len(sys.argv) == 3 else None

    data = read_file(filename)

    if period:
        plot_entry_counts(data, period)
    else:
        plot_duration(data)

if __name__ == "__main__":
    main()

