# -*- coding=utf-8 -*-
#@author: vincentping@gmail.com
#@github: https://github.com/vincentping
#@date: 2014-12-9

"""
https://oj.leetcode.com/problems/max-points-on-a-line/

Problem: 
Max Points on a Line 

Description: 
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Tags: Hash Table, Math

Difficulty: Hard

The Python model is:
---------------------------------
# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
----------------------------------
"""

def maxPoints0(points):
    """
    这个是我最初实现的，比较直观，避免了浮点运算导致的不准确，但是计算量比较大，运行速度慢
    在oj.leetcode.com站点得到的结果是
    Submission Result: Time Limit Exceeded
    """
    import operator
    pointset = set(points)
    if len(pointset) < 3:
        return len(points)
    else:
        pointdict ={pkey:points.count(pkey) for pkey in pointset}
        count = 0

        while len(pointset) > 1:
            point1 = pointset.pop()
            point2set = pointset.copy()

            while point2set:
                point2 = point2set.pop()
                point3set = point2set.copy()

                lineset = {point1, point2}

                if point3set:
                    for point3 in point3set:
                        #if (point1.x-point2.x)*(point2.y-point3.y) == (point2.x-point3.x)*(point1.y-point2.y) : #for the leetcode site test
                        if (point1[0]-point2[0])*(point2[1]-point3[1]) == (point2[0]-point3[0])*(point1[1]-point2[1]) :
                            lineset.add(point3)
                            point2set.remove(point3)

                linecount = reduce(operator.add, [pointdict[p] for p in lineset])

                if linecount > count: 
                    count = linecount
        return count

"""
以下是我在oj.leetcode.com相关问题的讨论区看到别人的答案，通过测试。
其中的gcd函数将浮点运算转换成分数，还没看明白。
"""
def gcd( a, b):
        if a == 0: return b
        return gcd(b % a, a)

