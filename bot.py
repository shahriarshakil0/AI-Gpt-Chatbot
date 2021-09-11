import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from tts import tts
from nlu import intent_nlu
from weather import weather
from gpt import single_response
import nltk
nltk.download('punkt')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('data.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Bot"
print("Let's chat! (type 'quit' to exit)")
while True:
    # sentence = "do you use credit cards?"
    sentence = input("You: ")
    intent = intent_nlu(sentence)
    gpt_model = single_response(sentence)
    if sentence == "quit":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['data']:
            if tag == intent["tag"]:
                reply = random.choice(intent['responses'])
                print(f"{bot_name}: {reply}")
                tts(reply)

    elif intent == 'weather':
        city = input(f"{bot_name}: In what location do you want to check?\nYou: ")
        temperature = round(weather(city)['main']['temp']-273.15)
        desc = weather(city)['weather'][0]['description']
        hum = weather(city)['main']['humidity']
        wind_spd = weather(city)['wind']['speed']
        print(f"{bot_name}: The current temperature at {city} is {temperature} degree Celsius. Weather is {desc}. The humidity is {hum}% and wind speed is {wind_spd}kph")
        reply = f"The current temperature at {city} is {temperature} degree Celsius. Weather is {desc}. The humidity is {hum}% and wind speed is {wind_spd}kph"
        tts(reply)
    else:
        reply = gpt_model
        print(f"{bot_name}: {reply}")
        tts(reply)