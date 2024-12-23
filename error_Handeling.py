# 1 Multiple Error in one block

try:
    num_list = [10, 20, 30]
    index = int(input("Enter the index to access: "))
    divisor = int(input("Enter a number to divide: "))
    result = num_list[index] / divisor
except (IndexError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
else:
    print(f"Result: {result}")
finally:
    print("Operation attempt completed.")



# 2 custom handeling

class InvalidAgeError(Exception):
    pass

def check_voter_eligibility(age):
    try:
        if age < 18:
            raise InvalidAgeError("Age must be 18 or above to vote.")
        print("You are eligible to vote.")
    except InvalidAgeError as e:
        print(f"Error: {e}")

check_voter_eligibility(16)
check_voter_eligibility(20)

# Error handeling in Dictionary

my_dict = {'name': 'Raffy', 'age': 19}

try:
    key = input("Enter the key to look up: ")
    value = my_dict[key]
except KeyError:
    print("Error: The key does not exist in the dictionary.")
else:
    print(f"Value for '{key}': {value}")
finally:
    print("Dictionary lookup attempt completed.")
