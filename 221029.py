#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[5]:


import pandas as pd


# In[7]:


import matplotlib as mpl


# In[8]:


# indexing 1[][] m[3, 3]
# slicing 1[1:3] m[1:3, 2:3]
#유니버설 함수(UFuncs)
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
print(l3)


# In[18]:


import numpy
x = np.arange(4)
y = np.arange(4)
print(x)
print(y)
z = x + y #유니버셜 함수
print(z)
z = x - y
print(z)
z = np.add(x,y)
print(z)
z = np.subtract(x, y)
print(z)


# In[24]:


#print(l1)
#z = l1 + 3

print(x)
print(y)
z = x + y #둘이 같은 크기인 4개씩 있으니 연산이 가능함
print(z)
z = x + 5 # [0 1 2 3] + [5 5 5 5]
          #+ [5 5 5 5] 브로드캐스팅 : 배열연산을 할려면 크기가 같아야되기에 
          #5가 4번 나열되도록, 같은수로 만들어 주는것을 브로드캐스팅이라고 함
print(z)


# In[29]:


a = np.arange(3)
print(a)
b = a[:, np.newaxis] #newaxis : x축으로된 나열을 y축 나열로 변경시킴
print(b)

z = a + b # [ 0 1 2] +[[0][0][0]
           #[0 1 2]   [1][1][1]
          #[0 1 2]   [2][2][2]] #계산하기 위해 크기를 맞주는 브로드캐스팅
M = np.ones((3,3))
print(M)
z = a + M #[0 1 2 ] + [[1 1 1]
                     #[1 1 1]
                     #[1 1 1]]
print(M)


# In[39]:


##집합함수
M = np.random.random((3,4)) # 0~1사이의 값
M
np.sum(M)
M.sum()
print(sum(M)) #python
print(np.sum(M))  #numpy



# In[ ]:


get_ipython().run_line_magic('timeit', 'sum(M)')
get_ipython().run_line_magic('timeit', 'np.sum(M)')


# In[54]:


print(M.max())                        # 4사분위
print(M.min())                        # 0사분위
print(M.mean()) #평균
print(np.median(M)) #중앙값 min0과 max100의 중앙값은 50. 평균은 50아닐 확률이 높음
print(np.percentile(M, 25)) #25%      # 1사분위
print(np.percentile(M, 50)) #중앙값   # 2사분위
print(np.percentile(M, 75))           # 3사분위
print(M.std())  #표준편차


# In[14]:


import pandas as pd
import numpy as np
data = pd.read_csv("https://raw.githubusercontent.com/SoongMoo/soldesk220924/main/%EC%B0%B8%EA%B3%A0%EC%9E%90%EB%A3%8C/NumPy/data/president_heights.csv")
heights = np.array(data['height(cm)'])
print(heights)
print(heights.min())                           #163 0사분위
print(np.percentile(heights, 25))              #1사분위
print(np.median(heights))            #182.0   #2사분위  중앙값
print(np.percentile(heights, 75))    #183.0   #3사분위
print(heights.max())  #193                   #4사분위
print(heights.std())   #6.931843442745892    #표준편차
print(heights.mean())  #179.73809523809524   #평균값
 


# In[64]:


heights


# In[243]:


#분포도
import matplotlib.pyplot as plt
import seaborn
seaborn.set()
plt.hist(heights)
plt.xlabel('heights')
plt.ylabel('number')


# In[29]:


# 팬시 indexing, 마스크
x = np.array([1,2,3,4,5])
x 
print(x > 3) # 팬시 indexing : [False True]값으로 불러오는것
print(np.greater(x, 3)) # 팬시 index
print(np.sum(x>3)) #3보다 큰것의 갯수는?
                   #비교연산자를 사용하면 팬시 index를 사용할 수 있다
print(np.sum([False, False, False,  True,  True]))
print(x < 3)
print(np.less(x, 3))
print(x <= 3)
print(np.less_equal(x, 3))
print(x >= 3)
print(np.greater_equal(x, 3))
print(x == 3)
print(np.equal(x, 3))
print(x != 3)
print(np.not_equal(x, 3))


# In[37]:


