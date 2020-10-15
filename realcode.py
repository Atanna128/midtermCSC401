import doctest

SMALL_SIZE_PRICE = 12
MEDIUM_SIZE_PRICE = 15
LARGE_SIZE_PRICE = 18


def main():
    # value = input("Enter : ")
    # gct(312)
    # alterCase(value)
    # priceTShirt('M', '   \n\n\n    ')
    # benford("MinnesotaLakes.txt")

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


def alterCase(string):
    # only course materials used
    count = 0
    string = string.upper()
    new = list(string)
    for char in new:
        if count % 2:
            new[count] = char.lower()
        count += 1
    string = "".join(new)
    print(string)


def priceTShirt(size, slogan):
    # only course materials used
    slogan_price = 0
    if size == 'S':
        size_price = SMALL_SIZE_PRICE
    elif size == 'M':
        size_price = MEDIUM_SIZE_PRICE
    elif size == 'L':
        size_price = LARGE_SIZE_PRICE
    else:
        return
    for char in slogan:
        if char.islower():
            slogan_price += 0.25
        elif char.isupper():
            slogan_price += 0.3
        elif char == '.' or char == ',' or char == '!' or char == '\'' or char == '\"' or char == '?' or char == ':':
            slogan_price += 0.2
        elif char == ' ' or char == '\n':
            pass
    print(slogan_price + size_price)


def benford(file):
    # only course materials used
    count_digit = 0
    count_total = 0
    f = open("MinnesotaLakes.txt", "r")
    f.readline()
    for line in f:
        count_total += 1
        for char in line:
            if char.isdigit():
                if char == '1':
                    count_digit += 1
                    break
                else:
                    break

    print("count digit = {}".format(count_digit))
    print("count_total = {}".format(count_total))
    print(count_digit/count_total)


main()
