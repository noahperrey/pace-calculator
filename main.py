"""Small program that calculates distances, paces or finish times based
on the other two values
"""


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


def convert_distance_output(distance: float) -> str:
    """Rounds distance to 2 decimals and converts it into a string like 16.3636 -> '16,36'"""
    return str(round(distance, 2)).replace(".", ",")


def convert_pace_output(pace: float) -> str:
    """Converts pace as float into a string like 5.7 -> '05:42 min'"""
    minutes = int(pace)
    seconds = round((pace - minutes) * 60)
    while seconds >= 60:
        minutes += 1
        seconds -= 60
    return f"{minutes:02}:{seconds:02} min"


def convert_time_output(finish_time: float) -> str:
    """Converts finish time as float into a string like 90.0 -> '01:30 h'"""
    hours = int(finish_time // 60)
    minutes = round(finish_time % 60)
    while minutes >= 60:
        hours += 1
        minutes -= 60
    return f"{hours:02}:{minutes:02} h"


def calculate_pace(distance: str, finish_time: str) -> str:
    """Calculates pace based on distance and finish time input"""
    calculable_distance = convert_distance_input(distance)
    calculable_finish_time = convert_time_input(finish_time)
    return convert_pace_output(calculable_finish_time / calculable_distance)


def calculate_finish_time(pace: str, distance: str) -> str:
    """Calculates finish time based on pace and distance input"""
    calculable_pace = convert_pace_input(pace)
    calculable_distance = convert_distance_input(distance)
    return convert_time_output(calculable_pace * calculable_distance)


def calculate_distance(pace: str, finish_time: str) -> str:
    """Calculates distance based on pace and finish time input"""
    calculable_pace = convert_pace_input(pace)
    calculable_finish_time = convert_time_input(finish_time)
    return convert_distance_output(calculable_finish_time / calculable_pace)


def main() -> None:
    """Ask the user what to calculate, read the two values and print the result"""
    menu_choices = ["1", "2", "3", "4"]
    input_text = (
        "What would you like to have calculated?\n1 for Distance\n"
        "2 for Pace\n3 for Finish Time\n4 to end the program: "
    )

    while True:
        menu_choice = input(input_text)

        while menu_choice not in menu_choices:
            menu_choice = input(
                "Unexpected Answer\nPlease retry\n1 for Distance\n"
                "2 for Pace\n3 for Finish Time\n4 to end the program: "
            )

        if menu_choice == "1":
            pace = input("Please enter your pace (e.g. 05:30): ")
            finish_time = input("Please enter your finish time (e.g. 01:30): ")
            print(f"{calculate_distance(pace, finish_time)} km")

        elif menu_choice == "2":
            distance = input("Please enter your distance (e.g. 42,2): ")
            finish_time = input("Please enter your finish time (e.g. 01:30): ")
            print(calculate_pace(distance, finish_time))

        elif menu_choice == "3":
            pace = input("Please enter your pace (e.g. 05:30): ")
            distance = input("Please enter your distance (e.g. 42,2): ")
            print(calculate_finish_time(pace, distance))

        else:
            print("Bye!")
            break

        input_text = (
            "Do you want to calculate something else?\n1 for Distance\n"
            "2 for Pace\n3 for Finish Time\n4 for no, end the program: "
        )


if __name__ == "__main__":
    main()
