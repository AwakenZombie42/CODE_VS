# we can import modules using the import keyword

# Import the built-in datetime module
import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()
print(f"Current date and time: {current_datetime}")

# Get the current date
current_date = datetime.date.today()
print(f"Current date: {current_date}")

# Create a specific date
specific_date = datetime.date(2024, 12, 25)
print(f"Specific date: {specific_date}")

# Calculate the difference between two dates
days_until_christmas = specific_date - current_date
print(f"Days until Christmas: {days_until_christmas.days}" )