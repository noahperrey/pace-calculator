"""Small program that calculates distances, paces or finish time based on the other two factors"""


def convert_distance_input(distance: str) -> float:
    """Converts distance string in format: 'x,x' into a float"""
    return float(distance.replace(",", "."))


def convert_pace_input(pace: str) -> float:
    """Converts pace string into a float of minutes"""
    minutes, seconds = pace.split(":")
    return float(minutes) + float(seconds) / 60


def convert_time_input(finish_time: str) -> float:
    """Converts finish time string into a float of minutes"""
    hours, minutes = finish_time.split(":")
    return float(hours) * 60 + float(minutes)


def convert_distance_output(distance: float) -> float:
    """Rounds distance to 2 decimals"""
    return round(distance, 2)


def convert_pace_output(pace: float) -> str:
    """Converts pace as float into a string like 5.7 -> '5:42 min'"""
    minutes = int(pace)
    seconds = round((pace - minutes) * 60)
    while seconds >= 60:
        minutes += 1
        seconds -= 60
    if seconds < 10:
        return f'{minutes}:0{seconds} min'
    else:
        return f'{minutes}:{seconds} min'


def convert_time_output(finish_time: float) -> str:
    """Converts finish time as float into a string like 90.0 -> '1:30 h'"""
    hours = int(finish_time // 60)
    minutes = round(finish_time % 60)
    while minutes >= 60:
        hours += 1
        minutes -= 60
    if minutes < 10:
        return f'{hours}:0{minutes} h'
    else:
        return f'{hours}:{minutes} h'


def calculate_pace(distance: str, finish_time: str) -> str:
    """Calculates pace based on distance and finish time input"""
    calculatable_distance = convert_distance_input(distance)
    calculatable_finish_time = convert_time_input(finish_time)
    return convert_pace_output(calculatable_finish_time / calculatable_distance)


def calculate_finish_time(pace: str, distance: str) -> str:
    """Calculates finish time based on pace and distance input"""
    calculatable_pace = convert_pace_input(pace)
    calculatable_distance = convert_distance_input(distance)
    return convert_time_output(calculatable_pace * calculatable_distance)


def calculate_distance(pace: str, finish_time: str) -> float:
    """Calculates distance based on pace and finish time input"""
    calculatable_pace = convert_pace_input(pace)
    calculatable_finish_time = convert_time_input(finish_time)
    return convert_distance_output(calculatable_finish_time / calculatable_pace)


def main() -> None:
    """Ask the user what to calculate, read the two values and print the result."""
    menu_choices = ["1", "2", "3", "4"]
    menu_choice = input("What would you like to have calculated?\n1 for Distance\n2 for Pace\n3 for Finish Time\n4 to end: ")

    while menu_choice not in menu_choices:
        menu_choice = input("Unexpected Answer\nPlease retry\n1 for Distance\n2 for Pace\n3 for Finish Time\n4 to end: ")

    if menu_choice == "1":
        pace = input("Please enter your pace like shown -> e.g. 5:30: ")
        finish_time = input("Please enter your finish time like shown -> e.g. 1:30: ")
        print(f'{calculate_distance(pace, finish_time)} km')

    elif menu_choice == "2":
        distance = input("Please enter your distance like shown -> e.g. 42,2: ")
        finish_time = input("Please enter your finish time like shown -> e.g. 1:30: ")
        print(calculate_pace(distance, finish_time))

    elif menu_choice == "3":
        pace = input("Please enter your pace like shown -> e.g. 5:30: ")
        distance = input("Please enter your distance like shown -> e.g. 42,2: ")
        print(calculate_finish_time(pace, distance))

    else:
        print("Bye Bye")


if __name__ == "__main__":
    main()