#마스크
# x에서 3보다 큰 값을 가지고 오시오
print(x)
print(x>3)
print(x[x>3]) #팬시 index를 이용해서 true 요소인 요소만 가져오기
print(x[[False, False, False,  True,  True]])
print(np.sum(x[[False, False, False,  True,  True]]))
print(np.sum(x[x>3]))
x1 = np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]])
#5를 초과하는 값은 몇개입니까?
print(x1 > 5)
print(sum(x1 > 5))
print(np.sum(x1 > 5))


# In[53]:


# 정렬
x = np.array([2,1,4,3,5])
#np.sort(x)
print(np.sort(x)) #정렬해서 출력
print(x)
x.sort() # 정렬해서 다시 저장
print(x)
x = np.random.randint(0, 10, (4,6))
print(x)
print(np.sort(x, axis = 1)) #1: 행단위, y축 기준
print(np.sort(x, axis = 0)) #0: 열단위  x축 기준 : 면단위는 axis = 2


# In[55]:


#파티션 나누기
print(x)
#작은수 3개를 앞으로 나머지는 뒤로
#열단위에서, x축 기준
print(np.partition(x, 3, axis = 0)) #순서는 없다
#행단위에서, y축 기준
print(np.partition(x, 3, axis = 1)) #순서는 없다


# In[60]:


##판다스
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/SoongMoo/soldesk220924/main/data/gapminder.tsv", sep = "\t")
df


# In[61]:


df.head() #위에서 5개만 출력
df.head(n = 3) #위에서 부터 n개만큼 출력
df.head(n = 10)
df.head(10)


# In[62]:


print(df.head()) #위에서 5개만 출력
print(df.head(n = 3)) #위에서 부터 n개만큼 출력
print(df.head(n = 10))
print(df.head(10))


# In[66]:


df.tail()  #()빈공간은 마지막에 5개를 뜻함
df.tail(n = 3)  #마지막부터 n개
df.tail(n = 10)
df.tail(10)


# In[70]:


df.tail(10)


# In[71]:


df.tail(n = 10)


# In[75]:


l = [1,2,3,4]
s = "pandas"
print(type(l))
print(type(s))
print(type(df))


# In[87]:


##크기
print(len(l))
print(len(s))
print(len(df))  #행의 갯수, Searis의 갯수
print(df.shape) #데이터프레임의 행과 열의 갯수 (1704, 6) 튜플형식
#                                                 0     1
#행의 갯수만 출력
print(df.shape[0])
#열의 갯수만 출력
print(df.shape[1])

#각 열의 이름
print(df.columns)
#각열의 자료형
print(df.dtypes)
#데이터프레임의 정보 확인
print(df.info())
#country       object 문자열
#continent     object
#year           int64 정수
#lifeExp      float64 실수
#pop            int64
#gdpPercap    float64
#dtype: object


# In[81]:


i = 3
i
s = "string"
s
l = [1,2,3]
l
t = (1,2,3)
t


# In[97]:


dic = {"country" : "Afghanistan", "continent" : "Africa"}
dic['country']
df['country']
df['continent']



# In[98]:


df.head()


# In[99]:


df


# In[101]:


#country 컬럼의 값을 출력
df['country']
#country 컬럼의 값에서 5개만 출력
df['country'].head()
df['country'].tail()


# In[103]:


type(df['country']) 
# 데이터프레임에서의 열은 Series이다
#데이터프레임은 Series의 집합체이다
df


# In[106]:


#country 컬럼을 출력하세요
df['country']

#country 컬럼과 lifeExp컬럼을 출력하세요 : 리스트로 묶어서 출력하기
df[['country', 'lifeExp']]
df[['country', 'lifeExp']].head() #위 아래 행 출력
df[['country', 'lifeExp']].tail() #위 아래 행 출력

# 리스트에 열이름 추가해서 출력
df[['country', 'gdpPercap', 'lifeExp']]


# In[107]:


#열(컬럼)을 출력하려면 df[]에 기입하기
df['country']
#특정행을 출력하려면 df.loc[]에 기입하기 ,시리즈로 가지고 옴
df.loc[0]


# In[108]:


df.loc[0]


# In[109]:


#101번째의 행의 데이터를 가지고 오시오
df.loc[100]


# In[111]:


