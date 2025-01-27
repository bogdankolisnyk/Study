class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        if min_value > max_value:
            raise ValueError("Мінімальне значення не може бути більше максимального.")

        self.current = current
        self.min_value = min_value
        self.max_value = max_value

        if not (self.min_value <= self.current <= self.max_value):
            raise ValueError("Початкове значення виходить за межі допустимого діапазону")

    def set_current(self, start):
        if self.min_value <= start <= self.max_value:
            self.current = start
        else:
            raise ValueError(
                f"Початкове значення {start} виходить за межі допустимого діапазону [{self.min_value}, {self.max_value}]")

    def set_max(self, max_max):
        if max_max >= self.min_value:
            self.max_value = max_max
        else:
            raise ValueError(
                f"Максимальне значення {max_max} повинно бути більше або рівне мінімальному значенню {self.min_value}.")

    def set_min(self, min_min):
        if min_min <= self.max_value:
            self.min_value = min_min
        else:
            raise ValueError(
                f"Мінімальне значення {min_min} повинно бути менше або рівне максимальному значенню {self.max_value}.")

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError(f"Досягнуто максимуму {self.max_value}. Неможливо збільшити.")
        self.current += 1

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError(f"Досягнуто мінімуму {self.min_value}. Неможливо зменшити.")
        self.current -= 1

    def get_current(self):
        return self.current

counter = Counter()
counter.set_current(7)

counter.step_up()
counter.step_up()
counter.step_up()

assert counter.get_current() == 10, 'Test1'

try:
    counter.step_up()
except ValueError as e:
    print(e)
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()

assert counter.get_current() == 7, 'Test3'

try:
    counter.step_down()
except ValueError as e:
    print(e)
assert counter.get_current() == 7, 'Test4'
