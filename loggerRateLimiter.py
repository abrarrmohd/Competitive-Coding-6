"""
Problem: Logger Rate Limiter
Approach: Straightforward hashmap Approach with key = msg and val = timestamp
t.c. => O(1)
s.c. => number of shouldPrintMessage calls
"""
from collections import defaultdict
class Logger:

    def __init__(self):
        self.timestampMap = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.timestampMap:
            self.timestampMap[message] = timestamp
            return True
        else:
            prevTime = self.timestampMap[message]
            if timestamp - prevTime >= 10:
                self.timestampMap[message] = timestamp
                return True
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)