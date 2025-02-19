import json

# manually update once got daily income
daily_income = 144


with open("notes.json", "r") as f:
    notes: dict[str, list] = json.loads(f.read())

earned = 0
for amount in notes["earned"]:
    earned += amount

x = 2
lock = -daily_income//x

risky_chop = 50
number_of_piece = 10
weights: dict[int, int] = {} # Answer: Frequency

data = [0]*number_of_piece
base_under = 100 / number_of_piece

for answer in notes["answers"]:
    answer = int(answer)
    
    bu = base_under
    for index in range(number_of_piece):
        if answer <= bu:
            data[index] += 1
            break
        
        bu += base_under

#     try:
#         weights[answer] += 1
#     except:
#         weights[answer] = 1

# sum_weight = len(notes["answers"])

print(f"""=============RESULT=============
鎖定金額: {lock}
共賺了：{earned}

落點統計：{data}""")