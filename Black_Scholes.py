import numpy as np
from scipy.stats import norm
import argparse

class BlackScholesModel:
    def __init__(self, underlying_spot_price, strike_price, days_to_maturity, risk_free_rate, sigma):
        self.S = underlying_spot_price
        self.K = strike_price
        self.T = days_to_maturity / 365
        self.r = risk_free_rate
        self.sigma = sigma

    def calculate_call_option_price(self):
        d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) / (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)
        return self.S * norm.cdf(d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(d2)

    def calculate_put_option_price(self):
        d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) / (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)
        return self.K * np.exp(-self.r * self.T) * norm.cdf(-d2) - self.S * norm.cdf(-d1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Black-Scholes European Option Pricing')
    parser.add_argument('--spot', type=float, required=True, help='Current underlying price')
    parser.add_argument('--strike', type=float, required=True, help='Option strike price')
    parser.add_argument('--days', type=int, required=True, help='Days until expiration')
    parser.add_argument('--rate', type=float, required=True, help='Annual risk-free rate (decimal)')
    parser.add_argument('--vol', type=float, required=True, help='Annual volatility (decimal)')
    
    args = parser.parse_args()
    
    pricer = BlackScholesModel(
        underlying_spot_price=args.spot,
        strike_price=args.strike,
        days_to_maturity=args.days,
        risk_free_rate=args.rate,
        sigma=args.vol
    )
    
    print(f"Call Price: {pricer.calculate_call_option_price():.4f}")
    print(f"Put Price: {pricer.calculate_put_option_price():.4f}")
