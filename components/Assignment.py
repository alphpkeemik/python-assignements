
def sort_values(*args):
    intList = []
    strList = []
    for i in args:
        if(type(i) == int):
            intList.append(i)
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
