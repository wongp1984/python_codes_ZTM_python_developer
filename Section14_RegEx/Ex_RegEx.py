import re
pattern = re.compile('search inside of this text please!')
string = 'search inside of this text please! 45fsd sdfg dsfgdfg'
a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)