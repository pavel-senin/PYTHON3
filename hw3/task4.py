def backpack(shop: dict[str:int], size: int) -> list[list[str]]:
    pcs, weight = zip(*sorted(shop.items(), key=lambda x: x[1], reverse=True))
    result, temp, temp_w = [], [], 0
    for index, w in enumerate(weight, 0):
        temp_w += w
        temp.append((pcs[index]))
        for index_n, wn in enumerate(weight[index:], index):
            if wn + temp_w <= size:
                temp_w += wn
                temp.append(pcs[index_n])
        result.append(temp)
        temp, temp_w = [], 0
    return result

items = {'Мультитул': 500,
         'Одеяло': 500,
         'Котелок': 1000,
         'Еда': 2500,
         'Вода': 1000,
         'Спички': 100,
         'Палатка': 3000,
         'Мешок': 2000,
         }
load_capacity = 10000
print(backpack(items, load_capacity))