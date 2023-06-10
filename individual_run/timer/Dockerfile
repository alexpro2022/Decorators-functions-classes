FROM python:3.11-slim
WORKDIR /app
RUN python -m pip install --upgrade pip && \
    pip install aiohttp[speedups]
COPY timer.py .
CMD python timer.py