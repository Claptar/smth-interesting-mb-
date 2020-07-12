# python3
import sys


def compute_min_refills(distance, tank, stops):
    count = 0
    last_stop = 0
    stops.append(distance)
    stops = [0] + stops
    i = 1
    while i <= len(stops) - 1:
        if stops[i] - last_stop <= tank:
            i += 1
        elif stops[i] - last_stop > tank and last_stop != stops[i - 1]:
            last_stop = stops[i - 1]
            count += 1
        else:
            return -1
    return count


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
