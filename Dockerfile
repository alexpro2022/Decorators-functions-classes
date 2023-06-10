FROM python:3.11-slim
WORKDIR /app
RUN python -m pip install --upgrade pip && \
    pip install aiohttp[speedups] && \
    pip install httpx
COPY . .
CMD python main.py
