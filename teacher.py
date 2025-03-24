import json
global_list = {}
class Teacher_Mode:
    def __init__(self, word, answer):
        self.word = word
        self.answer = answer
        global global_list
        self.words = global_list
    
    def inputs(self):
        self.words[self.word] = self.answer

num = int(input("How many words/answer would you like to input?"))

for i in range(num):
    words=Teacher_Mode(input("Can you input a word?"), input("Can you input an answer for the word?"))
    words.inputs()

def write_to_json(words):
    with open("FlashCards.json", "w") as file:
        json.dump(words, file, indent=4)
write_to_json(global_list)
    
