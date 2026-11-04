"""Small program that calculates distances, paces or finish time based on the other two factors"""


def convert_distance(distance: str) -> float:
    """Converts distance string in format: 'x,x' into a float"""
    nr_wth_dot = distance.replace(",", ".")
    result = float(nr_wth_dot)
    return result


a = "88,976567"
b = "0,23"
c = "167646,1111"

print(convert_distance(a))
print(convert_distance(b))
print(convert_distance(c))