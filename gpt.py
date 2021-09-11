import pickle
from tts import tts
import sys
# from termcolor import colored


my_model = pickle.load(open('./Gpt_Model/base_model_small.tar.gz', 'rb'))

a = ['hello']

def single_response(user_input): 
  reply,history = my_model.interact_single(message=user_input,history=a)
  for i in history :
    a.append(i)

  return reply


# print(colored('start chat to bot, want to stop say exit','green'))

# while 1:
    
#     talk = input(colored("you: ",'green'))
#     if talk=='exit':break
#     response = single_response(talk)
#     print(colored("Bot: ",'green'),response)
#     tts(response)

