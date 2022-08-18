import requests
from bs4 import BeautifulSoup
import datetime
from time import strftime

def GetDetailHtml(url):
    data_get=requests.get(url)
    html = BeautifulSoup(data_get.content, 'html.parser',from_encoding='gb18030')
    return html

if __name__ == '__main__':
    k=1
    now=datetime.datetime.now()
    today=now.strftime("%Y-%m-%d")
    while k<7:
        if k==1:
            urlk='http://xzspj.baoding.gov.cn/zyjy/011003/011003001/011003001004/secondPagezyjy.html'
        elif k<7 and k>1:
            urlk='http://xzspj.baoding.gov.cn/zyjy/011003/011003001/011003001004/'+str(k)+'.html'
        else:
            urlk='http://xzspj.baoding.gov.cn/zyjy/011003/011003001/011003001004/secondPagezyjy.html?categoryNum=011003001004&pageIndex='+str(k)
        k=k+1

        html=GetDetailHtml(urlk)
        for i in html.select('li') :
            #print(i)
            quyu=i.select('span')[0].text.strip('[]����').strip('������Դ')
            if quyu=='������':
                quyu='������-��Ͻ��'
            else:
                quyu='������-'+quyu
            fabushijian=i.select('span')[1].text
            if fabushijian!=today:
                break
            title=i.select('a')[0].attrs['title']
            url=i.select('a')[0].attrs['href']
            url="http://xzspj.baoding.gov.cn"+url
            #print(title,url)
            html1=GetDetailHtml(url)
            table=html1.select('table')
            print(quyu)
            print(fabushijian)
            print(title)
            print(url)
            if(table):
                zhongbiaodanwei='�б굥λ: '+table[1].select('tr')[2].select('td')[2].text.strip('\n').replace('\t','')
                jine='�б���:'+table[1].select('tr')[2].select('td')[3].text.strip('\n').replace('\t','')
                zhaobiaoren=table[2].select('tr')[1].select('td')[1].text.strip('\n').replace(' ','')
                zhaobiaodanwei=table[2].select('tr')[1].select('td')[0].text.strip('\n').replace(' ','')
                
                print(zhaobiaodanwei)
                print(zhaobiaoren)
                print(zhongbiaodanwei)
                print(jine)
                print(' ')
            else:
                strings2 = html1.select('p')
                for i in strings2:
                    #print(i.text)
                    if 'Ͷ����' in i.text or '�б굥λ��' in i.text or '�б굥λ:' in i.text or '�б굥λ��' in i.text or '�б���' in i.text or '�б굥λ����' in i.text:
                        zhongbiaodanwei = i.text
                        print(zhongbiaodanwei)
                        continue
                    if '�б�' in i.text or '�б���:' in i.text or '�б굥λ��' in i.text:
                        zhaobiaoren = i.text
                        print(zhaobiaoren)
                        continue
                    if '�б���������' in i.text or '�б�������:' in i.text:
                        zhaobiaodanwei = i.text
                        print(zhaobiaodanwei)
                        continue
                    if '���' in i.text or 'Ԫ' in i.text or '�ܱ���' in i.text or '��' in i.text or '����' in i.text :
                        jine = i.text
                        print(jine)
                        continue
                print(' ')
