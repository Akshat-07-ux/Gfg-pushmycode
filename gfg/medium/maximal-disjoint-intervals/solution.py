def maxDisjointInterval(arr):
    # code here
    
    if not arr:
        return []
        
    arr.sort(key=lambda x: x[1])
    
    selected = []
    last_end = -float("inf")
    
    for interval in arr:
        start, end = interval
        
        if start > last_end:
            selected.append(interval)
            last_end = end
            
    return selected