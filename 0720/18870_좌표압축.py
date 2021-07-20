import sys
input=sys.stdin.readline

#값 받아오기
N = int(input())
su = list(map(int,input().strip().split()))

#받은 값 중복 없애기
su_set = set(su)
set_length = len(su_set)

#중복없는 값 list로 만들기
su_li = sorted(list(su_set),reverse=True)

#중복없는 값을 key로 하여 result dict 만들기
result = {}
while su_set:
    result[su_set.pop()] = 0

for i in range(set_length):
    result[su_li[i]] = set_length-1
    set_length -=1

final = [0 for i in range(len(su))]
for i in range(len(su)):
    final[i] = result[su[i]]

print(*final)

#똑같은 방법인데 range(keys)로 내 코드 20~22번째 줄을 한번에 나타냄..
# keys = sorted(set(numbers))
# location = dict(zip(keys, map(str, range(len(keys)))))

# sys.stdout.write(' '.join([location[i] for i in numbers]))