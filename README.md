# Inflation Option Pricing

## 1. Jarrow–Yildirim Framework

In the Jarrow–Yildirim model, inflation is modeled as a geometric Brownian motion under the risk-neutral measure:

\[
\frac{dI(t)}{I(t)} = \mu_I(t)\,dt + \sigma_I(t)\, dW_t^Q
\]

When pricing inflation caps and floors, the key object is the expected inflation ratio:

\[
\mathbb{E}^{T_i}\!\left[\frac{I(T_i)}{I(T_{i-1})}\right]
\]

A crucial result is that this expectation is **not** equal to the naive forward inflation ratio.  
A **convexity adjustment** appears.

---

## 2. Origin of the Convexity Term

When changing from the risk-neutral measure to the forward measure associated with the nominal zero-coupon bond \( P(t,T_i) \), Girsanov’s theorem modifies the drift of inflation.

If:

- Inflation volatility = \( \sigma_I \)
- Nominal bond volatility = \( \sigma_P \)
- Correlation = \( \rho \)

then the expected ratio becomes:

\[
\mathbb{E}^{T_i}\!\left[\frac{I(T_i)}{I(T_{i-1})}\right]
=
\frac{I(0,T_i)}{I(0,T_{i-1})}
\times
\exp\big(\sigma_I \rho \sigma_P \Delta T\big)
\]

The exponential term:

\[
G = \exp(\sigma_I \rho \sigma_P \Delta T)
\]

is the **convexity adjustment**.

---

## 3. Economic Interpretation

The convexity term arises because:

- Inflation and discounting are stochastic,
- They are correlated,
- The payoff depends exponentially on inflation.

Due to the convexity of the exponential function (Jensen’s inequality), dispersion increases the expectation.

If \( \rho > 0 \), the adjustment is greater than 1.

---

## 4. Key Takeaway

In the Jarrow–Yildirim framework:

> The expected inflation ratio under the forward measure is corrected by a convexity term driven by inflation volatility, nominal rate volatility, and their correlation.

Without volatility or without correlation, the convexity adjustment disappears.