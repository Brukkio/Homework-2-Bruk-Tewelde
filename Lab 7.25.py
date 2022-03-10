def main():
    change_amount = int(input())
    if change_amount <= 0:
        print('no change')
        return
    dollars = change_amount // 100
    change_amount = change_amount % 100
    quarters = change_amount // 25
    change_amount = change_amount % 25
    dimes = change_amount // 10
    change_amount = change_amount % 10
    nickels = change_amount // 5
    change_amount = change_amount % 5
    pennies = change_amount
    if dollars > 0:
        if dollars == 1:
            print('1 dollar')
        else:
            print('{} dollars'.format(dollars))
    if quarters > 0:
        if quarters == 1:
            print('1 quarter')
        else:
            print('{} quarters'.format(quarters))
    if dimes > 0:
        if dimes == 1:
            print('1 dime')
        else:
            print('{} dimes'.format(dimes))
    if nickels > 0:
        if nickels == 1:
            print('1 nickel')
        else:
            print('{} nickels'.format(nickels))
    if pennies > 0:
        if pennies == 1:
            print('1 penny')
        else:
            print('{} pennies'.format(pennies))


main()
