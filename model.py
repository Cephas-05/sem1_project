#initialization
blood_bank = dict()
blood_bank = {"A+":3, "B+": 10, "A-":2, "O+":1, "O-":2}



need_or_want = input("Are you gonna donate or need blood? ")
if need_or_want == "Donate":
    blood_type = input("Enter your type of blood: ")
    for i in blood_bank:
        if blood_type == i:
            blood_bank[i] += 1
            print(f"{blood_type} has been added in the blood bank ")
        if blood_type not in blood_bank.keys():
            blood_bank[blood_type] = 1
            print(f"{blood_type} has been added newly in the blood bank")

elif need_or_want == "Need":
    need = input("What blood do you want? ")
    for i in blood_bank.keys():
        if i == need and blood_bank[i] > 0:
            print(f"{i} is available and it will arrive you shortly ")
            blood_bank[i] -= 1
    if need not in blood_bank.keys():
        print("Sorry this blood type is not available right now")

        