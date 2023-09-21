def premium(names: list[str], cash: list[int], percent: list[str]) -> dict[str:float]:
    return {name: money * perc / 100
            for name, money, perc in zip(names, cash, (float(i[:-1]) for i in percent))}

names = ["Andrew", "Bob", "Artur"]
cash = [456, 654, 572]
percent = ["10.25%", "20.55%", "33.35%"]
print(premium(names, cash, percent))