# A file members.txt contains list of all names and outstanding 
# amount separated by a space. Another file payments.txt contains list 
# of names and amount paid, for only those members who made a payment. 
# Find the list of members who:
#  1. Had outstanding but have not made payment
#  2. Had outstanding and have made partial payment
#  3. Have made extra payment


def reading_file_data(file_path):
    """
    Read data from a given file, store it in a dictionary, and return the dictionary.

    Parameters: 
        file_path: The path to the file specified by the user as an input.
    Result:
        members_amount (dictionary): The data read from the given file is stored in the dictionary, 
                                     with member as a key and amount as a value.
    """
    with open(file_path) as file:  
        members_amounts = dict() 
        for line in file.readlines():
            if line == " ":
                continue
            data = line.strip().split()
            member = " ".join(data[:-1])
            amount = "".join(data[-1:])
            members_amounts[member] = amount
    return members_amounts


def display_result(members_and_amounts, paid_members_and_amounts):
    """
    Takes the two dictionaries containing the data read from the members.txt and payments.txt files and returns three lists.
    The first list contains members who have not made any payments, the second list contains members who have made partial 
    payments, and the final list contains members who have made extra payments.

    Parameters:
        members_and_amounts (dictionary): The dictionary includes all of the names and outstanding amounts from the members.txt file.
        paid_members_and_amounts (dictionary): The dictionary includes all of the names and amounts paid as read from the payments.txt file.
    Result:
        members_not_paid (list): The list of members who had outstanding amount but have not made payment.
        members_partial_payment (list): The list of members who had outstanding amount and have made partial payment.
        members_extra_payment (llist): The list of members who had outstanding amount have made extra payment.
    """
    members_not_paid, members_partial_payment, members_extra_payment = [], [], []
    for member, amount in members_and_amounts.items():
        if member not in paid_members_and_amounts.keys():
            members_not_paid.append(member)
        if member in paid_members_and_amounts.keys():
            if amount < paid_members_and_amounts[member]:
                members_extra_payment.append(member)
            else:
                if str(int(int(amount) / 2)) >= paid_members_and_amounts[member]:
                    members_partial_payment.append(member)

    return (members_not_paid, members_partial_payment, members_extra_payment)


members_and_amounts, paid_members_and_amounts = {}, {}
file_not_valid = True
while file_not_valid:
    file_path = input("Enter full path (absolute path) of members.txt file: ")
    print(file_path[-11:])
    if file_path[-11::1] != "members.txt":
        print("Please enter the correct file path as specified name: ")
    else:
        members_and_amounts = reading_file_data(file_path)
        file_not_valid = False

file_not_valid = True
while file_not_valid:
    file_path = input("Enter full path (absolute path) of payments.txt file: ")
    if file_path[-12::1] != "payments.txt":
        print("Please enter the correct file path as specified name: ")
    else:
        paid_members_and_amounts = reading_file_data(file_path)
        file_not_valid = False

results = display_result(members_and_amounts, paid_members_and_amounts)
print("The list of members who had outstanding but have not made payment are:" + str(results[0]))
print("The list of members who had outstanding and have made partial payment are:" + str(results[1]))
print("The list of members who had outstanding and have made extra payment are:" + str(results[2]))
