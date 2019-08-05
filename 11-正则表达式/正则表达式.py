import re


# E-Mail匹配
def is_valid_email(addr):
    if re.match(r'^[0-9a-zA-Z\_\.]+[@]+[0-9a-zA-Z]+[.com|.cn|.org|.top]+$',addr):
    #if re.match(r'^([0-9a-zA-Z\_\.]+)([@]+[0-9a-zA-Z]+[.com|.cn|.org|.top]+)$',addr):
        print('YES')
    else:
        print('NO')
    return True

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert is_valid_email('bob#example.com')
assert is_valid_email('mr-bob@example.com')
print('ok')



# 进阶分组
print('\n分组')
def name_of_email(addr):
    re_email = re.compile(r'^([0-9a-zA-Z\_\.]+)([@]+[0-9a-zA-Z]+[.com|.cn|.org|.top]+)$')
    m = re_email.match(addr)
    if m:
        print(m.group(1))
    else:
        print('NO')
    return None

# 测试:
name_of_email('tom@voyager.org')
name_of_email('<Tom Paris> tom@voyager.org')

print('ok')