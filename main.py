import ffmpeg
import logging
from pathlib import Path
from yt_dlp import YoutubeDL
from utils.text_processing import (
    transcribe_audio,
    summarize_text,
    save_summary
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def download_youtube_video(url: str) -> Path:
    ydl_options = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': True,
    }
    with YoutubeDL(ydl_options) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = info_dict.get('title', 'unknown_video')
        video_ext = info_dict.get('ext', 'mp4')

    path_video = Path(f'{video_title}.{video_ext}')
    logging.info(f'Downloaded video: {path_video}')
    return path_video


def extract_audio(path_video: Path) -> Path:
    path_audio = Path('extracted_audio.mp3')
    ffmpeg.input(str(path_video)).output(str(path_audio)).run()
    logging.info(f'Extracted audio: {path_audio}')
    return path_audio


def main(url_video: str):
    path_video = download_youtube_video(url_video)
    path_audio = extract_audio(path_video)
    transcribed_text = transcribe_audio(path_audio)
    summary = summarize_text(transcribed_text)
    save_summary(summary)
    logging.info('Process completed successfully.')


if __name__ == '__main__':
    url = '<your_url>'
    main(url_video=url)
