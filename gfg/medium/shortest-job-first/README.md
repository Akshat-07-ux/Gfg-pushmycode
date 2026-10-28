# Shortest Job first

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

The shortest job first (SJF) or shortest job next, is a scheduling policy that selects the waiting process with the smallest execution time to execute next. Given an array of integers  **bt[]**  of size  **n**. Array  **bt[]**  denotes the  **burst time**  of each process. Calculate the  **average waiting time**  of all the processes and return the nearest integer which is smaller or equal to the output.

 **Note:**  Consider all process are available at time 0.

 **Examples:** 

```
Input: bt[] = [4,3,7,1,2]
Output: 4
Explanation: After sorting burst times by shortest job policy, calculated average waiting time is 4.
```

```
Input: bt[] = [1,2,3,4]
Output: 2
Explanation: After sorting burst times by shortest job policy, calculated average waiting time is 2.

```

 **Constraints:** 
1 <= n <= 105
1 <= arr[i] <= 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-28T07:26:36.476Z  

```py
class Solution:
    def solve(self, bt):
        # code here
        bt.sort()
        total_wait = 0
        current_wait = 0
        
        for t in bt:
            total_wait += current_wait
            current_wait += t
            
        return total_wait // len(bt)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/shortest-job-first/1)