from yt_dlp import YoutubeDL
import os

class download_API():
    def __init__(self):
        self.aviso = ''
        self.Download_folder = self.get_downloads_folder()
    
        self.ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': os.path.join(self.Download_folder, '%(title)s.%(ext)s'),

                }
        
        
    def get_downloads_folder(self):
        return 'musicas'

    def get_name(self, video_url):
        try:
            with YoutubeDL() as ydl:
                info = ydl.extract_info(video_url, download=False, process=False)
                titulo = info.get('title', None)
                return titulo, "OK"
        except Exception as e:
            print(e)
            return e, "ERROR"

    def audio(self, video_url):
        self.Download_folder = self.Download_folder
        
        try:    
            with YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([video_url])
                
            return "COMPLETE"
        except Exception as e:
            print(e)
            return e

if(__name__ == "__main__"):
    urls = input()

    downloader = download_API()
    downloader.audio(urls)
