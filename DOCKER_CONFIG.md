# Docker Image Configuration - Centralized Setup

## 🎯 Single Source of Truth

Docker image configuration is now centralized to reduce duplication and make updates easier.

## 📋 Configuration Locations

### 1. **.env** (Local/Server Deployment)
```env
DOCKER_REGISTRY=harbor.arpansahu.space
DOCKER_REPOSITORY=library/chew_and_cheer
DOCKER_IMAGE_TAG=latest
```
**Used by:** `docker-compose.yml`
**Purpose:** Single source of truth for local development and direct server deployment

### 2. **docker-compose.yml** (Uses .env variables)
```yaml
image: ${DOCKER_REGISTRY}/${DOCKER_REPOSITORY}:${DOCKER_IMAGE_TAG}
```
**Purpose:** 
- Local development: Builds from Dockerfile
- Server deployment: Can pull from registry if image exists
- Uses environment variables from .env

### 3. **Jenkinsfile-build** (CI/CD Build)
```groovy
environment {
    REGISTRY = "harbor.arpansahu.space"
    REPOSITORY = "library/chew_and_cheer"
    IMAGE_TAG = "${env.BUILD_ID}"
}
```
**Purpose:**
- Builds Docker image with versioned tags (BUILD_ID)
- Pushes to Harbor registry
- Independent of .env (uses Jenkins environment)

### 4. **Jenkinsfile-deploy** (CI/CD Deploy)
```groovy
environment {
    REGISTRY = "harbor.arpansahu.space"
    REPOSITORY = "library/chew_and_cheer"
    IMAGE_TAG = "latest"
}
```
**Purpose:**
- Pulls pre-built image from Harbor
- Deploys to Kubernetes or Docker
- Independent of .env (uses Jenkins environment)

## 🔄 Deployment Flow

```
┌─────────────────────────────────────────────────────────────┐
│  Development Flow                                            │
└─────────────────────────────────────────────────────────────┘

1. Local Development
   └─> docker-compose.yml (uses .env)
       └─> Builds from Dockerfile OR pulls from registry

┌─────────────────────────────────────────────────────────────┐
│  CI/CD Flow                                                  │
└─────────────────────────────────────────────────────────────┘

2. Code Push → GitHub
   └─> Triggers Jenkins Build

3. Jenkins Build (Jenkinsfile-build)
   └─> Builds image: harbor.arpansahu.space/library/chew_and_cheer:BUILD_ID
   └─> Tags as: harbor.arpansahu.space/library/chew_and_cheer:latest
   └─> Pushes to Harbor Registry

4. Jenkins Deploy (Jenkinsfile-deploy)
   └─> Pulls: harbor.arpansahu.space/library/chew_and_cheer:latest
   └─> Deploys to Server (Kubernetes or Docker)
```

## 🎨 Benefits of This Architecture

### ✅ Centralized Configuration
- `.env` is the single source for local/server deployment
- Change registry once, applies everywhere

### ✅ Environment Separation
- **Local:** Uses .env variables
- **CI/CD:** Uses Jenkins environment variables
- No cross-contamination

### ✅ Flexibility
```bash
# Local: Build from source
docker-compose build

# Local: Pull from registry
docker-compose pull

# Local: Build and run
docker-compose up --build

# Server: Deploy latest
docker-compose up -d
```

### ✅ Version Control
- Jenkins uses BUILD_ID for versioned images
- docker-compose uses 'latest' for simple deployment
- Can override tag: `DOCKER_IMAGE_TAG=123 docker-compose up`

## 🔧 Configuration Updates

### To Change Registry or Repository:

**Option 1: Local/Server Deployment**
Edit `.env`:
```env
DOCKER_REGISTRY=your-registry.com
DOCKER_REPOSITORY=your-org/your-app
DOCKER_IMAGE_TAG=latest
```

**Option 2: CI/CD Pipeline**
Update both Jenkinsfiles:
- `Jenkinsfile-build`: Change REGISTRY and REPOSITORY
- `Jenkinsfile-deploy`: Change REGISTRY and REPOSITORY

## 📝 Best Practices

1. **Keep .env out of version control** (already in .gitignore)
2. **Use env.example** as template for new environments
3. **Jenkinsfiles are committed** - they define CI/CD behavior
4. **docker-compose.yml references .env** - don't hardcode values

## 🚀 Quick Commands

```bash
# Use local .env configuration
docker-compose up -d

# Override image tag
DOCKER_IMAGE_TAG=v1.2.3 docker-compose up -d

# Pull latest from registry
docker-compose pull

# Build locally
docker-compose build

# View current configuration
docker-compose config
```

## 🔐 Security Notes

- Harbor credentials are in .env (HARBOR_USERNAME, HARBOR_PASSWORD)
- Jenkins uses credentials stored in Jenkins Credentials Manager
- Never commit .env to version control
- Use env.example for documentation only

---

**Last Updated:** February 14, 2026  
**Maintained by:** DevOps Team
