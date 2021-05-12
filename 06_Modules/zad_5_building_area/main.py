import areas


if __name__ == '__main__':
    flat = [
        ['rectangle', 4, 6],
        ['trapeze', 4,2,3],
    ]
    flat_area = []
    for room in flat:
        if room == ['rectangle']:
            ra = areas.rectangle_area(room[1], room[2])
            flat_area.append(['rectangle', ra])
        if room == ['trapeze']:
            ra = areas.trapeze_area(flat.index(['trapzez']))
            flat_area.append(['rectangle', ra])