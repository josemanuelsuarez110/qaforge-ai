# QAForge AI - Estructura de Carpetas Detallada

## Visión General del Árbol de Directorios

```
QAForge-AI/
│
├── 📄 README.md                          # Documentación principal
├── 📄 LICENSE                            # Licencia del proyecto
├── 📄 .gitignore                         # Git ignore rules
├── 📄 .env.example                       # Variables de entorno ejemplo
├── 📄 docker-compose.yml                 # Docker Compose configuration
├── 📄 Makefile                           # Comandos comunes
│
├── 📁 backend/                           # FastAPI Backend Application
│   ├── 📄 pyproject.toml                 # Python project metadata
│   ├── 📄 requirements.txt               # Python dependencies
│   ├── 📄 Dockerfile                     # Backend Docker image
│   ├── 📄 .env                           # Backend environment variables
│   ├── 📄 pytest.ini                     # Pytest configuration
│   ├── 📄 .flake8                        # Flake8 linting rules
│   │
│   ├── 📁 app/                           # Main application package
│   │   ├── 📄 __init__.py
│   │   ├── 📄 main.py                    # FastAPI application entry point
│   │   ├── 📄 config.py                  # Application configuration
│   │   │
│   │   ├── 📁 api/                       # API Layer
│   │   │   ├── 📄 __init__.py
│   │   │   ├── 📄 deps.py                # Dependency injection utilities
│   │   │   │
│   │   │   ├── 📁 v1/                    # API Version 1
│   │   │   │   ├── 📄 __init__.py
│   │   │   │   ├── 📄 router.py          # Main API router
│   │   │   │   │
│   │   │   │   ├── 📁 auth/              # Authentication endpoints
│   │   │   │   │   ├── 📄 __init__.py
│   │   │   │   │   ├── 📄 router.py      # Auth routes
│   │   │   │   │   ├── 📄 schemas.py     # Request/Response schemas
│   │   │   │   │   └── 📄 service.py     # Auth business logic
│   │   │   │   │
│   │   │   │   ├── 📁 users/             # User management endpoints
│   │   │   │   │   ├── 📄 __init__.py
│   │   │   │   │   ├── 📄 router.py
│   │   │   │   │   ├── 📄 schemas.py
│   │   │   │   │   └── 📄 service.py
│   │   │   │   │
│   │   │   │   ├── 📁 projects/          # Project management
│   │   │   │   │   ├── 📄 __init__.py
│   │   │   │   │   ├── 📄 router.py
│   │   │   │   │   ├── 📄 schemas.py
│   │   │   │   │   └── 📄 service.py
│   │   │   │   │
│   │   │   │   ├── 📁 test-runs/         # Test execution endpoints
│   │   │   │   │   ├── 📄 __init__.py
│   │   │   │   │   ├── 📄 router.py
│   │   │   │   │   ├── 📄 schemas.py
│   │   │   │   │   └── 📄 service.py
│   │   │   │   │
│   │   │   │   ├── 📁 ai/                # AI-powered features
│   │   │   │   │   ├── 📄 __init__.py
│   │   │   │   │   ├── 📄 router.py
│   │   │   │   │   ├── 📄 schemas.py
│   │   │   │   │   └── 📄 service.py
│   │   │   │   │
│   │   │   │   ├── 📁 reports/           # Test reports
│   │   │   │   │   ├── 📄 __init__.py
│   │   │   │   │   ├── 📄 router.py
│   │   │   │   │   ├── 📄 schemas.py
│   │   │   │   │   └── 📄 service.py
│   │   │   │   │
│   │   │   │   └── 📁 webhooks/          # Webhook handlers
│   │   │   │       ├── 📄 __init__.py
│   │   │   │       ├── 📄 router.py
│   │   │   │       ├── 📄 schemas.py
│   │   │   │       └── 📄 service.py
│   │   │   │
│   │   │   └── 📁 middlewares/           # Custom middlewares
│   │   │       ├── 📄 __init__.py
│   │   │       ├── 📄 authentication.py  # JWT authentication middleware
│   │   │       ├── 📄 cors.py            # CORS configuration
│   │   │       ├── 📄 rate_limit.py      # Rate limiting middleware
│   │   │       └── 📄 logging.py         # Request/Response logging
│   │   │
│   │   ├── 📁 core/                      # Core configuration
│   │   │   ├── 📄 __init__.py
│   │   │   ├── 📄 config.py              # Settings management
│   │   │   ├── 📄 security.py            # Security utilities
│   │   │   ├── 📄 logging.py             # Logging configuration
│   │   │   ├── 📄 database.py            # Database connection
│   │   │   └── 📄 celery.py              # Celery configuration
│   │   │
│   │   ├── 📁 models/                    # Database models (SQLAlchemy ORM)
│   │   │   ├── 📄 __init__.py
│   │   │   ├── 📄 base.py                # Base model class
│   │   │   ├── 📄 user.py                # User model
│   │   │   ├── 📄 project.py             # Project model
│   │   │   ├── 📄 test_run.py            # Test run model
│   │   │   ├── 📄 test_case.py           # Test case model
│   │   │   ├── 📄 report.py              # Report model
│   │   │   └── 📄 ai_prompt.py           # AI prompt history model
│   │   │
│   │   ├── 📁 schemas/                   # Pydantic schemas
│   │   │   ├── 📄 __init__.py
│   │   │   ├── 📄 base.py                # Base schema class
│   │   │   ├── 📄 user.py                # User schemas
│   │   │   ├── 📄 project.py             # Project schemas
│   │   │   ├── 📄 test_run.py            # Test run schemas
│   │   │   ├── 📄 test_case.py           # Test case schemas
│   │   │   ├── 📄 report.py              # Report schemas
│   │   │   ├── 📄 ai.py                  # AI-related schemas
│   │   │   └── 📄 common.py              # Common schemas (pagination, etc.)
│   │   │
│   │   ├── 📁 services/                  # Business logic layer
│   │   │   ├── 📄 __init__.py
│   │   │   │
│   │   │   ├── 📁 ai/                    # AI services
│   │   │   │   ├── 📄 __init__.py
│   │   │   │   ├── 📄 ollama_client.py   # Ollama API client
│   │   │   │   ├── 📄 test_generator.py  # Test generation service
│   │   │   │   ├── 📄 code_analyzer.py   # Code analysis service
│   │   │   │   ├── 📄 prompt_engineer.py # Prompt engineering utilities
│   │   │   │   └── 📄 model_manager.py   # Model selection and management
│   │   │   │
│   │   │   ├── 📁 auth/                  # Authentication services
│   │   │   │   ├── 📄 __init__.py
│   │   │   │   ├── 📄 jwt.py             # JWT token management
│   │   │   │   ├── 📄 oauth.py           # OAuth providers
│   │   │   │   ├── 📄 password.py        # Password hashing
│   │   │   │   └── 📄 permissions.py     # Permission management
│   │   │   │
│   │   │   ├── 📁 testing/               # Testing services
│   │   │   │   ├── 📄 __init__.py
│   │   │   │   ├── 📄 playwright_runner.py # Playwright test runner
│   │   │   │   ├── 📄 test_scheduler.py  # Test scheduling
│   │   │   │   ├── 📄 result_parser.py   # Parse test results
│   │   │   │   ├── 📄 report_generator.py # Generate reports
│   │   │   │   └── 📄 visual_regression.py # Visual regression testing
│   │   │   │
│   │   │   ├── 📁 notification/          # Notification services
│   │   │   │   ├── 📄 __init__.py
│   │   │   │   ├── 📄 email.py           # Email notifications
│   │   │   │   ├── 📄 slack.py           # Slack notifications
│   │   │   │   ├── 📄 webhook.py         # Webhook notifications
│   │   │   │   └── 📄 templates.py       # Notification templates
│   │   │   │
│   │   │   ├── 📁 storage/               # Storage services
│   │   │   │   ├── 📄 __init__.py
│   │   │   │   ├── 📄 local.py           # Local file storage
│   │   │   │   ├── 📄 s3.py              # AWS S3 storage
│   │   │   │   ├── 📄 minio.py           # MinIO storage
│   │   │   │   └── 📄 cleanup.py         # Storage cleanup
│   │   │   │
│   │   │   └── 📁 queue/                 # Message queue services
│   │   │       ├── 📄 __init__.py
│   │   │       ├── 📄 celery_tasks.py    # Celery task definitions
│   │   │       ├── 📄 rabbitmq.py        # RabbitMQ integration
│   │   │       └── 📄 worker.py          # Worker configuration
│   │   │
│   │   └── 📁 utils/                     # Utility functions
│   │       ├── 📄 __init__.py
│   │       ├── 📄 helpers.py             # Helper functions
│   │       ├── 📄 validators.py          # Custom validators
│   │       ├── 📄 formatters.py          # Data formatters
│   │       ├── 📄 exceptions.py          # Custom exceptions
│   │       └── 📄 constants.py           # Application constants
│   │
│   ├── 📁 alembic/                       # Database migrations
│   │   ├── 📄 env.py
│   │   ├── 📄 script.py.mako
│   │   ├── 📄 README
│   │   └── 📁 versions/                  # Migration files
│   │
│   └── 📁 tests/                         # Backend tests
│       ├── 📄 __init__.py
│       ├── 📄 conftest.py                # Pytest fixtures
│       ├── 📄 pytest.ini
│       ├── 📁 unit/                      # Unit tests
│       │   ├── 📄 test_auth.py
│       │   ├── 📄 test_projects.py
│       │   ├── 📄 test_ai.py
│       │   └── 📄 test_utils.py
│       ├── 📁 integration/               # Integration tests
│       │   ├── 📄 test_api.py
│       │   ├── 📄 test_database.py
│       │   └── 📄 test_services.py
│       └── 📁 fixtures/                  # Test fixtures
│           ├── 📄 users.py
│           ├── 📄 projects.py
│           └── 📄 test_data.py
│
├── 📁 frontend/                          # Next.js Frontend Application
│   ├── 📄 package.json                   # Node dependencies
│   ├── 📄 package-lock.json
│   ├── 📄 next.config.js                 # Next.js configuration
│   ├── 📄 tsconfig.json                  # TypeScript configuration
│   ├── 📄 tailwind.config.js             # Tailwind CSS configuration
│   ├── 📄 postcss.config.js              # PostCSS configuration
│   ├── 📄 .env.local.example             # Environment variables example
│   ├── 📄 Dockerfile                     # Frontend Docker image
│   ├── 📄 jest.config.js                 # Jest testing configuration
│   ├── 📄 playwright.config.ts           # Playwright E2E testing config
│   │
│   ├── 📁 src/                           # Source code
│   │   │
│   │   ├── 📁 app/                       # Next.js App Router
│   │   │   ├── 📄 layout.tsx             # Root layout
│   │   │   ├── 📄 page.tsx               # Home page
│   │   │   ├── 📄 loading.tsx            # Loading UI
│   │   │   ├── 📄 error.tsx              # Error boundary
│   │   │   ├── 📄 not-found.tsx          # 404 page
│   │   │   │
│   │   │   ├── 📁 dashboard/             # Dashboard section
│   │   │   │   ├── 📄 layout.tsx
│   │   │   │   ├── 📄 page.tsx
│   │   │   │   └── 📁 stats/
│   │   │   │       └── 📄 page.tsx
│   │   │   │
│   │   │   ├── 📁 projects/              # Projects section
│   │   │   │   ├── 📄 layout.tsx
│   │   │   │   ├── 📄 page.tsx
│   │   │   │   ├── 📁 [id]/
│   │   │   │   │   ├── 📄 page.tsx
│   │   │   │   │   └── 📁 test-runs/
│   │   │   │   │       └── 📄 page.tsx
│   │   │   │   └── 📁 new/
│   │   │   │       └── 📄 page.tsx
│   │   │   │
│   │   │   ├── 📁 auth/                  # Authentication section
│   │   │   │   ├── 📄 layout.tsx
│   │   │   │   ├── 📁 login/
│   │   │   │   │   └── 📄 page.tsx
│   │   │   │   ├── 📁 register/
│   │   │   │   │   └── 📄 page.tsx
│   │   │   │   └── 📁 forgot-password/
│   │   │   │       └── 📄 page.tsx
│   │   │   │
│   │   │   ├── 📁 settings/              # Settings section
│   │   │   │   ├── 📄 layout.tsx
│   │   │   │   ├── 📄 page.tsx
│   │   │   │   ├── 📁 profile/
│   │   │   │   │   └── 📄 page.tsx
│   │   │   │   └── 📁 api-keys/
│   │   │   │       └── 📄 page.tsx
│   │   │   │
│   │   │   ├── 📁 reports/               # Reports section
│   │   │   │   ├── 📄 layout.tsx
│   │   │   │   ├── 📄 page.tsx
│   │   │   │   └── 📁 [id]/
│   │   │   │       └── 📄 page.tsx
│   │   │   │
│   │   │   └── 📁 ai-assistant/          # AI Assistant section
│   │   │       ├── 📄 layout.tsx
│   │   │       ├── 📄 page.tsx
│   │   │       └── 📁 chat/
│   │   │           └── 📄 page.tsx
│   │   │
│   │   ├── 📁 components/                # React components
│   │   │   │
│   │   │   ├── 📁 ui/                    # Base UI components
│   │   │   │   ├── 📄 button.tsx
│   │   │   │   ├── 📄 input.tsx
│   │   │   │   ├── 📄 modal.tsx
│   │   │   │   ├── 📄 table.tsx
│   │   │   │   ├── 📄 card.tsx
│   │   │   │   ├── 📄 dropdown.tsx
│   │   │   │   ├── 📄 tooltip.tsx
│   │   │   │   ├── 📄 badge.tsx
│   │   │   │   ├── 📄 avatar.tsx
│   │   │   │   ├── 📄 skeleton.tsx
│   │   │   │   ├── 📄 toast.tsx
│   │   │   │   └── 📄 spinner.tsx
│   │   │   │
│   │   │   ├── 📁 layout/                # Layout components
│   │   │   │   ├── 📄 header.tsx
│   │   │   │   ├── 📄 sidebar.tsx
│   │   │   │   ├── 📄 footer.tsx
│   │   │   │   ├── 📄 navigation.tsx
│   │   │   │   └── 📄 breadcrumbs.tsx
│   │   │   │
│   │   │   ├── 📁 forms/                 # Form components
│   │   │   │   ├── 📄 form-field.tsx
│   │   │   │   ├── 📄 form-select.tsx
│   │   │   │   ├── 📄 form-checkbox.tsx
│   │   │   │   ├── 📄 form-radio.tsx
│   │   │   │   ├── 📄 form-textarea.tsx
│   │   │   │   └── 📄 form-validation.tsx
│   │   │   │
│   │   │   ├── 📁 charts/                # Chart components
│   │   │   │   ├── 📄 line-chart.tsx
│   │   │   │   ├── 📄 bar-chart.tsx
│   │   │   │   ├── 📄 pie-chart.tsx
│   │   │   │   ├── 📄 area-chart.tsx
│   │   │   │   └── 📄 dashboard-charts.tsx
│   │   │   │
│   │   │   ├── 📁 ai/                    # AI-related components
│   │   │   │   ├── 📄 chat-interface.tsx
│   │   │   │   ├── 📄 prompt-input.tsx
│   │   │   │   ├── 📄 code-preview.tsx
│   │   │   │   ├── 📄 model-selector.tsx
│   │   │   │   ├── 📄 response-stream.tsx
│   │   │   │   └── 📄 test-preview.tsx
│   │   │   │
│   │   │   └── 📁 testing/               # Testing-related components
│   │   │       ├── 📄 test-list.tsx
│   │   │       ├── 📄 test-runner.tsx
│   │   │       ├── 📄 test-results.tsx
│   │   │       ├── 📄 report-viewer.tsx
│   │   │       ├── 📄 visual-comparison.tsx
│   │   │       └── 📄 test-scheduler.tsx
│   │   │
│   │   ├── 📁 lib/                       # Libraries and utilities
│   │   │   ├── 📄 api.ts                 # API client
│   │   │   ├── 📄 axios.ts               # Axios configuration
│   │   │   ├── 📄 utils.ts               # Utility functions
│   │   │   ├── 📄 constants.ts           # Constants
│   │   │   ├── 📄 validations.ts         # Validation schemas
│   │   │   └── 📄 formatters.ts          # Data formatters
│   │   │
│   │   ├── 📁 hooks/                     # Custom React hooks
│   │   │   ├── 📄 use-auth.ts            # Authentication hook
│   │   │   ├── 📄 use-api.ts             # API calls hook
│   │   │   ├── 📄 use-local-storage.ts   # Local storage hook
│   │   │   ├── 📄 use-debounce.ts        # Debounce hook
│   │   │   ├── 📄 use-toast.ts           # Toast notification hook
│   │   │   └── 📄 use-media-query.ts     # Media query hook
│   │   │
│   │   ├── 📁 stores/                    # State management (Zustand)
│   │   │   ├── 📄 auth-store.ts          # Auth state
│   │   │   ├── 📄 project-store.ts       # Project state
│   │   │   ├── 📄 ai-store.ts            # AI state
│   │   │   ├── 📄 ui-store.ts            # UI state
│   │   │   └── 📄 test-store.ts          # Test state
│   │   │
│   │   ├── 📁 types/                     # TypeScript type definitions
│   │   │   ├── 📄 user.ts                # User types
│   │   │   ├── 📄 project.ts             # Project types
│   │   │   ├── 📄 test.ts                # Test types
│   │   │   ├── 📄 ai.ts                  # AI types
│   │   │   ├── 📄 api.ts                 # API types
│   │   │   └── 📄 common.ts              # Common types
│   │   │
│   │   ├── 📁 utils/                     # Utility functions
│   │   │   ├── 📄 cn.ts                  # Class name utility
│   │   │   ├── 📄 date.ts                # Date utilities
│   │   │   ├── 📄 string.ts              # String utilities
│   │   │   ├── 📄 array.ts               # Array utilities
│   │   │   └── 📄 object.ts              # Object utilities
│   │   │
│   │   └── 📁 config/                    # Configuration files
│   │       ├── 📄 site.ts                # Site configuration
│   │       ├── 📄 navigation.ts          # Navigation configuration
│   │       ├── 📄 api.ts                 # API configuration
│   │       └── 📄 features.ts            # Feature flags
│   │
│   ├── 📁 public/                        # Static assets
│   │   ├── 📁 images/                    # Image files
│   │   ├── 📁 fonts/                     # Font files
│   │   ├── 📁 icons/                     # Icon files
│   │   └── 📄 manifest.json              # PWA manifest
│   │
│   └── 📁 tests/                         # Frontend tests
│       ├── 📁 unit/                      # Unit tests
│       ├── 📁 integration/               # Integration tests
│       └── 📁 e2e/                       # E2E tests
│
├── 📁 tests/                             # Shared test suite
│   ├── 📁 unit/                          # Unit tests
│   │   ├── 📁 backend/                   # Backend unit tests
│   │   └── 📁 frontend/                  # Frontend unit tests
│   │
│   ├── 📁 integration/                   # Integration tests
│   │   ├── 📁 api/                       # API integration tests
│   │   └── 📁 db/                        # Database integration tests
│   │
│   ├── 📁 e2e/                           # End-to-end tests (Playwright)
│   │   ├── 📄 playwright.config.ts       # Playwright configuration
│   │   ├── 📁 auth/                      # Authentication E2E tests
│   │   ├── 📁 projects/                  # Projects E2E tests
│   │   ├── 📁 ai/                        # AI features E2E tests
│   │   ├── 📁 testing/                   # Testing features E2E tests
│   │   ├── 📁 fixtures/                  # Test fixtures
│   │   └── 📁 utils/                     # Test utilities
│   │
│   └── 📁 performance/                   # Performance tests
│       ├── 📁 load/                      # Load tests
│       ├── 📁 stress/                    # Stress tests
│       └── 📄 k6-scripts/                # k6 test scripts
│
├── 📁 infra/                             # Infrastructure as Code
│   ├── 📁 terraform/                     # Terraform configurations
│   │   ├── 📄 main.tf                    # Main Terraform config
│   │   ├── 📄 variables.tf               # Variable definitions
│   │   ├── 📄 outputs.tf                 # Output definitions
│   │   ├── 📄 providers.tf               # Provider configurations
│   │   ├── 📁 modules/                   # Terraform modules
│   │   │   ├── 📁 vpc/                   # VPC module
│   │   │   ├── 📁 eks/                   # EKS module
│   │   │   ├── 📁 rds/                   # RDS module
│   │   │   ├── 📁 elasticache/           # ElastiCache module
│   │   │   └── 📁 s3/                    # S3 module
│   │   └── 📁 environments/              # Environment-specific configs
│   │       ├── 📁 dev/
│   │       ├── 📁 staging/
│   │       └── 📁 prod/
│   │
│   ├── 📁 kubernetes/                    # Kubernetes manifests
│   │   ├── 📄 namespace.yaml             # Namespace definition
│   │   ├── 📄 configmap.yaml             # ConfigMap
│   │   ├── 📄 secrets.yaml               # Secrets (encrypted)
│   │   ├── 📁 deployments/               # Deployment manifests
│   │   │   ├── 📄 backend.yaml
│   │   │   ├── 📄 frontend.yaml
│   │   │   ├── 📄 ollama.yaml
│   │   │   └── 📄 worker.yaml
│   │   ├── 📁 services/                  # Service manifests
│   │   │   ├── 📄 backend-service.yaml
│   │   │   ├── 📄 frontend-service.yaml
│   │   │   └── 📄 ollama-service.yaml
│   │   ├── 📁 ingress/                   # Ingress configuration
│   │   │   └── 📄 ingress.yaml
│   │   └── 📁 hpa/                       # Horizontal Pod Autoscaler
│   │       └── 📄 hpa.yaml
│   │
│   └── 📁 helm/                          # Helm charts
│       ├── 📁 charts/
│       │   └── 📁 qaforge-ai/
│       │       ├── 📄 Chart.yaml
│       │       ├── 📄 values.yaml
│       │       ├── 📄 values-dev.yaml
│       │       ├── 📄 values-staging.yaml
│       │       ├── 📄 values-prod.yaml
│       │       └── 📁 templates/
│       │           ├── 📄 deployment.yaml
│       │           ├── 📄 service.yaml
│       │           ├── 📄 configmap.yaml
│       │           ├── 📄 ingress.yaml
│       │           └── 📄 hpa.yaml
│       └── 📁 templates/                 # Helm template partials
│
├── 📁 docker/                            # Docker configurations
│   ├── 📄 Dockerfile.backend             # Backend Dockerfile
│   ├── 📄 Dockerfile.frontend            # Frontend Dockerfile
│   ├── 📄 Dockerfile.ollama              # Ollama Dockerfile
│   ├── 📄 Dockerfile.playwright          # Playwright Dockerfile
│   ├── 📄 docker-compose.yml             # Docker Compose for development
│   ├── 📄 docker-compose.prod.yml        # Docker Compose for production
│   ├── 📄 .dockerignore                  # Docker ignore rules
│   └── 📁 scripts/                       # Docker scripts
│       ├── 📄 build.sh
│       ├── 📄 run.sh
│       └── 📄 cleanup.sh
│
├── 📁 .github/                           # GitHub configurations
│   ├── 📁 workflows/                     # GitHub Actions workflows
│   │   ├── 📄 ci.yml                     # CI pipeline
│   │   ├── 📄 cd.yml                     # CD pipeline
│   │   ├── 📄 security.yml               # Security scanning
│   │   ├── 📄 performance.yml            # Performance testing
│   │   ├── 📄 nightly-tests.yml          # Nightly test suite
│   │   └── 📄 release.yml                # Release automation
│   │
│   └── 📁 actions/                       # Custom GitHub Actions
│       ├── 📁 setup-ollama/
│       │   └── 📄 action.yml
│       ├── 📁 run-playwright/
│       │   └── 📄 action.yml
│       └── 📁 deploy-k8s/
│           └── 📄 action.yml
│
├── 📁 scripts/                           # Utility scripts
│   ├── 📄 setup.sh                       # Initial setup script
│   ├── 📄 dev.sh                         # Development environment setup
│   ├── 📄 test.sh                        # Run all tests
│   ├── 📄 lint.sh                        # Run linters
│   ├── 📄 format.sh                      # Format code
│   ├── 📄 backup.sh                      # Database backup
│   ├── 📄 deploy.sh                      # Deployment script
│   └── 📄 cleanup.sh                     # Cleanup script
│
├── 📁 shared/                            # Shared code between frontend/backend
│   ├── 📄 constants.ts                   # Shared constants
│   ├── 📄 validators.ts                  # Shared validators
│   ├── 📄 formatters.ts                  # Shared formatters
│   ├── 📄 errors.ts                      # Shared error definitions
│   ├── 📄 types.ts                       # Shared type definitions
│   └── 📄 utils.ts                       # Shared utilities
│
└── 📁 docs/                              # Documentation
    ├── 📄 ARCHITECTURE.md                # Architecture documentation
    ├── 📄 FOLDER_STRUCTURE.md            # This file
    ├── 📄 API.md                         # API documentation
    ├── 📄 DEPLOYMENT.md                  # Deployment guide
    ├── 📄 SECURITY.md                    # Security documentation
    ├── 📄 CONTRIBUTING.md                # Contribution guidelines
    ├── 📄 CHANGELOG.md                   # Version changelog
    └── 📁 diagrams/                      # Architecture diagrams
        ├── 📄 system-architecture.png
        ├── 📄 data-flow.png
        ├── 📄 deployment.png
        └── 📄 ci-cd-pipeline.png
```

