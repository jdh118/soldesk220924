#!/usr/bin/env python
# coding: utf-8

# In[10]:


#스크랩핑
import urllib.request
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"
urllib.request.urlretrieve(url, savename)


# In[14]:


mem = urllib.request.urlopen(url).read()
with open("test1.png", mode"wb") as f:
    f.write(mem)


# In[15]:


url = "http://api.aoikujira.com/ip/ini"
data = urllib.request.urlopen(url).read()
print(data)
text = data.decode("utf-8")
print(text)
with open("test2.txt", "w") as f:
    f.write(text)


# In[16]:


url = "http://www.naver.com"
data = data = urllib.request.urlopen(url).read()
print(data)
text = data.decode("utf-8")
print(text)


# In[ ]:


### https://search.naver.com/search.naver?query=주다함  ###
##  /<- -------------------------------------------->/ url
##                                         /<------->/ 쿼리스트링(?뒤,질문할내용)

## http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108
##  /<- ---------------------------------------------------------->/ url
##                                                       /<------->/ 쿼리스트링


# In[17]:


import urllib.parse
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
value = {"stnId":num}  ##딕셔너리
##딕셔너리를 쿼리스트링으로 변환하기
params = urllib.parse.urlencode(value) # "stnId=108"
url = API + "?" + params
## print(url) 
data = urllib.request.urlopen(url).read()  #스크랩핑(모든것을 긁어옴)
text = data.decode("utf-8")
print(text)


# In[30]:


import urllib.parse
num = input("지역번호를 입력해주세요, : ")
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
value = {"stnId":num}  ##딕셔너리
##딕셔너리를 쿼리스트링으로 변환하기
params = urllib.parse.urlencode(value) # "stnId=108"
url = API + "?" + params
## print(url) 
data = urllib.request.urlopen(url).read()  #스크랩핑(모든것을 긁어옴, url과request필요)
text = data.decode("utf-8")
print(text)


# In[18]:


#크롤링
from bs4 import BeautifulSoup
html = """
<html><body>
  <h1 id="title">스크레이핑이란?</h1>
  <p id="body">웹 페이지를 분석하는 것</p>
  <p><a href='a.html' id = 'link'>원하는 부분을 추출하는 것</a></p>
</body></html>
"""


#HTML분석하기
soup = BeautifulSoup(html, 'html.parser')
print(soup)
print(soup.prettify)


# In[19]:


#태그를 이용하여 원하는 부분 추출하기
h1 = soup.html.h1
print(h1)
print(h1.string)
p1 = soup.html.p
print(p1)
print(p1.string)
p2 = p1.next_sibling.next_sibling
print(p2)
p3 = soup.html.p.next_sibling.next_sibling
print(p3)
print(p3.sibling)


# In[52]:


#크롤링
from bs4 import BeautifulSoup
html = """
<html><body>
  <h1 id="title">스크레이핑이란?</h1>
  <p id="body">웹 페이지를 분석하는 것</p>
  <p><a href='a.html' id = 'link'>원하는 부분을 추출하는 것</a></p>
</body></html>
"""


#HTML분석하기
soup = BeautifulSoup(html, 'html.parser')
print(soup)
print(soup.prettify)

#<a>테ㅐ\그를 변수 a1에 할당
a1 = soup.html.a
print(a1)
print(a1.string)
print(a1.attrs)
print(type(a1.attrs))
print(a1['href'])


# In[20]:


import urllib.request as req #스크래핑
from bs4 import BeautifulSoup #크롤링
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
res = req.urlopen(url).read()
############################ 이곳까지가 스크래핑
soup = BeautifulSoup(res, "html.parser")
# print(soup)
title = soup.title
#print(title)


title = soup.find("title").string
print(title)
wf = soup.find("wf").string
print(wf)


# In[110]:


html = """
<html><body>
<div id="meigen">
  <h1>위키북스 도서</h1>
  <ul class="items">
    <li>유니티 게임 이펙트 입문</li>
    <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
    <li>모던 웹사이트 디자인의 정석</li>
  </ul>
</div>

<
</body></html>
"""
soup = BeautifulSoup(html, "html.parser")
### CSS 선택자 사용하기
h1 = soup.select_one("div#meigen > h1").string
print(h1)
li_list = soup.select("div > ul.items > li")
print(li_list)
print(type(li_list))
print(li_list[0].string)
for li in li_list:
    print(li.string)


