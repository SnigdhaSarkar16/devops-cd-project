# Simple CD Pipeline using GitHub Actions

A small Flask web app with an automated CI/CD pipeline.
Every push to `main` automatically **tests** the code, **builds a Docker image**, and **deploys** (publishes) it to GitHub Container Registry.

## Pipeline flow
```
git push -> GitHub Actions -> Run pytest -> Build Docker image -> Push to ghcr.io
```

## Tools used
Git, GitHub, GitHub Actions, Python (Flask), PyTest, Docker, GitHub Container Registry

## Project structure
```
app.py                      Flask application
tests/test_app.py           Automated unit tests
requirements.txt            Dependencies
Dockerfile                  Container definition
.github/workflows/cd.yml    CI/CD pipeline
```

## Run locally
```
pip install -r requirements.txt
pytest -v
python app.py                # open http://localhost:5000
```

## Run with Docker
```
docker build -t devops-cd-demo .
docker run -p 5000:5000 devops-cd-demo
```

## Endpoints
- `/`  welcome message
- `/health`  health check
- `/add/<a>/<b>`  adds two numbers