## Descripción de Carpetas Principales

### `/backend`
Contiene la aplicación FastAPI con arquitectura de capas:
- **api/**: Endpoints REST organizados por dominio
- **core/**: Configuración central y utilidades compartidas
- **models/**: Modelos de base de datos SQLAlchemy
- **schemas/**: Esquemas Pydantic para validación
- **services/**: Lógica de negocio separada por dominio

### `/frontend`
Aplicación Next.js 14 con App Router:
- **app/**: Rutas y páginas organizadas por feature
- **components/**: Componentes React reutilizables
- **lib/**: Utilidades y configuración de librerías
- **stores/**: State management con Zustand
- **types/**: Definiciones TypeScript

### `/tests`
Suite completa de pruebas:
- **unit/**: Tests unitarios para backend y frontend
- **integration/**: Tests de integración API y base de datos
- **e2e/**: Tests end-to-end con Playwright
- **performance/**: Tests de carga y estrés

### `/infra`
Infraestructura como código:
- **terraform/**: Configuración de infraestructura cloud
- **kubernetes/**: Manifiestos K8s para deployment
- **helm/**: Charts Helm para gestión de releases

### `/docker`
Contenedores Docker:
- Dockerfiles para cada servicio
- Docker Compose para desarrollo local
- Configuraciones de red y volúmenes

### `/.github`
Automatización con GitHub Actions:
- **workflows/**: Pipelines CI/CD
- **actions/**: Acciones personalizadas

### `/scripts`
Scripts de utilidad para desarrollo y operaciones

### `/shared`
Código compartido entre frontend y backend (tipos, validaciones, constantes)

### `/docs`
Documentación completa del proyecto

## Convenciones de Nomenclatura

### Archivos
- **Backend Python**: `snake_case.py`
- **Frontend TypeScript**: `kebab-case.tsx`
- **Configuración**: `.config.extension`
- **Tests**: `test_*.py` o `*.test.ts`

### Carpetas
- **Dominios**: `plural` (users, projects, tests)
- **Utilidades**: `singular` (utils, helpers, types)
- **Infraestructura**: `descriptive` (terraform, kubernetes)

## Estructura de Base de Datos

```
qaforge_db/
├── users/                    # User management
│   ├── id (UUID)
│   ├── email
│   ├── password_hash
│   ├── role
│   └── created_at
│
├── projects/                 # QA Projects
│   ├── id (UUID)
│   ├── name
│   ├── description
│   ├── owner_id (FK -> users)
│   ├── settings (JSON)
│   └── created_at
│
├── test_cases/               # Individual test cases
│   ├── id (UUID)
│   ├── project_id (FK -> projects)
│   ├── name
│   ├── description
│   ├── code (TEXT)
│   ├── type (e2e, unit, api)
│   ├── ai_generated (boolean)
│   └── created_at
│
├── test_runs/                # Test execution records
│   ├── id (UUID)
│   ├── project_id (FK -> projects)
│   ├── status (pending, running, completed, failed)
│   ├── started_at
│   ├── completed_at
│   ├── total_tests
│   ├── passed_tests
│   ├── failed_tests
│   └── report_url
│
├── ai_prompts/               # AI prompt history
│   ├── id (UUID)
│   ├── user_id (FK -> users)
│   ├── project_id (FK -> projects)
│   ├── prompt_text
│   ├── response_text
│   ├── model_used
│   └── created_at
│
└── reports/                  # Test reports
    ├── id (UUID)
    ├── test_run_id (FK -> test_runs)
    ├── report_type (html, pdf, json)
    ├── storage_url
    ├── generated_at
    └── metadata (JSON)
```

## Variables de Entorno

### Backend (.env)
```env
# Application
APP_NAME=QAForge AI
APP_ENV=development
DEBUG=True
SECRET_KEY=your-secret-key

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/qaforge

# Redis
REDIS_URL=redis://localhost:6379/0

# Ollama
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama2

# JWT
JWT_SECRET_KEY=your-jwt-secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
CORS_ORIGINS=http://localhost:3000

# Storage
STORAGE_TYPE=local
STORAGE_PATH=./uploads
```

### Frontend (.env.local)
```env
# API
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1

# Authentication
NEXT_PUBLIC_AUTH_PROVIDER=jwt

# Features
NEXT_PUBLIC_AI_ENABLED=true
NEXT_PUBLIC_PLAYWRIGHT_ENABLED=true
```

Esta estructura está diseñada para ser escalable, mantenible y seguir las mejores prácticas de la industria para proyectos enterprise-grade.