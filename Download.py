from pytube import YouTube, Playlist

# Funktion zum Herunterladen eines einzelnen Videos
def download_single_video(video_url, save_path):
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    stream.download(save_path)
    print("Video wurde heruntergeladen:", yt.title)

# Funktion zum Herunterladen einer Playlist
def download_playlist(playlist_url, save_path):
    playlist = Playlist(playlist_url)
    for video_url in playlist.video_urls:
        download_single_video(video_url, save_path)

# Beispielaufrufe
if __name__ == "__main__":
    # Beispielaufruf für das Herunterladen eines einzelnen Videos
    single_video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    download_single_video(single_video_url, "C:/Downloads")

    # Beispielaufruf für das Herunterladen einer Playlist
    playlist_url = "https://www.youtube.com/playlist?list=PLzCxunOM5WFKBxZJD-9oqqkGi6ekzKZUz"
    download_playlist(playlist_url, "C:/Downloads")