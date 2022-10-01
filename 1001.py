#!/usr/bin/env python
# coding: utf-8

# In[13]:


#indexing과 slicing을 혼합해서 사용
a = [1,2,3, ['a', 'b', 'c'], 4, 5]
#    0 1 2     3             4  5
#            0  1   2

#[3, ['0', 'b', 'c'], 4]
# 0   1                2
#       0     1       2
print(a[2 : 2 + 3])
print(a[2 : 2 + 3][1])
print(a[2 : 2 + 3][1][2])
print(a[3])
print(a[3][0:2])
print(a[3][1:3])
print(a[3][1:])
print(a[-3][1:])
print(a[-3][-2:])


# In[ ]:


#리터널 상수
#       자연어 : 한국어, 중국어, 등등
#                 문자열로 표현_따옴료사용함: "a" '가' 문자를 따옴표 없이 사용하는 a 가 는 변수임
#        자연수 : 실수, 정수, 지수
#
#           실수 : 10.5, 100.77, 소숫점있는 수
#
#            "10.5":문자, floot("10.5") : 문자를 실수로 바꾼다는 명령
#            정수 : 10, 100, 150, "10" 문자, int("10)") 문자를 숫자로 바꾼다는 뜻

#리스트 : 여러개의 값을 가지기 위한 것, []대괄호
#          [] : 빈리스트
#          [1,2,3] : 정수리스트
#          ['a', 'b','c'] : 문자열 리스트
#          [1,2,3, ['a', 'b', 'c'], 4, 5] : 혼합형 리스트
#


# In[35]:


#문자열 다루기
number = 10.0
day = "three"
'''나는 10개의 사과를 먹어서 three일 동안 아팠습니다'''
a = "나는 %d개의 사과를 먹어서 %s일 동안 아팠습니다"%(number, day)
b = "나는 %s개의 사과를 먹어서 %s일 동안 아팠습니다"%(number, day)
c = "나는 {0}개의 사과를 먹어서 {1}일 동안 아팠습니다"                        .format(number,day)
d = "나는 {0}개의 사과를 먹어서 {e}일 동안 아팠습니다"                        .format(number,e = day)
g = f"나는 {number}개의 사과를 먹어서 {day}일 동안 아팠습니다"
print(a)
print(b)
print(c)
print(d)
print(g)


# In[40]:


str1 = "Life is"
str2 = 'too short'

print(str1 + " " + str2)

print("=" * 30)

a = [1,2,3]
b = ['aaa', 'bbb', 'ccc']

print(a + b) # +는 붙이기 연산자
print(len(a)) #요소의 갯수
print(a[1])
a[1] = 10 #리스트에서는 요소의 값을 indexing을 이용해서 변경할 수 있다
a[2] = 10
print(a)


# In[42]:


c = ['Life', 'is', 'too', 'short']
#"your Leg"
c[0] = "your leg"
c
#########참고###########
str1 = "Life is"
#    0123456
str1[0]
#str1[0] = 'L'(x) # 문자열의 문자는 변경할 수 없다
print(str1)
print(c)


# In[50]:


#리스트 함수
### 리스트에 요소추가
a = [1,2,3]
b = [4,5,6]

print(a +b)
print(a)
print(b)
a.append("too")
a.append([4,5,6])
print(a)

#리스트 확장
a.extend(b)
print(a)


#삽입
a.insert(3,['a','b','c'])
print(a)


# In[26]:


l = ['Life', 'is', 'too', 'short',1,2,3]
l[4]
del l[4]
print(l)

l[3: 3+2]
del l[3: 2 +2]
print(l)

l[2:]
del l[2:]
print(l)


# In[38]:


# 요소의 값을 이용해서 요소 삭제
l = ['Life', 'is', 'too', 'short',[1,4],2,3]
l.remove(2)
print(l)
l.remove([1,4])
print(l)


# In[54]:


