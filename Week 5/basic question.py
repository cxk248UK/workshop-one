def complement():
    dna_string = input("please input the DNA sequence ")
    ans = ""
    for ch in dna_string:
        match ch:
            case "A":
                ans += "T"
            case "T":
                ans += "A"
            case "G":
                ans += "C"
            case "C":
                ans += "G"
            case _:
                ans += ""
    print("complement sequence is " + ans)


def dutch_flag():
    flag_list = input("please input list ")
    print(flag_list)
    red_num = flag_list.count("red")
    green_num = flag_list.count("green")
    blue_num = flag_list.count("blue")
    ans = ["red"] * red_num + ["green"] * green_num + ["blue"] * blue_num
    print(ans)


def main():
    while True:
        question_type = int(input("Please input the question number(1,2,3,4) "))
        if question_type == -1:
            print("exit program")
            break
        if question_type not in range(1, 4):
            print("invalid number please retry")
            continue
        match question_type:
            case 1:
                complement()
            case 2:
                dutch_flag()
            case _:
                continue


if __name__ == "__main__":
    main()
