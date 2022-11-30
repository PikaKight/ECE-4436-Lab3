import matplotlib.pyplot as plt
import csv


def getData(path):

    x = []
    y = []

    with open(path, newline='') as csvfile:

        hasHeader = csv.Sniffer().has_header(csvfile.read(512))
        csvfile.seek(0)

        data = csv.reader(csvfile, delimiter=',')

        if hasHeader:
            next(data)

        for row in data:
            if row[6].find('Win=') == -1:
                continue

            time = (float)(row[1])
            winSize = (int)(row[6][row[6].find('Win=')+4:row[6].find('Len=')])

            x.append(time)
            y.append(winSize)

        return (x, y)


def plotData(dataSet, percentLost):

    time, winSize = dataSet

    plt.plot(time, winSize)
    plt.xlabel('Time (sec)')
    plt.ylabel('Window Size')

    plt.title(f'Window Size vs Time of a TCP Connection of {percentLost}%')

    plt.show()


plotData(getData('csv/h1'), 10)
plotData(getData('csv/h3'), 1)
