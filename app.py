import json
global_list = []
class Teacher_Mode:
    def __init__(self, word, answer):
        self.word = word
        self.answer = answer
        global global_list
        self.words = global_list
    
    def inputs(self):
        for i in range(3):
            self.words.append(self.word, self.answer)
    
    def write_to_json(self):
        with open("FlashCards.json", "w") as file:
            json.dump(self.words, file, indent=4)

words=Teacher_Mode(input("Can you input a word?"), input("Can you input an answer for the word?"))
global_list(words.inputs)


    
    
