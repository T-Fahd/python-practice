from tqdm import tqdm


def numberOfWays(startPos: int, endPos: int, k: int) -> int:
    """
    Solving Leetcode Problem.
    https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

    Given two positive integers startPos and endPos
    Initially, you are standing at position startPos on an infinite
    number line. With one step, you can move either one position to the left,
    or one position to the right.

    Given a positive integer k, return the number of different ways to
    reach the position endPos starting from startPos, such that you
    perform exactly k steps.
    """
    paths = [[startPos]]

    for i in tqdm(range(k)):
        new_paths = []

        for path in paths:
            last_position = path[-1]

            new_path_left = path + [last_position - 1]
            new_path_right = path + [last_position + 1]

            new_paths.append(new_path_left)
            new_paths.append(new_path_right)

        paths = new_paths

    num_ways = 0

    for path in paths:
        if path[-1] == endPos:
            num_ways += 1

    return num_ways


def test_number_of_ways():
    print(numberOfWays(1, 2, 3))


if __name__ == "__main__":
    test_number_of_ways()