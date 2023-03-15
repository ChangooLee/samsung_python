#pip install pandas
#pip install openpyxl
#엑셀이 컴퓨터에 없어도 실행됩니다.

import pandas as pd

df=pd.read_excel('영어단어장.xlsx')
user_input=input("학습하고자하는 일자를 입력하시오 ex)2021-08-11\n>>>")
temp=df[df.day == user_input]
temp.reset_index(inplace=True)

def typeMeaning(df):
  n = 0
  n_last = len(df)
  while n<n_last:
      user_input=input(f'{df.word[n]}의 뜻을 적으시오 >>>  ')
      if user_input == df.meaning[n]:
        print('맞췄습니다')
        n += 1
        print()
      else:
        print('다시 입력하세요')

typeMeaning(temp)