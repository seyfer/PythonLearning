def canDate(age, sex="girl"):
    girlsAge = age/2 + 7
    if (sex != "girl"):
        return 0
    return girlsAge

canDate = canDate(27);
print("can", canDate)

def add(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add(1,2,3,4,5,6,7)

def health(age, apples, cigs):
    answer = (100 - age) + (apples * 1.5) - (cigs * 2)
    print(answer)

data = [27, 20, 0];

health(*data)
