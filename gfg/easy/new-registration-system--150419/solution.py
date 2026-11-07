class Solution:
    def generateUsernames(self, arr: list[str]) -> list[str]:
        # code here
        
        occupied = set(arr)
        assigned = set()
        next_suffix = {}
        result = []
        
        for name in arr:
            if name not in assigned:
                assigned.add(name)
                result.append(name)
                
            else:
                suffix = next_suffix.get(name, 1)
                candidate = f"{name}{suffix}"
                
                while candidate in occupied or candidate in assigned:
                    suffix += 1
                    candidate = f"{name}{suffix}"
                    
                assigned.add(candidate)
                next_suffix[name] = suffix + 1
                
                result.append(candidate)
                
        return result