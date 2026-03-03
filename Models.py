from dataclasses import dataclass, field
import math

@dataclass(slots=True)
class InflationBlackModel:

    rho: float = 0.5
    sigma_inflation: float = 0.01
    sigma_nominal: float = 0.02

    def _convexity_adjustment(self, deltaT: float) -> float:
        return math.exp(self.sigma_inflation * self.sigma_nominal * self.rho * deltaT)