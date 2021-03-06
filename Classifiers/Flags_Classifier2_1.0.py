from nltk import NaiveBayesClassifier as nbc
from nltk.tokenize import word_tokenize
from itertools import chain

classes = ('politics', 'accident', 'controversial', 'crime', 'disaster', 'disease', 'terrorism', 'religion', 'adult')
 
data = [
    ('party cheif minister reporter seats government parliament votes center opposing political scams', classes[0]),
    ('kill survived traffic signal helmet crash midnight drunk', classes[1]),
    ('sexist racist black people rape kill country gay lebsian', classes[2]),
    ('rob robbery theif police stole threath rich costly mask crime lead', classes[3]),
    ('Tsunmai earthquake flood hunger death disaster food', classes[4]),
    ('Thalessmia medicens disease suffer cure cancer treatment', classes[5]),
    ('osama bin laden bomb attack terror strike force dead killed human afghanistan al quida', classes[6]),
    ('atheist religion hindu god ganga religious pope church baptism muslim burkha', classes[7]),
    ('kiss fuck sex nude belly naked boobs tits penis ass butt', classes[8]),
    ('Candidate Bureaucracy citizen citizenship congress lok sabha constable lawsuit senator minister', classes[0]),
    ('civics constitution democracy right leader MLA prime president constables national cheif politics', classes[0]),
    ('fatal shaken unhurt damage escape drove drive direction', classes[1]),
    ('disputant controversy controversial eristic conflict difference lesbian', classes[2]),
    ('assault burglary kidnapping kidnap vandal murderer prosecution', classes[3]),
    ('avalanche cloud dam drought farmer forest fog fatal hurricane', classes[4]),
    ('cold fever malaria leprosy ill chronic doctor redness swelling hair loss', classes[5]),
    ('barricade battle bombard downfall drama authority zone danger', classes[6]),
    ('spiritual inspiration buddha deity lord jesus christianity religion service holy fast', classes[7]),
    ('NSFW porn xxx honeymoon boobs', classes[8])
]


vocabulary = set(chain(*[word_tokenize(i[0].lower()) for i in data]))

feature_set = [({i:(i in word_tokenize(sentence.lower())) for i in vocabulary},tag) for sentence, tag in data]

classifier = nbc.train(feature_set)

test_sentence = "According to police, the blast took place in the reception area of Jay Hospital in Agra on Saturday, September 17, 2011."
featurized_test_sentence =  {i:(i in word_tokenize(test_sentence.lower())) for i in vocabulary}

print "test_sent:",test_sentence
print "tag:",classifier.classify(featurized_test_sentence)
