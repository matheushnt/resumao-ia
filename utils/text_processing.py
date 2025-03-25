import whisper
import logging
from transformers import pipeline
from pathlib import Path


def transcribe_audio(path_audio: Path) -> str:
    model = whisper.load_model('medium')
    result = model.transcribe(str(path_audio))
    logging.info('Transcription completed.')
    return result['text']


def summarize_text(text: str) -> str:
    summarizer = pipeline(
        task='summarization',
        model='facebook/bart-large-cnn',
    )
    summary = summarizer(
        text,
        do_sample=False,
    )
    logging.info('Summary generated successfully.')
    return summary[0]['summary_text']


def save_summary(summary: str, filename: str = 'short_text.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(summary)
    logging.info(f'Result saved in: {filename}')
