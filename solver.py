import numpy as np
from data import Board
import time
import os
from pprint import pprint

board = Board.init()


# Scanning the section for missing numbers, and returns the index

def findMissing(section, all=False) -> list:

    missing = []
    if not all:
        return section.index(0)
    else:
        for pos, route in enumerate(section):
            if not route:
                missing.append(pos)
    return missing

def getRouteHeight(routePos) -> int:

    if routePos <= 2: return 2
    elif routePos <= 5: return 1
    elif routePos <= 8: return 0
    else: return -1

def getRouteWidth(routePos) -> int:

    if routePos in [0, 3, 6]: return 0
    elif routePos in [1, 4, 7]: return 1
    elif routePos in [2, 5, 8]: return 2
    else: return -1

def getHorizontalValues(section, height) -> list:

    values = []

    if height == 0:
        routes = [6, 7, 8]
        for route in routes:
            values.append(board[section][route])
            
    elif height == 1:
        routes = [3, 4, 5]
        for route in routes:
            values.append(board[section][route])

    elif height == 2:
        routes = [0, 1, 2]
        for route in routes:
            values.append(board[section][route])

    return values
    
def getVerticalValues(section, width) -> list:

    values = []

    if width == 0:
        routes = [0, 3, 6]
        for route in routes:
            values.append(board[section][route])
            
    elif width == 1:
        routes = [1, 4, 7]
        for route in routes:
            values.append(board[section][route])

    elif width == 2:
        routes = [2, 5, 8]
        for route in routes:
            values.append(board[section][route])

    return values

def getHorizontalSections(sectionId) -> list:

    a = [0, 1, 2]
    b = [3, 4, 5]
    c = [6, 7,8]

    if sectionId in a: return a
    elif sectionId in b: return b
    elif sectionId in c: return c

def getVerticalSections(sectionId) -> list:

    a = [0, 3, 6]
    b = [1, 4, 7]
    c = [2, 5, 8]

    if sectionId in a: return a
    elif sectionId in b: return b
    elif sectionId in c: return c

def posibilityCheck(sectionId, routePosition) -> list:

    width, height = (getRouteWidth(routePosition), getRouteHeight(routePosition))

    # Collect data for the horozontal side

    horizontalSections = getHorizontalSections(sectionId)
    horizontalValuesOfSections = []
    for section in horizontalSections:
        horizontalValuesOfSections += (getHorizontalValues(section, height))

    # Collect data for the vertical side

    verticalSections = getVerticalSections(sectionId)
    verticalValuesOfSections = []
    for section in verticalSections:
        verticalValuesOfSections += (getVerticalValues(section, width))

    # if horizontal, vertical and section values compined != the same as the for loop number, then append


    posibilities = []

    theArray = board[sectionId] + verticalValuesOfSections + horizontalValuesOfSections

    for i in range(1, 10):
        if i not in theArray:
            posibilities.append(i)

    print("SECTION: {}, ROUTE: {}, hs: {}, hv: {}, vs: {}, vv: {}, POSIBILITIES: {}".format(sectionId, routePosition, horizontalSections, horizontalValuesOfSections, verticalSections, verticalValuesOfSections, posibilities))

    return posibilities

    #X getHorizontalSections and getVerticalSections
    #X getHorizontalValues and getVerticalValues of both sections
    #X check if it is a posibility
    #X if so, append it to a list

ticks = 0
solved = False

while not solved:

    if ticks >= 8:
        solved = True

    for section in range(0, 9):

        missingRoutes = findMissing(board[section], all=True)
        if len(missingRoutes) <= 0:
            ticks += 1
            continue
        else:
            ticks = 0

        sectionPosibilities = []
        sectionPosibilitiesIndexes = []

        for missingRoute in missingRoutes:

            sectionPosibilities.append(posibilityCheck(section, missingRoute))
            sectionPosibilitiesIndexes.append(missingRoute)

        allSectionPosibilities = []
        for array in sectionPosibilities:
            allSectionPosibilities += array

        #X Go through the all posibilities and find a unique one
        #X Find out where the unique code came from in the sectionPosabilities
        #X Find the routeid in sectionPosabilitiesIndexes with the results of the last note

        l = []

        for num in allSectionPosibilities:
            if allSectionPosibilities.count(num) == 1:
                # found a unique posibility
                for a in sectionPosibilities:
                    if num in a:
                        l.append((sectionPosibilitiesIndexes[sectionPosibilities.index(a)], num))

        # draw the numbers

        for route, value in l:
            board[section][route] += value

        os.system("clear")
        pprint(board)
        #time.sleep(0.2)

print("\n")
pprint(board)
