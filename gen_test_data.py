import random
import time
from datetime import datetime, timedelta

def generate_test_data(filename, num_entries=1000, days=2):
    """Generate test data with the specified number of entries over the given number of days."""
    start_time = datetime.now() - timedelta(days=days)
    with open(filename, 'w') as file:
        for _ in range(num_entries):
            # Generate a random timestamp within the 2-day period
            random_seconds = random.randint(0, days * 24 * 3600)
            epoch_time = int((start_time + timedelta(seconds=random_seconds)).timestamp())
            # Generate a random duration between 1 and 1000 milliseconds
            duration = random.randint(1, 1000)
            file.write(f"{epoch_time} {duration}\n")

# Generate the test data file
generate_test_data('test_data.txt')

