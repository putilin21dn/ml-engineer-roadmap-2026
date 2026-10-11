FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
COPY /scripts /app/scripts
COPY /configs /app/configs
COPY /api /app/api

ENV MLFLOW_TRACKING_URI=sqlite:///mlflow.db \
    MODEL_NAME=churn-classifier \
    MODEL_ALIAS=production

RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]