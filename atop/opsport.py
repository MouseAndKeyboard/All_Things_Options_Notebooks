import BinomialOption from './options'

class OptionPortfolio(collections.abc.Collection):
    def __init__(self):
        self.assetlist = []

    def insert(self, value):
        self.assetlist.append(value)

    def remove(self, value):
        self.assetlist.remove(value)

    def total_payoff(self):
        total_payoff = plt.axhline(y=0)
        for asset in self.assetlist:
            # the assets in this asset list should implement the Asset abstract class (defined in Asset.py)
            total_payoff += asset.payoff()

        return total_payoff

    def __contains__(self, value):
        return value in self.assetlist

    def __iter__(self):
        return iter(self.assetlist)

    def __len__(self):
        return len(self.assetlist)
    