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
    quyu='������'
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
                    #���Խ�������뵽�б���˴�ֻ��ӡ�˱���
                    for tr in row.findAll('td'):
                        lcount+=1
                        if '����' in title:
                            if hcount==2:
                                if '�ݻ���' in tr.text or '�����ܶ�' in tr.text or '�̵���' in tr.text or 'ϵ��' in tr.text or 'Ͷ��ǿ��' in tr.text: 
                                    lie+=1
                                    continue
                            if '��֤��' in tr.text:
                                lie_bao=lcount
                            if lcount==2 and hcount>1:
                                zhaobiaoren='�б�:'+tr.text.replace('\n','')
                                print(zhaobiaoren)
                            if lcount==lie_bao+lie-1 and hcount>1:
                                jine='���:'+tr.text.replace('\n','')+'(��Ԫ)��֤��'
                                print(jine)
                                zhongbiaoren='�б�:������'
                                print(zhongbiaoren)
                        if '��ʾ' in title:    
                            if '����' in tr.text or '������' in tr.text:
                                lie_zhobr=lcount
                            if '�ɽ���' in tr.text:
                                lie_jine=lcount
                            if lcount==2 and hcount>1:
                                zhaobiaoren='�б�:'+tr.text.replace('\n','')
                                print(zhaobiaoren)
                            if lcount==lie_zhobr and hcount>1:
                                zhongbiaoren='�б�:'+tr.text.replace('\n','')
                                print(zhongbiaoren)
                            if lcount==lie_jine and hcount>1:
                                jine='���:'+tr.text.replace('\n','')+'(��Ԫ)�ɽ���'
                                print(jine)
                            
                        #print(hcount,'��',lcount,'��',tr.text.replace(' ','').replace('\t','').replace('\n',''))
                break                        

        else:
            continue