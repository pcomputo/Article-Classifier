import glob
import os
import nltk
import string
import itertools
import sys
import random
import string

"""API for finding the unsafe flags"""

'''Please specify the path in which the folder TagFiles will be stored'''
os.chdir("/home/pooja/Documents/Test/FileUsage/TagFiles")
data = []
for file in glob.glob("*.txt"):
   fileList = [word for line in open(file, 'r') for word in line.split()]
   words = ' '.join(fileList)
   data.append((words,file[:-4]))
 

def get_input():  
  """ 
  Takes the input in the form of string from user. 
  Returns it.
  """
  sentence = input("Enter the article: ")
  return sentence


def get_tag(sentence):
  """
  Returns a list of all the unsafe flags
  if any else returns an empty list.
  Takes the article as a paramter
  """
  tag = []
  stopwords = nltk.corpus.stopwords.words("english")
  
  sentence = sentence.lower()
  exclude = set(string.punctuation)
  sent = ''.join(ch for ch in sentence if ch not in exclude)
  senti = sent.split()
  sent = [x for x in senti if x not in stopwords]

  for i in data:
   text = i[0].split()
   lis = list(set(sent).intersection(text)) 
   if lis == []:
     pass
   else:
     tag.append(i[1])
  
  return tag


def is_unsafe(sentence):
  """
  Returns a bool value of whether the article is safe
  or unsafe
  True for unsafe
  """
  tags = get_tag(sentence)
  if tags == []:
    return False
  else:
    return True


