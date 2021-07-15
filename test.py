import unittest

from faker     import Faker

from functions import find_best_cache_size, simulate_cache


def custom_set_up(self):
    fake       = Faker()
    test_range = 100

    self.cache_size = 64
    self.hit_time   = 2
    self.miss_time  = 4
    #적당히 겹치는 랜덤값을 갖고오기 좋아서 first_name으로 생성.
    self.stocks     = [fake.first_name() for i in range(test_range)] 

    self.simulation_result = simulate_cache(
        self.cache_size,
        self.hit_time,
        self.miss_time,
        self.stocks
    )


class TestCacheSimulator(unittest.TestCase):
    def setUp(self):
        custom_set_up(self)

    def test_type_success(self):
        self.assertTrue(type(self.simulation_result) == list)

    def test_length_success(self):
        self.assertTrue(len(self.simulation_result) == self.cache_size)

    def test_cache_size_sorted_success(self):
        sorted = True
        for i in range(len(self.simulation_result)-1):
            index_cache_size  = self.simulation_result[i]["cache size"]
            bigger_cache_size = self.simulation_result[i+1]["cache size"]
            
            if index_cache_size >= bigger_cache_size:
                sorted = False
                break
        self.assertTrue(sorted)

    def test_runtime_sorted_success(self):
        sorted = True
        for i in range(len(self.simulation_result)-1):
            index_cache_runtime  = self.simulation_result[i]["runtime"]
            bigger_cache_runtime = self.simulation_result[i+1]["runtime"]

            if index_cache_runtime < bigger_cache_runtime:
                sorted = False
                break
        self.assertTrue(sorted)


class TestFindBestCacheSize(unittest.TestCase):
    def setUp(self):
        custom_set_up(self)
        self.best_cache_size = find_best_cache_size(self.simulation_result)

    def test_type_success(self):
        self.assertTrue(type(self.best_cache_size) == int)

    # 진짜로 가장 합리적인 캐시 크기인가?
    def test_reliability(self):
        #cache_size 순서대로 정렬되어 있으니 cache_size로 index 찾기 가능.
        index = self.best_cache_size - 1
        index_cache = self.simulation_result[index]

        if index - 1 >= 0:
            # 바로 한 단계 작은 사이즈의 캐시보다 런타임이 무조건 짧아야 함.
            index_cache_runtime   = index_cache["runtime"]
            smaller_cache_runtime = self.simulation_result[index - 1]["runtime"]
            option_1 = index_cache_runtime < smaller_cache_runtime
        else:
            # 애초에 가장 작은 캐시라면 그냥 true
            option_1 = True
        
        # 진짜 최소 runtime인가
        min_runtime = min(self.simulation_result, key=lambda x: x["runtime"])["runtime"]
        option_2    = min_runtime == index_cache["runtime"]

        self.assertTrue(option_1 and option_2)
        

if __name__ == '__main__':
    unittest.main()
