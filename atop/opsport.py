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




if __name__ == "__main__":
    import numpy as np
    from matplotlib import pyplot as plt
    from atop.options.calloption import CallOption, CallOptionLong
    from atop.options.calloption import PutOptionShort, PutOptionLong

    # Create some options
    Call_1 = CallOption(23.00, 24.00, None, None, None) # I don't know what all the parameters are
    Call_2 = CallOption(23.00, 26.00, None, None, None) # I don't know what all the parameters are
    Call_3 = CallOption(23.00, 28.00, None, None, None) # I don't know what all the parameters are

    # Create your portfolio
    my_portfolio = OptionPortfolio()
    
    # Add options to the portfolio
    my_portfolio.insert(Call_1)
    my_portfolio.insert(Call_2)
    my_portfolio.insert(Call_3)

    # Create an array of 100 points between 0 to 120
    x = np.linspace(0, 120, num=100)
    # Apply the profit function at each underlying value
    y = my_portfolio.total_payoff(x)

    # Plot the profit function for each underlying value
    plt.plot(x, y)

    plt.xlabel('Underlying Value')
    plt.ylabel('Profit')
    plt.legend()
    plt.grid(True)
    plt.show(block = True)