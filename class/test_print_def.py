# def hello():
#     print('hello 함수 시작')
#     print('hello')
#     print('hello 함수 끝')
 
# def world():
#     print('world 함수 시작')
#     print('world')
#     print('world 함수 끝')
 
# hello()
# world()

# def trace(func):                             # 호출할 함수를 매개변수로 받음
#     def wrapper():                           # 호출할 함수를 감싸는 함수
#         print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
#         func()                               # 매개변수로 받은 함수를 호출
#         print(func.__name__, '함수 끝')
#     return wrapper                           # wrapper 함수 반환
 
# def hello():
#     print('hello')
 
# def world():
#     print('world')
 
# trace_hello = trace(hello)    # 데코레이터에 호출할 함수를 넣음
# trace_hello()                 # 반환된 함수를 호출
# trace_world = trace(world)    # 데코레이터에 호출할 함수를 넣음
# trace_world()                 # 반환된 함수를 호출



# def trace(func):                             # 호출할 함수를 매개변수로 받음
#     def wrapper():
#         print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
#         func()                               # 매개변수로 받은 함수를 호출
#         print(func.__name__, '함수 끝')
#     return wrapper                           # wrapper 함수 반환
 
# @trace    # @데코레이터
# def hello():
#     print('hello')
 
# @trace    # @데코레이터
# def world():
#     print('world')
 
# hello()    # 함수를 그대로 호출
# world()    # 함수를 그대로 호출



# class TestClass:
#   def __init__(self):
#     self.result =0
#     pass
#   def sqr(self,x: int):
#     self.result = (x ** 2)
#     return self.result
#   def abs2(self,x: int):
#     self.result = abs(x)
#     return self.result


# obj = TestClass()
# variable = -1
# print("전달 받은 값: ", variable)
# print("절대값은: ", obj.abs2(variable))
# variable = 2
# print("전달 받은 값: ", variable)
# print("제곱값은: ", obj.sqr(variable))



import pandas as pd

roll_no = [501, 502, 503, 504, 505, 506]

student_df = pd.DataFrame({
    'Name': ["Jennifer", "Travis", "Bob", "Emma", "Luna", "Anish"],
    'Gender':  ["Female", "Male", "Male", "Female", "Female", "Male"],
    'Age': [17, 18, 17, 16, 18, 16]
}, index=roll_no)

print("The DataFrame is:")
print(student_df, "\n")

first_row = student_df["Name"].iloc[0]

print("First row from Name column is:")
print(first_row)