#마지막 행의 데이터를 가지고 오시오
df.loc[1703]
df.loc[len(df) -1]


# In[112]:


df.loc[len(df) -1]


# In[113]:


df.iloc[-1] #뒤에서부터,, -1은 가상인텍스로 iloc를 사용함


# In[129]:


df.loc[100] #명시적 인텍스
df.iloc[100]#loc는 실제번호 사용시, iloc는 가상인덱스로 암시적 인덱스번호
df.shape
df.shape[0]
#df[df.shape[0] - 1]


# In[115]:


df.iloc[100]  


# In[116]:


print(df.shape)


# In[130]:


number_of_rows = df.shape[0]
print(df[number_of_rows - 1])


# In[133]:


df
df['country'] #Series
#'country', "year", "gdpPercap"의 컬럼
df[['country',"year", "gdpPercap"]] #다른 따옴표 사용해도 괜찬음
#파이썬 자료형에 
#리터널 자료형
#정수 리터널 : 10, 2
#실수 리터널 : 10.5, 2.0
#문자열 리터널 : "a", 'a', '''a'''   a(변수)
#판다스 : 파이썬 딕셔너리로 데이터 프레임 만듬


# In[141]:


df
df.loc[0]  #searis
#0, 10, 100번재 열을 가져오기
df.loc[[0,10,100]] #dataFrame
#행의 값을 갖고 올때는 암시적 index 사용
df.iloc[[0,10,100]]


# In[149]:


x1
x1[1:3]
print(x1)
print(x1[1:2])
df
df.loc[1:4] #명시적 index인 경우 실제 번호까지 사용
df.iloc[1:5] #암시적 index인 경우
df.loc[1:4, :]
df.iloc[1: 5, :]


# In[155]:


df.iloc[1:4]


# In[168]:


#전체 행에서 컬럼 country 와 year 와 pop
df[['country', 'year', 'pop']]
df.loc[:, ['country', 'year', 'pop']]
df.loc[:, ['country', 'year', 'pop']].head()
subset = df.loc[:, ['country', 'year', 'pop']]
subset.head()
# 0~100에서 컬럼 country와 year
df.loc[0:100,['country', 'year', 'pop']]


# In[169]:


df


# In[175]:


'''
       0         1       2        3       4         5
	country	continent	year	lifeExp	  pop	    gdpPercap
0	Afghanistan	Asia	1952	28.801	 8425333	779.445314
1	Afghanistan	Asia	1957	30.332	 9240934	 820.853030
2	Afghanistan	Asia	1962	31.997	 10267083	853.100710
3	Afghanistan	Asia	1967	34.020	 11537966	836.197138
4	Afghanistan	Asia	1972	36.088	 13079460	739.981106
...	...	...	...	...	...	...
1699	Zimbabwe	Africa	1987	62.351	9216418	706.157306
1700	Zimbabwe	Africa	1992	60.377	10704340	693.420786
1701	Zimbabwe	Africa	1997	46.809	11404948	792.449960
1702	Zimbabwe	Africa	2002	39.989	11926563	672.038623
1703	Zimbabwe	Africa	2007	43.487	12311143	469.709298
'''
 #행과 열 모두 가상번호로 세기에 암시적인 iloc을 사용해야만됨
df.iloc[:, [0,2,3]]
df.iloc[0:101, [0,2,3]]
df.iloc[[0,10,100], [0,2,3]]
df.iloc[:, 0:5] #위아래 전체 행과, 1~5번째 열까지
df.iloc[:, range(5)] #df.iloc[:, 0:5]와 동일


# In[178]:


#위에서 부터 5개
df.head()
df.loc[0:4]
df.iloc[0:5]
df.loc[0:4, :]
df.iloc[0:5, :]
df.iloc[range(5), :]


# In[179]:


## 10번부터 5개 행을 가져오시오
df.loc[11:15]
df.iloc[10:10+5]
df.iloc[range(10, 15)]


# In[184]:


df.loc[11:15]


# In[189]:


#모든 행에 대해 3번열부터 3개의 열을 가져오시오
df.iloc[:, 3:6]
df.iloc[:, range(3,6)]


# In[193]:


#열을 0부터 5까지 중 한칸씩 뛰어서 가져오시오
df.iloc[:, 0:6:2]


# In[192]:


df.iloc[:, range(0,6,2)]


# In[196]:


#행과 열을 한칸씩 뛰어서 가져오시오
df.iloc[0:20:2, 0:6:2]
df.iloc[range(0,20,2), range(0,6,2)]


# In[200]:


#0행부터 100의 행을 두칸씩 띄우고 열은 하나씩 건너서 출력
df.iloc[0:101:3, ::2]
df.iloc[range(0,101,3), ::2]


# In[202]:


#0,99,999행과 0,3,5열을 출력하시오
df.iloc[[0,99,999],[0,3,5]]
df.loc[[0,99,999],['country','lifeExp','gdpPercap']]


# In[203]:


#10행부터 3개를 가져오고
#컬럼은  'counrty', 'lifeExp', 'gdpPercap'을 출력하시오
df.loc[10:13, ['country','lifeExp','gdpPercap']]


# In[204]:


df


# In[213]:


df['year']
df['year'] == 1952
sum(df['year'] == 1952)
##1952년도 평균수명 평균은?
df[df['year'] == 1957].mean()['lifeExp']


# In[219]:


#년도별 평균수명에 대한 평균
df.groupby('year')['lifeExp'].mean()
df.groupby('year')['lifeExp'].min()
df.groupby('year')['lifeExp'].max()

grouped_year_df.groupby('year')
mean_lifeExp_by_year = grouped_year_df['lifeExp']


# In[226]:


#년도별 각 대륙의 평균 수명의 평균
df.groupby(['year', 'continent']).mean()['lifeExp']
df.groupby(['year', 'continent'])['lifeExp'].mean()


# In[228]:


df.groupby(['year', 'continent']).mean()['lifeExp']


# In[230]:


#년도별 지역의 gdp에 따른 평균수명에 대한 평균은?
df.groupby(['year', 'continent'])['gdpPercap', 'lifeExp'].mean()


# In[ ]:


#년도별 지역의 gdp에 따른 평균수명에 대한 평균은?
df.groupby(['year', 'continent'])['gdpPercap', 'lifeExp'].mean()


# In[245]:


import pandas as pd
import matplotlib as plt
#년도별 평균 수명의 평균을 구하시오
grouped_year_df = df.groupby('year')
mean_lifeExp_by_year = grouped_year_df['lifeExp']
mean_lifeExp_by_year_mean = mean_lifeExp_by_year.mean()

mean_lifeExp_by_year_mean.plot


# In[247]:


##대륙에 대한 나라의 갯수
df
df.groupby('continent').country.nunique()
df.groupby('continent')['country'].nunique()


# In[251]:


#Series : 명시적 index를 가지는 1차원 배열, 다른 유형의 데이터도 가짐
x = np.array([1,2,3,4])
x
print(x[0]) #암시적 index
s = pd.Series(['banana', 42, 1500])
print(s)


# In[253]:


s = pd.Series(['banana', 42, 1500], index = ['goodName', 'qty', 'price'])
print(s)
s[0]  # 암시적 index
s['goodName'] #명시적 index


# In[255]:


###dataFrame
dic = {'Name': ['이승무','이상범','이장법'],
      'age' : [50,9,18],
      'born': ['1999-10-25', '2000-05-15', '2001-11-15']}
dic['Name']


# In[262]:


df = pd.DataFrame(dic)
df
df['Name']


# In[264]:


df = pd.DataFrame(dic, index = ['a', 'b', 'c'])
df
df.loc['a']


# In[265]:


df


# In[269]:


df = pd.DataFrame({'Name': ['이승무','이상범','이장법'],
      'age' : [50,9,18],
      'born': ['1999-10-25', '2000-05-15', '2001-11-15']}, index = ['a', 'b', 'c'])
df
df.loc['a']
df.iloc[0]


# In[272]:


df = pd.DataFrame({'Name': ['이승무','이상범','이장법'],
      'age' : [50,9,18],
      'born': ['1999-10-25', '2000-05-15', '2001-11-15']}, 
                  index = ['a', 'b', 'c'],
                 columns=['Name', 'born', 'age'])
df


# In[305]:


