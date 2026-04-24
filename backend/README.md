# QAForge AI Backend

Backend base para la plataforma **QAForge AI**, una demo de automatizacion de pruebas con:

- API Express
- Cola BullMQ con Redis
- Worker de ejecucion de tests
- Validacion con Zod
- Logging estructurado con Winston
- Tests con Jest y Supertest
- Docker y workflow de CI

## Quick start

```bash
cd backend
cp .env.example .env
npm install
npm test
npm run dev
```

## Endpoints

```text
GET    /health
POST   /api/auth/login
POST   /api/tests/run
GET    /api/runs
GET    /api/reports/summary
```

## Nota sobre Redis

Por defecto, `REDIS_DISABLED=true` para que el proyecto funcione sin infraestructura externa durante desarrollo y pruebas.

Cuando quieras usar BullMQ de verdad:

1. Levanta Redis
2. Cambia `REDIS_DISABLED=false`
3. Ejecuta `npm run worker`
