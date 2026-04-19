'''from typing import Tuple
person: Tuple[str, int]= ("alice",23)
'''
# exception handling
try:
    a = int(input("ENter a  number :"))
    print(a)
except Exception as e:
    print(e)
else:
    print("you enetered number")

finally:
    print("hey good")