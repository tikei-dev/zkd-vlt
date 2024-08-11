# user_choice.py
import csv
from datetime import datetime
import random

class UserChoice:
    @classmethod
    def input_array(cls):
        while True:
            try:
                choice_list = input("Enter your user_choice_list (e.g., 1 2 3 4 5 6):\n\t")
                num_arr = choice_list.split()
                if not num_arr:
                    raise ValueError("Input cannot be empty.")
                else:
                    num_arr = {int(num) for num in num_arr}
                    return num_arr
            except ValueError:
                print("Invalid input. Please enter integers only separated by spaces.")

    @classmethod
    def user_choice(cls, num_range=None, count=6):
        while True:
            no_list = cls.input_array()
            if len(no_list) >= count:
                results = sorted(list(no_list))
                print(f"Results >>: {results}\n")
                print(f"Type of results: {type(results)}")
                return results
            else:
                print(f"You need to enter at least {count} numbers. Auto random add no.")
                while len(no_list) < count:
                    no_list.add(random.randint(1, num_range))
                results = sorted(list(no_list))
                print(f"Results >>: {results}\n")
                #print(f"Type of results: {type(results)}")
                return results

    @staticmethod
    def save_results_to_csv(results, filename_prefix="user_choice", num_range=55):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{num_range}_{filename_prefix}_{timestamp}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["No 1", "No 2", "No 3", "No 4", "No 5", "No 6"])
            writer.writerow(results)

if __name__ == "__main__":
    results = UserChoice.user_choice(num_range=55)
    UserChoice.save_results_to_csv(results, num_range=55)
