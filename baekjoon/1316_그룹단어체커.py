n = int(input())
words = []
count = 0 # 그룹 단어가 아닌 단어 개수

for _ in range(n):
    words.append(list(input()))

for i in range(n):
    word = words[i]
    alphabet = {}

    for j in range(len(word)):
        if word[j] not in alphabet: # 처음 나온 알파벳인 경우
            alphabet[word[j]] = 1
        else: # 이미 나온 알파벳일 경우
            if word[j] == word[j-1]: # 앞글자랑 같을 때
                continue
            elif word[j] != word[j-1]: # 앞글자랑 다를 때
                count += 1
                break

print(n - count)