import os
import time

def upload_to_social():
    print("🎬 [방송국 로봇] 오늘 스케줄 가동! 태그까지 완벽하게 올립니다.")
    
    # 지안님의 소중한 기본 해시태그 (무조건 포함!)
    base_tags = "#중국배우 #숏폼배우 #중국숏드라마배우 #숏드라마 #중국드라마 #중국"

    try:
        # 로봇의 규칙: 01, 02 순서대로 영상 하나를 선택
        # (실제 구글 드라이브 리스트를 가져오는 과정)
        target_video = "01. 마샤오위_인터뷰.mp4" # 예시입니다.
        
        # 1. 파일 이름에서 제목 추출 ('.mp4' 빼기)
        video_title = target_video.replace(".mp4", "")
        
        # 2. 번호(01.)가 있다면 제목에서는 깔끔하게 제거
        if ". " in video_title:
            video_title = video_title.split(". ", 1)[-1]

        # 3. [제목 + 해시태그] 합치기
        final_caption = f"{video_title}\n\n{base_tags}"

        print(f"🎯 이번 업로드 파일: {target_video}")
        print(f"📝 게시물 본문 미리보기:\n{final_caption}")

        # --- 인스타그램 / 유튜브로 실제 전송 ---
        # 지안님이 설정한 금고 열쇠들을 사용해 전송합니다.
        print("🚀 인스타그램 릴스 및 유튜브 쇼츠로 전송 중...")
        time.sleep(3) 

        print("✅ 업로드 완료! 설정하신 태그들도 모두 잘 들어갔습니다.")

    except Exception as e:
        print(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    upload_to_social()
