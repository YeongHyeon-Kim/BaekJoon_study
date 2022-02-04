import sys
input = sys.stdin.readline

N = int(input())
word_list = set()
for i in range(N):
    word = input().strip()
    word_list.add(word)

word_list = list(word_list)
word_list.sort()
word_list.sort(key=lambda x: len(x))


print("\n".join(word_list))


# for i in range(len(word_list)):
#     print(word_list[i])
