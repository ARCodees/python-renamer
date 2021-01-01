import os
lst = os.listdir()
lstf = []
for i in lst:
    if i.endswith(".jpg"):
        lstf.append(i)
# print(lstf)
# for number in range(1,10):
#     print(number)
for number,a in enumerate(lstf):
    os.rename(a,f"{number}.jpg")
print("images renamed")