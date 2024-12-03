import re

from ..day_abc import AbsDay


EXAMPLE_INPUT = [
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
]


class DayThree(AbsDay):
    
    def __init__(self):
        super().__init__()

    def run(self):
        self.logger.info(f"----- {self.__class__.__name__} running -----")
        
        for part in [self.part_one, self.part_two]:
            # Example input
            self.logger.info(f"{part.__name__} running with example input")
            part(EXAMPLE_INPUT)

            # Actual input
            self.logger.info(f"{part.__name__} running with actual input")
            with open("days/day_3/input.txt") as f:
                input = f.readlines()
                part(input)

    def part_one(self, input: list):
        multiplications = 0
        regex = r"mul\([0-9]+,[0-9]+\)"
        for line in input:
            for match in re.findall(regex, line):
                self.logger.debug(f"Match: {match}")
                nums = re.findall(r"[0-9]+", match)
                multiplications += int(nums[0]) * int(nums[1])
        
        self.logger.info(f"--> Total multiplications: {multiplications}")

    def part_two(self, input: list):
        multiplications = 0
        regex = r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"
        current_instruction = "do()"
        for line in input:
            
            matches = re.findall(regex, line)
            self.logger.debug(f"{matches=}")
            
            for match in matches:
                self.logger.debug(f"Match: {match}")
                if "do" in match:
                    current_instruction = match
                if current_instruction == "do()" and "do" not in match:
                    nums = re.findall(r"[0-9]+", match)
                    self.logger.debug(f"{nums=}")
                    multiplications += int(nums[0]) * int(nums[1])
        
        self.logger.info(f"--> Total multiplications: {multiplications}")
