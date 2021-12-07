def get_position(data):
    horizontal, depth, aim = 0, 0, 0
    for loc in data:
        match loc.split(" "):
            case ["forward", x]:
                horizontal += int(x)
                depth += int(x) * aim
            case ["up", x]:
                aim -= int(x)
            case ["down", x]:
                aim += int(x)
    return (horizontal * aim, horizontal * depth)


if __name__ == "__main__":
    with open("../inputs/day2") as f:
        data = f.read().splitlines()
    print(get_position(data))
