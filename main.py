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


def convert_pace_output(pace: float) -> str:
    """Converts pace as float into a string"""
    minutes = int(pace)
    seconds = int(round((pace - minutes)*60))
    while seconds >= 60:
        minutes += 1
        seconds -= 60
    if (seconds) < 10:
        return f'{minutes}:0{int(seconds)} min'
    else:
        return f'{minutes}:{int(seconds)} min'


def convert_time_output(finish_time: float) -> str:
    """Converts finish time as float into a string"""
    hours = int(finish_time // 60)
    minutes = int(round(finish_time % 60))
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
    return round((calculatable_finish_time / calculatable_pace), 2)

print(calculate_distance("04:59", "03:30"))