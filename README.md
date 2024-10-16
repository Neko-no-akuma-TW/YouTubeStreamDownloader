# YouTubeStreamDownloader 

---

## 介紹
這是一個用於下載YouTube直播的Python程式碼</br>
本專案僅支持下載正在直播的YouTube直播，並不支持已結束以及尚未開始的YouTube直播

---

## 使用方法
1. 安裝Python
2. 安裝所需套件
```
pip install -r requirements.txt
```
3. 請確保您的電腦上有安裝ffmpeg，並且有將ffmpeg加入到系統環境變數PATH內。如果不知如何安裝，這裡有一個[文章](https://the-walking-fish.com/p/install-ffmpeg-on-windows/)可供您參考
4. 執行程式
```
python main.py
```

---

## 注意事項
### 關於本程式內的其中一個輸入，`輸入輸出文件名`，請注意以下事項：
如果您要將輸出檔案儲存在程式所在位置，請輸入如下格式(檔案名稱請自行更改成你所需要的檔案名稱)：
```
.\<檔案名稱>.mp4
```
若您需要自行指定儲存位置，請輸入如下格式(路徑與檔案名稱請自行更改成你所需要的檔案名稱)：
```
<硬碟符(即C、D、E等)>:\<路徑>\<檔案名稱>.mp4
```

---

## 歡迎各位創建PR(Pull Request)讓這個專案變得更好

---

## 感謝以下的協作者們
因為有你們，所以這個專案才會變得更好。<br/>
<a href="https://github.com/Neko-no-akuma-TW/YouTubeStreamDownloader/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Neko-no-akuma-TW/YouTubeStreamDownloader" />
</a>

---

# 版權聲明
此專案僅在此網站(Github)發布並開源，若於其他網站下載，造成使用者財產損失，開發者將不負相關責任。

此外，本專案為完全免費開源，若使用者於其他網站花費購買此開源軟件，開發者將不負賠償責任。

最後，任何使用者皆可以使用此專案進行二次開發，但是禁止將此專案用於商業與營利用途，並且需要標示原創作者與作品來源。