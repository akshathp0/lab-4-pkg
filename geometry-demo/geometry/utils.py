def area_stats(*shapes):
    if len(shapes) == 0:
        raise ValueError("Provide at least one Shape.")
    areas = [shape.area() for shape in shapes]

    return {
        "n": len(areas),
        "total": sum(areas),
        "mean": sum(areas) / len(areas),
        "min": areas[0],
        "max": areas[-1]
    }