#POP : 맨 뒤에서 부터 삭제
l = ['Life', 'is', 'too', 'short',[1, 4],2,3]
l.pop()
print(l)
l.pop()
print(l)
l.pop()
print(l)
l1=l.pop()
print(l1)
print(l)
l1 = l.pop(1)
print(l1)
print(l)
l.pop(0)
print(l)
# 삭제한 값을 대입하고 싶을 때 pop()


# In[65]:


l = [5,3,6,7,1,9,10]
print(len(l))
#정렬
#오름차순으로 정렬
l.sort()
print(l)
l=['나','가','라'] #사전순으로 정렬됨
l.sort()
print(l)

#내림차순으로 정렬
l.sort(reverse=True);
print(l)
l.reverse()  #정렬과 관계업싱 뒤에서부터 거꾸로 나열

a = [1,3,2,7,4]
a.reverse()
print(a)


# In[84]:


str3 = 'hobby'
#b 가 몇개일까?
str3.count('b')
print(str3.count('b'))
a = [1,2,3,4,5]
a.count(4)
print(a.count(4))
print(a)
str3.index('o')
a.index(3)
str3.index('b', str3.index('b') + 1)
print(str3.index('b', str3.index('b') + 1))


#str3.index('b', 4 + 1)
#a.index(4, a.index(4) + 1)
#print(a.index(4, a.index(4) + 1))

