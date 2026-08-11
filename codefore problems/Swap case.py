def swap_case(s):
    result=""
    for c in s:
        num=ord(c)
        if 65<=num<=90:
            num=num+32
            c=chr(num)
        elif 97<=num<=122:
            num=num-32
            c=chr(num)
        result+=c 
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)