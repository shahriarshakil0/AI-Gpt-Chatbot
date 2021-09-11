import numpy as np
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences

class IntentClassifier:
    def __init__(self,classes,model,tokenizer,label_encoder):
        self.classes = classes
        self.classifier = model
        self.tokenizer = tokenizer
        self.label_encoder = label_encoder

    def get_intent(self,text):
        self.text = [text]
        self.test_keras = self.tokenizer.texts_to_sequences(self.text)
        self.test_keras_sequence = pad_sequences(self.test_keras, maxlen=16, padding='post')
        self.pred = self.classifier.predict(self.test_keras_sequence)
        return label_encoder.inverse_transform(np.argmax(self.pred,1))[0]

import pickle
from tensorflow.python.keras.models import load_model


model = load_model('./Nlu_Model/model2.h5')
with open('./Nlu_Model/classes.pkl','rb') as file:
    classes = pickle.load(file)
with open('./Nlu_Model/tokenizer.pkl','rb') as file:
    tokenizer = pickle.load(file)
with open('./Nlu_Model/label_encoder.pkl','rb') as file:
    label_encoder = pickle.load(file)
nlu = IntentClassifier(classes,model,tokenizer,label_encoder)

def intent_nlu(text):
    # text = input("enter your text to find intent: ")
    intent = nlu.get_intent(text)
    return intent
# print(intent())