print(a.index(4))
print(a.index(4, 2))
print(str3.find('t')
print(str3.find('t')


# In[72]:


#자료형
#리터널 상수 : 문자열 자료형 
#리스트 자료형 : []
#듀플 자료형 : ()
t = (1234)
l = [1234]
s = "1234"
i = 1234


# In[85]:


l = [] #빈리스트
t = () #빈튜플 튜플=괄호
l = [1] #요소가 한개인 리스트
t = (1,) # 요소가 한개인 큐플에는 꼭 콤머를 찍어야됨
t = (1,2,3) # 요소가 여러개일때는 마지막에 콤머를 찍어줄 필요 없음
print(1)
print(a)
#() :  최우선 연산자
print(3 + 2 * 4)
print((3 + 2) * 4)


# In[95]:


l = [1,2,3,4]
t = (1,2,3,4)
t1 = (1,2,3,'a','b')
t1 = (1,2,3,'a','b', (1,2,3), [1,2,3])
l = (1,2,3,'a','b', (1,2,3), [1,2,3])
print(l[0])
print(t[0])
print(t1[0])
print(t1[-4])
print(l[3:3 +3])
print(t1[3:3 +3])
print(l[:4])
print(t1[:4])
print(l[4:])
print(t1[4:])


# In[134]:


t1 = (1,2,3,'a','b', (1,2,3), [1,2,3])
l = [1,2,3,'a','b', (1,2,3), [1,2,3]]
print(l[4:])
l[4] = 'c'  #리스트는 index를 이용해서 요소의 값을 수정
print(l)
print(t1[4])  
#t1[4] = 'c'#튜플은 index를 이용해서 요소의 값을 수정하지 못함

del l[4]
print(l)
#튜플은 indexing과 slicing만 가능
print(l.index('a'))
#find(x)
print(t1.index('a'))
print(t1)
l2 = list(t1)
print(l2)

t2 = tuple(l)
print(t2)
l = ['a','b','c']

"".join(l)
",".join(l)
print("".join(l))
print(",".join(l))

t1 = ['(1,2)', '(1,2)']
"".join(t1)
",".join(t1)
print("".join(t1))
print(",".join(t1))

t2 = ['가', '33']
"".join(t2)
",".join(t2)
print("".join(t2))
print(",".join(t2))

t= [1,2,4,3,3,2];
print(t.count(3))
print(3 + 3)
print(int("3") + int("3"))


# In[147]:


#자료형
#리터널 상수 : 문자열 자료형 : "", '', 정수형 자료형, 실수형 자료형
#리스트 자료형 : []
#튜플 자료형 : ()
#딕셔너리 자료형 : {}
l = [] #빈리스트
t = () # 빈 튜플
d = {} #빈 딕셔너리 
#딕셔너리 : 사전으로 단어(key)와 내용(value)가 있는것, 키와 값이 하나로 쌍으로 이루어진 것
#딕셔너리는 인덱스를 사용하지 못하고 키만 사용, 키는 숫자만 사용
# d = {k1:v1, k2:v2, ...., kn:vn}

dic = {'name':'이승무', 'phone':'0119993323', 'birth': '1118'}
l = [1,2,3]
print(l[0])
t = (1,2,3)
print(t[0])
print("="*30)
print(dic['name']) #요소를 가지고 올때  index를 사용하지 않고 key를 사용한다

d2 = {2: '이승무', 0:'이상범', 1:"이장법"}
print(d2[1])
print(d2[2])

l = [1,2,3,4]
l[1] = 5
print(l)
d2[1]='김찬중'
print(d2[1])

l[2] = 5
print(l)

d2[4]='박준현'
print(d2) #키가 존재하면 수정, 키가 없으면 추가됨

a = {1:'a', 1:'b'} #키가 앞과 동일하면 수정을 한셈이 됨. 첨에 1이 a로 저장되었으나 후에 b로 수정된셈임
print(a)


# In[153]:


l = [1,2,3,4,5,6]
del l[2]
print(l)
l.remove(6)
print(l)
l.pop(1)
print(l)

dic = {'name':'이승무', 'phone':'0119993323', 'birth': '1118'}
del dic['name']
print(dic)

dic[3] = '이상범';
print(dic)
del dic[3]
print(dic)


# In[171]:


dic = {'name':'이승무', 'phone':'0119993323', 'birth': '1118'}
dic['birth'] = '19991108'
print(dic)

dic = {'birth' : '19991108'}
print(dic)

print(dic['birth'][:4])
print(dic['birth'][4:4+2])
print(dic['birth'][6:6+2])

#월일만 같이 출력
print(dic['birth'][4:])
print(dic['birth'][-4:])

###딕셔너리 관련함수
dic = {'name':'이승무', 'phone':'0119993323', 'birth': '1118'}
###딕셔너리에 있는 키만 가져오기
print(dic.keys())
###딕셔너리에 있는 값만 가져오기
print(dic.values())
#키와 값을 쌍으로 묵어서
print(dic.items())
#딕셔너리 모두 삭제
dic.clear()
print(dic)
#f리스트 비우기
print(dic)
l = [1,2,3,4]
l.clear()
print(l)


# In[284]:


#변수에 있는 값을 서로 교환하기
a = 10
b = 20
#################
temp = b
b = a
a = temp
print(a, b)
a, b = b, a

print(a)
print(b)


# In[ ]:





# In[182]:


dic = {'name':'이승무', 'phone':'0119993323', 'birth': '1118'}
dic
#print(dic['name'])
print(dic)
dic[money] = ('3')
print(dic.get('money'))
del dic[money] # money 가 없어 에러생김
print(dic.get('money'))
print(dic.get('name'))
print(dic.get('money', 0))

dic1 = {'classic' : 500, "pop" : 600}
dic1 = {'classic' : 500, "pop" : 600, "money" : 100}


# In[190]:


dic1 = {'classic' : 500, "pop" : 600}
dic2 = {'classic' : 500, "pop" : 600, "money" : 100}
print(dic1['classic'])
print(dic1['classic'] + dic2['classic'])
print(dic1['pop'] + dic2['pop'])


# In[212]:


#자료형
#리터널 자료형 :  문자열형 자료형 : "", '',  정수형 자료형
#리스트 자료형 : []
#튜플 자료형 : ()
#딕셔너리 자료형 : {} : 빈 딕셔너리 존재함
#                {키:값, ....}
#집합 자료형 : {} : {1,2,3,4} : 빈공간은 안되고 요소가 1개 이상 존재해야만 됨
s = {1}
print(s)
dic = {1:1}
print(dic)
'''
{1} : 집합으로 봄
{1:1} : 딕셔너리 로 봄

'''
s = {1,2,3,4,5}
print(s)
s1 = set([1,2,3,4])
print(s1)
s2 = set((1,2,3,4))
print(s2) 
s5 = set("hello") #중복데이터는 허용하지 않는다
print(s3)

ㅣ = list({1,2,3,4})
print(1)
t = tuple({1,2,3,4})
print(t)
s5 = {'h','l', 'e', 'o', 'h'}
print(s5)
print("".join(s5))
print(t[0])


# In[ ]:





# In[216]:


####교집합, 합집합, 차집합, 인덱스틑 사용하지 않음

s1 = set([1,2,3,4,5,6,])
s2 = set([4,5,6,7,8,9])

#교집합 intersection
print(s1 & s2)

###합집합 union
print(s1 | s2) #집합 : 중복을 허용한함

###차집합 difference
print(s1 - s2)
print(s1.difference(s2)) 


# In[234]:


s1 = {1,2,3,4,5,6}
#요소 추가
print(s1)
s1.add(7)
print(s1)
'''
s1.add([8,9,10])
print(s1)
'''
s1.add((8,9,10)) #add는 요소 하나만 추가할 수 있음
print(s1)

s1.update((11,12,10))
print(s1)

s1.remove((8,9,10)) #remove는 요소 하나만 삭제할 수 있음
print(s1)

s1.remove((12)) 
print(s1)


# In[ ]:





# In[258]:


#자료형
#문자 자료형 : "", '',"""""", ''''''
#정수형 자료형 : 10
#실수형 자료형 : 10.6
#리스트 자료형 : []
#튜플자료형 : ()
#딕셔너리 자효형 : {}
#집합 자료형 : set : {1}
#부울 자료형 : True/ False
print("True") #문자열 자효형
print("True") #참
print("False") #False문자
print("False") #거짓

#문자연산
print("True" and "False")
print("A" and "B")
print("A" or "B")
#논리 연산 : 부울 타입끼리의 연산
print(True and True)  #True
print(True and False) # False
print(False and True) # False
print(False and False)# False

#비교(관계)연산 : 결과는 부울타입
print(1 + 1)
print(1 > 2)
print(1 < 2)
print(1 >= 2)
print(1 <= 2)
print(1 == 2)
print(1 != 2)
i = 2;
print(i == 2) #== : 같다
# print(i = 2)  #=:대입

#논리 연산 : 부울타입
i = 3
j = 4
y = 5
print(i > y and j < y) #논리연산 할때는 관계연산이 항상 같이 따라다님

print(True and False)

###2200s년은 윤년입니까?
### 4년마다 윤년, 단 100년마다는 윤년이 아님.400면마다는 윤년을 주어야됨
### 연산결과는 부울타입이 와야됨
print(2200 % 4 == 0 and 2200 % 100 != 0 or 2200 % 400 == 0)
print(1 + 1 * 5)

if 2200 % 4 == 0 and 2200 % 100 != 0 or 2200 % 400 == 0:
    print("윤년")
else :
    print("평년")


# In[275]:


print(bool(" ")) #공백문자
print(bool("")) #공blank
print(bool([1,2]))
print(bool([]))
print(bool((1,2)))
print(bool(1))
print(bool(-1))
print(bool(0))
print(bool("이승무"))
print(bool("ㅁㅁ"))


# In[277]:


#booL()함수
print(bool("이승무"))
if "이승무":
    print(True)
print(bool(" ")) #공백문자
print(bool("")) #공blank
print(bool([1,2]))
print(bool((1,2)))
print(bool(1))
print(bool(-1))
print(bool(0)) #False

print(bool("None"))

print(bool("이승무"))
print(bool("ㅁㅁ"))


# In[ ]:





# In[286]:


###파이썬 변수 선언법
a = 'python'
b = 'life'
(c, d)= ('python', 'life')
(c, d)= 'python', 'life'
c, d, e = 'python', 'life', 'is'
print(c,d)
print(c,d,e)
print("*" *30)


a = b = c = 0
print(a,b,c)

a, b = b, a
print(a,b)


# In[290]:


###3장 제어문
### bool 타입을 이용햇 원하는 결과를 얻어 오는 것을 말한다

# 조건문 / 반복문
# 조건문 : 여러가지 주에 하나를 선택할 때
#조건식 뒤에는  :클론  이 와야 한다
#수행문은 드려쓰기를 해야한다
#들여쓰기는 공백문자나  Tab키를 사용할 수 있으나 두가지 혼용할 수 없다
# 두개 중 하나만 선택해서 사용
#주로 Tab키를 사용한다
#조건문은 꼭 들여쓰기를 해주어야 실행됨
#들여쓰기 하지 않으먄 다른문으로 취급됨

'''
if 조건식: #결과가 True인경우의 
     수행문1
     수행문2
실행문 : 들여쓰기를 하지 않으며 조건문의 영향을 받지 않음
'''

if False:     #아래 실행되지 않음
    print("수행문1")
    print("수행문2")
    print("실행문")
    
if True:   #아래 실행됨
    print("수행문1")
    print("수행문2")
    print("실행문")

if False:
    print("수행문1")  #아래 실행되지 않음
    print("수행문2")  #아래 실행되지 않음
print("실행문")   #아래 따로 독립적으로 실행


# In[7]:


#단일 if문 : if문만 존재 : True일때만 실행
money = 3000
if money >= 3500:
    print("버스를 타고 간다.")
print("if문 종료")

money = 3000
if money >= 3500:
    print("버스를 타고 간다.")
else :
    print("aa")


# In[6]:


###false 일때도 실행되자
# if ~ else
money = 3000
if money >= 3500:
    print("차를 타고 간다")
else :
    print("걸어간다")
print("if문 종료")


# In[8]:


# and, or, not : 반대를 의미
print(not True)
print(not False)


# In[10]:


money = 2000
if not money >= 3500 : 
    print("걸어가시오")
else :
    print("차를 타고 가시오")


# In[25]:


#IN 연산자 사용하기 : 포함되어 있는지 물어볼 때 사용
l = [1,2,3,4,5]
print( 2 in l)
print( 7 in l)
print( 2 in [1,3,4,5])
print( 2 in [1,2,3,4,5])
print( 7 not in [1,2,3,4,5])
print('t' in 'python')
print('t' not in 'python')
print('z' in 'python')
print('z' not in 'python')

print("*" *30)
print( {'a':1, 'b':2})
print('a' in {'a':1, 'b':2})
print('a' not in {'a':1, 'b':2})

print("*" *30)
print(3 in {1,2,3,4,5})
print(3 not in {1,2,3,4,5})


# In[29]:


l = [1,2,3,4,5,6]
print(4 in l)
if 4 in l:
    print("리스트에 4가 포함되어 있다")
else:
    print("리스트에 4가 포함되어 있지 않다")
    
print("=" * 30)
if 7 not in l:
    print("리스트에 7이 포함되어 잇지 않다")
else:
    print("리스트에 7이 포함되어 있다")


# In[34]:


pocket = ['paper', 'card', 'money']
print('money in pocket')

if 'money' in pocket:
    print("주머니에 돈이 있습니다")
else:
    print("주머니에 돈이 없습니다")
    
    


# In[ ]:


mat = 55
eng = 70
kor = 40
result = ();
print(result)


# In[ ]:


pocket = ['paper', 'card', 'money']
print('money in pocket')

if 'money' in pocket:
    print("주머니에 돈이 있습니다")
else:
    print("주머니에 돈이 없습니다")


# In[ ]:





# mat = 55
# eng = 70
# kor = 40
# result = (mat + eng + kor) / 3 >= 60 and mat >=40 and eng >=40 and kor >=40;
# print(result)
# 
# if (mat + eng + kor) / 3 >= 60 and mat >=40 and eng >=40 and kor >=40 :
# print("합격)
# else:
#     print("불합격"
# 

# In[43]:


mat = 55 
eng = 70 
kor = 40 
result(mat + eng + kor) / 3 >= 60 and mat >=40 and eng >=40 and kor >=40; 
print(result)

if (mat + eng + kor) / 3 >= 60 and mat >=40 and eng >=40 and kor >=40 : 
    print("합격") 
else: 
    print("불합격")


# In[45]:


#score가 90이상이면 A, 80이상이면 B ...
#조건이 여러개인 경우
'''
if 조건식:
   수행식
elif 조건식:
   수행식
elif 조건식:
   수행식
elif 조건식:
   수행식

else :
  수행식
'''

#else문 뒤에는 조거식 올 수 없다
#조건식은 if 문 뒤에 와야 한다
#else if : elif
#다중 if문
score = 75
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else : 
    print('F')


# In[ ]:


###95이상이면 A+ 이하면 A
###85이상이면 B+ 이하면 B
###75이상이면 C+ 이하면 C
###65이상이면 D+ 이하면 D
###F


# In[47]:





# In[48]:


score = 75
if score >= 90:
    print('A+')
elif score >= 90:
    print('A')
elif score >= 85:
    print('B+')
elif score >= 80:
    print('B')
elif score >= 75:
    print('C+')
elif score >= 70:
    print('C')
elif score >= 65:
    print('D+')
elif score >= 60:
    print('D')
else : 
    print('F')


# In[49]:


score = 75
if score >= 90:
    if score >=95:
        print('A+')
    else :
        print('A')
elif score >= 80:
    if score >=85:
        print('B+')
    else :
        print('B')
elif score >= 70:
    if score >=75:
        print('C+')
    else :
        print('C')
elif score >= 60:
    if score >=65:
        print('D+')
    else :
        print('D')
else : 
    print('F')


# In[56]:


'''
score가 60이면 message 변수에 success를
아니면 messege에 failure를 저장한 후 출력하기
'''


score = 75
if score >= 60:
    message = 'success'
else:
    message = 'failure'
print(message)

print("==" * 30)
message = 'success' if score >= 60 else 'failure'
print(message)


# In[59]:


a = 10; b = 20; opt = 'add'
if opt == 'add':
    result = a + b
elif opt == 'sub' :
    result = a - b
elif opt == 'mul' :
    result = a* b
else :
    result = a / b
print(result)


# In[65]:


a = 10; b = 20; opt = 'mul'
if opt == 'add':
    result = a + b

elif opt == 'mul' :
    result = a * b
else :
    if opt == 'sub' :
        result = a - b
    else :
        if opt == 'mul' :
            result = a* b
        else :
            result = a / b
print(result)


# In[66]:


result = a + b if opt == 'add' else (
         a - b if opt == 'sub' else (       
         a * b if opt == 'mul' else a / b
      ))
print(result)


# In[68]:


c = 10; d = 20; 
result = c + d if opt == 'add' else (
         c - d if opt == 'sub' else (       
         c * d if opt == 'mul' else c / d
      ))
print(result)


# In[97]:


## 반복문 : 수행문을 반복해서 반복사용
## for, while
print("나무를 1번 찍었습니다")
print("나무를 2번 찍었습니다")
print("나무를 3번 찍었습니다")
print("나무를 4번 찍었습니다")
print("나무를 5번 찍었습니다")
print("나무를 6번 찍었습니다")
print("나무를 7번 찍었습니다")
print("나무를 8번 찍었습니다")
print("나무를 9번 찍었습니다")
print("나무를 10번 찍었습니다")
print("나무가 넘어갑니다")
#한번만 적어서 10번이 수행되게 하자

i = 1
while i <=10:  # i가 10이 될땨까지만 +1하기
    i =  i + 1  
    print(i)
    
i = 1
while i <=10:  # i가 10이 될땨까지만 +1하기
    print("나무를 %d번 찍었습니다" % i)
    i =  i + 1  


# In[100]:


## 반복문 : 수행문을 반복해서 반복사용
## for, while
i = 1
print("나무를 1번 찍었습니다" % i)
i = 2
print("나무를 2번 찍었습니다"  % i)
print("나무를 3번 찍었습니다")
print("나무를 4번 찍었습니다")
print("나무를 5번 찍었습니다")
print("나무를 6번 찍었습니다")
print("나무를 7번 찍었습니다")
print("나무를 8번 찍었습니다")
print("나무를 9번 찍었습니다")
print("나무를 10번 찍었습니다")
print("나무가 넘어갑니다")
#한번만 적어서 10번이 수행되게 하자
i = 1
while i <=10:  # i가 10이 될땨까지만 +1하기
    i =  i + 1  
    print(i)
    
i = 1
while i <=10:  # i가 10이 될땨까지만 +1하기
    i =  i + 1  
    print(i)
    
i = 1
while i <=10:  # i가 10이 될땨까지만 +1하기
    print("나무를 %d번 찍었습니다" % i)
    i =  i + 1  


# In[114]:



'''
8단 출력
8 * %d= 8 * 1
8 * 1 = 8 * 1
8 * 1 = 8 * 1
'''

i = 1
while i <=9:  # i가 10이 될땨까지만 +1하기
    print("8 * %d = 8 * %d" % (i, i))
    i =  i + 1  
    
print("==" * 30)
i = 1
while i <=9:  # i가 10이 될땨까지만 +1하기
    print("8 * {0} = 8 * {0}".format(i))
    i =  i + 1  
    
print("==" * 30)
i = 1
while i <=9:  # i가 10이 될땨까지만 +1하기
    print("8 * %d = %d" % (i, 8 * i))
    i =  i + 1  

print("==" * 30)
i = 1
while i <=9:  # i가 10이 될땨까지만 +1하기
    print("8 * {0}= {1}".format(i, 8 * i))
    i += 1 

print("==" * 30)
i = 1
while i <=9:  # i가 10이 될땨까지만 +1하기
    print("8 * {0}= {r}".format(i, r = 8 * i))
    i += 1 


# In[120]:


dan = int(input("원하는 단을 입력해 주세요 : "))
print(dan)
i = 1
while i <= 9:
    print(f"{dan} * {1} = {dan  * i}")
    i += 1
    
#print("5" + "5")


# In[126]:


dan = int(input("원하는 단을 입력해주세요 : "))
start = int(input("시작 숫자를 입력해 주세요 : "))
end = int(input("끝 숫자를 입력해 주세요. : "))
i = start
while i <= end:
    print(f"{dan} * {i} = {dan * i}")
    i += 1


# In[127]:


# 3단을 출력하시오
i = 1
while i <=9:  # i가 10이 될땨까지만 +1하기
    print("3 * {0}= {r}".format(i, r = 3 * i))
    i += 1 

#4단을 출력하시오
i = 1
while i <=9:  # i가 10이 될땨까지만 +1하기
    print("4 * {0}= {r}".format(i, r = 4 * i))
    i += 1 

#5단을 출력하시오
i = 1
while i <=9:  # i가 10이 될땨까지만 +1하기
    print("5 * {0}= {r}".format(i, r = 5 * i))
    i += 1 


# In[ ]:


# 3단을 출력하시오
j = 3
while j <= 5:  # i가 5이 될땨까지만 +1하기
    i = 1
    while i <=9:
         print(f"{j} * {1}= {j* i}")
        i += 1 
    j += 1
 


# In[ ]:





# In[ ]:




