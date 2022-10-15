#!/usr/bin/env python
# coding: utf-8

# In[7]:


startDan = 2
endDan = 4
startGop = 4
endGop = 8
dan = startDan

while dan <= endDan:
    gop = startGop
    while gop <= endGop:
        print(f"{dan} * {gop} = {dan * gop}")
        gop+=1
        dan +=1


# In[8]:


startDan = int(input("시작단을 입력하세요 : "))
endDan = int(input("마지막단을 입력하세요 : "))
startGop = int(input("시작곱을 입력하세요 : "))
endGop = int(input("마지막곱을 입력하세요 : "))
dan = startDan

while dan <= endDan:
    gop = startGop
    while gop <= endGop:
        print(f"{dan} * {gop} = {dan * gop}")
        gop+=1
        dan +=1


# In[27]:


#로또
import random
lotto = []
i = 1
while i <= 45:
    lotto.append(i)
    i += 1
    print(lotto)
    lottosize = len(lotto)
    j = 1
while j <= 6:
    lottosize -= 1
    idx = random.randint(0, lottosize) #
    lottoNum =  lotto.pop(idx) ## 0 ~ 44
    print(lottoNum, end = ", ")
    j += 1


# In[23]:


import random
lotto = []

qty = int(input("원하는 수를 입력하세요 : "))  #로또 몇장살것인지 적기
cnt = 1;
while cnt <= qty:
    i = 1
    while i <= 45: #선택할수 있는 수범위
        lotto.append(i)
        i+=1
    print(lotto)
    
    lottosize = len(lotto)
    j = 1
    while j <= 8: #로또에 적히는 숫자의 수
        lottosize -= 1
        idx = random.randint(0, lottosize) #
        lottoNum =  lotto.pop(idx) ## 0 ~ 44
        print(lottoNum, end = ", ")
        j += 1
    
    cnt += 1
    lotto.clear()
    print()


# In[40]:


# 1 ~ 10 까지의 합을 구하시오
'''
i = 1
sum = 0
sum = sum + 1
sum = sum + 2
sum = sum + 3
...
sum = sum + 10
'''

i = 1
sum = 0
while i <= 100:
    sum = sum + 1
    i += 1
print(sum)

i = 1
sum = 0
while True:
    if i > 100:
        break ##반복문을 강제 종료
    sum += i
    i += 1
print(sum)


# In[52]:


# 1 ~ 20 중 짝수만 출력하시오
'''
print(2)
print(4)
print(6)
...
print(20)
'''
i = 0
while i < 20 :
    i += 1
    if i % 2 == 1:
        continue 
    print(i)


# In[53]:


# 1 ~ 20 중 홀수만 출력하시오
'''
print(2)
print(4)
print(6)
...
print(20)
'''
i = 0
while i < 20 :
    i += 1
    if i % 2 == 0:
        continue 
    print(i)


# In[56]:


i = 0
while i <= 19 :
    i += 1
    if i % 2 == 1:
        print(i)


# In[58]:


i = 0
while True:
    i += 1
    if i > 20:
        break;
    if i % 2 == 1:
        continue
    print(i)


# In[74]:


#리스트에 있는 합을 구하시오
l = [1,43,5,56]
sum = 0
sum = sum + l[0]
sum = sum + l[1]
sum = sum + l[2]
print(sum)
sum = 0
idx = 0 #index
while idx  < len(l):
    sum += l[idx]
    idx += 1
print(sum)

sum = 0
for num in l: #[1,43,5,56]
    sum += num
print(sum)

idx = 0
sum = 0
for num in l: #[1,43,5,56]
    print(f"l[idx] = {num}")
    idx += 1
    

idx = 0
sum = 0
for num in l: #[1,43,5,56]
    sum += num
    print(sum)
print(sum)

idx = 0
sum = 0
for num in l: #[1,43,5,56]
    sum += num
print(sum)

### 범위인 경우
sum = 0
idx = 0
while idx < len(l):
    sum += l[idx]
    idx += 1
print(sum)


# In[78]:


l = [1,2,3,4]
print(l[0])
print(l[1])
print(l[2])
print(l[3])

idx = 0
while idx <= 3:
    print(l[idx])
    idx += 1
for num in l:
    print(num)


# In[7]:


t = (1,2,3,4)
print(t[0]) #수동식 나열
print(t[1])
print(t[2])
print(t[3])

idx = 0
while idx <= 3:
    print(t[idx])
    idx += 1


for nn in t:
    print(nn)


# In[3]:


