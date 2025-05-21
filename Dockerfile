FROM python:3.13-slim
WORKDIR /app
RUN pip install --no-cache-dir aiogram openai python-dotenv
COPY app/ ./app/
COPY run.py config.py ./
RUN useradd -m botuser && chown -R botuser:botuser /app
USER botuser

CMD ["python", "run.py"]