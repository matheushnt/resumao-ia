# ResumãoIA

Este projeto permite baixar vídeos do YouTube, extrair o áudio, transcrevê-lo, gerar um resumo e salvá-lo em um arquivo .txt.

## 📌 Funcionalidades
- Baixa vídeos do YouTube
- Extrai o áudio do vídeo
- Transcreve o áudio usando Whisper
- Resume o conteúdo utilizando BART
- Salva o resumo em um arquivo de texto

## 🚀 Tecnologias Utilizadas
- `whisper` (Reconhecimento de fala)
- `yt-dlp` (Download de vídeos do YouTube)
- `ffmpeg` (Extração de áudio)
- `transformers` (Modelos de NLP da Hugging Face)
- `pathlib` (Gerenciamento de arquivos)

## 🛠️ Instalação
Antes de executar o projeto, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

## 📌 Como Usar
1. Defina a URL do vídeo do YouTube no `main.py`.
2. Execute o script:

```bash
python main.py
```

3. O resumo será salvo no arquivo `short_text.txt`.
