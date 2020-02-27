
class Column:

    def __init__(self, name: str, data: list, table_name: str):
        self.table_name = table_name
        self.name = name
        self.data = list(filter(lambda d: d != '', data))  # remove the NaN values
        self.size = len(data)

    @property
    def long_name(self):
        return self.table_name, self.name