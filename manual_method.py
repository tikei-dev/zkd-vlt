# manual_method.py
import random
import csv
from datetime import datetime

class ManualMethod:
    def __init__(self, num_range=55):
        self.num_range = num_range

    def input_array(self):
        choice_list = input(f"Enter your choice_list/{self.num_range} (e.g., 1 2 3):\n\t ")
        num_arr = choice_list.split()
        num_arr = [int(num) for num in num_arr]
        return num_arr

    def manual_generate_numbers(self, num, num_range=None, count=6):
        if num_range is None:
            num_range = self.num_range

        unique_numbers = set()
        unique_numbers.add(num)
        while len(unique_numbers) < count:
            unique_numbers.add(random.randint(1, num_range))
        return sorted(unique_numbers)

    def manual_method(self):
        choice_list_1 = self.input_array()
        choice_list_2 = self.input_array()
        results = []

        for i in choice_list_1:
            if i == 0:
                continue

            if i in choice_list_2:
                x = (self.num_range + i) // 2
                results.append(self.manual_generate_numbers(x))
            else:
                results.append(self.manual_generate_numbers(i))

        return results

    @staticmethod
    def save_results_to_csv(results, filename_prefix="manual_method", num_range=55):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{num_range}_{filename_prefix}_{timestamp}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["No 1", "No 2", "No 3", "No 4", "No 5", "No 6"])
            for result in results:
                writer.writerow(result)

if __name__ == "__main__":
    manual_method_instance = ManualMethod(num_range=55)
    results = manual_method_instance.manual_method()
    ManualMethod.save_results_to_csv(results, num_range=55)
