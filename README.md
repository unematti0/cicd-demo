# CI/CD Demo

![CI/CD](https://github.com/USERNAME/cicd-demo/actions/workflows/ci.yml/badge.svg)

Automaatse CI/CD pipeline'iga Flask API.

## Endpoints

- `GET /` - API info
- `GET /health` - Health check
- `GET /products` - Products list
- `GET /api/version` - Version info
- `GET /api/status` - API status

## Pipeline

Pipeline koosneb 4 stage'ist:

1. **Validate** - Python syntax check
2. **Test** - Automated tests (pytest)
3. **Build** - Docker image + health check
4. **Deploy** - Manual production deployment

## Features

✅ Automaatne testimine  
✅ Docker containerization  
✅ Manual production approval  
✅ Health checks  
✅ Negatiivse hinna kontroll  
