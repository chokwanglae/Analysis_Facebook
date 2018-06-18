import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

def ex1():
    # plt.plot([1, 2, 3, 4], [10, 20, 30, 40])
    plt.plot([10, 20, 30, 40])
    plt.show()

def ex2():
    fig = plt.figure()

    sp1 = fig.add_subplot(2, 1, 1)
    sp1.plot(nrows=[1, 2, 3, 4], ncols=[10, 20, 30, 40])

    sp2 = fig.add_subplot(2, 1, 2)
    sp2.plot([1, 2, 3, 4], [100, 200, 300, 400])

    plt.show()


def ex3():
    fig = plt.figure()

    sp1 = fig.add_subplot(2, 2, 1)
    sp1.plot(randn(50).cumsum(), 'k--')

    sp2 = fig.add_subplot(2, 2, 2)
    sp2.hist(randn(1000), bins=20, color='red', alpha=0.3)

    sp3 = fig.add_subplot(2, 2, 3)
    sp3.scatter(np.arange(100), np.arange(100) + 3 * randn(100))

    plt.show()

def ex4():
    fig, subplot = plt.subplots(1, 1)

    subplot.plot([10, 20, 30, 40])

    plt.show()

def ex5():
    fig, subplots = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)

    for i in range(2):
        for j in range(2):
            subplots[i, j].hist(randn(100), bins=20, color='k', alpha=0.3) # k는 블랙(black의 k)

    plt.subplots_adjust(wspace=0, hspace=0)

    plt.show()

def ex6():
    fig, subplots = plt.subplots(1, 1)

    subplots.plot([1, 2, 3, 4], [10, 20, 30, 40], 'go--')

    plt.show()

def ex7():
    pass #걍 생략 ㅎㅎ;

def ex8():
    fig, subplots = plt.subplots(1, 1)

    subplots.plot([1, 2, 3, 4],
                  [10, 20, 30, 40],
                  color = '#335522',
                  linestyle = 'solid',
                  marker='v'
                  )

    plt.show()

def ex9():
    # 같은 데이터로 그래프 두개(한 창에)
    fig, subplot = plt.subplots(1, 1)

    data = randn(50).cumsum()
    subplot.plot(data, color='black', linestyle='dashed', label='AAA')
    subplot.plot(data, color='green', drawstyle='steps-mid', label='AAA')

    plt.legend(loc='best')

    plt.show()

# x축의 눈금을 변경
def ex10():
    fig, subplots = plt.subplots(1, 1)

    subplots.plot(randn(1000).cumsum())
    subplots.set_xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])

    plt.show()

def ex11():
    fig, subplots = plt.subplots(1, 1)

    subplots.plot(randn(1000).cumsum())
    subplots.set_xticks(
        [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])

    subplots.set_xticklabels(
        ['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'pt7', 'pt8', 'pt9', 'pt10'],
        # rotation=30,
        # fontsize='small'
    )
    subplots.set_xlabel('Posints')
    subplots.set_title('My First Matplotlib Plot')

    plt.show()

def ex12():
    fig, subplots = plt.subplots(1, 1)

    # 한글 설정 경로
    # D:\pythonPycharm\analysis_fb\venv\Lib\site-packages\matplotlib\matplotlibrc 파일
    # font.family = Malgun Gothic 으로 변경

    subplots.plot(randn(1000).cumsum(), 'k', label='basic')
    subplots.plot(randn(1000).cumsum(), 'k-.', label='dash')
    subplots.plot(randn(1000).cumsum(), 'k.', label='점')
    # subplots.plot(randn(1000).cumsum(), 'k--', label='four')
    # subplots.plot(randn(1000).cumsum(), 'k..', label='five') # k..은 없네...

    subplots.set_xticklabels(
        ['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'pt7', 'pt8', 'pt9', 'pt10'],
        rotation=30,
        fontsize='small')
    subplots.set_xlabel('포인트')
    subplots.set_title('예제12 한글처리')
    plt.legend(loc='best')

    plt.show()


# color: 복합 문자열 전달에서는 k, r, b, g, y, ...... 명시적 표현에서는 black, red, blue, gree, yellow....와  rrggbb도  가능하다
# linestyle: - (solid), - -(dashed), -.(dashdot), dotted, ‘ ‘(None) 등이 가능하다. marker:.(dot) v(화살표), o(big dot)

if __name__ == '__main__':
    ex11()


# import matplotlib.pyplot as plt
# from numpy.random import rand
# import numpy as np
# # numpy는 랜덤함수가 굉장히 많아요...
#
# def ex1():
#     # plt.plot([1, 2, 3, 4], [10, 20, 30, 40])
#     plt.plot([10, 20, 30, 40])
#     plt.show()
#
# def ex2():
#     fig = plt.figure()
#
#     sp1 = fig.add_subplot(2, 1, 1)
#     sp1.plot([1, 2, 3, 4], [10, 20 ,30 ,40])
#
#     sp2 = fig.add_subplot(2, 1, 2)
#     sp2.plot([1, 2, 3, 4], [100, 200 ,300 ,400])
#
#     plt.show()
#
# def ex3():
#     fig = plt.figure()
#
#     sp1 = fig.add_subplot(2, 2, 1)
#     # print(rand(50).cumsum())
#     sp1.plot(rand(50).cumsum(), 'k--') # k--은 그래프를 대시형태로 해주겟다.
#
#
#     sp2 = fig.add_subplot(2, 2, 2)
#     sp2.hist(rand(1000), bins=20, color='red', alpha=0.3) # alpha는 투명도, bins는 바 그래프에 사용되는 속성
#
#     sp3 = fig.add_subplot(2, 2, 3)
#     sp3.scatter(np.arange(100), np.arange(100) +3*rand(100))
#
#
#     plt.show()
#
# def ex4():
#     fig, subplot = plt.subplots(1, 1)
#     subplot.plot([10, 20, 30, 40])
#     plt.show()
#
#
# if __name__ == '__main__':
#     ex3()
