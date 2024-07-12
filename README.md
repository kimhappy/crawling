# Python Crawling
## Shell 사용법
### 현재 디렉토리 변경하기
```sh
cd Desktop/test # 현재 디렉토리 안의 Desktop 디렉토리 안의 test 디렉토리로 이동
cd ~/Download   # 홈 디렉토리 안의 Download 디렉토리로 이동
cd ..           # 현재 디렉토리의 상위 디렉토리로 이동
cd              # 홈 디렉토리로 이동
```

### 디렉토리의 내용 보기
```sh
ls            # 디렉토리의 내용 보기
ls ~/Download # ~/Download 디렉토리의 내용 보기
```

### 디렉토리 생성하기
```sh
mkdir test # test 디렉토리 생성
```

### Visual Studio Code 열기
```sh
code . # 현재 디렉토리 (.) 에서 Visual Studio Code 열기
```

### Python 파일 실행
```sh
python3 example1.py # example1.py 파일 실행
```

## Conda 환경 관리
```sh
conda create -n crawling python=3.9           # crawling 이라는 conda 환경을 생성
conda activate crawling                       # crawling 이라는 conda 환경을 활성화
pip3 install requests beautifulsoup4 selenium # requests, beautifulsoup4, selenium를 현재 환경에 설치
conda deactivate                              # 현재 환경 비활성화
```

## Example 1 - 정적 페이지 크롤링
- URL을 입력하는 것만으로도 모든 정보를 가져올 수 있는 웹 페이지를 '정적 페이지'라고 합니다.
- 이 예시에서는,
  1. 네이버 증권 서버에 HTML 파일을 request 합니다.
  2. 받아온 HTML 파일을 parse 하여 주요 뉴스를 가져옵니다.

## Example 2 - 동적 페이지 크롤링
- URL을 입력하는 것만으로는 모든 정보를 가져올 수 없는 웹 페이지를 '동적 페이지'라고 합니다.
  - 로그인을 해야 보이는 페이지
  - 드래그를 함에 따라 컨텐츠가 업데이트되는 페이지 (예: 유튜브, 네이버 뉴스)
  - 시간이 지남에 따라 컨텐츠가 업데이트되는 페이지 (예: 기상청)
  - 요즘 웹 사이트는 대부분 동적 페이지입니다.
- 이 예시에서는,
  1. 브라우저의 조작을 코드로 자동화하여, 기상청 홈페이지에 접속합니다.
  2. 사용자의 입력을 코드로 흉내내어, 날씨 정보가 로딩되길 기다립니다.
  3. 현재 HTML 내용을 parse 하여 앞으로 3일 동안의 날씨를 출력합니다.

## 더 보시면 좋을 토픽
- Command Line 입력받기
- 사용자 키보드 입력받기
- requirements.txt 사용해서 환경 공유하기
- Git과 GitHub 사용하기
- 텍스트, PDF, 이미지 등 파일 읽고 쓰기
- 메일 자동으로 보내기
- 원격 서버에서 프로그램 주기적으로 실행시키기
- API 사용하기 (OpenAI GPT-3.5, The New York Times, ...)