from collections import OrderedDict
df=pd.DataFrame(OrderedDict([
                ('Name', ['이숭무','이상범','이장범']),
                ('age' , [50,19,18]),
                ('born', ['1999-10-25', '2000-05-15','2001-11-15'])
                ]),
               index = ('a','b','c'))


df


# In[288]:


#행번호 가져올 대
df.index
#컬럼명을 가져올 대
df.keys()
df


# In[291]:


df.loc['a']
#type(df.loc['a'])
df.loc['a'].index
df.loc['a'].keys()


# In[292]:


df.loc['a'].keys()


# In[314]:


df
#df에서 나이만 출력
df.loc[:, 'age']
df['age']
df
#'이상범'의 나이를 출력하시오
df.loc['b', 'age']
df.iloc[1,1]
#나이의 평균, 최소값, 최대값, 표준편차를 구하시오
df['age'].mean()
df['age'].min()
df['age'].max()
df['age'].std()


# In[318]:


df['age'].mean()


# In[334]:


df=pd.read_csv('https://raw.githubusercontent.com/SoongMoo/soldesk220924/main/data/scientists.csv')
df
df['Age'].mean()
df['Age'].min()
df['Age'].max()
df['Age'].std()


# In[338]:


#평군나이보다 많은 사람을 출력하시오
df['Age'] > df['Age'].mean()
df[df['Age'] > df['Age'].mean()]
df[[False,True,True,True,False,False,False,True ]]


# In[337]:


df['Age'] > df['Age'].mean()


# In[339]:


df[[False,True,True,True,False,False,False,True ]]


# In[341]:


#평균 나이보다 많은 사람을 출력시 나이만 출력
df['Age'][[False,True,True,True,False,False,False,True ]]
df['Age'][df['Age'] > df['Age'].mean()]


# In[342]:


df['Age'][df['Age'] > df['Age'].mean()]


# In[345]:


#브로드케스팅
s = pd.Series(range(9))
s         #Series
#0    0   0    37
#1    1   1    61
#2    2   2    90
#3    3   3    66
#4    4   4    56
#5    5   5    45
#6    6   6    41
#7    7   7    77
#8    8    8    8행없음 Nan으로 표현됨


# In[346]:


df['Age'] #Series


# In[348]:


df['Age']
df['Age'] + s # index 가 같은 것 끼리 연산
#S에는 8행이 있으나 Age에는 8행이 없어 Nan 으로 나타남, 빈곳에 Nan이 채워짐=확장됨(브로드캐스팅)
df['Age'] + 20 # 모든 빈행에 20이 채워져 더해짐, 브로드케스팅됨


# In[357]:


df['Age']
print(df['Age'])
ev_df = df['Age'].sort_index(ascending = False) #데이터를 reverse
ev_df
print(ev_df)
df['Age'] + ev_df


# In[359]:


#데이터프레임 다루기
# 0, 1, 3행을 출력하시오
df
df.iloc[[0,1,3]]
df.loc[[True,True,False,True,False,False,False,False]]
df.iloc[[True,True,False,True,False,False,False,False]]


# In[369]:


df


# In[366]:


df['Age']


# In[367]:


df['Age'] * 2


# In[370]:


df


# In[371]:


df * 2


# In[372]:


df


# In[373]:


df.info()


# In[374]:


df['Born']


# In[376]:


df['Died']


# In[388]:


#날짜 빼기 연산
#df['Died'] - df['Born'] #문자열의 더하기는 가능해도 빼기는 되지 않음
#문자열의 연산자는 +, *  하지만 -, / 는 오류생김
Died = pd.to_datetime(df['Died'], format = "%Y-%m-%d")
Born = pd.to_datetime(df['Born'], format = "%Y-%m-%d")
(Died - Born) / 365
df['age_days_dt'] = (Died - Born) /365
df['Died_dt'], df['Born_dt'] = Died,Born
df
df.info()


# In[391]:


#DateFrame에서 열 삭제 : drop
df_drop = df.drop(['age_days_dt'], axis = 1)
df_drop


# In[392]:


df


# In[460]:


print(df_drop.columns)
print(df.columns)


# In[395]:


get_ipython().system('pip install xlwt')


# In[396]:


#엑셀파일로 저장
import xlwt #xls
df.to_excel("df.xls")


