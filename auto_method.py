# auto_method.py
import random
import csv
from datetime import datetime

class AutoMethod:
    @classmethod
    def auto_generate_numbers(cls, x, y, min_number, max_number, len_arr):
        unique_numbers = set()
        unique_numbers.add(random.randint(x, y))
        while len(unique_numbers) < len_arr:
            unique_numbers.add(random.randint(min_number, max_number))
        return sorted(unique_numbers)

    @classmethod
    def auto_method(cls, max_number):
        no_list = [1, 10, 20]
        results = []
        for i in no_list:
            x = i
            y = i + 9 if i != 1 else 9
            result = cls.auto_generate_numbers(x, y, i, max_number, 6)
            results.append(result)
        return results

    @staticmethod
    def save_results_to_csv(results, filename_prefix="auto_method", num_range=55):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{num_range}_{filename_prefix}_{timestamp}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["No 1", "No 2", "No 3", "No 4", "No 5", "No 6"])
            for result in results:
                writer.writerow(result)

if __name__ == "__main__":
    results = AutoMethod.auto_method(max_number=55)
    AutoMethod.save_results_to_csv(results)
