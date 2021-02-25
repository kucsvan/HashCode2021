import sys

class graph:

    def __init__ (self, nodesNumber, distances):
        self.nodes = nodesNumber
        self.distances = distances

    def IsGreen (self, intersectionId, streetId, trafficLights, second):
        intersectionTrafficLights = trafficLights[intersectionId]

        if trafficLights[intersectionId][streetId] == 0:
            return False

        lastTour = second % (sum (intersectionTrafficLights))

        return lastTour - sum (intersectionTrafficLights[:streetId]) >= 0


    def IsUnderJurney (self, begin, end, second):
        return second <= self.distances[begin][end] 


    def IsEndOfTheJourney (self, carIndex, journeyPosition, journey):
        return len (journey[carIndex]) == journeyPosition


    def Simulate (self, journey, seconds, trafficLights, F):
        points = 0

        carsTime = [0] * len (journey)
        carsPosition = [-1] * len (journey)
        carCurrentJurneyPosition = [0] * len (journey)
        carsAtPosition = [[]] * self.nodes
        finishedCars = []

        for s in range (seconds):
            for carIndex in range (len (carCurrentJurneyPosition)):
                if len (journey[carIndex]) > carCurrentJurneyPosition[carIndex]:
                    (begin, end) = journey[carIndex][carCurrentJurneyPosition[carIndex]]

                    if carCurrentJurneyPosition[carIndex] == 0:
                        carsTime[carIndex] = self.distances[begin][end] + 1

                    if self.IsUnderJurney (begin, end, carsTime[carIndex]):
                        carsTime[carIndex] += 1
                    else:
                        if self.IsEndOfTheJourney (carIndex, carCurrentJurneyPosition[carIndex], journey):
                            points += F + (seconds - s)
                        else:
                            if self.IsGreen (end, begin, trafficLights, s):
                                if len (carsAtPosition[end]) == 0 or carsAtPosition[end][0] == carIndex:
                                    carCurrentJurneyPosition[carIndex] += 1
                                    carsTime[carIndex] = 0
                                    if carIndex in carsAtPosition[end]:
                                        carsAtPosition[end].remove (carIndex)
                                else:
                                    carsTime[carIndex] += 1
                            else:
                                if carIndex not in carsAtPosition[end]:
                                    carsAtPosition[end].append (carIndex)
                                carsTime[carIndex] += 1
                else:
                    if carIndex not in finishedCars:
                        finishedCars.append (carIndex)
                        points += F + (seconds - s)

        return points


    def __str__ (self):
        return "Graph\n" + str (self.nodes) + "\n" + str (self.distances) + ""


def main ():
    gr = graph (4, [[sys.maxsize, 1, sys.maxsize, sys.maxsize], [sys.maxsize, sys.maxsize, 3, sys.maxsize], [1, sys.maxsize, sys.maxsize, 2], [sys.maxsize, 1, sys.maxsize, sys.maxsize]])
    journey = [[(2, 0), (0, 1), (1, 2), (2, 3)], [(3, 1), (1, 2), (2, 0)]]
    seconds = sys.maxsize
    trafficLights = [[0, 0, 2, 0], [1, 0, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0]]

    print  (gr.Simulate (journey, 100, trafficLights, 1000))

if __name__ ==  "__main__":
    main ()





# if carsTime[carIndex] >= self.distances[begin][end]:

                
#                 if carsPosition
#                 carsTime[carIndex] += 1
#                 if carsTime[carIndex] == self.distances[begin][end]:
#                     carsPosition[carIndex] = end
#                     carsPreviousTime += self.distances[begin][end]
#                     carsTime[carIndex] = 0
#                     carCurrentJurneyPosition[carIndex] += 1