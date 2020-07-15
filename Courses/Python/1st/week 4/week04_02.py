class Value:
    amount = None

    def __set__(self, instance, value):
        self.amount = value - value * instance.commission

    def __get__(self, instance, owner):
        return self.amount


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission
