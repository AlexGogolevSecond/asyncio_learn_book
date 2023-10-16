def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    #return True if num == reversed_num else False
    return num == reversed_num
    '''
    if num == reversed_num:
        return num
    else:
        return False
    '''
    
res = is_palindrome(121)
print(res)
