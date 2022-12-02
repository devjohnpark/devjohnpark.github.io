dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}

left_s = dic['*']
right_s = dic['#']
now = dic[4]
left_d = 0
right_d = 0
for a, b, c in zip(left_s , right_s , now):
    left_d += abs(a-c)
    right_d += abs(b-c)
print(left_d ,right_d)