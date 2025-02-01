def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")


string = "Kundan kuldeep karthik kuldeep"
sub_str = "Kuldeep"
check(string, sub_str)