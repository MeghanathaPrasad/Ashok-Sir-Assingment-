# 2) Given list, need to find the duplicate number and missing number
#    input: [17,19,18,18,21] output: 18,20(duplciate,missing)
#    input: [28,31,31,29,30] output: 31,32(duplciate,missing)





given_numbers=[28,31,31,29,30,27,30,29]
sorted_order  = set(given_numbers)
result=[[],[]]
temp = min(given_numbers)
while True:
    if given_numbers.count(temp)>1:
        result[0].append(temp)
    if temp not in sorted_order:
        sorted_order.add(temp)
        result[1].append(temp)
    if len(sorted_order)==len(given_numbers):
        break
    temp+=1
print(given_numbers)   
print(temp)