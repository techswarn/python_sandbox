b = "][][]"

def check_balance(str):
    size = len(b)
    balanced = True
    check = 0
    for v in b:
        if v == '[':
            check += 1
            print(check)
        elif v == ']':
            check -= 1
            print(check)
        if check < 0:
            break
    return check == 0


print(check_balance(b))