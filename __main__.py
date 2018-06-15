# analysis_fb 프로젝트의 실행 프로그램...
import collect
import analyze
import visualize

# print('run analysis_fb...')
if __name__ == '__main__':
    items = [
        {'pagename': 'jtbcnews', 'since':'2017-01-01', 'until':'2017-12-31'},
        {'pagename': 'chosun', 'since':'2017-01-01', 'until':'2017-12-31'}
    ]

    # 데이터 수집(collection)
    for item in items:
        resultfile = collect.crawling(**item, fetch=False)
        item['resultfile'] = resultfile


    # 데이터 분석(analyze)
    for item in items:
        data = analyze.json_to_str(item.get('resultfile'), 'message')
        item['count_wordfreq'] = analyze.count_wordfreq(data)
        # print(item['count'])

    # 데이터 시각화(visualize)
    for item in items:
        count = item['count_wordfreq']
        count_m50 = dict(count.most_common(50))

        filename = "%s_%s_%s" % (item['pagename'], item['since'], item['until'])
        visualize.wordcloud(filename, count_m50)

