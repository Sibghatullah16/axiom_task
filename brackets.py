def check_balance(brackets):  # The argument is a string
    check_right = 0
    check_left = 0

    if brackets == "":
        return True
    else:
        for i in range(len(brackets)):
            if brackets[i]=="[":
                check_right += 1
            elif brackets[i] == "]":
                check_left += 1
            else:
                continue
        if check_left == check_right:
            return True
        else:
            return False
# Replace with your code