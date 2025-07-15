from fastapi import FastAPI, Request
import uvicorn
import os
from prometheus_client import Counter

# Define Prometheus metrics
REQUESTS = Counter("http_requests_total", "Total HTTP requests", ["endpoint"])

app = FastAPI()


@app.get("/")
def hello(request: Request):
    REQUESTS.labels(endpoint="/").inc()
    return "Hello World!"


if __name__ == "__main__":
    print("Starting webserver...")
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8080)),
        log_level=os.getenv("LOG_LEVEL", "info"),
        proxy_headers=True
    )
