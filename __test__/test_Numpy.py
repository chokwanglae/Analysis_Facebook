import numpy as np

# 성능 좋은 배열이라고 생각하세요...
# matplot을 사용하기 위해 배워봅니다...

arr = np.arange(10)
print(type(arr), arr)

arr = np.random.normal(5, 3, 500)
print(arr)

print('평균: ', arr.mean())

print('합계: ', arr.sum())

print('최대값: ', arr.max())
print('최소값: ', arr.min())

arr = np.arange(10)
print(type(arr))
print(arr)

arr = np.random.normal(5, 3, 500)
print(arr)

# 표준편차
print(arr.std())

# 분산
print(arr.var())


# 최대값, 최소값 위치
print(arr.argmax(), arr.argmin())