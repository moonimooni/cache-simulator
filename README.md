# cache simulator

## 파일 구성.

__functions.py__ <br/>
  - simulate_cache() --> 1부터 주어진 캐시 사이즈까지의 시뮬레이션 결과를 return. <br/>
  - find_best_cache_size() --> simulate_cache() 결과를 기반으로 가장 합리적인 캐시 사이즈 return. <br/>

__simulator.py__ --> 캐시 시뮬레이션을 구성하기 위한 클래스 파일.<br/>
__test.py__ --> 테스트코드.

<br/>

## Idea.

초기 접근 : LRU을 구현하기 위해 Queue를 쓰는게 좋을 것 같다고 생각.<br/>
하지만 queue에서 pop, insert를 하면 인덱스 재정렬 작업이 필요하므로 O(n)의 시간이 소요. <br/>
따라서 python의 내장 모듈 중 더블 링크드 리스트로 이루어진 deque를 사용하기로 함.<br/>

cache 내에서 원하는 데이터를 찾는 과정 또한 O(n) 소요.<br/>
이 시간을 줄이기 위해 hash map(dict)을 만들어놓고 현재 cache에 존재하는 데이터값을 key로 저장.<br/>

<img src="https://github.com/moonimooni/images/blob/main/ezgif-2-f929d2977146.gif?raw=true" width=600 />

<br />

## 아쉬운 점
- 테스트케이스에 hash map의 key들과 deque의 node들이 정말 일치하는지 증명하는 테스트가 필요하지 않을까? <br/>
- hash map을 좀 더 적극적으로 활용할 수 있을 거 같은데, 왜냐하면 node를 remove하는 과정에서 node 탐색 작업이 선행되어야 하기 때문에, 시간이 O(n)만큼 소요될 수 있음. hash map의 value로 해당 node를 바로 삭제할 수는 없을까?

<img src="https://github.com/moonimooni/images/blob/main/IMG_0188.jpg?raw=true" width=600 />

<br/>

## 뿌듯한 점
- linked list와 hash를 결합해서 써보자! 하고 구현해보고 나서 인터넷을 뒤져보니 이런 방향이 정석인 것 같아서 뿌듯.