# In[21]:


url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
price = soup.select_one("div.head_info > span.value").string
print("usd/krw = ", price)
prices = soup.select("div.head_info > span.value")
for pri in prices:
     print(pri.string)
        
prices = soup.select("#exchangeList > li.on > a.head.cny > div > span.value")
print(prices)
'''
price = soup\
          .select_one("#exchangeList > li.on > a.head.cny > div > span.value")\
          .string
print(price)
'''


# In[25]:


import requests
from bs4 import BeautifulSoup
import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt


# In[11]:


import requests
from bs4 import BeautifulSoup
import pandas
import matplotlib as mpl
import matplotlib.pyplot as plt

source = requests.get("https://www.weather.go.kr/weather/observation/currentweather.jsp")


soup = BeautifulSoup(source.content,"html.parser")
#print(soup.prettify()) 

table = soup.find("table",{'class' : 'table-col'})
# print(table)
data = []

print("*" * 30)
print("오늘 각 지역의 날씨")
print("*" *30 )


###크롤링
#print(type(table)) # bs4.element.Tag
for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds:
        if td.find('a'):
            point = td.find('a').text
            temp = tds[5].text
            humidity = tds[10].text
            #print("{0:<7}{1:<7} {2:<7}".format(point, temp, humidity))
            data.append([point, temp, humidity])
#print(data)
with open('weather.csv', 'w', encoding='utf-8') as f:
    f.write('지역, 온도, 습도\n')
    for i in data:
        f.write("{0},{1},{2}\n".format(i[0], i[1], i[2]))
    
###분석
df = pandas.read_csv('weather.csv', index_col='지역', encoding='utf-8')
city_df = df.loc[['서울','인천','대전','대구','광주','부산','울산']]
#print(city_df)

font_name = mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\malgun.ttf').get_name()
mpl.rc('font',family=font_name)


ax = city_df.plot(kind='bar',title='날씨',figsize=(12,4),legend=True,fontsize=15)
ax.set_xlabel('도시',fontsize=15)
ax.set_ylabel('기온/습도',fontsize=15)
ax.legend(['기온','습도'],fontsize=15)
 
plt.show()


# In[ ]:


#python  기본 자료형 : 자료 정수,실수, 문자열, 리스트, 튜플, 딕셔너리, 집합, 부울
#numpy : 자료형 : numeric python : 숫자를 다루는 파이썬 : 숫자 배열 자료형


# In[13]:


import numpy
num = numpy.random.randint(10)
print(num)


# In[14]:


import numpy as np
num = np.random.randint(10)
print(num)


# In[18]:


#0~9 사이의 수로 크기가 6인 1차원의 배열을 만드시오
num = np.random.randint(10, size=6)
print(num)
l = [1,2,3,4,5,6]
print(l)
print(l[4])
print(num[4]) #1차원 배열 리스트처럼 index를 사용한다.


# In[20]:


# 0~9 사이의 수인 크기가 2행 3행인 2차원 배열을 반드시오
num2 = np.random.randint(10, size=(2,3))
print(num2)
l2 = [[7,2,8], [9,6,7]]
print(l2)


# In[22]:


num1 = np.random.randint(10, size = 6)
num3 = np.random.randint(10, size = (1,6))
print(num1)
print(num3)


# In[24]:


print(num)
print(l)
print(num[2])
print(l[2])
print(num[-4])
print(l[-4])


# In[25]:


# slcing
# [3 5 6 6 1 5]  : 배열
#  1 2 3 4 5 6  : 열번호
# [1, 5, 6, 6, 9, 1] : 리스트
# 1 2 3 4 5 6 : 인덱스
print(l[0:4])  #[1, 2, 3, 4]
print(num[0:4]) #[0 3 4 4]
print(l[0:6:2]) # [1, 3, 5]
print(num[0:6:2]) #[0 4 0]
print(l[:4]) #[1, 2, 3, 4]
print(num[:4]) #[0 3 4 4]
print(l) #[1, 2, 3, 4, 5, 6]
print(num) #[0 3 4 4 0 5]
print(l[:]) #[1, 2, 3, 4, 5, 6]
print(num[:]) #[0 3 4 4 0 5]
#reverse
print(l[::-1]) # [6, 5, 4, 3, 2, 1]뒤에서 부터 출력
print(num[::-1]) #[5 0 4 4 3 0]
# indexing이나 slicing은 리스트나 1차원 배열은 같다.


