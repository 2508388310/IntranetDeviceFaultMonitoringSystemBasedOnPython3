import re
# s="<re.Match object; span=(91, 94), match='cpe'>"
# s2="username=fff name=z1hangshan url=www.baidu.com password=ddd256"
# #p=re.compile(r'((?:\s)name=(\S)+)')
# p=re.compile(r'span=<(\S)+>')
# iter=p.finditer(s)
# for m in iter:
#   print("m", m.group())
# iter2=p.finditer(s2)
# for m2 in iter:
#   print("m2", m2.group())
# url = "http://www.6mm.cc/uploads/allimg/1306/2-13060F12S3.jpg"
# print(url[0:url.rfind('/', 1) + 1])
import re
s="username=fffname=zangshanaaurl=www.baidu.com password=ddd256"
s2="username=fff name=z1hangshan url=www.baidu.com password=ddd256"
#p=re.compile(r'((?:\s)name=(\S)+)')
p=re.compile(r'(^name=(\S)+)')
iter=p.finditer(s)
for m in iter:
  print("m", m.group())
