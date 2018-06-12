# 0부터 10까지 자승을 구하라.

# 1. 리스트를 생성하고, 리스트에 그 결과를 하나씩 붙여 한번에 결과를 반환한다.
# def squares(n=10):
#     results = []
#     for i in range(n+1):
#         results.append(i**2)
#     return results

# 2. 결과값 하나씩을 반환한다. (X) 함수를 여러번 출력해야함
# def squares(n=10):
#     results = []
#     for i in range(n+1):
#         return i**2

# 3. yield를 사용하자
def squares(n=10):
    for i in range(n+1):
        yield i**2

for x in squares(10):
    print(x)

