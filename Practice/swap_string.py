def swap_case(s):
    print(len(s))
    if not 0<len(s)<1000:
        return
    str_res = ''
    for i in s :
        if i.isupper():
            str_res += i.lower()
        else:
            str_res +=  i.upper()
    return str_res

inp_str = input("Enter String: ")
res = swap_case(inp_str)
print(res)