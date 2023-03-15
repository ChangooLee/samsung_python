import random
import time
word_lst = ['fox', 'tree', 'love', 'hi']
print("타자 게임 준비 되면 엔터를 입력하세요")
input()
last_n = len(word_lst)
start = time.time()
n = 0

while n < last_n:
    word = random.choice(word_lst)
    print(word)
    user_unput = input()
    if user_unput == word:
        print("통과\n")
        word_lst.remove(word)
        n += 1
    else:
        print("다시 입력해주세요")

end = time.time()
at = end - start
print(f'타자시간은 {at:.2f}초 걸렸습니다')
