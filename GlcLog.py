import pandas as pd
import matplotlib.pyplot as plt

class Log:
    def __init__(self, filePath):
        self.DF = pd.read_csv(filePath, header=1)

        self.DF['Device Timestamp'] = pd.to_datetime(self.DF['Device Timestamp'], format='%d-%m-%Y %H:%M')

    def plotDay(self, date):
        day = self.getDay(date)

        plt.plot(day['Device Timestamp'], day['Historic Glucose mmol/L'])
        plt.plot(day['Device Timestamp'], day['Scan Glucose mmol/L'], '.k', markersize=16)
        plt.show()

    def getDay(self, date):
        end = date + pd.Timedelta(days=1)
        return self.getTimeRange(date, end)

    def getTimeRange(self, start, end):
        timeRange = self.DF[self.DF['Device Timestamp'] > start]
        timeRange = timeRange[timeRange['Device Timestamp'] < end]
        return timeRange


if __name__ == '__main__':
    log = Log(r'C:\Users\Mark\Google Drive\Coding\LibreLink\MarkFomenko_glucose_5-6-2020.csv')
    log.plotDay(pd.to_datetime('2020-06-04'))
