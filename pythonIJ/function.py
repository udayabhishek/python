def user(name, *info):
    print(name,info)
    for item in info:
        print(item)

user('ram', 1,2,3,4,"hi")

def userInfo(fname, lname, **userInfo):
    userInfo['first_name'] = fname
    userInfo['last_name'] = lname
    return userInfo

userProfile = userInfo('ram', 'shayam', location='ayodhya', field = 'dharma')
print(userProfile)