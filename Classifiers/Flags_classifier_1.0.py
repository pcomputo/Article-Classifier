import nltk
import itertools
import sys
import random
 
class Classifier(object):
    def __init__(self, data):
        self.data = data
        self.stopwords = nltk.corpus.stopwords.words("english")
        self.stemmer = nltk.PorterStemmer()
 
    def text_entry(self, example):
        site_text = nltk.clean_html(example[0]).lower()
        original_tokens = itertools.chain.from_iterable(nltk.word_tokenize(w) for w in nltk.sent_tokenize(site_text))
        tokens = original_tokens
        tokens = [w for w in tokens if not w in self.stopwords]
        
        return (tokens, example[1])
 
    def process_all(self, exampleset):
        processed_training_set = [self.text_entry(i) for i in self.data]
        processed_training_set = filter(lambda x: len(x[0]) > 0, processed_training_set) # remove empty crawls
        processed_texts = [i[0] for i in processed_training_set]
        all_words = nltk.FreqDist(itertools.chain.from_iterable(processed_texts))
        #print all_words
        features_to_test = all_words.keys()[:5000]
        self.features_to_test = features_to_test
        featuresets = [(self.doc_features(d), k) for (d,k) in processed_training_set]
       
        return featuresets
 
    def doc_features(self, document):
        features = {}
        for word in self.features_to_test:
            features['contains(%s)' % word] = (word in document)
            #print features
        return features
 
    def build_classifier(self, featuresets):
        cut_point = len(featuresets) / 5
        train_set, test_set = featuresets[cut_point:], featuresets[:cut_point]
        classifier = nltk.NaiveBayesClassifier.train(train_set)
        
        return (classifier, test_set)
 
    def execute(self):
        featuresets = self.process_all(self.data)
        classifier, test_set = self.build_classifier(featuresets)
        self.classifier = classifier
        self.test_classifier(classifier, test_set)
 
    def classify(self, text):
        return self.classifier.classify(self.doc_features(text))
 
    def test_classifier(self, classifier, test_set):
        print nltk.classify.accuracy(classifier, test_set)
        classifier.show_most_informative_features(400)
 
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
 
test_sent = "According to police, the blast took place in the reception area of Jay Hospital in Agra on Saturday, September 17, 2011."
 
if __name__ == '__main__':
    classifier = Classifier(data)
    classifier.execute()
    print "test_sent:",test_sent
    print "tag: %s" % (classifier.classify(test_sent))
    
   

