# QAForge AI - Arquitectura del Sistema

## Visión General

QAForge AI es una plataforma enterprise-grade de automatización de pruebas QA potenciada por inteligencia artificial. La arquitectura está diseñada para ser escalable, segura y production-ready.

## Stack Tecnológico

| Capa | Tecnología | Propósito |
|------|------------|-----------|
| Backend | FastAPI + Python 3.11 | API RESTful de alto rendimiento |
| Frontend | Next.js 14 + TypeScript | SPA moderna con SSR/SSG |
| IA | Ollama (Llama 2/Mistral) | Modelos LLM locales para generación de tests |
| QA Automation | Playwright | Automatización de pruebas multi-navegador |
| Base de Datos | PostgreSQL 15 | Datos persistentes |
| Cache | Redis 7 | Sesiones y cache distribuido |
| Message Queue | RabbitMQ/Celery | Procesamiento asíncrono |
| Containerización | Docker + Docker Compose | Entornos consistentes |
| Orquestación | Kubernetes (opcional) | Escalabilidad production |
| CI/CD | GitHub Actions | Automatización de deployment |

---

## Estructura del Proyecto

```
QAForge-AI/
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── api/               # Endpoints REST
│   │   │   └── v1/
│   │   │       ├── auth/      # Autenticación
│   │   │       ├── users/     # Gestión de usuarios
│   │   │       ├── projects/  # Proyectos QA
│   │   │       ├── test-runs/ # Ejecución de tests
│   │   │       ├── ai/        # Endpoints IA
│   │   │       ├── reports/   # Reportes
│   │   │       └── webhooks/  # Webhooks
│   │   │   ├── deps.py        # Dependencias
│   │   │   └── middlewares/   # Middlewares
│   │   ├── core/              # Configuración central
│   │   │   ├── config.py      # Settings
│   │   │   ├── security.py    # Seguridad
│   │   │   └── logging.py     # Logging
│   │   ├── models/            # Modelos ORM (SQLAlchemy)
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── services/          # Lógica de negocio
│   │   │   ├── ai/            # Servicios IA
│   │   │   ├── auth/          # Servicios auth
│   │   │   ├── testing/       # Servicios testing
│   │   │   ├── notification/  # Notificaciones
│   │   │   ├── storage/       # Almacenamiento
│   │   │   └── queue/         # Colas
│   │   └── utils/             # Utilidades
│   ├── alembic/               # Migraciones DB
│   └── tests/                 # Tests backend
│
├── frontend/                  # Next.js Frontend
│   ├── src/
│   │   ├── app/               # App Router
│   │   │   ├── dashboard/     # Dashboard principal
│   │   │   ├── projects/      # Gestión proyectos
│   │   │   ├── auth/          # Autenticación
│   │   │   ├── settings/      # Configuración
│   │   │   ├── reports/       # Reportes
│   │   │   └── ai-assistant/  # Asistente IA
│   │   ├── components/
│   │   │   ├── ui/            # Componentes UI base
│   │   │   ├── layout/        # Layout components
│   │   │   ├── forms/         # Formularios
│   │   │   ├── charts/        # Gráficos
│   │   │   ├── ai/            # Componentes IA
│   │   │   └── testing/       # Componentes testing
│   │   ├── lib/               # Librerías y utilidades
│   │   ├── hooks/             # Custom hooks
│   │   ├── stores/            # State management (Zustand)
│   │   ├── types/             # TypeScript types
│   │   ├── utils/             # Funciones utilitarias
│   │   └── config/            # Configuración frontend
│   └── public/                # Assets estáticos
│
├── tests/                     # Tests E2E y Performance
│   ├── unit/                  # Tests unitarios
│   ├── integration/           # Tests integración
│   ├── e2e/                   # Tests E2E con Playwright
│   └── performance/           # Tests de carga
│
├── infra/                     # Infraestructura
│   ├── terraform/             # IaC Terraform
│   ├── kubernetes/            # K8s manifests
│   └── helm/                  # Helm charts
│
├── docker/                    # Docker configs
│   ├── Dockerfile.backend
│   ├── Dockerfile.frontend
│   └── docker-compose.yml
│
├── .github/
│   ├── workflows/             # GitHub Actions
│   └── actions/               # Custom actions
│
├── scripts/                   # Scripts utilitarios
├── shared/                    # Código compartido
└── docs/                      # Documentación
```

---

## Arquitectura Backend

### Diseño de Capas

