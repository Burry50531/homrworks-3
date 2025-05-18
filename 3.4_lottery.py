import random

def draw_lottery():
    print("7 of 49:", sorted(random.sample(range(1, 50), 7)))
    print("6 of 36:", sorted(random.sample(range(1, 37), 6)))

while True:
    draw_lottery()
