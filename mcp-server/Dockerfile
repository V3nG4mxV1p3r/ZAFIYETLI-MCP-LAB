FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Log klasörünü oluştur (Wazuh'un okuması için yetkileri ayarlıyoruz)
RUN mkdir -p /var/log/mcp && chmod 777 /var/log/mcp

COPY server.py .

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]