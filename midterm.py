import doctest

def main():
    value = input("Enter : ")
    gct(value)

def gct(num):
    # only course materials used
    num = int(num)
    gallons = num // 256
    cups = (num - gallons * 256) // 16
    tablespoons = num - gallons * 256 - cups * 16
    gallons = gallons.__str__()
    cups = cups.__str__()
    tablespoons = tablespoons.__str__()
    if int(gallons) < 10:
        gallons = '0' + gallons
    if int(cups) < 10:
        cups = '0' + cups
    if int(tablespoons) < 10:
        tablespoons = '0' + tablespoons
    result = gallons + 'g,' + cups.__str__() + 'c,' + tablespoons.__str__() + 't'
    print(result)


main()
