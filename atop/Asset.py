from abc import ABC, abstractmethod

class Asset(ABC):
    
    @abstractmethod
    def payoff(self):
        pass