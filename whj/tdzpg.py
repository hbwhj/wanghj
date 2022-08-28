import requests
from bs4 import BeautifulSoup
import datetime
from time import strftime

def GetDetailHtml(url):
    data_get=requests.get(url)
    html = BeautifulSoup(data_get.content, 'html.parser',from_encoding='gb18030')
    return html

if __name__ == '__main__':
    url='http://zrgh.baoding.gov.cn/bdzrzy/ywpd/tdgl/tdzpg/'
    emptylist=[]
    now=datetime.datetime.now()
    today=now.strftime("%Y-%m-%d")
    quyu='保定市'
    html=GetDetailHtml(url)
    for i in html.select('li') :
        fabushijian=i.select('span')
        if fabushijian!=emptylist:
            if fabushijian[0].text!=today:
                break
            else:
                time=fabushijian[0].text
                title=i.select('a')[0].attrs['title']
                url1='http://zrgh.baoding.gov.cn'+i.select('a')[0].attrs['href']
                print(time)
                print(title)
                print(url1)
            html1=GetDetailHtml(url1)
            hcount=0
            
            lie_bao=0
            lie=0
            lie_zhobr=0
            lie_jine=0
            for table in html1.findAll('table'):
                for row in table.findAll('tr'):
                    lcount=0
                    hcount+=1
                    #可以将结果放入到列表里，此处只打印了变量
                    for tr in row.findAll('td'):
                        lcount+=1
                        if '公告' in title:
                            if hcount==2:
                                if '容积率' in tr.text or '建筑密度' in tr.text or '绿地率' in tr.text or '系数' in tr.text or '投资强度' in tr.text: 
                                    lie+=1
                                    continue
                            if '保证金' in tr.text:
                                lie_bao=lcount
                            if lcount==2 and hcount>1:
                                zhaobiaoren='招标:'+tr.text.replace('\n','')
                                print(zhaobiaoren)
                            if lcount==lie_bao+lie-1 and hcount>1:
                                jine='金额:'+tr.text.replace('\n','')+'(万元)保证金'
                                print(jine)
                                zhongbiaoren='中标:待公布'
                                print(zhongbiaoren)
                        if '公示' in title:    
                            if '竞得' in tr.text or '受让人' in tr.text:
                                lie_zhobr=lcount
                            if '成交价' in tr.text:
                                lie_jine=lcount
                            if lcount==2 and hcount>1:
                                zhaobiaoren='招标:'+tr.text.replace('\n','')
                                print(zhaobiaoren)
                            if lcount==lie_zhobr and hcount>1:
                                zhongbiaoren='中标:'+tr.text.replace('\n','')
                                print(zhongbiaoren)
                            if lcount==lie_jine and hcount>1:
                                jine='金额:'+tr.text.replace('\n','')+'(万元)成交价'
                                print(jine)
                            
                        #print(hcount,'行',lcount,'列',tr.text.replace(' ','').replace('\t','').replace('\n',''))
                break                        

        else:
            continue