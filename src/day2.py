def get_position(data):
    horizontal, depth = 0, 0
    for loc in data:
        match loc.split(" "):
            case ["forward", x]:
                horizontal += int(x)
            case ["up", x]:
                depth -= int(x)
            case ["down", x]:
                depth += int(x)
    return horizontal * depth


if __name__ == "__main__":
    with open("../inputs/day2p1") as f:
        data = f.read().splitlines()
    print(get_position(data))
