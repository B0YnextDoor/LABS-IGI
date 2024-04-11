from matplotlib import pyplot as plt


class PlotDrawer():
    def drawYearPricePlot(self, df):
        ''' Method draws average car price chart depending on year. '''
        years, prices = [], []
        for year in range(1995, 2025):
            cars = df[df['year'] == year]
            if len(cars) > 0:
                years.append(year)
                prices.append(cars['price'].mean())
        plt.figure()
        plt.title('Average car price 1995-2024')
        plt.plot(years, prices, marker='o', markersize=2, linestyle='-')
        plt.xlabel('Years')
        plt.ylabel('Average price')
        plt.savefig('./analysis/year-price.png')

    def drawMileagePricePlot(self, df):
        ''' Method draws average car price chart depending on mileage '''
        mileages, prices = [], []
        for m in range(1, 41):
            cars = df[(df['mileage'] < int(
                1e4*m)) & (df['mileage'] > int(1e4*(m - 1)))]
            if (len(cars) == 0):
                continue
            mileages.append(1e4*m)
            prices.append(cars['price'].mean())
        plt.figure()
        plt.title('Average car price depending on mileage')
        plt.plot(mileages, prices, marker='o', markersize=2, linestyle='-')
        plt.xlabel('Mileages')
        plt.ylabel('Average price')
        plt.savefig('./analysis/mileage-price.png')

    def drawMpgPricePlot(self, df):
        ''' Method draws average car price chart depending on mpg '''
        mpgs, prices = [], []
        for i in range(10, 480, 10):
            cars = df[(df['mpg'] < i) & (df['mpg'] > i - 10)]
            if len(cars) == 0:
                continue
            mpgs.append(i)
            prices.append(cars['price'].mean())
        plt.figure()
        plt.title('Average car price depending on mpg')
        plt.plot(mpgs, prices, marker='o', markersize=2, linestyle='-')
        plt.xlabel('MPG')
        plt.ylabel('Average price')
        plt.savefig('./analysis/mpg-price.png')