nn = t[0]
print(nn)
nn = t[1]
print(nn)
nn = t[2]
print(nn)
nn = t[3]
print(nn)

for nn in t:
    print(nn)


# In[4]:


nn = t[0]
nn = t[1]
nn = t[2]
nn = t[3]

for nn in t:
    print(nn)


# In[13]:


l = [1,2,3]
num = l[0]
print(num)
num = l[1]
print(num)
num = l[2]
print(num)

print("==" * 30)
idx = 0
while idx <= 2:
    num = l[idx]  #f<= or구문에선 적지 않아도 자동으로 실행됨
    print(num)
    idx += 1  #f<= or구문에선 적지 않아도 자동으로 실행됨
    
print("==" * 30)    
for num in l: 
    print(num)
    #idx += 1  #f<= or구문에선 적지 않아도 자동으로 실행됨


# In[16]:


# 1 ~ 100까지
i = 0
while i <= 100:
    print(i)
    i += 1



# In[33]:


t = (1,2,3,4)  #튜플
num = t[0]
print(num)
num = t[1]
print(num)
num = t[2]
print(num)
num = t[3]
print(num)

num = t[0]
print(num, end = "")
num = t[1]
print(num, end = "")
num = t[2]
print(num, end = "")
num = t[3]
print(num, end = "")

idx = 0
while idx <=2:
    num = t[idx]
    idx += 1
    print(num)

for num in t:  #for은 무한반복을 하지 않기에 break를 사용할 필요 없음
    print(num, end = "")
for num in t:
    #num = t[0] while에서 실행되고 있는것이 for에서는 자동으로 실행됨
    #num = t[1]
    #num = t[2]
    #num = t[3]
    print(num)


# In[46]:


print(f" 2 * 1 = {2 * 1}")
print(f" 2 * 2 = {2 * 2}")
print(f" 2 * 3 = {2 * 3}")
print(f" 2 * 4 = {2 * 4}")
idx = 1
while idx <= 5:
    print(f" 2 * {idx} = {2 * idx}")
    idx += 1
    
l = [1,7,3,11]
#    0 1 2 3
print(l[0])
print(l[1])
print(l[2])
print(l[3])

size = len(l)  #4

idx = 0
while idx < size:
    print(l[idx])
    idx += 1


# In[50]:


l1 = [(1,2), (3,4), (5,6)]
for t in l1 : # t = L1[0],L1[1],L1[2]
    print(t)
    
for (a, b) in l1 : 
    print(a, b)
    print(a + b)


# In[65]:


l1 = [(1,2,3),(3,4,5),(5,6,7)]
for t in l1 :
    print(t)
    i += 1
    if i % 2 == 0:
        continue
        prnit(t1)


# In[66]:


l1 = [(1,2,3),(3,4,5),(5,6,7)]
i = 0
for t1 in l1 :
    i += 1
    if i % 2 == 1:
        continue
        print(t1)


# In[69]:


l1 = [(1,2,3),(3,4,5),(5,6,7)]
i = 0
for t1 in l1 :
    print(t1)
    print(t1[0], t1[1], t1[2])  
    print(t1[0] + t1[1] + t1[2])  


# In[73]:


l1 = [(1,2,3),(3,5,8),(5,6,7)] #튜플의 크기는 같아야됨(현재 모두 3개씩)
i = 0
for (a,b,c) in l1 :
    print(a,b,c)


# In[76]:


# 1~100가지 출력
#범위일 경우 while, 리스트일 경우 for. for 에서 range 사용 가능(while 대신 사용가능)
#while은 주로 무한로프를 돌려야될 경우에만 사용함
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

sum = 0
for num in range(1,1+1000):
    sum += num
print(sum)


# In[79]:


# 3단
for gop in range(1, 1+9):
    print(f"3 * {gop} = {3 * gop}")
    
    gop = 1
    while gop <= 9:
        print(f"3 * {gop} = {3 * gop}")
        gop += 1


# In[80]:


#딕셔너리에서는 키값을 알아야만 출력 가능함
dic = {1 : "이", 2: "숭", 3:"무"}
for key in dic.keys():
    print(dic[key])
    
for value in dic.values():
    print(value)


# In[84]:


# 3단
for gop in range(1, 9):
    print(f"3 * {gop} = {3 * gop}")
for gop in range(1, 1+9):
    print(f"4 * {gop} = {4 * gop}")
for gop in range(1, 1+9):
    print(f"5 * {gop} = {5 * gop}")

    
