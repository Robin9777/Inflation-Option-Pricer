from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List
from DATA import REAL, NOMINAUX, MATURITIES


@dataclass(slots=True)
class Curve(ABC):
    maturities: List[float] = field(default_factory=list)
    rates: List[float] = field(default_factory=list)

    @abstractmethod
    def __post_init__(self):
        """Post-init must be defined in subclasses."""
        pass

    def forward_rates(self) -> List[float]:
        """Compute forward rates from the spot curve."""
        fwd = [0.0] * len(self.rates)
        for i, m in enumerate(self.maturities):
            if i == 0:
                fwd[i] = self.rates[i]
            else:
                fwd[i] = (self.rates[i]*m - self.rates[i-1]*self.maturities[i-1]) / (m - self.maturities[i-1])
        return fwd


# =================== SPOT CURVES ===================
@dataclass(slots=True)
class NominalCurve(Curve):
    maturities: List[float] = field(default_factory=lambda: MATURITIES.copy())
    rates: List[float] = field(default_factory=lambda: NOMINAUX.copy())

    def __post_init__(self):
        assert len(self.maturities) == len(self.rates), "Maturities and rates must match"


@dataclass(slots=True)
class RealCurve(Curve):
    maturities: List[float] = field(default_factory=lambda: MATURITIES.copy())
    rates: List[float] = field(default_factory=lambda: REAL.copy())

    def __post_init__(self):
        assert len(self.maturities) == len(self.rates), "Maturities and rates must match"


@dataclass(slots=True)
class BreakevenCurve(Curve):
    maturities: List[float] = field(default_factory=lambda: MATURITIES.copy())
    rates: List[float] = field(default_factory=list)

    def __post_init__(self):
        self.rates = [
            round(((n/100 + 1) / (r/100 + 1) - 1)*100, 2) 
            for n, r in zip(NOMINAUX, REAL)
        ]
        assert len(self.maturities) == len(self.rates), "Maturities and rates must match"


# =================== FORWARD CURVES ===================
@dataclass(slots=True)
class ForwardNominalCurve(Curve):
    maturities: List[float] = field(default_factory=lambda: MATURITIES.copy())
    rates: List[float] = field(default_factory=list)

    def __post_init__(self):
        self.rates = NominalCurve().forward_rates()


@dataclass(slots=True)
class ForwardRealCurve(Curve):
    maturities: List[float] = field(default_factory=lambda: MATURITIES.copy())
    rates: List[float] = field(default_factory=list)

    def __post_init__(self):
        self.rates = RealCurve().forward_rates()


@dataclass(slots=True)
class ForwardBreakevenCurve(Curve):
    maturities: List[float] = field(default_factory=lambda: MATURITIES.copy())
    rates: List[float] = field(default_factory=list)

    def __post_init__(self):
        self.rates = BreakevenCurve().forward_rates()


# =================== TEST ===================
if __name__ == "__main__":
    print("Spot Curves:")
    for c in [NominalCurve(), RealCurve(), BreakevenCurve()]:
        print(c)

    print("\nForward Curves:")
    for f in [ForwardNominalCurve(), ForwardRealCurve(), ForwardBreakevenCurve()]:
        print(f)