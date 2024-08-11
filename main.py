# main.py
from auto_method import AutoMethod
from manual_method import ManualMethod
from user_choice import UserChoice

auto_instance = AutoMethod()
manual_instance = ManualMethod()
user_instance = UserChoice()

def show_menu():
    print("1. AUTO Method")
    print("2. MANUAL Method")
    print("3. USER CHOICE")
    print("4. Exit\n")

def option1(input_mode):
    print(f"\n____________Result for AUTO Method 6/{input_mode}____________\n")
    results = auto_instance.auto_method(max_number=input_mode)
    auto_instance.save_results_to_csv(results, num_range=input_mode)
    print(f"Generated Results: >>")
    for result in results:
        print(result)
    print(f"\n____________Result for AUTO Method 6/{input_mode}____________\n")

def option2(input_mode):
    print(f"\n____________Result for MANUAL Method 6/{input_mode}____________\n")
    results = manual_instance.manual_method()
    manual_instance.save_results_to_csv(results, num_range=input_mode)
    print(f"Generated Results: >>")
    for result in results:
        print(result)
    print(f"\n____________Result for MANUAL Method 6/{input_mode}____________\n")

def option3(input_mode):
    print(f"\n____________Result for USER CHOICE 6/{input_mode}____________\n")
    results = user_instance.user_choice(num_range=input_mode)
    user_instance.save_results_to_csv(results, num_range=input_mode)
    print(f"Generated Results: >> {results}")
    print(f"\n____________Result for USER CHOICE 6/{input_mode}____________\n")

def main():
    print("\n_________________[ TIKEI APP ]_________________\n")

    input_mode = int(input("Enter your choice (45 OR 55): "))
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            option1(input_mode)
        elif choice == "2":
            option2(input_mode)
        elif choice == "3":
            option3(input_mode)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
