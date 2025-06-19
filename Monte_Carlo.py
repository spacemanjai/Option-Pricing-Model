import numpy as np
import matplotlib.pyplot as plt
import argparse

class MonteCarloPricing:
    def __init__(self, underlying_spot_price, strike_price, days_to_maturity, risk_free_rate, sigma, number_of_simulations):
        self.S_0 = underlying_spot_price
        self.K = strike_price
        self.T = days_to_maturity / 365
        self.r = risk_free_rate
        self.sigma = sigma
        self.N = number_of_simulations
        self.num_of_steps = days_to_maturity
        self.dt = self.T / self.num_of_steps
        self.simulation_results_S = None

    def simulate_prices(self):
        np.random.seed(20)
        S = np.zeros((self.num_of_steps, self.N))
        S[0] = self.S_0
        for t in range(1, self.num_of_steps):
            Z = np.random.standard_normal(self.N)
            S[t] = S[t - 1] * np.exp((self.r - 0.5 * self.sigma ** 2) * self.dt + 
                                     (self.sigma * np.sqrt(self.dt) * Z))
        self.simulation_results_S = S

    def calculate_call_option_price(self):
        if self.simulation_results_S is None:
            self.simulate_prices()
        return np.exp(-self.r * self.T) * np.mean(np.maximum(self.simulation_results_S[-1] - self.K, 0))

    def calculate_put_option_price(self):
        if self.simulation_results_S is None:
            self.simulate_prices()
        return np.exp(-self.r * self.T) * np.mean(np.maximum(self.K - self.simulation_results_S[-1], 0))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Monte Carlo European Option Pricing')
    parser.add_argument('--spot', type=float, required=True, help='Current underlying price')
    parser.add_argument('--strike', type=float, required=True, help='Option strike price')
    parser.add_argument('--days', type=int, required=True, help='Days until expiration')
    parser.add_argument('--rate', type=float, required=True, help='Annual risk-free rate (decimal)')
    parser.add_argument('--vol', type=float, required=True, help='Annual volatility (decimal)')
    parser.add_argument('--sims', type=int, default=10000, help='Number of simulations (default: 10000)')
    
    args = parser.parse_args()
    
    pricer = MonteCarloPricing(
        underlying_spot_price=args.spot,
        strike_price=args.strike,
        days_to_maturity=args.days,
        risk_free_rate=args.rate,
        sigma=args.vol,
        number_of_simulations=args.sims
    )
    
    print(f"Call Price: {pricer.calculate_call_option_price():.4f}")
    print(f"Put Price: {pricer.calculate_put_option_price():.4f}")
