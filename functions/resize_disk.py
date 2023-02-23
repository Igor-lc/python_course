def resize_disk(size, parts):
    percent = (size / sum(parts))

    new_parts = []
    new_parts_size = 0
    for part in parts:
        ik = part * percent
        new_parts.append(int(ik))
        new_parts_size += ik - int(ik)

    new_parts[-1] = round(new_parts[-1] + new_parts_size)
    return new_parts


print(resize_disk(102, [10, 10, 20, 10]))


def resize_disk2(new_size, parts):
    percent = new_size / sum(parts)

    new_parts = []
    new_parts_size = 0
    for part in parts:
        new_part_size = int(part * percent)
        new_parts.append(new_part_size)
        new_parts_size += new_part_size

    if new_parts_size < new_size:
        new_parts[-1] += new_size - new_parts_size

    return new_parts


print(resize_disk2(102, [10, 10, 20, 10]))
