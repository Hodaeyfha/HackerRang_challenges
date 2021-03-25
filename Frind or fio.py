
def friend(x):
    #Code
    answer = []
    
    for j in x:
        if len(j) == 4:
            answer.append(j)
    return answer

print(friend(["Ryan", "Kieran", "Mark"]))
