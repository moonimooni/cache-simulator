from simulator import CacheSimulator


def simluate_cache() -> list:
    cache_size = int(input("Please enter maximum cache size : "))
    hit_time = int(input("Please enter cache hit time : "))
    miss_time = int(input("Please enter cache miss time : "))
    stocks = list(
        map(str, input("Please enter sequence of stocks : ").split()))

    cache = CacheSimulator(hit_time, miss_time)
    simulation_result = list()

    for size in range(1, cache_size):
        simulation_result.append(cache.simulate(stocks, size))

    return simulation_result


def find_best_cache() -> int:
    simulation_result = sorted(
        simluate_cache(), key = lambda x: (x["runtime"], x["cache size"]))

    best_cache_size = simulation_result[0]["cache size"]
    return best_cache_size
