class Values:
    def __init__(self, name, category, amount, month) -> None:
        self.name = name
        self.category = category
        self.amount = amount
        self.month = month

        def __repr__(self):
            return f"<Value: {self.name}, {self.category}, £{self.amount}, {self.month}>"