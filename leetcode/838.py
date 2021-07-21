"""
    https://leetcode.com/problems/push-dominoes/
    838. Push Dominoes (Medium)
"""

class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        d = ['L'] + list(dominoes) + ['R']

        pre_char, pre_loc = 'L', -1
        for i in range(len(d)):
            if d[i] != '.':
                if pre_char == d[i]:
                    self.update(d, pre_loc+1, i, d[i])
                elif pre_char > d[i]:
                    mid = int((pre_loc+i)/2)
                    remain = (pre_loc+i)%2
                    self.update(d, pre_loc+1, mid+remain, 'R')
                    self.update(d, mid+1, i, 'L')
                pre_char = d[i]
                pre_loc = i
        
        return ''.join(d[1:-1])
                    
    def update(self, d, left, right, c):
        for i in range(left, right):
            d[i] = c