from simulator import CacheSimulator


def simluate_cache():
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


def find_best_cache():
    simluation_results = simluate_cache()

    min_runtime = min(simluation_results,
                      key=lambda x: x["runtime"])["runtime"]

    simluation_results = [
        result for result in simluation_results if result["runtime"] == min_runtime]

    simluation_results.sort(key=lambda x: x["cache size"])
    smallest_cache_size = simluation_results[0]["cache size"]
    return smallest_cache_size


print("best cache size : ", find_best_cache())
