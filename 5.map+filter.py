marks=[78,92,34,60,39]
def div(score):
    if score>=80:
        return("Distinction")
    elif score>=60 and score<80:
        return("First Division")
    elif score>=50 and score<60:
        return("Second Division")
    elif score>=40 and score<50:
        return("Third Division")
    else:
        return("Failed")

print(list(map(div,marks)))
# print("Marks:",marks)
# print("Division:",division)

def fail(score):
    return score<40

failed=filter(fail,marks)
print("Failed:",list(failed))
