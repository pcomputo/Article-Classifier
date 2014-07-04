import nltk
import itertools
import sys
import random
import string


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
  classes = ('politics', 'accident', 'controversial', 'crime', 'disease', 'disaster', 'terrorism', 'religion', 'adult')
 
  training_set = [
    ('party cheif minister reporter seats government parliament votes center opposing political scams Candidate Bureaucracy citizen citizenship congress lok sabha constable lawsuit senator minister civics constitution democracy right leader mla prime president constables national cheif politics campaign caucus convention delegate demagogue filibuste gerrymander incumbent muckraker pundit alliance constitution embassy judicial legislative tax', classes[0]),
    ('kill survived traffic signal helmet crash midnight drunk fatal shaken unhurt damage escape drove drive direction fatalities wreckage scratches collision brakes sideswiped guardrail skid skidding tailgating drunk reckless accident towed dent bumper insurance totaled',   classes[1]),
    ('sexist racist black people rape kill country gay nightclub lebsian disputant controversy controversial eristic conflict difference polemic polemical controversus ', classes[2]),
    ('assault burglary kidnapping kidnap vandal murderer prosecution rob robbery theif police stole threath rich costly mask crime lead rape murder arrest arson breaking broke abuse trafficking drug fraud hijacking shoplifting smuggling terrorism theft torture vandalism criminal arsonist kamikaze', classes[3]),
    ('Thalessmia medicens disease suffer cure cancer treatment cold fever malaria leprosy ill chronic doctor redness swelling hair loss tenderness swelling rash dermatitis itchy itching acne pimple boil blister burn scar scratch corn callus wart eczema psoriasis dandruff split ends thinning hair hair loss baldness nearsightedness farsightedness astigmatism headache migraine dizziness giddiness vertigo fainting neuralgia meningitis epilepsy convulsions seizure stroke paralysis', classes[4]),
    ('blackout tsunmai earthquake flood hunger death disaster food avalanche cloud dam drought farmer forest fog fatal hurricane arson arsonist avalanche blizzard blow crust cumulonimbus calamity cataclysm catastrophe fire gale tragedy hail hailstrom kamikaze povert uproot', classes[5]),
    ('osama bin laden bomb attack terror strike force dead killed human afghanistan al qaida barricade battle bombard downfall drama authority zone danger blast cyber pakistan', classes[6]),
    ('atheist religion hindu god ganga religious pope church baptism muslim burkha spiritual inspiration buddha deity lord jesus christianity religion service holy fast faith judaism sisterhood ram laxman sita protestant islam jainism Advent alleluia angelic angels announcement astrologers Bethlehem ceremonies creche holy incarnation jerusalem lord miracle prophecy sacred', classes[7]),
    ('NSFW porn xxx honeymoon boobs kiss fuck sex nude belly naked boobs tits penis ass butt threesome', classes[8]),
  ]
  
  tag = []
  stopwords = nltk.corpus.stopwords.words("english")
  #print stopwords
  sentence = sentence.lower()
  exclude = set(string.punctuation)
  sent = ''.join(ch for ch in sentence if ch not in exclude)
  senti = sent.split()
  sent = [x for x in senti if x not in stopwords]

  for i in training_set:
   text = i[0].split()
   lis = list(set(text).intersection(sent)) 
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


