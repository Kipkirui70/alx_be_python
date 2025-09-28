# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")
    return current_date


def calculate_future_date(days: int):
    """
    Calculate and display the future date after adding given days.

    Parameters:
        days (int): Number of days to add.

    Returns:
        datetime: The future date.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future Date after {days} day(s): {formatted_future_date}")
    return future_date


def main():
    # Part 1: Show current date and time
    display_current_datetime()

    # Part 2: Calculate future date
    try:
        days = int(input("Enter number of days to add: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input! Please enter an integer.")


if __name__ == "__main__":
    main()
# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")
    return current_date


def calculate_future_date(days: int):
    """
    Calculate and display the future date after adding given days.

    Parameters:
        days (int): Number of days to add.

    Returns:
        datetime: The future date.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future Date after {days} day(s): {formatted_future_date}")
    return future_date


def main():
    # Part 1: Show current date and time
    display_current_datetime()

    # Part 2: Calculate future date
    try:
        days = int(input("Enter number of days to add: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input! Please enter an integer.")


if __name__ == "__main__":
    main()
