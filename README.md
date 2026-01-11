# testfile

OCR(Optical Character Recognition) 처리 과정과 파일 입력 실험을 위한 테스트 프로젝트입니다.  
이미지 및 PDF 파일을 대상으로 한 OCR 처리 로직과 전처리 과정을 단계별로 실습하고 정리했습니다.

---

## 📖 프로젝트 개요

이 저장소는 **OCR 처리 흐름을 이해하고 실험하기 위한 학습용 프로젝트**입니다.  
이미지(`.jpg`)와 문서(`.pdf`) 파일을 입력으로 받아 텍스트를 추출하는 과정을  
Python 스크립트 형태로 단계별 구현 및 테스트하였습니다.

---

## 📂 파일 구성

```
testfile/
├── 01.py        # OCR 기본 처리 실습
├── 02.py        # 이미지 전처리 + OCR
├── 03.py        # OCR 결과 가공 및 출력
├── 04.py        # PDF 파일 OCR 처리
├── 05.py        # OCR 처리 결과 개선 실험
├── 01.jpg       # OCR 테스트용 이미지
├── sample.pdf   # OCR 테스트용 PDF 문서
├── config.json  # OCR 설정 및 테스트용 구성 파일
├── README.md
└── .gitignore
```

---

## ⚙️ 실행 환경

- Python 3.x
- OCR 관련 라이브러리 (예: pytesseract, OpenCV 등)
- PDF 처리 라이브러리 (예: pdf2image 등)

> 사용 라이브러리는 실행 환경에 따라 다를 수 있습니다.

---

## 🚀 실행 방법 (예시)

```bash
python 01.py
```

또는

```bash
python 04.py
```

> 각 스크립트는 **독립적으로 실행 가능한 OCR 실험 코드**입니다.

---

## 🛠 사용 기술

- **Language**: Python
- **OCR**: Tesseract OCR (기반 실습)
- **Image Processing**: OpenCV
- **File Handling**: Image / PDF 처리

---

## 📌 참고 사항

- 본 프로젝트는 **OCR 처리 학습 및 테스트 목적**으로 작성되었습니다.
- 실습 위주의 코드로 구성되어 있으며, 상용 서비스 목적은 아닙니다.
- 각 파일은 OCR 처리 단계별 실험 결과를 포함합니다.# testfile
