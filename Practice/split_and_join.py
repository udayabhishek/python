def split_and_join(line):
    split_str = line.split(" ")
    print("-".join(split_str))

inp_str = input("Enter String: ")
res = split_and_join(inp_str)
print(res)