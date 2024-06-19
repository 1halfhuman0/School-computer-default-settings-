import os

# 현재 작업 디렉토리 출력
print("Current working directory:", os.getcwd())

# 파일 존재 여부 확인
file_name = 'requirements.txt'
if os.path.isfile(file_name):
    print(f"{file_name} exists.")
else:
    print(f"{file_name} does not exist.")