# In[399]:


get_ipython().system('pip install openpyxl')
df.to_excel('df1.xlsx')


# In[403]:


df_drop
df_drop.to_excel("df_drop.xlsx", index = False)


# In[417]:


df_drop
df_drop = df_drop.drop(['Born_dt'], axis =1)
df_drop


# In[413]:


df_drop
df_drop = df_drop.drop([0,1,3], axis = 0)
df_drop


# In[418]:


df_drop = df_drop.drop([2,4,6], axis = 0)
df_drop


# In[426]:


df1 = pd.read_csv("https://raw.githubusercontent.com/SoongMoo/soldesk220924/main/data/concat_1.csv")
df2 = pd.read_csv("https://raw.githubusercontent.com/SoongMoo/soldesk220924/main/data/concat_2.csv")
df3 = pd.read_csv("https://raw.githubusercontent.com/SoongMoo/soldesk220924/main/data/concat_3.csv")


# In[430]:


print(df1)
print(df2)
print(df3)


# In[433]:


row_concat = pd.concat([df1, df2, df3], axis = 0) #열이 확장
row_concat #열 이름이 같은 것 끼리 확장


# In[436]:


col_concat = pd.concat([df1, df2, df3], axis = 1) #행이 확장
col_concat  #행번호가 같은 것끼리 확장됨


# In[440]:


row_concat
row_concat.loc[0]
row_concat.loc[1]
row_concat.iloc[0]


# In[ ]:


#a5를 암시적 인덱스를 사용해서 출력하시오
row_concat
row_concat.loc[1]
row_concat.iloc[5]
row_concat.iloc[5,:]
row_concat.iloc[5,]


# In[446]:


row_concat.iloc[5,]


# In[456]:


#"n1", "n2" 'n3, 'n4'를 가지는 Series를 만드시오  new_row_series
new_row_series = pd.Series(['n1', 'n2', 'n3', 'n4'])
new_row_series
print(new_row_series)
print(df1)


# In[457]:


dataframe_series = pd.concat([df1, new_row_series], axis = 0)
dataframe_series  #열번호가 같은것끼지 합쳐지면서 빈공간에는  NaN이 기입됨 x축 기준


# In[458]:


dataframe_series = pd.concat([df1, new_row_series], axis = 1)
                                      #axis =1  행번호같은것끼리 붙음
dataframe_series 


# In[462]:


## 행 1개로 구성된 데이터프레임 생성
df4 = pd.DataFrame([['n1', 'n2', 'n3', 'n4']], columns = ['A', 'B', 'C', 'D'])
df4


# In[463]:


df1


# In[464]:


df4


# In[466]:


row_concat1 = pd.concat([df1, df4], axis = 0)#0 열이름이 갖은것끼리 붙임
row_concat1


# In[471]:


col_concat1 = pd.concat([df1, df4], axis = 1)
col_concat1
#NaN을 누락 값
df1 + df4


# In[474]:


df1, df4


# In[473]:


df1 + df4   #a01 + NaN = Nan 아는값에 모르는값을 더하면 모르는값이 됨


# In[476]:


row_df1 = df1.append(df4)#append : 열번호가 같은것끼리 합쳐짐
                        #dp.cpncat([df1, df4], axis = 0)과 같음
row_df1


# In[479]:


row_df2 = pd.concat([df1, df2, df3],ignore_index = True) #ignore있는것 제거
row_df2


# In[481]:


row_df3 = pd.concat([df1, df2, df3],ignore_index = True, axis = 1) #ignore있는것 제거
row_df3 #열번호 삭제


# In[489]:


df1, df2, df3


# In[496]:


df2.columns = ['E','F','G','H']
df3.columns = ['A','B','F','H']
df1, df2, df3


# In[500]:


row_concat2 = pd.concat([df,df2,df3])
row_concat2


# In[507]:


#열 이름이 일치하는 것끼리만 연결하기
df1, df3
df6 = pd.concat([df1, df3], join = 'inner')
df6


# In[508]:


df6 = pd.concat([df1, df3], join = 'inner', ignore_index =True)
df6


# In[518]:


print(df2.index)
print(df3.index)


# In[517]:


