def cm2_to_m2(area_cm2: float) -> float:
    return area_cm2 / 10000.0

def compare_areas(area1: float, area2: float) -> str:
    if area1 > area2:
        return "First shape is larger."
    elif area2 > area1:
        return "Second shape is larger."
    else:
        return "Both shapes have equal area."
