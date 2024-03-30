def Coins(summ,count):
    money = [0, 0, 0, 0]
    if count > summ:
        return 'There is no solution.'
    if count * 25 < summ:
        return 'There is no solution.'
    
    if count * 25 == summ:
        money[0] = count
        return money
    if count * 10 == summ:
        money[1] = count
        return money
    if count * 5 == summ:
        money[2] = count
        return money
    if count == summ:
        money[3] = count
        return money
    
    remaining = summ // 25
    money[0] = summ // 25              
    remaining = summ - remaining * 25   
    money[1] = remaining // 10
    remaining -= (remaining // 10) * 10 # 4, 1, u 7mnacord
    money[2] = remaining // 5           # 4, 1, 1 7 mnac
    remaining -= (remaining // 5) * 5
    money[3] = remaining

    if sum(money) > count:
        return 'There is no solution.'
    if sum(money) == count:
        return money
    
    while sum(money) < count:   # 5 < 10 money = [4, 1, 0, 0]
        if money[0] != 0 and count - sum(money) >= 2:  #
            money[0] -= 1
            money[1] += 2
            money[2] += 1   # money = [3, 3, 1, 0]
        elif money[1] != 0 and count - sum(money) >= 1:
            money[1] -= 1
            money[2] += 2
        elif money[2] != 0 and count - sum(money) >= 4:
            money[2] -= 1
            money[3] += 5
        else:
            return 'There is no solution.'
    if sum(money) == count:
        return money

print(Coins(110,10))