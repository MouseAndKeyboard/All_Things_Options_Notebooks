from collections.abc import Collection

class OptionPortfolio(Collection):
    def __init__(self):
        self.assetlist = []

    def insert(self, value):
        self.assetlist.append(value)

    def remove(self, value):
        self.assetlist.remove(value)

    def total_cost(self, underlying):
        total_cost = 0
        for asset in self.assetlist:
            # the assets in this asset list should implement the Asset abstract class (defined in Asset.py)
            total_cost += asset.cost(underlying) # depending on whether you have a long or a short the cost function may be constant or changing

        return total_cost

    def total_revenue(self, underlying):
        total_revenue = 0
        for asset in self.assetlist:
            total_revenue += asset.revenue(underlying)
        return total_revenue


    def total_payoff(self, underlying):
        # Logically is:
        # total_payoff(underlying) = total_revenue(underlying) - total_cost(underlying)
        
        total_profit = 0
        for asset in self.assetlist:
            total_profit += asset.profit(underlying)
        return total_profit

    def __contains__(self, value):
        return value in self.assetlist

    def __iter__(self):
        return iter(self.assetlist)

    def __len__(self):
        return len(self.assetlist)
    