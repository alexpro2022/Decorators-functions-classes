FROM python:3.11-slim
WORKDIR /app
RUN python -m pip install --upgrade pip && \
    pip install aiohttp[speedups] && \
    pip install httpx
COPY data .
COPY functions .
CMD python github_links.py && \
    python create_dict.py && \
    python new_list.py && \
    python text_class.py && \
    python timer.py