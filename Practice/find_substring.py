def count_substring(string, sub_string):
    if not 0<=len(string)<=200:
        return
    count = 0
    for i in range(0, (len(string)-len(sub_string)+1)):
        print(string[i:i+len(sub_string)])
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

"""Using List Comprehension"""
def count_substring1(string, sub_string):
    if not 0<=len(string)<=200:
        return
    return sum([ 1 for i in range(0, (len(string)-len(sub_string)+1)) if string[i:i+len(sub_string)] == sub_string])

# string, substring = (input().strip(), input().strip())
# print(count_substring(string, substring))
print(count_substring1("ABCDQWQWQABCDWQEWEABCD", "ABCD"))
print(count_substring1("ABCDCDC", "CDC"))

