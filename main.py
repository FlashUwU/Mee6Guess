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

dict_data: dict[float, list[int]] = {}
list_data = [0]*number_of_piece
base_under = 100 / number_of_piece

for answer in notes["answers"]:
    answer = int(answer)
    
    bu = base_under
    for index in range(number_of_piece):
        if answer <= bu:
            list_data[index] += 1

            try: dict_data[bu].append(answer)
            except: dict_data[bu] = [answer]
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

落點統計：{list_data}
分佈圖：{dict(sorted(dict_data.items()))}""")