'''f = open("Chapter9/poems.txt")
c=f.read()
if("twinkle" in c):
    print("twinkle is present")
else:
    print("twinkle is not present")
f.close()'''
"""import random


def game():
    print("you are playing game")
    score=random.randint(1,65)
    with open("Chapter9/hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore=int(hiscore)
        else:
            hiscore=0

    print(f"Your Score: {score}")
    if(score>hiscore):
        with open("Chapter9/hiscore.txt","w") as f:
            f.write(str(score))
    return score

game()"""

'''def generateTable(n):
    table = " "
    for i in range (1,11):
        table += f"{n} x {i} = {n*i}\n"

    with open(f"Chapter9/table/tables_{n}.txt","w") as f:
        f.write(table)

for i in range(2,21):
    generateTable(i)'''

words = ["donkey", "bad"]
with open("Chapter9/poems.txt","r") as f:
    content = f.read()
for word in words:
    content= content.replace(word,"#"* len(word))

with open("Chapter9/poems.txt","w") as f:
    f.write(content)