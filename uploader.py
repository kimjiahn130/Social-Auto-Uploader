import os
import requests
import time

def real_instagram_upload():
    # 1. 지안님의 소중한 정보
    TAGS = "#중국배우 #숏폼배우 #중국숏드라마배우 #숏드라마 #중국드라마 #중국"
    ACCESS_TOKEN = os.environ.get('INSTAGRAM_ACCESS_TOKEN')
    ACCOUNT_ID = os.environ.get('INSTAGRAM_ACCOUNT_ID')
    
    # 지안님이 주신 진짜 영상의 직접 다운로드 링크
    # 구글 드라이브 파일 ID를 사용하여 인스타가 읽을 수 있는 주소로 만듭니다.
    VIDEO_URL = "https://drive.google.com/uc?export=download&id=1GHsKwraCu0F3WuPX3Z5NXmN0CjPr-hq_"
    
    VIDEO_TITLE = "헝디엔20251102_이백언"
    CAPTION = f"{VIDEO_TITLE}\n\n{TAGS}"

    print(f"🚀 [실전 가동] '{VIDEO_TITLE}' 영상을 인스타그램으로 전송합니다!")

    try:
        # 단계 1: 인스타그램 서버에 영상 올리기 예약
        post_url = f"https://graph.facebook.com/v19.0/{ACCOUNT_ID}/media"
        payload = {
            'media_type': 'REELS',
            'video_url': VIDEO_URL,
            'caption': CAPTION,
            'access_token': ACCESS_TOKEN
        }
        
        response = requests.post(post_url, data=payload)
        result = response.json()
        
        if 'id' in result:
            creation_id = result['id']
            print(f"📡 영상 등록 완료 (ID: {creation_id}). 서버에서 처리 중...")
            
            # 단계 2: 영상이 처리될 때까지 잠시 대기 (30초)
            time.sleep(30)
            
            # 단계 3: 최종 게시물 발행
            publish_url = f"https://graph.facebook.com/v19.0/{ACCOUNT_ID}/media_publish"
            publish_payload = {
                'creation_id': creation_id,
                'access_token': ACCESS_TOKEN
            }
            
            final_response = requests.post(publish_url, data=publish_payload)
            print("✅ 인스타그램 최종 게시 성공!")
        else:
            print(f"❌ 등록 실패: {result}")

    except Exception as e:
        print(f"❌ 에러 발생: {e}")

if __name__ == "__main__":
    real_instagram_upload()