dan = 3
while dan <= 5:
    for gop in range(3, 3 + 3):
        print(f"5 * {gop} = {5 * gop}")
    dan += 1

for dan in range()


# In[88]:


startDan = 3
endDan = 5 + 1
startGop = 1
endGop = 9
for dan in range(startDan,endDan+1 ):
    for gop in range(startGop, endGop + 1):
        print(f"{dan} * {gop} = {dan * gop}")


# In[89]:


startDan = int(input("시작단을 입력해주세요 : "))
endDan = int(input("끝단을 입력해주세요 : "))
startGop = int(input("시작곱을 입력해주세요 : "))
endGop = int(input("끝곱을 입력해주세요 : "))
for dan in range(startDan, endDan + 1):
    for gop in range(startGop, endGop + 1):
        print(f"{dan} * {gop} = {dan * gop}")


# In[94]:


for num in range(5,0,-1):
     print(num)
for num in range(5,0,-1):
     print(num)
for num in reversed(range(1,6)):
     print(num)


# In[110]:


score = 75
if score >= 90:
    massage = 'A'
else :
    if score >= 80:
        massage = 'B'
    else :
        if score >= 70:
            massage = 'C'
        else :
            if score >= 60:
                massage = 'D'
            else:
                massage = 'F'
print(massage)
massage = 'A' if score >= 90 else (
           'B' if score >= 80 else (
           'C' if score >= 70 else (
           'D' if score >= 60 else  'F'
           )))
print(massage)


# In[113]:


result = []
i = 1
while i <= 100:
    result.append(i)
    i += 1
print(result)
    
for num in range(1, 101):
    result.append(num)
print(result)


result = [num for num in range(1, 101)]
print(result)


# In[119]:


a = (1,2,3,4)
result = []
for num in a:
    result.append(num * 3)
print(result)

result = [num * 3 for num in a]
print(result)


# In[124]:


result = []
for num in (1,2,3,4,5):
    result.append(num * 3)
print(result)

result = [num * 3 for num in (1,2,3,4,5)]
print(result)


# In[128]:


#a튜플에서 값이 짝수인 것만 3을 곱한 값을 리스트에 추가하시오
a = (1,2,3,4, 12)
result = []
for num in a:
    if num % 2 == 0:
        result.append(num * 3)
print(result)

result = [num * 3 for num in a
                        if num % 2 == 0]
print(result)


# In[137]:


lotto = []
i = 1
while i <= 5 :
    lotto.append(i)
    i += 1
print(lotto)
print("==" * 30)
lotto = []
for i in range(1,6) :
    lotto.append(i)    
print(lotto)
print("==" * 30)
lotto = []
for i in range(1,6) :
    lotto.append(i)    
    print(lotto)
print("==" * 30)   
lotto = []
for num in range(1,6) :
    lotto.append(i)    
    print(lotto)


# In[142]:


for dan in range(3, 7):
    for gop in range(4,8):
        print(f"{dan} * {gop} = {dan * gop}")
gogodan = []
for dan in range(3, 7):
    for gop in range(4,8):
        gogodan.append(dan * gop)
print(gogodan)

gogodan = [dan * gop for dan in range(3, 7)
                     for gop in range(4, 8)]
print(gogodan)
#append 에만 for문 리스트 있음


# In[144]:


## 함수  
'''
-함수정의
f1(x,y) = 2 x + 3y
--함수호출
z = f1(2,3)
z = 13
'''

###  함수 정의
def f1(x, y):
    return 2 * x + 3 *y

##함수호출
z = f1(2,3)
print(z)

###  함수 정의
def f1(x, y, i): #x,y,i : parameter : 매개변수
    return 2 * x + 3 *y

##함수호출
z = f1(2,3,4) # xyi에 전달되는 argument : 인수
print(z)


# In[ ]:


z = f1(3,5,7)
print(z)


# In[ ]:


#3단
for gop in range(1,10):
    print(f"{3} * {gop} = {3 * gop}")
#4단
for gop in range(1,10):
    print(f"{4} * {gop} = {4 * gop}")
#7단
for gop in range(1,10):
    print(f"{7} * {gop} = {7 * gop}")


# In[153]:


def gugu(dan):
    for gop in range(1, 10):
        print(f"{dan} * {gop} = {dan * gop}")

gugu(7)


# In[154]:


gugu(6)


# In[168]:



for dan in range(4,7):
     gugu(dan)
gugu(8)
gugu(3)


# In[171]:


### 함수를 만드는 4가지 형식
### 1. 일반적인 유형 : 입력값과 결과갑시 있는 함수
def test(x, y) : # 입력값이 있다는 것은 매개변수가 있다.
    return x + y # 결과 값이 있다는 것은 return 문이 있다.
