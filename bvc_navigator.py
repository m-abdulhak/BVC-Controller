#!/usr/bin/env python
from __future__ import division
from math import sqrt, atan2, pi
from utils.angles import get_smallest_signed_angular_difference
from utils.geometry import *
from execute import execute_with_three_pi

class BvcNavigator:
    def __init__(self, goal_x, goal_y):
        self.goal = {"x": goal_x, "y": goal_y}

    def findPointInCellClosestToGoal(self, cell):
        tempG = None
        minDist = -1

        for index, point in enumerate(cell):
            v1 = point
            v2 = cell[nxtCircIndx(index, len(cell))]
            closestPointInLineSeg = closestPointInLineSegToPoint(self.goal["x"], self.goal["y"], v1[0], v1[1], v2[0], v2[1])

            distGoalToLineSeg = distanceBetween2Points(self.goal, closestPointInLineSeg)
            
            if (tempG == None or distGoalToLineSeg < minDist):
                tempG = {"x":closestPointInLineSeg["x"], "y":closestPointInLineSeg["y"]}
                minDist = distGoalToLineSeg
            
        return tempG


# print(closestPointInLineSegToPoint(0, 0, 0, 1, 1, 0))
# bvcNav = BvcNavigator(0,0)
# print(bvcNav.findPointInCellClosestToGoal([[0,1],[1,1],[1,0]]))