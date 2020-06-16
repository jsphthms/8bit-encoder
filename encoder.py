def Encode(string):

    while len(string) % 4 != 0:
        string += "~"

    st = string[::-1]
    binary_str = ""
    b = []
    dic = {}
    final_list = []

    for x in bytearray(st, "utf8"):
        b.append(format(x, "08b"))

    binstr = "".join(b)

    for i, n in enumerate(b):
        if i % 4 == 0:
            if n == "01111110":
                dic.setdefault("A", []).append("00000000")
            else:
                dic.setdefault("A", []).append(n)
        if i % 4 == 1:
            if n == "01111110":
                dic.setdefault("B", []).append("00000000")
            else:
                dic.setdefault("B", []).append(n)
        if i % 4 == 2:
            if n == "01111110":
                dic.setdefault("C", []).append("00000000")
            else:
                dic.setdefault("C", []).append(n)
        if i % 4 == 3:
            if n == "01111110":
                dic.setdefault("D", []).append("00000000")
            else:
                dic.setdefault("D", []).append(n)

    dic["A"] = "".join(dic["A"])
    dic["B"] = "".join(dic["B"])
    dic["C"] = "".join(dic["C"])
    dic["D"] = "".join(dic["D"])

    for i in range(len(binstr)):
        if i % 4 == 0:
            binary_str += dic["A"][0]
            dic["A"] = dic["A"][1:]
        if i % 4 == 1:
            binary_str += dic["B"][0]
            dic["B"] = dic["B"][1:]
        if i % 4 == 2:
            binary_str += dic["C"][0]
            dic["C"] = dic["C"][1:]
        if i % 4 == 3:
            binary_str += dic["D"][0]
            dic["D"] = dic["D"][1:]
        if len(binary_str) == 32:
            final_decimal = int(binary_str, 2)
            binary_str = ""
            final_list.append(final_decimal)

    final_list = final_list[::-1]

    return final_list


def Decode(list):
    l = list
    binary_list = []
    dic = {"A": [], "B": [], "C": [], "D": []}
    b_list = []
    final_list = []

    for i in l:
        dec = format(i, "032b")
        binary_list.append(dec)
    binary_list = binary_list[::-1]

    bin_string = "".join(binary_list)

    for i, n in enumerate(bin_string):
        if i % 4 == 0:
            dic["A"] += n
            if len(dic["A"]) == 8:
                dic["A"] = "".join(dic["A"])
        if i % 4 == 1:
            dic["B"] += n
            if len(dic["B"]) == 8:
                dic["B"] = "".join(dic["B"])
        if i % 4 == 2:
            dic["C"] += n
            if len(dic["C"]) == 8:
                dic["C"] = "".join(dic["C"])
        if i % 4 == 3:
            dic["D"] += n
            if len(dic["D"]) == 8:
                dic["D"] = "".join(dic["D"])

    dic["A"] = [(dic["A"][i : i + 8]) for i in range(0, len(dic["A"]), 8)]
    dic["B"] = [(dic["B"][i : i + 8]) for i in range(0, len(dic["B"]), 8)]
    dic["C"] = [(dic["C"][i : i + 8]) for i in range(0, len(dic["C"]), 8)]
    dic["D"] = [(dic["D"][i : i + 8]) for i in range(0, len(dic["D"]), 8)]

    for x in range(int(len(bin_string) / 8)):
        if x % 4 == 0:
            if len(dic["A"]) > 0:
                b_list.append(dic["A"][0])
                dic["A"] = dic["A"][1:]
        if x % 4 == 1:
            if len(dic["B"]) > 0:
                b_list.append(dic["B"][0])
                dic["B"] = dic["B"][1:]
        if x % 4 == 2:
            if len(dic["C"]) > 0:
                b_list.append(dic["C"][0])
                dic["C"] = dic["C"][1:]
        if x % 4 == 3:
            if len(dic["D"]) > 0:
                b_list.append(dic["D"][0])
                dic["D"] = dic["D"][1:]

    for x in b_list:
        if x == "00000000":
            pass
        else:
            x = int(x, 2)
            x = chr(x)
            final_list.append(x)
    final_list = final_list[::-1]
    final_str = "".join(final_list)
    return final_str


print("Welcome to the Art+Logic Text Formatter \n")
menu = input("Type option: 1. Encode String 2. Decode List q. Quit program: ")

while menu != "q":
    if menu == "1":
        raw_string = input("What string would you like to encode?\n")
        print("This is your encoded list: \n")
        print(Encode(raw_string))
    elif menu == "2":
        encoded_list = input(
            "What numbers would you like to decode?(Seperated by a comma and space. No brackets.)\n"
        )
        input_numbers = [int(i) for i in encoded_list.split(", ")]
        print("This is your string: \n")

        print(Decode(input_numbers))

    else:
        print("That is not an option. Choose an option. ")

    menu = input(
        "\nType option: 1. Add new movie to database 2. View movie database q. Quit program: "
    )
