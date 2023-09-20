def uniq(numbers: list) -> list:
    result = []
    for i in numbers:
        if i not in result:
            result.append(i)
    return result

mylist = [1,3,7,2,4,7,12,74,1,4,2]
mylist = uniq(mylist)
print(mylist)