import pandas as pd
from sys import maxsize
from analysis.plotDrawer import PlotDrawer


class DataAnalisys(PlotDrawer):
    def __init__(self, path: str = './data.csv') -> None:
        ''' Inits class object. '''
        self.df = pd.read_csv(path)

    def __call__(self) -> None:
        ''' Method runs class methods. '''
        self.getInfo()
        print('Dataset analisys:\n')
        self.getYearDifference()
        self.getMileageDifference()
        self.getAvgMpg()
        self.drawYearPricePlot(self.df)
        self.drawMileagePricePlot(self.df)
        self.drawMpgPricePlot(self.df)

    def getInfo(self) -> None:
        ''' Method returns dataset info. '''
        print('Dataset:')
        print(self.df.info())
        print(self.df)

    def getAllModels(self, model: str, year: int = 1970, price: int = maxsize, fuelType: str = 'Petrol') -> None:
        ''' Method returns all cars satisfying release year (`year`), max price (`price`) & fuel type (`fuelType`). '''
        cars = self.df[(self.df['model'] == model) & (self.df['year'] >= year) &
                       (self.df['price'] <= price) & (self.df['fuelType'] == fuelType)]
        print(cars)

    def getAvgPrice(self, yearStart: int = 1970, yearEnd: int = 2024) -> float:
        ''' Method returns price mean of cars released between `yearStart` & `yearEnd`. '''
        cars = self.df[(self.df['year'] <= yearEnd) &
                       (self.df['year'] >= yearStart)]
        return cars['price'].mean()

    def getMedianTax(self) -> float:
        ''' Method returns median car tax. '''
        return self.df['tax'].median()

    def getAvgMpg(self) -> None:
        ''' Method compares car\'s MPG depending on tax. '''
        print('MPG compare depending on tax:')
        tax = self.getMedianTax()
        print(f'Average tax: {tax}')
        print(
            f'Average MPG of cars with tax >= {tax}: {self.df[self.df["tax"] >= tax]["mpg"].mean():.2f}')
        print(
            f'Average MPG of cars with tax < {tax}: {self.df[self.df["tax"] < tax]["mpg"].mean():.2f}\n')

    def getYearDifference(self, year: int = 2019):
        ''' Method compares car\'s price depending on release year. '''
        print('Price compare depending on release year:')
        p1, p2 = self.getAvgPrice(
            yearEnd=year), self.getAvgPrice(yearStart=year)
        print(f'Average price before {year}:  ${p1:,.0f}')
        print(f'Average price after {year}:  ${p2:,.0f}')
        print(f'Ratio (after {year} / before {year}): {p2/p1:.2f}\n')

    def getMileageDifference(self):
        ''' Method compares car\'s price depending on mileage'''
        print('Price compare depending on car mileage:')
        maxMil = self.df.iloc[self.df['mileage'].idxmax()]
        print('Max mileage car:')
        self.printModelInfo(maxMil)
        minMil = self.df.iloc[self.df['mileage'].idxmin()]
        print('Min mileage car:')
        self.printModelInfo(minMil)
        print(
            f"Price difference: {minMil['price']} - {maxMil['price']} = {minMil['price'] - maxMil['price']}\n")

    def printModelInfo(self, car) -> None:
        ''' Method returns car info. '''
        print(f'Model: {car["model"]}')
        print(f'Year: {car["year"]}')
        print(f'Price: {car["price"]}')
        print(f'Transmission: {car["transmission"]}')
        print(f'Mileage: {car["mileage"]}')
        print(f'FuelType: {car["fuelType"]}')
        print(f'Tax: {car["tax"]}')
        print(f'MPG: {car["mpg"]}')
        print(f'EngineSize: {car["engineSize"]}')
        print(f'Manufacturer: {car["Manufacturer"]}\n')