def maxPointsz(points):
        count = len(points)
        results = 0
        for i in range(0, count):
            dk = {}
            inf = 0
            same = 1
            for j in range(i + 1, count):
                pi = points[i]
                pj = points[j]
                if pi[0] == pj[0] and pi[1] == pj[1]: same += 1
                elif pi[0] == pj[0]: inf += 1
                else:
                    k_gcd = gcd(abs(pi[1] - pj[1]), abs(pi[0] - pj[0]))
                    sign = '-' if (pi[1] - pj[1]) * (pi[0] - pj[0]) < 0 else ''
                    k = ''.join([sign, str(abs(pi[1] - pj[1]) // k_gcd), str(abs(pi[0] - pj[0]) // k_gcd)])
                    if dk.get(k) == None: dk[k] = 1
                    else: dk[k] += 1
            maxDk = 0 if len(dk) == 0 else max(dk.items(), key=lambda p: p[1])[1]
            maxAll = max(maxDk, inf) + same
            results = max(results, maxAll)
        return results

def maxPoints1(points):
    """
    这个函数，是我在maxPoints的基础上引入gcd()函数
    但是在oj.leetcode.com站点测试结果出现超时。
    """
    pointset = set(points)
    if len(pointset) < 3:
        return len(points)
    else:
        pointdict ={pkey:points.count(pkey) for pkey in pointset}
        result = 0
        while len(pointset)>1:
            slopedict = {'infinite':0}
            point1 = pointset.pop()
            pcount = pointdict[point1]
            
            point2set = pointset.copy()
            
            for point2 in point2set:
                if point1[0] == point2[0]:
                    slopedict['infinite'] += pointdict[point2]
                else:
                    pp0 = point1[0] - point2[0]
                    pp1 = point1[1] - point2[1]
                    k_gcd = gcd(abs(pp1), abs(pp0))
                    sign = '-' if pp1 * pp0 < 0 else ''
                    slope = ''.join([sign, str(abs(pp1) // k_gcd), str(abs(pp0) // k_gcd)])

                    if slopedict.get(slope,None):
                        slopedict[slope] += pointdict[point2]
                    else:
                        slopedict[slope] = pointdict[point2]
    
            pcount += max(slopedict.values())
            if pcount > result:
                result = pcount
        return result

def maxPoints(points):
    """
    这个是我在maxPoints0的基础上，使用计算斜率的方式运算，速度很快，在精度要求不高的情况下，
    使用截位字符串更能大大提高运算速度。
    
    速度快的原因主要是使用了set首先过滤掉重复点。
    
    但是在oj.leetcode.com站点上出现：Wrong Result的错误，分析下来，估计是points是Point类型的实例，
    set对于类操作有问题。
    """
    pointset = set(points)
    if len(pointset) < 3:
        return len(points)
    else:
        pointdict ={pkey:points.count(pkey) for pkey in pointset}
        result = 0
        while len(pointset)>1:
            slopedict = {'infinite':0}
            point1 = pointset.pop()
            pcount = pointdict[point1]
            
            point2set = pointset.copy()
            
            for point2 in point2set:
                if point1[0] == point2[0]:
                    slopedict['infinite'] += pointdict[point2]
                else:
                    # 在精度要求不高的情况下，使用截位字符串可以大大提高运算速度。
                    slope = '%.5f', float(point1[1]-point2[1])/(point1[0]-point2[0])
                    
                    if slopedict.get(slope,None):
                        slopedict[slope] += pointdict[point2]
                    else:
                        slopedict[slope] = pointdict[point2]
    
            pcount += max(slopedict.values())
            if pcount > result:
                result = pcount
        return result

if __name__ == '__main__':
    ps = ([(0,0),(0,0)],
            [(0,0),(1,0)],
            [(0,0),(1,1),(1,-1)],
            [(0,0),(1,2),(-1,-2)],
            [(1,1),(1,1),(2,3)],
            [(1,1),(1,1),(2,2),(2,2)],
            [(0,0),(0,0),(1,2),(2,3),(2,4)],
            [(1,1), (2,2), (3,3), (5,4), (0, 0)],
            [(0,0),(0,0),(1,2),(-1,-2),(2,4),(23,12)],
            [(-4,-4),(-8,-582),(-3,3),(-9,-651),(9,591)],
            [(84,250),(0,0),(1,0),(0,-70),(0,-70),(1,-1),(21,10),(42,90),(-42,-230)] ,
            [(29,87),(145,227),(400,84),(800,179),(60,950),(560,122),(-6,5),(-87,-53),(-64,-118),(-204,-388),(720,160),(-232,-228),(-72,-135),(-102,-163),(-68,-88),(-116,-95),(-34,-13),(170,437),(40,103),(0,-38),(-10,-7),(-36,-114),(238,587),(-340,-140),(-7,2),(36,586),(60,950),(-42,-597),(-4,-6),(0,18),(36,586),(18,0),(-720,-182),(240,46),(5,-6),(261,367),(-203,-193),(240,46),(400,84),(72,114),(0,62),(-42,-597),(-170,-76),(-174,-158),(68,212),(-480,-125),(5,-6),(0,-38),(174,262),(34,137),(-232,-187),(-232,-228),(232,332),(-64,-118),(-240,-68),(272,662),(-40,-67),(203,158),(-203,-164),(272,662),(56,137),(4,-1),(-18,-233),(240,46),(-3,2),(640,141),(-480,-125),(-29,17),(-64,-118),(800,179),(-56,-101),(36,586),(-64,-118),(-87,-53),(-29,17),(320,65),(7,5),(40,103),(136,362),(-320,-87),(-5,5),(-340,-688),(-232,-228),(9,1),(-27,-95),(7,-5),(58,122),(48,120),(8,35),(-272,-538),(34,137),(-800,-201),(-68,-88),(29,87),(160,27),(72,171),(261,367),(-56,-101),(-9,-2),(0,52),(-6,-7),(170,437),(-261,-210),(-48,-84),(-63,-171),(-24,-33),(-68,-88),(-204,-388),(40,103),(34,137),(-204,-388),(-400,-106)])
    
    funcs = (maxPoints, maxPoints0, maxPoints1, maxPointsz)
    
    for func in funcs:
        print '%s running...' %func.func_name
        for p in ps:
            print func(p)
    

    import time
    n=100
    m = range(n)
    p = [(29,87),(145,227),(400,84),(800,179),(60,950),(560,122),(-6,5),(-87,-53),(-64,-118),(-204,-388),(720,160),(-232,-228),(-72,-135),(-102,-163),(-68,-88),(-116,-95),(-34,-13),(170,437),(40,103),(0,-38),(-10,-7),(-36,-114),(238,587),(-340,-140),(-7,2),(36,586),(60,950),(-42,-597),(-4,-6),(0,18),(36,586),(18,0),(-720,-182),(240,46),(5,-6),(261,367),(-203,-193),(240,46),(400,84),(72,114),(0,62),(-42,-597),(-170,-76),(-174,-158),(68,212),(-480,-125),(5,-6),(0,-38),(174,262),(34,137),(-232,-187),(-232,-228),(232,332),(-64,-118),(-240,-68),(272,662),(-40,-67),(203,158),(-203,-164),(272,662),(56,137),(4,-1),(-18,-233),(240,46),(-3,2),(640,141),(-480,-125),(-29,17),(-64,-118),(800,179),(-56,-101),(36,586),(-64,-118),(-87,-53),(-29,17),(320,65),(7,5),(40,103),(136,362),(-320,-87),(-5,5),(-340,-688),(-232,-228),(9,1),(-27,-95),(7,-5),(58,122),(48,120),(8,35),(-272,-538),(34,137),(-800,-201),(-68,-88),(29,87),(160,27),(72,171),(261,367),(-56,-101),(-9,-2),(0,52),(-6,-7),(170,437),(-261,-210),(-48,-84),(-63,-171),(-24,-33),(-68,-88),(-204,-388),(40,103),(34,137),(-204,-388),(-400,-106)]
    
    timetable ={}
    for func in funcs:
        print ' '*50
        print 'Testing Function %s() ...' %func.func_name
        start = time.time()
        for i in m:
            func(p)
        elapse = time.time()-start
        timetable[elapse] = func.func_name
        print 'Function %s() runs %d times, takes\n' %(func.func_name, n), elapse
        print '*'*50
    
    print 'The Most Fast Function is Function %s().' % timetable[min(timetable.keys())]
#EOF