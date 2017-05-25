# -*- coding:utf-8 -*-
import re

object = "hello world?#$#%$#%!"

print("\n**********Match**********")
# match(string[, pos[, endpos]]) | re.match(pattern, string[, flags]): 
m =re.match(r"(\w\w+)\s(\w+)(?P<fuck>.*)",object)
print("m.string:",m.string)
print("m.re:",m.re)
print("m.pos:",m.pos)
print("m.endpos:",m.endpos)
print("m.lastindex:",m.lastindex)
print("m.lastgroup:",m.lastgroup)

print("m.group(1,2):",m.group(1,2))
print("m.groups():",m.groups())
print("m.groupdict():",m.groupdict())
print("m.start(2):",m.start(2))
print("m.end(2):",m.end(2))
print("m.span(2):",m.span(2))
print("m.expand(r'\2 \1\3'):",m.expand(r'\2 \1\3'))


print("\n**********Pattern**********")
# match(string[, pos[, endpos]]) | re.match(pattern, string[, flags]): 
# 这个方法将从string的pos下标处起尝试匹配pattern；如果pattern结束时仍可匹配，则返回一个Match对象；如果匹配过程中pattern无法匹配，或者匹配未结束就已到达endpos，则返回None。
p =re.compile(r"(\w+)\s(\w+)(?P<fuck>.*)",re.DOTALL)
print("p.pattern:",p.pattern)
print("p.flags:",p.flags)
print("p.groups:",p.groups)
print("p.groupindex:",p.groupindex)


print("\n**********Search**********")
# search(string[, pos[, endpos]]) | re.search(pattern, string[, flags]): 
# 这个方法用于查找字符串中可以匹配成功的子串。从string的pos下标处起尝试匹配pattern，如果pattern结束时仍可匹配，则返回一个Match对象；若无法匹配，则将pos加1后重新尝试匹配；直到pos=endpos时仍无法匹配则返回None。 
# pos和endpos的默认值分别为0和len(string))；re.search()无法指定这两个参数，参数flags用于编译pattern时指定匹配模式。 
pattern = re.compile('world')
match = pattern.search('hello world')
if match:
	print(match.group())


print("\n**********Split**********")
# split(string[, maxsplit]) | re.split(pattern, string[, maxsplit]): 
# 按照能够匹配的子串将string分割后返回列表。maxsplit用于指定最大分割次数，不指定将全部分割。 
p = re.compile(r'\d+')
print(p.split('one1two2three3four4'))


print("\n**********Findall**********")
# findall(string[, pos[, endpos]]) | re.findall(pattern, string[, flags]): 
# 搜索string，以列表形式返回全部能匹配的子串。 
p = re.compile(r'\d+')
print(p.findall('one1two2three3four4'))


print("\n**********Finderiter**********")
# finditer(string[, pos[, endpos]]) | re.finditer(pattern, string[, flags]): 
# 搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。 
p = re.compile(r'\d+')
for m in p.finditer('one1two2three3four4'):
	print(m.group())


print("\n**********Sub**********")
# sub(repl, string[, count]) | re.sub(pattern, repl, string[, count]): 
# 使用repl替换string中每一个匹配的子串后返回替换后的字符串。 
# 当repl是一个字符串时，可以使用\id或\g<id>、\g<name>引用分组，但不能使用编号0。 
# 当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。 
# count用于指定最多替换次数，不指定时全部替换。 
p = re.compile(r'(\w+)\s(\w+)')
s = 'i say,hello world!'
print(p.sub(r'\2 \1',s))
def func(m):
	return(m.group(1).title()+' '+m.group(2).title())
print(p.sub(func,s))


print("\n**********Subn**********")
# subn(repl, string[, count]) |re.sub(pattern, repl, string[, count]): 
p = re.compile(r'(\w+)\s(\w+)')
s = 'i say,hello world!'
print(p.subn(r'\2 \1',s))
def func(m):
	return (m.group(1).title()+' '+m.group(2).title())
print(p.subn(func,s))