df2.index = [4,5,6,7]
df3.index = [0,2,5,7]
print(df2.index)
print(df3.index)


# In[519]:


df1, df3
df7 = pd.concat([df1, df3], join = 'inner', ignore_index =True, axis = 1)
df7


# In[524]:


site = pd.read_csv("https://raw.githubusercontent.com/SoongMoo/soldesk220924/main/data/survey_site.csv")
visited = pd.read_csv("https://raw.githubusercontent.com/SoongMoo/soldesk220924/main/data/survey_visited.csv")
survey = pd.read_csv("https://raw.githubusercontent.com/SoongMoo/soldesk220924/main/data/survey_survey.csv")
person = pd.read_csv("https://raw.githubusercontent.com/SoongMoo/soldesk220924/main/data/survey_person.csv")
print(site)
print(visited)
print(survey)
print(person)


# In[531]:


#같은 값끼리 병합하기, 데이터베이스의 join과 같음
#site 와 visit
site, visited
site_visited = site.merge(visited, left_on = "name", right_on = 'site')
site_visited


# In[534]:


#person, survey 병합을 하자
#설문조사를 한 사용자들을 출력하기
person, survey
person_survey = person.merge(survey, left_on='ident', right_on='person')
person_survey


# In[535]:


## 설문을 안한 사용자도 출력
person_survey_left  = person.merge(survey, left_on='ident', right_on='person',
                                   how='left')
person_survey_left


# In[536]:


person_survey_left  = person.merge(survey, left_on='ident', right_on='person',
                                   how='inner')
person_survey_left #how='inner'는 default
'''inner, outer, left, right'''


# In[549]:


#누락값 Nan # null : 누락값, 알수 없는 값
#Not a Number
#Nan 이 무엇인가?
from numpy import NaN, NAN, nan
print(NaN == True) #True도 아니고
print(NaN == False) #Fals도 아니고
print(NaN == 0) #0도 아니고
print(NaN == '') #공백도 아니고
print(NaN == None) #둘다 알수 없는 값이기에 ==이 안됨


# In[547]:


print(pd.isnull(NaN))#NaN은 null임
print(pd.isnull(30))
print(pd.notnull(30))#30은 null이 아님


# In[553]:


#데이터갯수 : Nan은 갯수에서 제외됨
visited.info()
visited


# In[554]:


#데이터갯수 : Nan은 갯수에서 제외됨
visited.count()
visited.shape[0]
print(visited.shape[0] - visited.count())


# In[555]:


num_legs = pd.Series({'goat': 4, 'amoeba': nan }) # 누락값을 갖는 시리즈
num_legs


# In[557]:


df = pd.DataFrame( {'Name':['이숭무','이상범','이장범'],
                   'age' :[50, 19, 18],
                   'born' : ['1999-10-25', '2000-05-15','2001-11-15'],
                    'missing' : [NaN,NaN,NaN]}) 
df


# In[558]:


df = pd.read_csv('https://raw.githubusercontent.com/SoongMoo/soldesk220924/main/data/gapminder.tsv',sep="\t")
df.count()


# In[559]:


###년도별 평균수명의 평균?
life_Exp = df.groupby(['year'])['lifeExp'].mean()
life_Exp


# In[560]:


life_Exp = df.groupby(['year'])['lifeExp'].mean()
life_Exp


# In[563]:


life_Exp = df.groupby(['year']).mean().lifeExp
life_Exp


# In[564]:


life_Exp = df.groupby(['year']).mean().lifeExp
life_Exp
life_Exp[1957]


# In[565]:


life_Exp.index


# In[568]:


#2000도 이후의 평균 수명
life_Exp.index > 2000
life_Exp[life_Exp.index > 2000]#마스크


# In[574]:


#2000년도 이전의 평균 수명
life_Exp.index > 2000
life_Exp[life_Exp.index > 2000] # 마스크
life_Exp[[False, False, False, False, False, False, False, False, False,
       False,  True,  True]] # 마스크


# In[575]:


#2000년도 이전의 평균 수명
life_Exp.index <= 2000
life_Exp[life_Exp.index <= 2000]


# In[ ]:


ebola.fillna(metho)


# In[ ]:





# In[ ]:





# In[ ]:




