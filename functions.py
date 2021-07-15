from simulator import CacheSimulator


def simulate_cache(cache_size: int, hit_time: int, miss_time: int, stocks: list) -> list:
    cache = CacheSimulator(hit_time, miss_time)
    return [cache.simulate(stocks, size) for size in range(1, cache_size+1)]


def find_best_cache_size(simulation_result) -> int:
    simulation_result = sorted(
        simulation_result,
        key=lambda x: (x["runtime"], x["cache size"])
    )
    best_cache_size = simulation_result[0]["cache size"]
    return best_cache_size
