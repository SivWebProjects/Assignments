# 1. A large file contains a list of mobile numbers. Print the list of
# VIP numbers in this file. A VIP number meets any of these criteria
# 1. First 5 digits and last 5 digits are identical ex: 9810198101
# 2. First 5 digits and last 5 digits are in a series, either
# increasing or decreasing. For example: 9810098101, 9811198110
# 3. Has 4 or more repeating digits, must be consecutive. For example:
# 9812222910 is a VIP number but 9812211223 is not
# 4. The first 5 and last 5 digits have the first 3 digits identical,
# with a pair of digits flipped at the end. Example: 9923999293


def store_phone_numbers(file_path): 
    """
    Read data from a given file, store it in a list, and return the list.

    Parameters:
        file_path: The location of the file containing the phone numbers.
    Result:
        phone_numbers (list): The list contains all of the phone numbers read from the file.
    """
    with open(file_path) as file:
        phone_numbers = [line.strip() for line in file.readlines() if line != " "]
    
    return phone_numbers


def display_vip_numbers(phone_numbers):
    """
    Takes the list of phone numbers read from the given file and returns the list of VIP 
    phone numbers that meet the conditions specified in the problem statement.

    Parameters:
        phone_numbers (list): The list contains all of the phone numbers read from the file.
    Result:
        vip_numbers (list): The list contains all of the VIP phone numbers.
    """
    phone_numbers = store_phone_numbers(file_path)
    vip_numbers = []
    for ph_num in phone_numbers:
        if ph_num[:5] == ph_num[5:]:
            vip_numbers.append(ph_num)
            continue
        elif (ph_num[:5] == "".join(sorted(ph_num[:5])) or ph_num[:5] == "".join(sorted(ph_num[:5], reverse=True))):
            if (ph_num[5:] == "".join(sorted(ph_num[5:])) or ph_num[5:] == "".join(sorted(ph_num[5:], reverse=True))):
                vip_numbers.append(ph_num)
                continue
        elif (ph_num[0:3] == ph_num[5:8]) and (ph_num[3:5] == ph_num[-1:-3:-1]):
            vip_numbers.append(ph_num)
            continue
        else:
            repeated_digits = []
            for char in ph_num:
                if ph_num.count(char) >= 4:
                    if char not in repeated_digits:
                        repeated_digits.append(char)
            for char in repeated_digits:
                for i in range(len(ph_num)):
                    if char == ph_num[i]:
                        char_start_index = i
                        if char*4 ==  ph_num[char_start_index:char_start_index+4]:
                            vip_numbers.append(ph_num)
                            break
    return vip_numbers
    

file_path = input("Please enter absolute file path (full path) which contains phone numbers: ")
phone_numbers = store_phone_numbers(file_path)
vip_numbers = display_vip_numbers(phone_numbers)
print("The list of VIP numbers from given list of phone numbers are: " + str(vip_numbers))
