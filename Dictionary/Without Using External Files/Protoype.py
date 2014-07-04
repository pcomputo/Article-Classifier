import unsafe

'''Prototype for unsafe.y API'''
article = unsafe.get_input()

tags = unsafe.get_tag(article)
print tags

flag = unsafe.is_unsafe(article)
if (flag):
  print "This article has been marked as unsafe!"
else:
  print "This article is safe and can be processed!"