```
┌─────────────────────────────────────────────────────────────┐
│                      API Layer (FastAPI)                     │
│  ┌─────────┐ ┌─────────┐ ┌──────────┐ ┌──────────┐         │
│  │  Auth   │ │ Projects│ │Test Runs │ │   AI     │  ...     │
│  │ Routes  │ │ Routes  │ │ Routes   │ │ Routes   │         │
│  └────┬────┘ └────┬────┘ └────┬─────┘ └────┬─────┘         │
└───────┼───────────┼───────────┼────────────┼────────────────┘
        │           │           │            │
┌───────▼───────────▼───────────▼────────────▼────────────────┐
│                    Service Layer                             │
│  ┌─────────┐ ┌─────────┐ ┌──────────┐ ┌──────────┐         │
│  │ AuthService│ProjectService│TestService│AIService│        │
│  └────┬────┘ └────┬────┘ └────┬─────┘ └────┬─────┘         │
└───────┼───────────┼───────────┼────────────┼────────────────┘
        │           │           │            │
┌───────▼───────────▼───────────▼────────────▼────────────────┐
│                    Data Access Layer                         │
│  ┌─────────────────┐  ┌─────────────────┐                   │
│  │  Repository     │  │  Cache (Redis)  │                   │
│  │  (SQLAlchemy)   │  │                 │                   │
│  └────────┬────────┘  └─────────────────┘                   │
└───────────┼─────────────────────────────────────────────────┘
            │
┌───────────▼─────────────────────────────────────────────────┐
│                    Database (PostgreSQL)                     │
└─────────────────────────────────────────────────────────────┘
```

### Principios de Diseño

1. **Dependency Injection**: Uso extensivo de Depends() de FastAPI
2. **Repository Pattern**: Abstracción de acceso a datos
3. **Service Layer**: Lógica de negocio aislada
4. **Schema Validation**: Pydantic para validación estricta
5. **Async/Await**: Operaciones no bloqueantes

### Endpoints Principales

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | /api/v1/auth/login | Autenticación JWT |
| POST | /api/v1/auth/register | Registro de usuario |
| GET | /api/v1/projects | Listar proyectos |
| POST | /api/v1/projects | Crear proyecto |
| POST | /api/v1/ai/generate-tests | Generar tests con IA |
| POST | /api/v1/test-runs | Ejecutar tests |
| GET | /api/v1/reports/{id} | Obtener reporte |

---

## Arquitectura Frontend

### Next.js 14 App Router

