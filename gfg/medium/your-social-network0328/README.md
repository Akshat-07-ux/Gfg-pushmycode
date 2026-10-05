# Your Social Network

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Geek is creating a social networking site called Geeksbook with  **n**  users numbered from  **1 to n**. Each user i (2 ≤ i ≤ n) has exactly one friend, and that friend must have a smaller user number than i. User 1 has no friend. The friends of users 2 to n are given in an array  **arr[]**  of size n - 1, where:

- arr[0] is the friend of user 2.
- arr[1] is the friend of user 3.
-...
- arr[i - 2] is the friend of user i.

The relationship is one-way. A user can reach another user by repeatedly following their friend's link. For every user i from 2 to n, find all users j (1 ≤ j < i) that can be reached from i. For every reachable pair (i, j), create an array [i, j, k] where:

- i is the starting user.
- j is the reachable user.
- k is the number of links that must be followed to reach j from i.

The result should contain these arrays in the following order:

- Process users i from 2 to n.
- For each user i, consider users j from 1 to i - 1 in increasing order.
- Include [i, j, k] only if j is reachable from i.

Return a 2D array containing information about all reachable pairs.

 **Examples:** 

```
Input: arr[] = [1, 2]
Output: [[2, 1, 1], [3, 1, 2], [3, 2, 1]]
Explanation: The links are 2 → 1 and 3 → 2. User 2 can reach user 1 in 1 link. User 3 can reach user 1 in 2 links. User 3 can reach user 2 in 1 link.
```

```
Input: arr[] = [1, 1]
Output: [[2, 1, 1], [3, 1, 1]]
Explanation: The links are 2 → 1 and 3 → 1. User 2 can reach user 1 in 1 link. User 3 can reach user 1 in 1 link.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-05T06:10:55.325Z  

```py
class Solution:
    def socialNetwork(self, arr):
        # code here
        n = len(arr) + 1
        ans = []
        
        for i in range(2, n + 1):
            curr = i
            dist = 0
            reachable = []
            
            while curr >= 2:
                parent = arr[curr - 2]
                
                dist += 1
                reachable.append((parent, dist))
                curr = parent
                
            reachable.sort(key=lambda x: x[0])
            
            for j, k in reachable:
                ans.append([i, j, k])
                
        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/your-social-network0328/1)