# In[26]:


print(l) #[1, 2, 3, 4, 5, 6] 
print(num) #[0 3 4 4 0 5]


# In[28]:


#숫자바꾸기
l[1] = 20 # index를 사용해서 요소값 변경
num[1] = 20 #열번호를 이용해서 요소값 변경
print(l)
print(num)


# In[29]:


print(num2)
#  0 1  2  열
#[[4 7 6]  0행 -2행
#[9 2 2]] 1행 -1행

print(l2)
#[[7,2,8],[9,6,7]]
#     0       1
#     2       1   -
#  0 1 2    0 1 2
#  3 2 1-   3 2 1 -


# In[30]:


print(l2[0][1])  #2
print(num2[0][1]) # 리스트 형식
print(num2[0,1]) # 배열 형식 num2[행, 열]
# print(l2[0,1]) #리스트에서는 배열 형식을 사용하지 못함

print(l2[-2][-2]) # 리스트 형식
print(num2[-2][-2]) # 리스트 형식
print(num2[-2,-2]) # 배열 형식 [행, 열]


# In[40]:


num3 = np.random.randint(10, size = (3, 4))  #3행 4열
num3

l3 = np.random.randint(10, size = (3, 4))  #3행 4열
l3



# In[41]:


print(num3)
print(l3)


# In[44]:


print(l3[1]) #index 1
print(num3[1]) # 1행
print(l3[1][1:3]) 
print(num3[1][1:3]) # 리스트형
print(num3[1,1:3])  #배열형식
#print(l3[1 , 1:3]) #리스트에서는 배열형식을 사용할 수 없다

print(l3[0:2])
print(num3[0:2]) #0행과 1행을 가져와라
#[[7 0 0 6]
# [1 2 3 3]]
print(l3[2][0:2]) #8, 9
print(num3[2][0:2]) # 2행에서 0열부터 1열까지 : 8 9
print(num3[2, 0:2])


# In[59]:


a = 1000000000000000
print(l3) #[[1 3 4 7] [9 8 6 4] [6 9 5 5]]
print(num3) #[[9 1 4 7] [3 7 5 3] [2 6 4 4]]
print(l3[0:2][1:3]) #[[9 8 6 4]]
print(num3[0:2][1:3]) #[[3 7 5 3]]
print(num3[0:2,1:3]) #[[1 4][7 5]]
print(l3[0][::2])
print(num3[0][::2])
print(num3[0,::2])
print(l3[::2][::2])
print(a)
print(num3[::2][::2])
print(a)
print(num3[::2, ::2])

### 모든 행에서 열을 한칸씩 건너 띄우기
print(num3[:, ::2])
### 행을 한칸씩 건너 띄우고 열은 모두 출력
print(a)
print(num3[::2, :])
print(a)
print(num3[::1, :])


# In[74]:


print(num)
print("num")
print(num[::-1])
print("num[::-1]")
print(l3)
print("l3")
print(l3[::-1])
print("l3[::-1]")
print(num3)
print("num3[::-1]")
print(num3[::-1])
print("num3[:,::-1]")
print(num3[:,::-1])


# In[76]:


#행과 열을 모두 거꾸로 출력
print("num3[::-1, ::-1]")
print(num3[::-1, ::-1])
print("num3[:,0]")
print(num3[:,0])
print("num3[:,3]")
print(num3[:,3])
print(l3)
print(l3[:][1])


# In[84]:


