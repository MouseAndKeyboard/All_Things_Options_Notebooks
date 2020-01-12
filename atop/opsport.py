import BinomialOption from './options'

class OptionPortfolio(collections.abc.Collection):
    def __init__(self):
        self.assetlist = []

    def insert(self, value):
        assert isinstance(value, BinomialOption)
        self.assetlist.append(value)

    def remove(self, value):
        assert isinstance(value, BinomialOption)
        self.assetlist.remove(value)

    def calc_graph(self):
        pass

    def __contains__(self, value):
        return value in self.assetlist

    def __iter__(self):
        return iter(self.assetlist)

    def __len__(self):
        return len(self.assetlist)
    