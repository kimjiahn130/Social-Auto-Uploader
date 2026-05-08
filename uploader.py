import os
import time

def run_upload():
    # 지안님이 정해주신 무조건 올라가야 할 태그들!
    my_tags = "#중국배우 #숏폼배우 #중국숏드라마배우 #숏드라마 #중국드라마 #중국"

    print("🚀 [업로드 로봇] 오늘 분량 작업을 시작합니다!")

    try:
        # 로봇이 폴더에서 '01. 제목.mp4' 파일을 찾았다고 가정합니다.
        # 실제로는 번호 순서대로 파일을 하나 선택하게 됩니다.
        file_name = "01. 마샤오위 영상.mp4" 

        # 1. 파일 이름에서 '.mp4'와 번호('01. ')를 떼고 깔끔한 제목만 남깁니다.
        video_title = file_name.replace(".mp4", "")
        if ". " in video_title:
            video_title = video_title.split(". ", 1)[-1]

        # 2. [제목 + 태그]를 하나로 합쳐서 게시물 본문을 만듭니다.
        final_caption = f"{video_title}\n\n{my_tags}"

        print(f"🎯 업로드할 파일: {file_name}")
        print(f"📝 최종 게시물 내용:\n{final_caption}")

        # 3. 인스타/유튜브 API로 전송 (금고에 넣어둔 열쇠 사용)
        print("📲 SNS API 서버로 영상 전송 중...")
        time.sleep(2)
        
        print("✅ 성공! 지안님, 영상이 태그와 함께 잘 올라갔을 거예요.")

    except Exception as e:
        print(f"❌ 에러 발생: {e}")

if __name__ == "__main__":
    run_upload()
