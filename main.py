import streamlink
import subprocess
import time
import os

# tkinter 應不需額外安裝 除非出現錯誤
import tkinter as tk
from tkinter import filedialog

def selectPath():
    root = tk.Tk()
    root.withdraw() # 隱藏主視窗

    path = filedialog.asksaveasfilename(
        title="選擇儲存位置",
        defaultextension=".mp4", # 預設副檔名
        initialfile="stream.mp4", # 預設檔名
        initialdir=os.path.join(os.path.expanduser("~"), "Downloads"), # 預設下載位置
        filetypes=[(".mp4", "*.mp4"), (".wmv", "*.wmv"), (".mkv", "*.mkv"), (".flv", "*.flv"), (".webm", "*.webm"),\
                   ("Video", "*.mp4;*.wmv;*.mkv;*.flv;*.webm"), ("All File", "*.*")] # 下載格式過濾
    )

    return path


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

    # 防止誤關視窗
    output_file = ""
    while output_file == "":
        output_file = selectPath()

    # 確保輸出目錄存在
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    download_stream(youtube_url, output_file)
