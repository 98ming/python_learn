"""
    一段注释
"""
ACCOUNT = 'user'
PASSWORD = '123456'
print('please input account')
user_account = input()
print('please input password')
user_password = input()
if user_account == ACCOUNT and user_password == PASSWORD:
    print('success')
else:
    print('fail')
