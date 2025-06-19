from scipy  import stats
from numpy import exp, log, sqrt


def calculate_call_option_price(S, E, T, sigma, rf):

    # calculate d1 and d2
    d1 = (log(S/E) + (rf + 0.5*sigma*sigma)*T)/(sigma*sqrt(T))
    d2 = d1 - sigma*sqrt(T)
    print('The value of d1:', d1)
    print('The value of d2:', d2)

    return S*stats.norm.cdf(d1) - E*exp(-rf * T)*stats.norm.cdf(d2)


def calculate_put_option_price(S, E, T, sigma, rf):

    # calculate d1 and d2
    d1 = (log(S / E) + (rf + 0.5 * sigma * sigma) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    print('The value of d1:', d1)
    print('The value of d2:', d2)

    return -S * stats.norm.cdf(-d1) + E * exp(-rf * T) * stats.norm.cdf(-d2)

if __name__ == '__main__':
    S = 100
    E = 100
    T = 1
    rf = 0.05
    sigma = 0.2
    print('The price of call option is:', calculate_call_option_price(S, E, T, sigma, rf))
    print('The price of put option is:', calculate_put_option_price(S, E, T, sigma, rf))
