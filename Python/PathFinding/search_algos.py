import math
import random
from levels import level
import pandas as pd
import os

class SearchNode:
    def __init__(self, state, action=-1, prevNode=None):
        self.state = state
        self.action = action
        self.prevNode = prevNode
        self.totalG = 0 # kustannus alusta nykyiseen tilaan
        self.heuristicCost = 0 # Arvioitu kustannus loppuun
    
def traversePath(node, visitFunc):
    if (node == None):
        return # rekursion loppuehto
    traversePath(node.prevNode, visitFunc)
    visitFunc(node)

def dijkstra(agentState, popBest, isGoalFound, branch):
    # lisää alkutila open listiin
    openList = [SearchNode(agentState)]
    closedList = []
    goaledNode = None

    def isInClosedList(node):
        for n in closedList:
            if(node.state == n.state):
                return True #löytyi
        return False #ei löytynyt

    while len(openList) > 0 and goaledNode == None:
        currentNode = popBest(openList)

        # lisää solmu closed listaan
        closedList.append(currentNode)
        if isGoalFound(currentNode):
            goaledNode = currentNode
            continue

        # Laske seuraavat naapurisolmut
        adjacentNodes = branch(currentNode) # kutsu branch funktiota kanditaattien saamiseksi
        for n in adjacentNodes:
            if(isInClosedList(n)):
                continue
            closedList.append(n)
            openList.append(n)  

    return goaledNode, openList, closedList

def searhPathFindInGrid(initialState, endState, isLegalState, level, actions, popBest):

    # maalifunktio:
    def isGoalFound(node):
        return node.state[0] == endState[0] and node.state[1] == endState[1]   
    
    # Suorittaa annetun actionin nykyisestä tilasta eteenpäin
    def makeAction(currentState, actionId):
        deltaAction = actions[actionId]
        newState = []
        for i in range(len(currentState)):
            newState.append(currentState[i]+deltaAction[i])
        return newState

    # Suorittaa actionin nykyiseen tilaan ja tekee uuden solmun
    def stepAction(prevNode, actionId):
        newState = makeAction(prevNode.state, actionId)
        return SearchNode(newState, actionId, prevNode)

    def vectorLen(vec):
        dotProduct = 0
        for value in vec:
            dotProduct += value*value
        return math.sqrt(dotProduct)

    def sub(v1, v2):
        result = []
        for i in range(len(v1)):
            result.append(v1[i] - v2[i])
        return result

    # branch funktio algoritmille
    def getNextNodes(prevNode):
        NextNodes = []
        for actionId in range(len(actions)):
            newNode = stepAction(prevNode, actionId)
            x = prevNode.state[0]
            y = prevNode.state[1]
            levelCost = level[y][x] + 1
            if(isLegalState(newNode.state)):
                #  G-kustannus on edellisten g plus kustannus yhdelle askeleelle:
                newNode.totalG = prevNode.totalG + levelCost*vectorLen(sub(prevNode.state, newNode.state))
                newNode.heuristicCost = int(vectorLen(sub(newNode.state, endState))) #euklidinen pituus
                NextNodes.append(newNode)
        return NextNodes
    
    return dijkstra(initialState, popBest, isGoalFound, getNextNodes) 




#arvotaan lähtöpaikka
def startpoint():
    starts = [[random.randint(1, 63), random.randint(1, 63)] for _ in range(5)]
    start = starts[0]
    return start

#arvotaan maali
def finishpoint():
    finishes = [[random.randint(1, 63), random.randint(1, 63)] for _ in range(5)]
    finish = finishes[0]
    return finish

# actionit taulukoituna: (0 suuntaa)
actions = [[-1, 0], [1, 0],[0, -1], [0, 1]]
#actions = [[-1, 0], [1, 0],[0, -1], [0, 1], [-1, -1], [1, 1], [1, -1], [-1, 1]]

# Laillisen tilan tarkastusfunktio:
def isLegalState(state):
    x = state[0]
    y = state[1]
    if( x < 0 or y < 0):
        return False
    if( y >= len(level) or x >= len(level[y]) ):
        return False
    return level[y][x] < 9 #estetään seinien läpi kävely

def printpic(putPixel, goaledNode, printMap, openList):

    def printNodeOnLevel(node):
        putPixel(level, node.state, 11)

    def printOpenNodeOnLevel(node):
        putPixel(level, node.state, 10)

    traversePath(goaledNode, printNodeOnLevel)

    for openNode in openList:
        printOpenNodeOnLevel(openNode)
    printMap(level)

def dataTallennus(openList, closedList, goaledNode, name, suoritusaika):
    solmut = len(openList) + len(closedList)
    #if goaledNode == None:
        #goaledNode = SearchNode(state=[0, 0]) #lisäys!!!!!!!!!!
    kustannus = str(goaledNode.totalG)

    # Oletetaan, että meillä on DataFrame
    data = {
        "nimi": [name],
        "suoritusaika": [suoritusaika],
        "kustannus": [kustannus],
        "solmut": [solmut]
    }

    df = pd.DataFrame(data)

    file_path = "testi.csv"
    if not os.path.exists(file_path):
        # Jos tiedostoa ei ole, luodaan se ja lisätään otsikot
        df.to_csv(file_path, index=False)
    else:
        # Jos tiedosto on olemassa, lisätään tiedot ilman otsikoita
        df.to_csv(file_path, mode='a', index=False, header=False)

    print(df[["nimi", "suoritusaika", "kustannus", "solmut"]])

# Leveyssuunnatun haun kustannusfunktio:    
def popBestG(openList):
    # oleta ensimmäinen pienimmäksi
    currentNode = openList[0]
    minIndex = 0
    minG = currentNode.totalG
    for index, item in enumerate(openList):
        itemG = item.totalG
        if( itemG < minG):
            currentNode = item
            minIndex = index
            minG = itemG
    openList.pop(minIndex)
    return currentNode

# Ahneen haun kustannusfunktio:
def popBestH(openList):
    # oleta ensimmäinen pienimmäksi
    currentNode = openList[0]
    minIndex = 0
    minH = currentNode.heuristicCost
    for index, item in enumerate(openList):
        itemH = item.heuristicCost
        if( itemH < minH):
            currentNode = item
            minIndex = index
            minH = itemH
    openList.pop(minIndex)
    return currentNode

# A* haun kustannusfunktio:
k = 1.0
def popBestF(openList):
    # oleta ensimmäinen pienimmäksi
    currentNode = openList[0]
    minIndex = 0
    name = "A*"
    # F = G + k*H
    minF = currentNode.totalG + k*currentNode.heuristicCost
    for index, item in enumerate(openList):
        itemF = item.totalG + k*item.heuristicCost
        if( itemF < minF):
            currentNode = item
            minIndex = index
            minF = itemF
    openList.pop(minIndex)
    return currentNode

"""
def zero():
    goaledNode = SearchNode(state=[0, 0])  # Initialize with a default state
    goaledNode.totalG = 0
    return goaledNode
"""