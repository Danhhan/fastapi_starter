FROM python:3.11-slim

WORKDIR /app

# Sao chép file requirements.txt từ thư mục gốc vào
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ code dự án vào container
COPY . .

# Lệnh chạy chuẩn (Vì main.py giờ nằm trong folder app nên phải gọi là app.main)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]