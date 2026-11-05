"""Small program that calculates distances, paces or finish time based on the other two factors"""


def convert_distance_input(distance: str) -> float:
    """Converts distance string in format: 'x,x' into a float"""
    return float(distance.replace(",", "."))


def convert_pace_input(pace: str) -> float:
    """Converts pace string into a float of minutes"""
    minutes, seconds = pace.split(":")
    return float(minutes) + float(seconds) / 60