### 배열을 만드는 방법
i = np.random.randint(10, size=(3, 3))
# arange()
i2= np.arange(9).reshape(3,3) #  0~8까지 9개의 수를 가지는 2차원 배열
print(i2)
# i2= np.arange(10).reshape(3,3) # 에러생김 숫자의 갯수와 배열의 크기는 같아야 한다. 
i3 = np.arange(12).reshape(3,4)
print(i3)
i4 = np.arange(12).reshape(4,3)
print(i4)
#  11~ 19까지 수를 가지는 2차원 배열
i5 = np.arange(11, 20).reshape(3,3)
print(i5)
# 1~3까지의 수를 가지는 1행짜리 2차원배열
i6 = np.arange(1, 4).reshape(1,3)
print(i6)
# 1~3까지의 수를 가지는 3행짜리 2차원배열
i7 = np.arange(1, 4).reshape(3,1)
print(i7)
# 1~3까지의 수를 가지는 1차원배열
i8 = np.arange(1, 4).reshape(3)
print(i8)
i9 = np.arange(1,9).reshape(2,2,2)
print(i9)

i10 = np.arange(1,17,2).reshape(2,2,2)
print(i10)


# In[87]:


# array()
# 2,5,7을 가지는 1차원 배열을 만드시오.
ii1 = np.array((2,5,7))
print(ii1)
# [[1,2,3],[4,5,6],[7,8,9]]을 가지는 2차원배열 만들자.
ii2 = np.array(([1,2,3],[4,5,6],[7,8,9]))
print(ii2)
# [[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]]
#                     0행     1행       2행
#                  0 1 2   0 1 2   0 1 2   열
ii3 = np.array( [[[1,2,3],[4,5,6],[7,8,9]], # 0면
                 [[1,2,3],[4,5,6],[7,8,9]], # 1면
                 [[1,2,3],[4,5,6],[7,8,9]]])# 2면
print(ii3[0,1,2]) #6출력 ㅣ 0열, 1행, 2번째
print(ii3)
print(ii1[0]) # 열
print(ii2[1, 2]) # 행 , 열
print(ii3[1, 2, 2]) # 면, 행, 열


# In[ ]:


#배열을 만드는 방법 : 3가지방법
#random, arrange, array 사용방법


# In[92]:


ll1 = [1,2,3]
ll2 = [4,5,6]
ll3 = [1,2,3] + [4,5,6]
print(ll3)
print(ll1)
ll1.extend(ll2)
print(ll1)


# In[101]:


x = np.array([1, 2, 3]) # 1차원 배열
y = np.array([3, 2, 1]) # 1차원 배열
print(x)
print(y)
z = x + y #덧셈의 결과가 나타남 [4 4 4]
print(z)
z = np.concatenate((x,y))
print(z)
v = [99,99,99] # 리스트
z = np.concatenate((x,y,v))
print(z)


# In[104]:


l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]
z = np.concatenate((l1,l2,l3))
print(z)
z = np.concatenate(([1,2,3],[4,6],[7,8,9]))
print(z)


# In[116]:


x2 = np.array([1, 2, 3])   # 1차원 배열
grid = np.array([[9, 8, 7], 
                 [6, 5, 4]]) # 2차원 배열
grid1 = np.array([[9, 8, 7], 
                 [6, 5, 4]])
#z = np.concatenate((x2,grid)) #에러생김 <=차원이 다르면 합쳐지지 않음
z = np.concatenate((grid, grid1), axis = 0) #밑으로 붙는다
print(z) #열의 크기 일치해야됨
z = np.concatenate((grid, grid1), axis = 1)#옆으로 붙는다
print(z)

grid3 = np.array([[9, 8], 
                 [6, 5]])
z = np.concatenate((grid, grid3), axis = 1) #옆으로 붙는다
print(z) #행의 크기가 일치해야된다


# In[119]:


# 차원이 서로 다른 경우
#1차원 배열과 2차원 배열의 열의 크기가 일치해야 한다.
z = np.vstack([grid, x2]) # 열의 크기가 다르면 합쳐지지 않는다.
print(z)
z = np.vstack([x2 ,grid]) # axis = 0 , x축기준
print(z)

y2 = [[10],[20]]
z = np.hstack([y2, grid]) # 행의 크기가 다르면 합쳐지지 않는다. # axis = 1,  y축기준
print(z)
#행의 크기가 다르면 합쳐지지 않는다 #axis = 1


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




