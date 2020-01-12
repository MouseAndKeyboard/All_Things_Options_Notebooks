from abc import ABC, abstractmethod

class Asset(ABC):

    @abstractmethod
    def payoff(self):
        # returns a payoff function/line
        pass