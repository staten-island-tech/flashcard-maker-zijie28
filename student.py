import json
flash_cards = open("./FlashCards.json", encoding="utf8")
data = json.load(flash_cards)
correct_num=0
streak=0
print(data)
for word, answer in data.items():
    ans = input(f"What does {word} mean?")
    if ans.lower() == answer.lower():
        print("Correct!")
        streak+=1
        correct_num+=1
    else:
        print("Incorrect!")
        streak=0
print(f"You got {correct_num} correct!")
print(f"You got a streak of {streak}!")
if streak > len(data)/2:
    print("Extra points of 5")
    correct_num+=5
print(f"You got {correct_num} points!")