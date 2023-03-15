# pip install youtube_dl
import youtube_dl
import os

output_dir = os.path.join('./', '%(title)s.%(ext)s')

# 여러 영상을 받을 수 있고 플레이리스트도 가능함
download_list = ['https://www.youtube.com/watch?v=f53Xk2uuwNY']
ydl_opt = {
    'outtmpl': output_dir,
    'format': 'worst',  # 최상 품질의 비디오 형식 선택 = best, 최악 worst
    'preferredcodec': 'mp4',
    'nocheckcertificate': True,  # ssl인증서 해결
}

with youtube_dl.YoutubeDL(ydl_opt) as ydl:
    print(output_dir)

    ydl.download(download_list)

print('다운로드 완료했습니다.')

# 참고
# 스크립트에 넣고 싶으면 이렇게 os.system('''youtube-dl -F "ytsearch:'https://www.youtube.com/watch?v=qjlEnO4zHwc'"''')
# 터미널에서 하려면 이렇게 youtube-dl -f 22 'http://www.youtube.com/watch?v=P9pzm5b6FFY' # 받고싶은 거 선택하면 됨

# 실행되는 폴더 안에 '영상제목.확장자' 형식으로 다운로드
# 저렇게 포맷형은 처음에 파이썬 돌아갈 때 형식을 읽고
# 나중에 아래서 with구문 돌아가면서 title받아서 출력해줌
# 그래서 output_dir = os.path.join('./', '%(title)s.%(ext)s') 이 코드에 title이 있어도 잘 돌아감
