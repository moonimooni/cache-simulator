from simulator import CacheSimulator


def simluate_cache():
    cache_size = int(input("최대 캐시 사이즈를 입력하세요 : "))
    hit_time = int(input("캐시 히트시 소요시간을 입력하세요 : "))
    miss_time = int(input("캐시 미스시 소요시간을 입력하세요 : "))
    stocks = list(input("주식 종목의 시퀀스를 입력하세요 : "))

    cache = CacheSimulator(hit_time, miss_time)

    for size in range(1, cache_size):
        simulation_result = list()
        simulation_result.append(cache.simulate(stocks, size))
        return simulation_result


print(simluate_cache())