result = test(3, 7)
print(result)

result = test(5, 7)
print(result)


# In[177]:


#입력값은 없고결과값만 있는 함수
def test1(): #입력값이 없다는 것은 매개변수가 없다
    x = 10; y = 20
    return x + y
result = test1()
print(result)


# In[180]:


def test1():
    x = int(input("숫자를 입력해주세요 :"))
    y = int(input("숫자를 입력해주세요 :"))
    return x + y
result = test1()
print(result)


# In[184]:


# 3.입력값은 있으나 결과값은 없다
def test2(x, y): #입력값이 있다는 것은 매개변수가 있다
    result = x + y
    print(result) #결과값이 없다는 것은 return 문이 없다
test2(2, 3)


# In[186]:


# 3.입력값은 있으나 결과값은 없다
def test333(x, y):
    result = x + y
test333(2, 3)
print(result)


# In[189]:


'''
입력   결과
o       o
x       o
o       x
x       x
'''
def test3():
    x =10; y = 20
    result = x + y
    print(result)
test3()


# In[205]:


def test3():
    x = int(input("숫자를 입력해주세요: "))
    y = int(input("숫자를 입력해주세요: "))
    result = x + y
    print(result)


# In[224]:


import random
def lottoFnc():
    lotto = [num for num in range(1, 46)]
    lottoSize = len(lotto)
    for n in range(1, 7) :
        lottoSize -= 1
        idx = random.randint(0, lottoSize)
        lottoNum = lotto[idx]
        print(lottoNum, end = ",")


# In[223]:


lottoFnc()


# In[218]:


cnt = int(input("구매수량을 입력해주세요 : "))
for n in range(0, cnt):
    lottoFnc()
    print()


# In[225]:


def lottoCnt():
    cnt = int(input("구매수량을 입력해 주세요 : "))
    for n in range(0, cnt):
        lottoFnc()
        print()
lottoCnt()


# In[226]:


start = 1
end = 100

sum = 0
for num in range(start, end + 1):
    sum += num
print(sum)


# In[250]:


### 매개변수가 있는 함수
### 1, 100 : 10, 300

start = 10
end = 300

sum = 0
for num in range(start, end + 1):
    sum += num
print(sum)


# In[297]:


### 매개변수가 있는 함수
### 1, 100 : 10, 300

def sum1(start, end):
    sum = 0
    for num in range(start, end + 1):
        sum += num
    return sum


# In[298]:


result = sum1(10, 300)
print(result)
result = sum1(1,100)
print(result)


# In[262]:


result = sum1(end = 300, start = 10 )
print(result)


# In[264]:


def sum11(*para): #앞에 *를 주면 동일한 이름에도 여러 값을 줄수 있음
     print(para)


# In[266]:


sum11(1,2)
sum11(1,2,3,4)


# In[270]:


def sum11(*para): #앞에 *를 주면 동일한 이름에도 여러 값을 줄수 있음
    sum = 0
    for num in para:
        sum += num
    print(sum)


# In[271]:


sum11(1,2)
sum11(1,2,3,4)
sum11(1,2,3,4,5,6)
sum11(4,5,6,7,8)


# In[274]:


def sum12(num1, *num2):
    print(num1)
    print(num2)


# In[275]:


sum12(1, 2,3,4,5) #2,3,4,5여러개는 *표 있는 num2가 받은 것임


# In[281]:


def calc(opt, *num):
    sum1 = 1
    if opt == "add":
        for n in num:
            sum1 += n
    elif opt == "mul":
        for n in num:
            sum1 *= n
    print(sum1)
    


# In[283]:


calc('add', 1,2,3,4,5)
calc('mul', 1,2,3,4,5)


# In[307]:


#return 문에 의해 전달되는 값은 오로지 하나이다
def add():
    x = 10; y = 30;
    return (x + y, 10)


# In[309]:


result = add()
print(result)
print(result[0], result[1])


# In[302]:


a, b = (10, 30)
print(a, b)
i = (10, 20)
l = [10, 20]
print(i)


# In[312]:


i = 10
print(i)
l = [10, 20, 30]
print(l)

t = 10, 20
print(t)
s = {1,2,3,4,5}
print(s)


# In[314]:


i = 10, 20
print(i)


# In[316]:


def test12(x, y):
    add = x + y
    mul = x * y
    return add, mul #리턴된 값은 튜플로 전달된다


# In[319]:


