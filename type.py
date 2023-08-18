# 1. 파이썬 정수 변환 - int() =1,2,3
# 2. 파이썬 실수 변환 - float() =-1, 0, 12 √2, e, π 
# 3. 파이썬 문자열 변환 - str() =메모리에 저장된 연속된 숫자 / 기호의 순차수열
# 4. 파이썬 문자 변환 - chr()
# 5. 파이썬 불리언 변환 - bool() =참/거짓



# 1. 파이썬 정수 변환 - int()
# 파이썬 int 타입 변환 예제
 
# int(정수) : 정수를 정수로 변환 (가능함. 의미없음)
a = int(10)
print(f'1. int(10) = {a}, type(a) = {type(a)}')
 
 
# int(실수) : 실수를 정수로 변환
b = int(3.141592)
print(f'2. int(3.141592) = {b}, type(b) = {type(b)}')
 
 
# int(불리언) : 불리언을 정수로 변환
c = int(True)
print(f'3. int(True) = {c}, type(c) = {type(c)}')
 
 
# int(문자) : 문자를 정수로 변환
# d = int('a') 오류 변환할 정수가 없음
d = int('1')
print(f'4. int("1") = {d}, type(d) = {type(d)}')
 
 
# int(문자열) : 문자열을 정수로 변환
# e = int('blockdmask') 오류 변환할 정수가 없음
e = int('112')
print(f'5. int(\'112\') = {e}, type(e) = {type(e)}')




# 2. 파이썬 실수 변환 - float()  float(x)는 인자로 들어온 x를 실수 타입으로 변환해서 반환

# 파이썬 float 타입 변환 예제
 
# float(정수) : 정수를 실수로 변환
a = float(10)
print(f'1. float(10) = {a}, type(a) = {type(a)}')
 
 
# float(실수) : 실수를 실수로 변환 (가능, 의미없음)
b = float(3.141592)
print(f'2. float(3.141592) = {b}, type(b) = {type(b)}')
 
 
# float(불리언) : 불리언을 실수로 변환
c = float(False)
print(f'3. float(False) = {c}, type(c) = {type(c)}')
 
 
# float(문자) : 문자를 실수로 변환
# d = float('a')  # 오류 : 변환할 실수가 없음
d = float('2')
print(f'4. float("2") = {d}, type(d) = {type(d)}')
 
 
# float(문자열) : 문자열을 정수로 변환
# e = float('blockdmask') # 오류 : 변환할 실수가 없음
e = float('3434')
print(f'5. float(\'3434\') = {e}, type(e) = {type(e)}')




# 3. 파이썬 문자열 변환 - str() str(x)는 인자로 들어온 x를 문자열로 변환시켜서 반환

# 파이썬 str 타입 변환 예제
 
# str(정수) : 정수를 문자열로 변환
a = str(10)
print(f'1. str(10) = {a}, type(a) = {type(a)}')
 
 
# str(실수) : 실수를 문자열로 변환
b = str(3.141592)
print(f'2. str(3.141592) = {b}, type(b) = {type(b)}')
 
 
# str(불리언) : 불리언을 문자열로 변환
c1 = str(True)
print(f'3-1. str(True) = {c1}, type(c1) = {type(c1)}')
 
c2 = str(False)
print(f'3-2. str(False) = {c2}, type(c2) = {type(c2)}')
 
 
# str(문자) : 문자를 문자열로 변환
d1 = str('2')
print(f'4-1. str("2") = {d1}, type(d1) = {type(d1)}')
 
d2 = str('a')
print(f'4-2. str("a") = {d2}, type(d2) = {type(d2)}')
 
 
# str(문자열) : 문자열을 문자열로 변환 (가능, 의미없음)
e = str('BlockDMask')
print(f'5. str(\'3434\') = {e}, type(e) = {type(e)}')




# 4. 파이썬 문자 변환 - chr() chr(x)는 인자로 들어온 x를 문자로 변환시켜서 반환

# 파이썬 chr 타입 변환 예제
 
# chr(정수) : 정수를 문자로 변환
a = chr(54)
print(f'1. chr(54) = {a}, type(a) = {type(a)}')
 
b = chr(55)
print(f'2. chr(55) = {b}, type(b) = {type(b)}')
 
i = 64
while i <= 70:
    print(f'chr({i}) : {chr(i)}')
    i = i + 1
 
 
# chr(실수) : 실수를 문자로 변환 - 불가능
# b = chr(3.141592)
 
 
# chr(불리언) : 불리언을 문자로 변환
# 이 경우에는 True가 1, False가 0으로 취급되어서 가능
c1 = chr(True)
print(f'3-1. chr(True) = {c1}, type(c1) = {type(c1)}')
 
c2 = chr(1)
print(f'3-2. chr(1) = {c2}, type(c2) = {type(c2)}')
 
if c1 == c2:
    print('c1 == c2')
 
 
c3 = chr(False)
print(f'3-3. chr(False) = {c3}, type(c3) = {type(c3)}')
c4 = chr(0)
print(f'3-4. chr(0) = {c4}, type(c4) = {type(c4)}')
 
if c3 == c4:
    print('c3 == c4')
 
 
# chr(문자) : 문자 입력 - 불가능
# d1 = chr('2')
# d2 = chr('a')
 
# chr(문자열) : 문자열 입력 - 불가능
# e = chr('BlockDMask')




# 5. 파이썬 불리언 변환 - bool() bool(x)는 인자로 들어온 x를 bool 타입으로 변환시켜서 반환

# 파이썬 bool 타입 변환 예제
 
# bool(정수) : 정수를 불리언으로 변환
a1 = bool(54)
print(f'1-1. bool(54) = {a1}, type(a1) = {type(a1)}')
 
a2 = bool(0)
print(f'1-2. bool(0) = {a2}, type(a2) = {type(a2)}')
 
 
# bool(실수) : 실수를 불리언으로 변환
b1 = bool(3.141592)
print(f'2-1. bool(3.141592) = {b1}, type(b1) = {type(b1)}')
 
b2 = bool(0.00)
print(f'2-2. bool(0.00) = {b2}, type(b2) = {type(b2)}')
 
 
# bool(불리언) : 불리언을 불리언으로 변환
c1 = bool(True)
print(f'3-1. bool(True) = {c1}, type(c1) = {type(c1)}')
 
c2 = bool(False)
print(f'3-3. bool(False) = {c2}, type(c3) = {type(c2)}')
 
 
# bool(문자, 문자열) : 문자열을 불리언으로 변환 (비어있는지 아닌지가 중요)
e = bool('BlockDMask')
print(f'4-1. bool(\'BlockDMask\') = {e}, type(e) = {type(e)}')
 
f = bool('')
print(f'4-2. bool(\'\') = {f}, type(f) = {type(f)}')
