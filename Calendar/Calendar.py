import calendar

def display_calendar(year, month):
    """
    Display a calendar for the given year and month.

    Parameters:
    year (int): The year for which the calendar will be displayed.
    month (int): The month for which the calendar will be displayed.
    """
    try:
        # Display the formatted month and year
        print(calendar.month(year, month))
    except Exception as e:
        print(f"An error occurred: {e}")

def fetch_year():
    """
    Prompts the user to enter a valid year.
    Returns:
    int: A valid year entered by the user.
    """
    while True:
        try:
            year = int(input("Enter year: "))
            if year <= 0:
                raise ValueError("Year must be a positive integer.")
            return year
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please try again.")

def fetch_month():
    """
    Prompts the user to enter a valid month.
    Returns:
    int: A valid month entered by the user.
    """
    while True:
        try:
            month = int(input("Enter month (1-12): "))
            if month < 1 or month > 12:
                raise ValueError("Month must be between 1 and 12.")
            return month
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please try again.")

if __name__ == "__main__":
    # Fetch user input for year and month
    year = fetch_year()
    month = fetch_month()

    # Display the calendar for the specified year and month
    display_calendar(year, month)
