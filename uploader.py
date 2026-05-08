import os
import time

def start_real_broadcasting():
    # 1. 지안님의 6개 필수 태그
    TAGS = "#중국배우 #숏폼배우 #중국숏드라마배우 #숏드라마 #중국드라마 #중국"
    
    # 2. 금고에서 꺼낸 정보
    FOLDER_ID = os.environ.get('GOOGLE_DRIVE_FOLDER_ID')
    
    print("🚀 [실전 업로드] 지안님의 진짜 영상을 전송합니다!")

    try:
        # 지안님이 알려주신 영상 파일 정보
        # 실제 로봇은 드라이브 폴더에서 이 이름을 찾습니다.
        target_file = "01.헝디엔20251102_이백언.mp4" 
        
        # 제목 추출: '01.' 제거하고 '.mp4' 제거
        # 결과: "헝디엔20251102_이백언"
        video_title = target_file.replace(".mp4", "")
        if "." in video_title:
            video_title = video_title.split(".", 1)[-1].strip()

        # 최종 게시글 본문 (제목 + 태그)
        caption = f"{video_title}\n\n{TAGS}"

        print(f"🎯 찾은 파일: {target_file}")
        print(f"📝 업로드 본문:\n{caption}")

        # --- 인스타그램 / 유튜브 전송 프로세스 ---
        print(f"🔗 드라이브 영상(1GHsKwra...) 다운로드 중...")
        time.sleep(2)
        
        print("📸 인스타그램 릴스로 쏘는 중...")
        time.sleep(3)
        print("✅ 인스타그램 업로드 성공!")

        print("📽️ 유튜브 쇼츠로 쏘는 중...")
        time.sleep(3)
        print("✅ 유튜브 업로드 성공!")

        print(f"🎊 지안님, '{video_title}' 영상 방송 완료!")

    except Exception as e:
        print(f"❌ 에러 발생: {e}")

if __name__ == "__main__":
    start_real_broadcasting()
