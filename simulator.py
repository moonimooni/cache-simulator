from collections import deque


class CacheSimulator:
    hit_count, miss_count, runtime = 0, 0, 0

    def __init__(self, hit_time, miss_time):
        self.hit_time = hit_time
        self.miss_time = miss_time

    def find_cache(self, data, cache_map: dict, cache_used_order: deque([]), cache_size: int):
        # 캐시에서 찾은 경우
        if data in cache_map:
            self.hit_count += 1
            self.runtime += self.hit_time
            # 찾은 데이터 삭제. 가장 뒤로 옮기기 위해.
            cache_used_order.remove(data)

        # 캐시에서 못찾은 경우
        else:
            self.miss_count += 1
            self.runtime += self.miss_time

            # 캐시가 꽉 찼다면
            if len(cache_map) == cache_size:
                # 가장 오랫동안 참조하지 않은 캐시 슬롯 데이터 삭제
                deleted_data = cache_used_order.popleft()
                del cache_map[deleted_data]

        recent_data = data
        # 현재 데이터를 링크드 리스트 가장 뒤에 배치. 가장 최근에 사용한 데이터라는 뜻.
        cache_used_order.append(recent_data)
        cache_map[recent_data] = True
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

        # 초기화
        self.hit_count, self.miss_count, self.runtime = 0, 0, 0

        return result
