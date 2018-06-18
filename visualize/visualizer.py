import os
import pytagcloud
import collections
import matplotlib.pyplot as plt

RESULT_DIRECTORY = "__results__/visualization"


def wordcloud(filename, wordfreq):
    taglist = pytagcloud.make_tags(wordfreq.items(), maxsize=80)
    # print(taglist)
    save_filename = '%s/wordcloud_%s.jpg' % (RESULT_DIRECTORY, filename)
    pytagcloud.create_tag_image(
        taglist,
        save_filename,
        size=(900, 600),
        fontname='Malgun',
        rectangular=False,
        background=(0, 0, 0))

def graph_bar( # 그래프 생성에 들어가는 기본 속성값들을 입력받도록 해보자 ~
        title=None,
        xlabel=None,
        ylabel=None,
        showgrid=False,
        values=None,
        ticks=None,
        filename=None,
        showgraph=True
      ):
    fig, subplots = plt.subplots(1, 1)  # subplot과 subplots의 차이 복습해야겟다..
    subplots.bar(range(len(values)), values, align='center')

    # ticks
    if ticks is not None and isinstance(ticks, collections.Sequence):
        subplots.set_xticks(range(len(ticks)))
        subplots.set_xticklabels(ticks, rotation=90, fontsize='small')

    # title
    if title is not None:
        subplots.set_title(title)
    if xlabel is not None:
        subplots.set_xlabel(xlabel)
    if ylabel is not None:
        subplots.set_ylabel(ylabel)


    # save file?
    if filename is not None and isinstance(filename, str): # 타입까지 체크하자
        save_filename = '%s/bar_%s.png' % (RESULT_DIRECTORY, filename)
        plt.savefig(save_filename, dpi=400, bbox_inches='tight')

    # show grid?
    subplots.grid(showgrid)

    # show graph?
    if showgraph:
        plt.show()



if os.path.exists(RESULT_DIRECTORY) is False:
    os.mkdir(RESULT_DIRECTORY)