from fastapi import FastAPI

app = FastAPI(
    title="DevOps CI/CD Platform",
    description="A sample API for DevOps automation",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to DevOps CI/CD Platform",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/api/v1/status")
def application_status():
    return {
        "application": "devops-cicd-platform",
        "status": "running",
        "environment": "development"
    }