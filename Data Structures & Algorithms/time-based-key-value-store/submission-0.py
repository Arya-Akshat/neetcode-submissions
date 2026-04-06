from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.arr = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.arr[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        vals = self.arr[key]
        if not vals:
            return ""
        times = [t for _, t in vals]
        i = bisect.bisect_right(times, timestamp)
        return vals[i-1][0] if i!=0 else ""
            

        
