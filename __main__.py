# analysis_fb 프로젝트의 실행 프로그램...
import collect
import analyze
import visualize

import time
startTime = time.time()

# print('run analysis_fb...')
if __name__ == '__main__':
    items = [
        {'pagename': 'jtbcnews', 'since':'2017-01-01', 'until':'2017-12-31'},
        {'pagename': 'chosun', 'since':'2017-01-01', 'until':'2017-12-31'}
    ]

    # 데이터 수집(collection)
    for item in items:
        endTime = time.time() - startTime
        print('Running crawler : '+str(endTime))

        resultfile = collect.crawling(**item, fetch=False)
        item['resultfile'] = resultfile



        # 데이터 분석(analyze)  --> konlpy(...jpype --> +java 64bit, python 64bit 비트 맞춰야함)
    for item in items:
        endTime = time.time() - startTime
        print('Running analyze : '+str(endTime))

        data = analyze.json_to_str(item.get('resultfile'), 'message')
        item['count_wordfreq'] = analyze.count_wordfreq(data)

    # 데이터 시각화(visualize)
    for item in items:
        endTime = time.time() - startTime
        print('Running visualize : '+str(endTime))

        # 분석된 단어들 중에 most 50개만..
        count = item['count_wordfreq']
        count_m50 = dict(count.most_common(50))

        # wordclud, graph bar
        filename = "%s_%s_%s" % (item['pagename'], item['since'], item['until'])
        visualize.wordcloud(filename, count_m50)
        visualize.graph_bar( # 다른 바에도 적용하기위해 함수로 제작
            title='%s 빈도 분석' % (item['pagename']),
            xlabel='단어',
            ylabel='빈도 수',
            values=list(count_m50.values()), #, filename) # 딕셔너리니까 리스트 형태로 바꿔서 ..
            ticks=list(count_m50.keys()), # x, y의 값축(항목축) 지정
            showgrid=True, # grid = 격자
            filename=filename, # 파일로 저장 할건데,
            showgraph=False # 그래프로도 바로 보여줄것인가?
        )
