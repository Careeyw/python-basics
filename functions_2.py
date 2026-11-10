# def add(a, b, c):
#     res=a + b + c
#     return res
# print(add(2, 2, 2))
# if res>=2:
#     print("thats the correct answer")
# else:
#     print("thats the wrong answer")
def addition(*nums):
    total=sum(nums)
    return total
print(addition(1,2,3,4,5))

def build_profile(*kwargs):
    for k,w in kwargs.items():
        print(k,w)

square=lambda x: x*x
print (square(5))


People=[
    {"name":"macharia","age":25 },
    {"name":"carey","age":22 },
    {"name":"honn","age":23 },
]