```
┌─────────────────────────────────────────────────────────────┐
│                      Next.js Frontend                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                 App Router (SSR/SSG)                 │   │
│  │  ┌─────────┐ ┌─────────┐ ┌──────────┐ ┌──────────┐  │   │
│  │  │Dashboard│ │Projects │ │   AI     │ │ Reports  │  │   │
│  │  │  /      │ │ /projects│ │Assistant│ │ /reports │  │   │
│  │  └─────────┘ └─────────┘ └──────────┘ └──────────┘  │   │
│  └─────────────────────────────────────────────────────┘   │
│                           │                                 │
│  ┌────────────────────────▼────────────────────────────┐   │
│  │                  Component Library                   │   │
│  │  ┌─────────┐ ┌─────────┐ ┌──────────┐ ┌──────────┐  │   │
│  │  │   UI    │ │  Forms  │ │  Charts  │ │   AI     │  │   │
│  │  │Components│ │Components│ │Components│ │Components│  │   │
│  │  └─────────┘ └─────────┘ └──────────┘ └──────────┘  │   │
│  └─────────────────────────────────────────────────────┘   │
│                           │                                 │
│  ┌────────────────────────▼────────────────────────────┐   │
│  │              State Management (Zustand)              │   │
│  │  ┌─────────┐ ┌─────────┐ ┌──────────┐              │   │
│  │  │ Auth    │ │ Project │ │   AI     │              │   │
│  │  │ Store   │ │ Store   │ │  Store   │              │   │
│  │  └─────────┘ └─────────┘ └──────────┘              │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Características Frontend

- **Server Components**: Máximo rendimiento
- **Streaming SSR**: Carga progresiva
- **TypeScript**: Type-safety completo
- **Tailwind CSS**: Estilos utilitarios
- **React Query**: Data fetching optimizado
- **Zustand**: State management ligero

---

## Módulos de IA

### Arquitectura IA con Ollama

```
┌─────────────────────────────────────────────────────────────┐
│                     AI Service Layer                         │
│  ┌─────────────────┐  ┌─────────────────┐                   │
│  │  Test Generator │  │  Code Analyzer  │                   │
│  │     Service     │  │     Service     │                   │
│  └────────┬────────┘  └────────┬────────┘                   │
│           │                    │                             │
│  ┌────────▼────────────────────▼────────┐                   │
│  │         Ollama Client Service         │                   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ │                   │
│  │  │ Llama 2 │ │ Mistral │ │ Codellama│ │                   │
│  │  │  70B    │ │  8x7B   │ │  34B    │ │                   │
│  │  └─────────┘ └─────────┘ └─────────┘ │                   │
│  └──────────────────────────────────────┘                   │
└─────────────────────────────────────────────────────────────┘
```

### Casos de Uso IA

1. **Generación de Tests**: Crear tests automatizados desde descripciones en lenguaje natural
2. **Análisis de Código**: Detectar patrones y sugerir mejoras
3. **Auto-curación**: Auto-healing de tests flaky
4. **Generación de Datos**: Crear datos de prueba realistas
5. **Optimización**: Sugerir optimizaciones de tests

### Modelos Soportados

| Modelo | Uso | VRAM Requerida |
|--------|-----|----------------|
| Llama 2 70B | Generación compleja | 140GB |
| Llama 2 13B | Uso general | 26GB |
| Mistral 8x7B | Balance calidad/rendimiento | 48GB |
| Codellama 34B | Generación de código | 68GB |
| Codellama 7B | Entornos limitados | 14GB |

---

## Sistema QA Automation

### Playwright Integration

```
┌─────────────────────────────────────────────────────────────┐
│                   Test Execution Engine                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Playwright Test Runner                  │   │
│  │  ┌─────────┐ ┌─────────┐ ┌──────────┐ ┌──────────┐  │   │
│  │  │ Chrome  │ │ Firefox │ │  Safari  │ │  Edge    │  │   │
│  │  │ Worker  │ │ Worker  │ │  Worker  │ │  Worker  │  │   │
│  │  └─────────┘ └─────────┘ └──────────┘ └──────────┘  │   │
│  └─────────────────────────────────────────────────────┘   │
│                           │                                 │
│  ┌────────────────────────▼────────────────────────────┐   │
│  │              Test Management Service                 │   │
│  │  ┌─────────┐ ┌─────────┐ ┌──────────┐              │   │
│  │  │ Test    │ │ Test    │ │  Test    │              │   │
│  │  │ Queue   │ │ Scheduler│ │ Reporter │              │   │
│  │  └─────────┘ └─────────┘ └──────────┘              │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Tipos de Tests Soportados

1. **E2E Tests**: Flujos completos de usuario
2. **Visual Regression**: Detección de cambios visuales
3. **API Tests**: Validación de endpoints
4. **Performance Tests**: Métricas de rendimiento
5. **Accessibility Tests**: Validación WCAG

### Reportes

- **HTML Reports**: Reportes interactivos
- **Allure Reports**: Reportes detallados
- **Video Recording**: Grabación de fallos
- **Trace Viewer**: Trazas de ejecución
- **Screenshots**: Capturas automáticas

---

## Seguridad

### Autenticación y Autorización

```
┌─────────────────────────────────────────────────────────────┐
│                    Security Layer                            │
│  ┌─────────────────┐  ┌─────────────────┐                   │
│  │    JWT Auth     │  │   OAuth 2.0     │                   │
│  │   (Access +     │  │   (Google,      │                   │
│  │   Refresh)      │  │    GitHub)      │                   │
│  └────────┬────────┘  └────────┬────────┘                   │
│           │                    │                             │
│  ┌────────▼────────────────────▼────────┐                   │
│  │         RBAC (Role-Based Access)      │                   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ │                   │
│  │  │  Admin  │ │  User   │ │ Viewer  │ │                   │
│  │  └─────────┘ └─────────┘ └─────────┘ │                   │
│  └──────────────────────────────────────┘                   │
└─────────────────────────────────────────────────────────────┘
```

### Medidas de Seguridad

1. **HTTPS/TLS**: Encriptación en tránsito
2. **JWT**: Tokens con expiración
3. **Rate Limiting**: Prevención de abuso
4. **CORS**: Control de origen cruzado
5. **SQL Injection**: ORM con parameterized queries
6. **XSS Protection**: Sanitización de inputs
7. **CSRF Protection**: Tokens CSRF
8. **Secrets Management**: Vault/Secrets Manager

