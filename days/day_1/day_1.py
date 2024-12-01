from datetime import datetime

from ..day_abc import AbsDay


EXAMPLE_INPUT = [
    "3   4",
    "4   3",
    "2   5",
    "1   3",
    "3   9",
    "3   3",
]

class DayOne(AbsDay):
    
    def __init__(self):
        super().__init__()

    def run(self):
        self.logger.info("Day 1 running")
        
        for part in [self.part_one, self.part_two]:
            # Example input
            part(EXAMPLE_INPUT)

            # Actual input
            with open("days/day_1/input.txt") as f:
                input = f.readlines()
                part(input)
    
    def parse_input(self, input: list) -> tuple[list, list]:
        # Parse input and create two lists
        left, right = [], []
        for line in input:
            a, b = line.split("   ")
            self.logger.debug(f"{a=} {b=}")
            left.append(int(a))
            right.append(int(b))
        
        # Sort lists
        left.sort()
        right.sort()
        self.logger.debug(f"{left=}")
        self.logger.debug(f"{right=}")
        
        return (left, right)
        
    def part_one(self, input: list):
        self.logger.info("Part one running")
        left, right = self.parse_input(input)

        # Calculate total distance between pairs in the two lists
        total_distance = 0
        for a, b in zip(left, right):
            self.logger.debug(f"{a=} {b=}")
            total_distance += abs(a - b)
        
        self.logger.info(f"--> Total distance: {total_distance}")

    def part_two(self, input: list):
        self.logger.info("Part two running")
        left, right = self.parse_input(input)
        
        # Calculate similarity
        similarity = 0
        for a in left:
            similarity += a * right.count(a)

        self.logger.info(f"--> Similarity: {similarity}")
