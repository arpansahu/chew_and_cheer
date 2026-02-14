# Docker Image Configuration - Centralized Setup

## 🎯 Single Source of Truth

Docker image configuration is now **fully centralized** in the `.env` file - used by both local deployment and Jenkins CI/CD pipelines.

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
// Loads configuration from .env file
environment {
    REGISTRY = readDockerConfig('DOCKER_REGISTRY')      // from .env
    REPOSITORY = readDockerConfig('DOCKER_REPOSITORY')  // from .env
    IMAGE_TAG = "${env.BUILD_ID}"                       // dynamic per build
}
```
**Purpose:**
- Reads registry/repository from .env (single source of truth)
- Uses BUILD_ID for versioned tags (e.g., image:103)
- Pushes to Harbor registry
- Tags successful builds as `:latest`

### 4. **Jenkinsfile-deploy** (CI/CD Deploy)
```groovy
// Loads configuration from .env file
environment {
    REGISTRY = readDockerConfig('DOCKER_REGISTRY')      // from .env
    REPOSITORY = readDockerConfig('DOCKER_REPOSITORY')  // from .env
    IMAGE_TAG = readDockerConfig('DOCKER_IMAGE_TAG')    // from .env (usually "latest")
}
```
**Purpose:**
- Reads all Docker config from .env (single source of truth)
- Pulls pre-built image from Harbor
- Deploys to Kubernetes or Docker

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

### ✅ True Single Source of Truth
- **`.env` is the ONLY place** to configure Docker registry/repository/tag
- Used by local development, server deployment, AND Jenkins CI/CD
- Change once, applies everywhere automatically
- Zero duplication across files

### ✅ Environment Separation
- **Local/Server:** Uses .env variables directly
- **CI/CD:** Jenkins reads from .env file in workspace
- All environments stay in sync automatically

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

### To Change Registry, Repository, or Tag:

**Single Step - Edit `.env`:**
```env
DOCKER_REGISTRY=your-registry.com
DOCKER_REPOSITORY=your-org/your-app
DOCKER_IMAGE_TAG=latest
```

**That's it!** Changes automatically apply to:
- ✅ Local docker-compose deployment
- ✅ Server docker-compose deployment  
- ✅ Jenkins build pipeline (registry/repository)
- ✅ Jenkins deploy pipeline (all three values)

**Note:** Jenkinsfile-build always uses `BUILD_ID` for `IMAGE_TAG` to create versioned builds, but reads registry and repository from .env.

## 📝 Best Practices

1. **Keep .env out of version control** (already in .gitignore)
2. **Use env.example** as template for new environments
3. **All Docker config is in .env** - truly single source of truth
4. **docker-compose.yml uses env vars** - no hardcoded values
5. **Jenkins reads .env at runtime** - always up to date

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
