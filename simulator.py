from collections import deque


class CacheSimulator:
    hit_count, miss_count, runtime = 0, 0, 0

    def __init__(self, hit_time, miss_time):
        self.hit_time = hit_time
        self.miss_time = miss_time

    def find_cache(self, data, cache_map, cache_used_order, cache_size):
        if data in cache_map:
            self.hit_count += 1
            self.runtime += self.hit_time
            cache_used_order.remove(data)

        else:
            self.miss_count += 1
            self.runtime += self.miss_time

            if len(cache_map) == cache_size:
                deleted_data = cache_used_order.pop()
                del cache_map[deleted_data]
            
        recent_data = data
        cache_used_order.appendleft(recent_data)
        cache_map[recent_data] = recent_data
        return

    def simulate(self, stocks, size):
        cache_map = dict()
        cache_used_order = deque([])

        for stock in stocks:
            self.find_cache(stock, cache_map, cache_used_order, size)

        result = {
            "cache size": size,
            "hit count": self.hit_count,
            "miss count": self.miss_count,
            "runtime": self.runtime
        }
        self.hit_count, self.miss_count, self.runtime = 0, 0, 0
        
        return result