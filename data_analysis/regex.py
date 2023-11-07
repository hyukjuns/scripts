import re

# return object
re.search('keyword','string')

# return list
re.search('kw','string')

# ^시작문자, 끝문자$, \특수문자
# [abc]: a or b or c, [a-zA-Z]
a = re.findall('[tajjb]', 'abcedfg')
print(a)

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

target = "abced123asdf"
result = re.findall('[^ab]', target)
print(result)