result = test12(3,4)
print(result)
print(result[0], result[1])


# In[322]:


def say_myself(name, old, man = True) :
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다" % old)
    if man :
          print("남자입니다.")
    else:
          print("여자입니다")


# In[324]:


say_myself('이승무', 15)
say_myself('박준현', 20, False)


# In[332]:


def say_myself(name, old=25, man = True) :
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다" % old)
    if man :
          print("남자입니다.")
    else:
          print("여자입니다")
say_myself(name = "이숭무", man = False)
#say_myself(name = "이숭무", False) #False가 old에게 기에 실패됨


# In[338]:


#전역변수 : 보통 프로그램이 종료되지 전까지 사용할수 있는 변수
#지역변수 : 함수가 종료되면 변수도 같이 소멸

b = 1 # 전역변수
def test4():
     b = 100 #지역변수 함수내에서 변수를 사용시 지역변수가 우선, 전역변수 사용안함
     print(f"함수안에서 실행 : {b}")
test4()
print(b)


# In[ ]:


b = 1 # 전역변수
def test4():
    global b #global을 적음으로 아래b 가 전역변수가 됨
     b = 100 #지역변수 함수내에서 변수를 사용시 지역변수가 우선, 전역변수 사용안함
     print(f"함수안에서 실행 : {b}")
test4()


# In[341]:


b = 10
def test5():
    print(f"함수안에서 실행 : {b}")
test5()
print(f"함수 밖에서 실행 b : {b}")


# In[343]:


b = 10
def test6():
    b = 100
    print(f"함수안에서 실행 : {b}")
test6()
print(f"함수 밖에서 실행 b : {b}")


# In[345]:


b = 10 #전역변수
def test7():
    global b  #w전역변수화 한다느 뜻
    b = 100 
    print(f"함수안에서 실행 : {b}")
test7()
print(f"함수 밖에서 실행 b : {b}")


# In[346]:


### Lambda 함수
def add(a, b):
    return a + b
add(3,4)


# In[347]:


add = lambda a, b : a + b
add(3,4)


# In[350]:


def add(a, b = 4):
    return a + b
add(3, 6)


# In[349]:


add = lambda a, b = 4 : a + b
add(3)


# In[351]:


def add(opt, a, b):
    if opt == "add":
        return a + b
    else:
        return a - b
result = add("add", 4, 3)
print(result)


# In[361]:


add = lambda opt, a, b : a + b if opt == "add" else a - badd('add', 3, 4)


# In[356]:


def add(opt, a, b):
    if opt == "add":
        return a + b
    else:
        if opt == "sub":
            return a - b
        else:
            if opt == "mul":
                return a * b
            else:
                return a / b
result = add("add", 4 , 3)
print(result)


# In[369]:


add = lambda opt, a, b : a + b if opt == "add" else(
                         a - b if opt == "sub" else(
                         a * b if opt == "mul" else 
                        a / b
))
add('mul', 3, 4)
add('add', 3, 4)
add('a / b', 3, 4)


# In[ ]:


##파일 입출력
##변수가 가지고 있는 데이터를 파일에 저장하거나
##또는 파일에 있는 값을 변수로 가져오는 것을 말한다.


# In[385]:


##파일에 데이터를 저장
f = open("bb.txt", "w", encoding='utf-8')
f.write("1번째 줄입니다.\n")
f.write("2번째 줄입니다.\n")
f.write("3번째 줄입니다.\n")
f.close()


# In[387]:


f = open("cc.txt", "w")
for n in range(1, 10):
    f.write(f"{n}번째 줄입니다. \n")
f.close()


# In[391]:


f = open("ee.txt", mode = "a") #같은 폴더에 메모장 저장됨
for n in range(15, 20):
    f.write(f"{n}번째 줄입니다. \n")
f.close()


# In[407]:


f = open("bb.txt", mode = "r")
'''
line = f.readline()
print(line)
line = f.readline()
print(line)
'''
while True:
    line = f.readline()
    if not line:
        break
    print(line, end="")


# In[413]:


f = open("ee.txt", "r")
lines = f.readlines()
print(lines)
for line in lines:
    print(line)
print("".join(lines))


# In[417]:


f = open("cc.txt", "r")
data = f.read()   # read, readline, readlines 3가지가 있음
print(data)


# In[422]:


with open("cc.txt", "w") as f:
    for num in range(1, 9):
        f.write(f"{num}번째 줄입니다.\n")


# In[423]:


with open("cc.txt", "r") as f:
     data = f.read() 
print(data)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




