import re

# return object
re.search('keyword','string')

# return list
re.search('kw','string')

# ^시작문자, 끝문자$, \특수문자
# [abc]: a or b or c, [a-zA-Z]
a = re.findall('[tajjb]', 'abcedfg')
print(a)

# [^abc] : Not, a or b or c가 아닌것
# \d: digit, 모든숫자, 2자리: \d\d, 3자리: \d{3}, 숫자가아님: \D, 스페이스바검색: \s, 스페이스가 아닌것 \S(모든문자)
# a+ : a 라는 숫자 반복해서 찾음
# case insensitive: re.findall('kw','string', re.IGNORECASE)

# 2023-10-10 to 2023.10.10
# re.sub('target', 'change', 'string')
s = re.sub('\-', '.', '2023-10-10')
print(s)

target = 'abseasdflkj123123adnflk513414'
s = re.sub('\d','',target)
print(s)

# email check
result = re.findall('\D\S+\@\D\S+.\D\S+', 'a123bc123@example.com')
print(result)
