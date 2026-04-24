# QAForge AI

QAForge AI es una plataforma SaaS de automatización de pruebas que centraliza ejecuciones en paralelo, análisis de fallos, sugerencias AI simuladas y métricas en tiempo real.

## Arquitectura

[ Next.js Frontend ]
        ↓
[ API Gateway - Express ]
        ↓
 ┌───────────────┬───────────────┬───────────────┐
 │ Auth Service  │ Test Service  │ Report Service│
 └───────────────┴───────────────┴───────────────┘
        ↓
[ Supabase PostgreSQL ]

        ↓
[ Redis Queue ]
        ↓
[ Test Workers (Playwright runners) ]

        ↓
[ Observability Layer (logs + metrics) ]

## Características

- Ejecución de pruebas en paralelo usando BullMQ y Redis
- Detección automática de fallos
- Sugerencias AI simuladas para mejorar cobertura de pruebas
- Dashboard de métricas en tiempo real con Next.js
- Integración con pipelines CI/CD en GitHub Actions
- Seguridad con JWT y rate limiting
- Validación de inputs con Zod
- Observabilidad con Winston y logs estructurados

## Estructura del proyecto

- `backend/`: API Express, colas Redis, workers y pruebas
- `frontend/`: Interfaz de usuario Next.js con dashboard de métricas

## Cómo ejecutar

### Backend

1. Copia `.env.example` a `.env` y ajusta las variables.
2. Ejecuta:

```bash
cd backend
npm install
npm run dev
```

3. Arranca el worker en otra terminal:

```bash
npm run worker
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Docker

```bash
cd backend
docker-compose up --build
```

## Endpoints principales

- `POST /api/auth/login`
- `POST /api/auth/register`
- `POST /api/tests/run`
- `GET /api/tests`
- `GET /api/tests/status/:id`
- `GET /api/reports/ai-suggestions`
- `GET /api/runs`

## Notas

- El backend usa datos mock para reports y test run details.
- El worker simula ejecución de Playwright con progreso en la cola.
- El proyecto está listo para integrar Supabase real y Playwright real.
