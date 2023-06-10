FROM python:3.11-slim
WORKDIR /app
RUN python -m pip install --upgrade pip && \
    pip install httpx
COPY github_links.py .
CMD python github_links.py