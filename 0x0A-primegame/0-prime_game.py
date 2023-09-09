#!/usr/bin/python3
""" Solution to  prime game question """

def isWinner(x, nums):
    """ A function that checks for a winner in the game"""
    if not nums or x < 1:
        return None
    highest_num = max(nums)

    filt = [True for _ in range(max(highest_num + 1, 2))]
    for i in range(2, int(pow(highest_num, 0.5)) + 1):
        if not filt[i]:
            continue
        for j in range(i * i, highest_num + 1, i):
            filt[j] = False
    filt[0] = filt[1] = False
    y = 0
    for i in range(len(filt)):
        if filt[i]:
            y += 1
        filt[i] = y
    player1 = 0
    for x in nums:
        player1 += filt[x] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
