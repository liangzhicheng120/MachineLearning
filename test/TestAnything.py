#!/bin/bash
# -*- coding: utf-8 -*-

def testTuples2classVec():
    classVec = []
    data = [[10, 1], [5, 0]]
    for tuples in data:
        number = tuples[0]
        element = tuples[1]
        for n in range(0, number):
            classVec.append(element)
    print classVec


def testCombine():
    a = [[1, 1]]
    b = [[2, 2]]
    print a + b


if __name__ == '__main__':
    testCombine()
