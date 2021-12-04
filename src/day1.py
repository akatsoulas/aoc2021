import itertools


def part1a(payload: list[int]) -> int:
    return sum(n1 < n2 for n1, n2 in zip(payload, itertools.islice(payload, 1, None)))


def part1b(payload: list[int]) -> int:
    # 3.10 fun
    return sum(n1 < n2 for n1, n2 in itertools.pairwise(payload))


if __name__ == "__main__":

    with open("../inputs/day1") as f:
        # `filter` out empty items and map to int
        data = list(map(int, filter(None, f.read().splitlines())))
    print(f"part v1_out: {part1a(data)}")
    print(f"v2 out: {part1b(data)}")