### Roles y Permisos

| Rol | Permisos |
|-----|----------|
| Admin | Acceso completo, gestión de usuarios |
| Manager | Crear/editar proyectos, ejecutar tests |
| Developer | Ejecutar tests, ver reportes |
| Viewer | Solo lectura |

---

## Docker Setup

### Servicios Docker

```yaml
version: '3.8'

services:
  # Backend API
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/qaforge
      - REDIS_URL=redis://redis:6379
      - OLLAMA_HOST=http://ollama:11434
    depends_on:
      - db
      - redis
      - ollama

  # Frontend
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://backend:8000/api/v1

  # PostgreSQL
  db:
    image: postgres:15-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=qaforge

  # Redis
  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data

  # Ollama (IA)
  ollama:
    image: ollama/ollama:latest
    volumes:
      - ollama_models:/root/.ollama
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]

  # RabbitMQ
  rabbitmq:
    image: rabbitmq:3-management
    ports:
      - "15672:15672"

  # Playwright (para tests)
  playwright:
    build: ./tests
    depends_on:
      - backend

volumes:
  postgres_data:
  redis_data:
  ollama_models:
```

### Dockerfiles

#### Backend Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Frontend Dockerfile
```dockerfile
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM node:20-alpine

WORKDIR /app

COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/next.config.js ./

CMD ["npm", "start"]
```

---

## Flujo CI/CD

### GitHub Actions Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    GitHub Actions                            │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                    On Push/PR                        │  │
│  └─────────────────────┬────────────────────────────────┘  │
│                        │                                    │
│  ┌─────────────────────▼────────────────────────────────┐  │
│  │                   Build Stage                        │  │
│  │  ┌─────────┐ ┌─────────┐ ┌──────────┐              │  │
│  │  │ Lint    │ │ Type    │ │ Build    │              │  │
│  │  │ Check   │ │ Check   │ │ Docker   │              │  │
│  │  └─────────┘ └─────────┘ └──────────┘              │  │
│  └─────────────────────┬────────────────────────────────┘  │
│                        │                                    │
│  ┌─────────────────────▼────────────────────────────────┐  │
│  │                   Test Stage                         │  │
│  │  ┌─────────┐ ┌─────────┐ ┌──────────┐              │  │
│  │  │ Unit    │ │Integration│ │ E2E    │              │  │
│  │  │ Tests   │ │ Tests   │ │ Tests   │              │  │
│  │  └─────────┘ └─────────┘ └──────────┘              │  │
│  └─────────────────────┬────────────────────────────────┘  │
│                        │                                    │
│  ┌─────────────────────▼────────────────────────────────┐  │
│  │               Deploy Stage (main only)               │  │
│  │  ┌─────────┐ ┌─────────┐ ┌──────────┐              │  │
│  │  │ Staging │ │ Security│ │ Production│             │  │
│  │  │ Deploy  │ │ Scan    │ │ Deploy   │              │  │
│  │  └─────────┘ └─────────┘ └──────────┘              │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Workflows Principales

1. **CI Pipeline**: Lint → Test → Build
2. **CD Pipeline**: Deploy to Staging → Security Scan → Deploy to Production
3. **Nightly Tests**: Tests de regresión nocturnos
4. **Performance Tests**: Tests de carga semanales

---

## Consideraciones de Producción

### Escalabilidad

- **Horizontal Scaling**: Kubernetes HPA
- **Database**: Read replicas, connection pooling
- **Cache**: Redis Cluster
- **Load Balancing**: Nginx/HAProxy

### Monitoreo

- **Application**: Prometheus + Grafana
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana)
- **Tracing**: Jaeger/OpenTelemetry
- **Alerting**: AlertManager

### Backup y Recovery

- **Database**: pgBackRest con retención de 30 días
- **Configuraciones**: GitOps con ArgoCD
- **Disaster Recovery**: Multi-region deployment

---

## Conclusión

QAForge AI está diseñado como una plataforma enterprise-grade que combina:

1. **Arquitectura modular** para mantenibilidad
2. **Seguridad por diseño** con múltiples capas
3. **Escalabilidad horizontal** para crecimiento
4. **Automatización completa** con CI/CD
5. **IA integrada** para potenciar QA automation

Esta arquitectura permite evolucionar el proyecto de manera sostenible mientras se mantienen los más altos estándares de calidad y seguridad.