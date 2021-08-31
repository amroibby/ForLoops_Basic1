# # # 1.Basic
# # for 0-150
# # for x in range(151):
# #   print(x)

# # # 2. Multiples of Five
# # x = range(5, 1001, 5)
# # for n in x:
# #   print(n)


# # #3. Counting the Dojo Way
# # for x in range(1, 101, 1):
# #     if x % 10 == 0:
# #         print("Coding Dojo")
# #     elif x % 5 == 0:
# #         print("Coding")
# #     else:
# #         print(x)

# # # 4.Whoa. That Sucker's Huge
# # x = 0
# # for add in range(1, 5000001, 2):
# #     x = x + add

# # print(x)

# # 5. Countdown By Fours
# for x in range(2018,0,-4):
#     print(x)

# 6. Flexible Counter

lownum = int(input('num1:'))
highnum = int(input('num2:'))
mult = int(input('num3:'))
for x in range(lownum,highnum + 1,1):
    if x % mult == 0:
        print(x)
