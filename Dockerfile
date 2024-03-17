# Python 3.6 이미지를 기반으로 함
FROM krmp-d2hub-idock.9rum.cc/goorm/python:3.6-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 Python 스크립트를 이미지에 추가
COPY . .
RUN pip install -r requirements.txt

# 서버가 실행될 때 사용되는 포트
EXPOSE 5000

# 컨테이너를 시작할 때 Python 스크립트를 실행
CMD ["waitress-serve", "--port=5000", "--call", "app:create_app"]