
import re
reIsInt = re.compile('^\d+$')


def sort_values(*args):
    intList = []
    strList = []
    for i in args:
        if(type(i) == int):
            intList.append(i)
        elif reIsInt.match(i):
            intList.append(int(i))
        else:
            strList.append(i)
    intList.sort()
    strList.sort()
    return "\n".join([
        ' '.join(map(str, intList)),
        ' '.join(strList)
    ])


def population(personCount):
    womenCount = (personCount * personCount)
    return personCount + womenCount + personCount * womenCount


def sum_map(map):

    sum = 0
    for key, value in map.items():
        if key.find('s') > -1:
            sum += value

    f = open("summa.txt", "a+")
    f.write(str(sum) + "\n")
    f.close()
    return sum


def key_contains(map):

    sum = 0
    count = 0
    for key, value in map.items():
        if key.find('st') > -1:
            sum += value
            count += 1

    return round(sum/count, 2)
