# A file members.txt contains list of all names and outstanding 
# amount separated by a space. Another file payments.txt contains list 
# of names and amount paid, for only those members who made a payment. 
# Find the list of members who:
#  1. Had outstanding but have not made payment
#  2. Had outstanding and have made partial payment
#  3. Have made extra payment

from numpy import true_divide


def reading_file_data(file_path):
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
# print(display_result(members_and_amounts, paid_members_and_amounts))
