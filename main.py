import streamlink
import subprocess
import time
import os

def download_stream(url, output_filename, quality='best'):
    while True:
        try:
            # 獲取直播流
            streams = streamlink.streams(url)
            if streams:
                # 選擇指定質量的流
                stream_url = streams[quality].url

                # 使用ffmpeg下載流
                command = [
                    'ffmpeg',
                    '-i', stream_url,
                    '-c', 'copy',
                    '-f', 'mpegts',
                    output_filename
                ]

                process = subprocess.Popen(command)

                print(f"開始下載直播到 {output_filename}")
                process.wait()

                if process.returncode != 0:
                    print("下載中斷，嘗試重新連接...")
                else:
                    print("直播結束")
                    break
            else:
                print("無法獲取直播流，等待重試...")
                time.sleep(10)  # 等待10秒鐘後重試
        except Exception as e:
            print(f"發生錯誤: {e}")
            print("等待重試...")
            time.sleep(10)  # 等待10秒鐘後重試


if __name__ == "__main__":
    youtube_url = input("請輸入YouTube直播URL: ")
    output_file = input("請輸入輸出文件名 (包括路徑): ")

    # 確保輸出目錄存在
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    download_stream(youtube_url, output_file)