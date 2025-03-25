#if total bill 500, 10% discount, if 1000 20% discount, 2000 30% discount take bill and print final price after discount
bill=float(input('What is the bill cost?'))
def billing(bill):
    if(bill>500 and bill<=1000):
        total=bill-(0.1*bill)
        print(total)
    elif(bill>1000 and bill<=2000):
        total=bill-(0.2*bill)
        print(total)
    elif(bill>2000):
        total=bill-(0.3*bill)
        print(total)
    else:
        print(bill)
billing(bill)