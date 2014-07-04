import unsafe_flags

article = unsafe_flags.get_input()

tags = unsafe_flags.get_tag(article)
print tags

flag = unsafe_flags.is_unsafe(article)
if (flag):
  print "This article has been marked as unsafe!"
else:
  print "This article is safe and can be processed!"
