def check_sum(num_list):
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            sum = num_list[i] + num_list[j]
            if sum==0:
                return True
            else:
                continue
    return False
    #pass  # Replace with your code
