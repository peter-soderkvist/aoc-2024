import sys

from ..day_abc import AbsDay


EXAMPLE_INPUT = [
    "7 6 4 2 1",
    "1 2 7 8 9",
    "9 7 6 2 1",
    "1 3 2 4 5",
    "8 6 4 4 1",
    "1 3 6 7 9",
]


class DayTwo(AbsDay):
    
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
            with open("days/day_2/input.txt") as f:
                input = f.readlines()
                part(input)


    def part_one(self, input: list):
        
        safe_reports = 0
        for line in input:
            
            last_num = "first"
            direction = ""
            nums = line.split()
            self.logger.debug(f"--- {nums=}")
            for i, num in enumerate(nums):
                
                # Skip first number
                if last_num == "first":
                    last_num = int(num)
                    continue
                
                # Determine direction
                if i == 1:
                    if int(num) > last_num:
                        direction = "up"
                    else:
                        direction = "down"
                
                
                current_num = int(num)
                comparison = [current_num - 3, current_num - 2, current_num - 1, current_num + 1, current_num + 2, current_num + 3]
                self.logger.debug(f"{last_num=} {current_num=}")
                self.logger.debug(f"{comparison=}")
                
                # Break if the numbers aren't in the correct order
                if direction == "up" and current_num < last_num:
                    break
                if direction == "down" and current_num > last_num:
                    break
                
                # Break if the numbers are to far apart
                if not last_num in comparison:
                    break
                
                # Assign last_num if we're not at the end of the list
                if i != len(nums) - 1:
                    last_num = current_num
                    continue
                
                # If we're at the end of the list, the report is safe
                self.logger.debug(f"Safe report: {line.strip()}")
                safe_reports += 1
        
        self.logger.info(f"--> Safe reports: {safe_reports}")

    def part_two(self, input: list):
        
        safe_reports = 0
        for line_number, line in enumerate(input):
            
            dampener = 0
            last_num = "first"
            direction = ""
            nums = line.split()
            self.logger.debug(f"--- {nums=}")
            for i, num in enumerate(nums):
                
                current_num = int(num)
                use_dampener = False
                
                # Skip first number
                if last_num == "first":
                    last_num = int(num)
                    continue
                
                # Determine direction
                if i == 1:
                    if current_num > last_num:
                        direction = "up"
                    else:
                        direction = "down"
                
                comparison = [current_num - 3, current_num - 2, current_num - 1, current_num + 1, current_num + 2, current_num + 3]
                self.logger.debug(f"{last_num=} {current_num=}")
                self.logger.debug(f"{comparison=}")
                
                # Use dampener if the numbers aren't in the correct order
                if direction == "up" and current_num < last_num:
                    use_dampener = True
                if direction == "down" and current_num > last_num:
                    use_dampener = True
                
                # Use dampener if the numbers are to far apart or the same
                if not last_num in comparison:
                    use_dampener = True
                    
                # Break if the dampener has already been used
                if use_dampener:
                    dampener += 1
                    if dampener > 1:
                        self.logger.debug(f"dampener already used, breaking on element {i} in line {line_number} - {current_num=} on {nums=}")
                        break
                    continue
                
                # Assign last_num if we're not at the end of the list
                if i != len(nums) - 1:
                    last_num = current_num
                    continue
                
                # If we're at the end of the list, the report is safe
                self.logger.debug(f"Safe report: {line.strip()}")
                safe_reports += 1
                
        self.logger.info(f"--> Safe reports: {safe_reports}")
