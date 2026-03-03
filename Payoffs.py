from abc import ABC, abstractmethod


class InflationOptionPayoff(ABC):
    @abstractmethod
    def payoff(self, inflation_ratio : float) -> float:
        pass


class CapletsPayoff(InflationOptionPayoff):
    
    def __init__(self, strike:float, notional:float):
        self.k = strike
        self.notional = notional

    def payoff(self, inflation_ratio:float)->float:
        return self.notional * max((inflation_ratio-1) - self.k, 0)

class FloorletPayOff(InflationOptionPayoff):
    
    def __init__(self, strike:float, notional:float):
        self.k = strike
        self.notional = notional

    def payoff(self, inflation_ratio:float)->float:
        return self.notional * max(self.k - (inflation_ratio-1), 0)
    

class CapPayoff:

    def __init__(self, caplets: list[CapletsPayoff]):
        self.caplets = caplets
    
    def payoff(self, inflation_ratios: list[float])->list[float]:
        return [caplet.payoff(inflation_ratio) for caplet, inflation_ratio in zip(self.caplets, inflation_ratios)]
    
class FloorPayoff:

    def __init__(self, floorlets: list[FloorletPayOff]):
        self.floorlets = floorlets
    
    def payoff(self, inflation_ratios: list[float])->list[float]:
        return [floorlet.payoff(inflation_ratio) for floorlet, inflation_ratio in zip(self.floorlets, inflation_ratios)]
    


# %%%%%%%%%% TEST %%%%%%%%%%
if __name__ == "__main__":
    caplet = CapletsPayoff(strike=0.02, notional=1000)
    floorlet = CapletsPayoff(strike=0.01, notional=1000)

    print("Caplet Payoff:", caplet.payoff(1.03))
    print("Floorlet Payoff:", floorlet.payoff(1.03))