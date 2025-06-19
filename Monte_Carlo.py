import numpy as np

class OptionPricing:

    def __init__(self, s0, E, T, sigma, rf, iterations):
        self.s0 = s0
        self.E = E
        self.T = T
        self.sigma = sigma
        self.rf = rf
        self.iterations = iterations


    def call_option_simulation(self):
        #Creating a option data
        option_data = np.zeros([self.iterations, 2])

        #creating a normally distributed random variable
        rand = np.random.normal(0, 1, self.iterations)

        #Calculating Stock Prices
        stock_prices = self.s0*np.exp((self.rf - 0.5 * self.sigma**2) + self.sigma*rand)

        #adding it to option data
        option_data[:, 1] = stock_prices-self.E

        #Calculating avarage value of max(S-E, 0)
        avarage = np.sum(np.amax(option_data, axis=1)) / float(self.iterations)

        #we have to return the present value of this average as the price
        return avarage*np.exp(-self.rf*self.T)

    def put_option_simulation(self):
        #Creating a option data
        option_data = np.zeros([self.iterations, 2])

        #creating a normally distributed random variable
        rand = np.random.normal(0, 1, self.iterations)

        #Calculating Stock Prices
        stock_prices = self.s0*np.exp((self.rf - 0.5 * self.sigma**2) + self.sigma*rand)

        #adding it to option data
        option_data[:, 1] = self.E - stock_prices

        #Calculating avarage value of max(S-E, 0)
        avarage = np.sum(np.amax(option_data, axis=1)) / float(self.iterations)

        #we have to return the present value of this average as the price
        return avarage*np.exp(-self.rf*self.T)


if __name__ == '__main__':

    model = OptionPricing(100, 100, 1, 0.2, 0.05, 100000)
    print('The price of the call option :%.2f'%model.call_option_simulation())
    print('The price of the put option :%.2f'%model.put_option_simulation())
