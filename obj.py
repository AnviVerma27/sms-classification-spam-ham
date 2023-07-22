import nltk
nltk.download('stopwords')

import string
from nltk.corpus import stopwords

class PreProcessText(object):
    def __init__(self):
        pass
    
    def __remove_punctuation(self, text):
        message = []
        for x in text:
            if x in string.punctuation:
                pass
            else:
                message.append(x)
        message = ''.join(message)
        return message
    
    def __remove_stopwords(self, text):
        words= []
        for x in text.split():
            if x.lower() in stopwords.words('english'):
                pass
            else:
                words.append(x)
        return words    
    
    def token_words(self,text=''):
        message = self.__remove_punctuation(text)
        words = self.__remove_stopwords(message)
        return words


