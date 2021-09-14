import sys
input=sys.stdin.readline

#값 받아오기
N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
#이진트리를 위한 정렬
house.sort()

start, end = 1, house[-1] - house[0]
result = 0
while (start <= end):
    mid = (start+end)//2
    count = 1 #first에 지을수 있으니
    first = house[0]
    for i in range(1, len(house)):
        if house[i] >= first+mid:# 좌표값 + mid(최대거리) --> 공유기 설치 가능 지역
            count+=1
            first = house[i] # 다음집으로 변경
    if count >= C: # 현재 mid값으로는 공유기 모두 설치 가능 --> 거리를 더 크게
        start = mid + 1 #다음 while에서 현재 mid 는 볼 필요가 없으니 +1로 더 크게 시작
        result = mid
    else: #현재 mid값으로는 공유기 모두 설치 불가능 --> 거리를 더 좁게
        end = mid - 1 #다음 while에서 현재 mid 는 볼 필요가 없으니 -1로 더 작게 시작

print(result)
