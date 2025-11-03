import requests
import json

def ocr_space_api(image_path, api_key, language='kor'):
    url_api = "https://api.ocr.space/parse/image"

    with open(image_path, 'rb') as f:
        response = requests.post(
            url_api,
            files={"filename": f},
            data={"apikey": api_key, "language": language},
            timeout=30
        )

    # JSON 파싱 예외 처리
    try:
        result = response.json()
    except json.JSONDecodeError:
        print("❌ JSON 파싱 실패. 원본 응답:")
        print(response.text[:300])
        return ""

    # 처리 오류 확인
    if result.get("IsErroredOnProcessing"):
        print("❌ OCR.Space 처리 오류:", result.get("ErrorMessage"))
        return ""

    parsed = result.get("ParsedResults")
    if not parsed:
        print("❌ ParsedResults가 비어있습니다.")
        return ""

    text_detected = parsed[0].get("ParsedText", "")
    return text_detected


# ✅ 반드시 실제 API 키 입력!
API_KEY = "K88720166588957"  

text_result = ocr_space_api('01.jpg', api_key=API_KEY, language='kor')
print("API로부터 추출된 텍스트:")
print(text_result)
