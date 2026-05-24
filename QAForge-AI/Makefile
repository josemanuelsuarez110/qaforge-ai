# QAForge AI - Makefile
# Common development and deployment commands

.PHONY: help setup dev stop clean test lint format build push deploy

# ──────────────────────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────────────────────
DOCKER_COMPOSE := docker-compose
PYTHON := python3
PIP := pip3
NPM := npm
NPM_FRONTEND := cd frontend && npm
NPM_TESTS := cd tests && npm
ALEMBIC := cd backend && alembic
PYTEST := cd backend && pytest
BLACK := cd backend && black
RUFF := cd backend && ruff
MYPY := cd backend && mypy

# Colors for output
COLOR_RESET := \033[0m
COLOR_GREEN := \033[32m
COLOR_YELLOW := \033[33m
COLOR_BLUE := \033[34m
COLOR_RED := \033[31m

# ──────────────────────────────────────────────────────────────
# Help
# ──────────────────────────────────────────────────────────────
help:
	@echo "$(COLOR_BLUE)QAForge AI - Available Commands$(COLOR_RESET)"
	@echo ""
	@echo "$(COLOR_YELLOW)Development:$(COLOR_RESET)"
	@echo "  make setup          - Initial project setup"
	@echo "  make dev            - Start development environment"
	@echo "  make stop           - Stop all containers"
	@echo "  make restart        - Restart all containers"
	@echo "  make logs           - View container logs"
	@echo "  make shell-backend  - Open shell in backend container"
	@echo "  make shell-frontend - Open shell in frontend container"
	@echo "  make shell-db       - Open psql shell in database"
	@echo ""
	@echo "$(COLOR_YELLOW)Testing:$(COLOR_RESET)"
	@echo "  make test           - Run all tests"
	@echo "  make test-backend   - Run backend tests"
	@echo "  make test-frontend  - Run frontend tests"
	@echo "  make test-e2e       - Run E2E tests with Playwright"
	@echo "  make test-coverage  - Generate coverage report"
	@echo ""
	@echo "$(COLOR_YELLOW)Code Quality:$(COLOR_RESET)"
	@echo "  make lint           - Run linters"
	@echo "  make format         - Format code"
	@echo "  make type-check     - Run type checking"
	@echo "  make security       - Run security scans"
	@echo ""
	@echo "$(COLOR_YELLOW)Database:$(COLOR_RESET)"
	@echo "  make migrate        - Run database migrations"
	@echo "  make migration      - Create new migration (name=$$name)"
	@echo "  make db-reset       - Reset database"
	@echo "  make db-backup      - Backup database"
	@echo ""
	@echo "$(COLOR_YELLOW)Docker:$(COLOR_RESET)"
	@echo "  make build          - Build Docker images"
	@echo "  make push           - Push images to registry"
	@echo "  make clean          - Clean Docker resources"
	@echo ""
	@echo "$(COLOR_YELLOW)Deployment:$(COLOR_RESET)"
	@echo "  make deploy-staging - Deploy to staging"
	@echo "  make deploy-prod    - Deploy to production"
	@echo ""

# ──────────────────────────────────────────────────────────────
# Setup
# ──────────────────────────────────────────────────────────────
setup:
	@echo "$(COLOR_GREEN)Setting up QAForge AI development environment...$(COLOR_RESET)"
	
	@echo "$(COLOR_BLUE)Creating virtual environment...$(COLOR_RESET)"
	$(PYTHON) -m venv venv
	source venv/bin/activate
	
	@echo "$(COLOR_BLUE)Installing backend dependencies...$(COLOR_RESET)"
	cd backend && $(PIP) install -r requirements.txt
	cd backend && $(PIP) install -r requirements-dev.txt
	
	@echo "$(COLOR_BLUE)Installing frontend dependencies...$(COLOR_RESET)"
	cd frontend && $(NPM) install
	
	@echo "$(COLOR_BLUE)Installing test dependencies...$(COLOR_RESET)"
	cd tests && $(NPM) install
	
	@echo "$(COLOR_BLUE)Installing Playwright browsers...$(COLOR_RESET)"
	cd tests && npx playwright install
	
	@echo "$(COLOR_GREEN)Setup complete!$(COLOR_RESET)"
	@echo ""
	@echo "$(COLOR_YELLOW)Next steps:$(COLOR_RESET)"
	@echo "  1. Copy .env.example to .env and configure"
	@echo "  2. Run 'make dev' to start development environment"

# ──────────────────────────────────────────────────────────────
# Development Environment
# ──────────────────────────────────────────────────────────────
dev:
	@echo "$(COLOR_GREEN)Starting development environment...$(COLOR_RESET)"
	$(DOCKER_COMPOSE) up -d
	@echo ""
	@echo "$(COLOR_GREEN)Services started!$(COLOR_RESET)"
	@echo ""
	@echo "$(COLOR_YELLOW)Access URLs:$(COLOR_RESET)"
	@echo "  Frontend:     http://localhost:3000"
	@echo "  Backend API:  http://localhost:8000"
	@echo "  API Docs:     http://localhost:8000/docs"
	@echo "  PGAdmin:      http://localhost:8080"
	@echo "  Redis Cmdr:   http://localhost:8081"
	@echo "  RabbitMQ:     http://localhost:15672"
	@echo "  Flower:       http://localhost:5555"

stop:
	@echo "$(COLOR_YELLOW)Stopping all containers...$(COLOR_RESET)"
	$(DOCKER_COMPOSE) down

restart:
	@echo "$(COLOR_YELLOW)Restarting all containers...$(COLOR_RESET)"
	$(DOCKER_COMPOSE) restart

logs:
	@echo "$(COLOR_BLUE)Viewing logs (Ctrl+C to exit)...$(COLOR_RESET)"
	$(DOCKER_COMPOSE) logs -f

# ──────────────────────────────────────────────────────────────
# Shell Access
# ──────────────────────────────────────────────────────────────
shell-backend:
	@echo "$(COLOR_BLUE)Opening shell in backend container...$(COLOR_RESET)"
	$(DOCKER_COMPOSE) exec backend /bin/bash

shell-frontend:
	@echo "$(COLOR_BLUE)Opening shell in frontend container...$(COLOR_RESET)"
	$(DOCKER_COMPOSE) exec frontend /bin/bash

shell-db:
	@echo "$(COLOR_BLUE)Opening psql shell in database...$(COLOR_RESET)"
	$(DOCKER_COMPOSE) exec db psql -U qaforge -d qaforge

shell-redis:
	@echo "$(COLOR_BLUE)Opening redis-cli...$(COLOR_RESET)"
	$(DOCKER_COMPOSE) exec redis redis-cli

# ──────────────────────────────────────────────────────────────
# Testing
# ──────────────────────────────────────────────────────────────
test: test-backend test-frontend

test-backend:
	@echo "$(COLOR_GREEN)Running backend tests...$(COLOR_RESET)"
	cd backend && $(PYTEST) tests/ -v --tb=short

test-backend-unit:
	@echo "$(COLOR_GREEN)Running backend unit tests...$(COLOR_RESET)"
	cd backend && $(PYTEST) tests/unit -v --tb=short

test-backend-integration:
	@echo "$(COLOR_GREEN)Running backend integration tests...$(COLOR_RESET)"
	cd backend && $(PYTEST) tests/integration -v --tb=short

test-frontend:
	@echo "$(COLOR_GREEN)Running frontend tests...$(COLOR_RESET)"
	cd frontend && $(NPM) run test:unit

test-e2e:
	@echo "$(COLOR_GREEN)Running E2E tests with Playwright...$(COLOR_RESET)"
	cd tests && npx playwright test --reporter=list

test-e2e-ui:
	@echo "$(COLOR_GREEN)Running E2E tests with UI...$(COLOR_RESET)"
	cd tests && npx playwright test --ui

test-coverage:
	@echo "$(COLOR_GREEN)Generating coverage report...$(COLOR_RESET)"
	cd backend && $(PYTEST) tests/ --cov=app --cov-report=html --cov-report=term
	@echo "$(COLOR_BLUE)Open coverage report: open backend/htmlcov/index.html$(COLOR_RESET)"

# ──────────────────────────────────────────────────────────────
# Code Quality
# ──────────────────────────────────────────────────────────────
lint: lint-backend lint-frontend

lint-backend:
	@echo "$(COLOR_GREEN)Running backend linters...$(COLOR_RESET)"
	cd backend && $(RUFF) check . --output-format=grouped
	cd backend && $(MYPY) app --ignore-missing-imports

lint-frontend:
	@echo "$(COLOR_GREEN)Running frontend linters...$(COLOR_RESET)"
	cd frontend && $(NPM) run lint
	cd frontend && $(NPM) run type-check

format: format-backend format-frontend

format-backend:
	@echo "$(COLOR_GREEN)Formatting backend code...$(COLOR_RESET)"
	cd backend && $(BLACK) app/
	cd backend && $(RUFF) check . --fix

format-frontend:
	@echo "$(COLOR_GREEN)Formatting frontend code...$(COLOR_RESET)"
	cd frontend && $(NPM) run format

type-check:
	@echo "$(COLOR_GREEN)Running type checking...$(COLOR_RESET)"
	cd backend && $(MYPY) app --ignore-missing-imports
	cd frontend && $(NPM) run type-check

security:
	@echo "$(COLOR_GREEN)Running security scans...$(COLOR_RESET)"
	cd backend && $(PIP) install bandit safety
	cd backend && bandit -r app/
	cd backend && safety check
	cd frontend && $(NPM) audit --audit-level=high

# ──────────────────────────────────────────────────────────────
# Database
# ──────────────────────────────────────────────────────────────
migrate:
	@echo "$(COLOR_GREEN)Running database migrations...$(COLOR_RESET)"
	cd backend && $(ALEMBIC) upgrade head

migration:
	@echo "$(COLOR_GREEN)Creating new migration...$(COLOR_RESET)"
	cd backend && $(ALEMBIC) revision --autogenerate -m "$(name)"

db-reset:
	@echo "$(COLOR_RED)WARNING: This will delete all data!$(COLOR_RESET)"
	@read -p "Are you sure? (y/N) " confirm; \
	if [ "$$confirm" = "y" ]; then \
		$(DOCKER_COMPOSE) down -v; \
		$(DOCKER_COMPOSE) up -d db; \
		sleep 5; \
		$(DOCKER_COMPOSE) exec backend alembic upgrade head; \
		echo "$(COLOR_GREEN)Database reset complete!$(COLOR_RESET)"; \
	else \
		echo "$(COLOR_YELLOW)Operation cancelled$(COLOR_RESET)"; \
	fi

db-backup:
	@echo "$(COLOR_GREEN)Creating database backup...$(COLOR_RESET)"
	@mkdir -p backups
	$(DOCKER_COMPOSE) exec db pg_dump -U qaforge qaforge > backups/qaforge_$(shell date +%Y%m%d_%H%M%S).sql
	@echo "$(COLOR_GREEN)Backup created in backups/ directory$(COLOR_RESET)"

db-restore:
	@echo "$(COLOR_GREEN)Restoring database from backup...$(COLOR_RESET)"
	cat backups/$(file) | $(DOCKER_COMPOSE) exec -T db psql -U qaforge -d qaforge
	@echo "$(COLOR_GREEN)Database restored!$(COLOR_RESET)"

# ──────────────────────────────────────────────────────────────
# Docker
# ──────────────────────────────────────────────────────────────
build:
	@echo "$(COLOR_GREEN)Building Docker images...$(COLOR_RESET)"
	$(DOCKER_COMPOSE) build --no-cache

build-dev:
	@echo "$(COLOR_GREEN)Building Docker images (dev mode)...$(COLOR_RESET)"
	$(DOCKER_COMPOSE) build

push:
	@echo "$(COLOR_GREEN)Pushing Docker images to registry...$(COLOR_RESET)"
	docker push qaforge-backend:latest
	docker push qaforge-frontend:latest

clean:
	@echo "$(COLOR_YELLOW)Cleaning Docker resources...$(COLOR_RESET)"
	$(DOCKER_COMPOSE) down -v --rmi all
	docker system prune -af
	@echo "$(COLOR_GREEN)Cleanup complete!$(COLOR_RESET)"

# ──────────────────────────────────────────────────────────────
# Deployment
# ──────────────────────────────────────────────────────────────
deploy-staging:
	@echo "$(COLOR_GREEN)Deploying to staging...$(COLOR_RESET)"
	git push origin main
	@echo "$(COLOR_GREEN)Deployment triggered! Check GitHub Actions for status.$(COLOR_RESET)"

deploy-prod:
	@echo "$(COLOR_RED)WARNING: Deploying to production!$(COLOR_RESET)"
	@read -p "Are you sure? (y/N) " confirm; \
	if [ "$$confirm" = "y" ]; then \
		git push origin main; \
		echo "$(COLOR_GREEN)Production deployment triggered!$(COLOR_RESET)"; \
	else \
		echo "$(COLOR_YELLOW)Operation cancelled$(COLOR_RESET)"; \
	fi

# ──────────────────────────────────────────────────────────────
# Utilities
# ──────────────────────────────────────────────────────────────
stats:
	@echo "$(COLOR_GREEN)Project Statistics$(COLOR_RESET)"
	@echo ""
	@echo "$(COLOR_YELLOW)Backend:$(COLOR_RESET)"
	find backend/app -name "*.py" | xargs wc -l | tail -1
	@echo ""
	@echo "$(COLOR_YELLOW)Frontend:$(COLOR_RESET)"
	find frontend/src -name "*.ts" -o -name "*.tsx" | xargs wc -l | tail -1
	@echo ""
	@echo "$(COLOR_YELLOW)Tests:$(COLOR_RESET)"
	find tests -name "*.py" -o -name "*.ts" | xargs wc -l | tail -1

health:
	@echo "$(COLOR_GREEN)Checking service health...$(COLOR_RESET)"
	@echo ""
	@echo "Backend API:"
	curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/api/health || echo "❌ Down"
	@echo ""
	@echo "Frontend:"
	curl -s -o /dev/null -w "%{http_code}" http://localhost:3000 || echo "❌ Down"
	@echo ""
	@echo "Database:"
	$(DOCKER_COMPOSE) exec -T db pg_isready -U qaforge && echo "✅ Healthy" || echo "❌ Down"
	@echo ""
	@echo "Redis:"
	$(DOCKER_COMPOSE) exec -T redis redis-cli ping || echo "❌ Down"
	@echo ""
	@echo "RabbitMQ:"
	curl -s -u guest:guest http://localhost:15672/api/health || echo "❌ Down"

# ──────────────────────────────────────────────────────────────
# CI/CD
# ──────────────────────────────────────────────────────────────
ci: lint test security
	@echo "$(COLOR_GREEN)All CI checks passed!$(COLOR_RESET)"

pre-commit: lint format test-backend-unit
	@echo "$(COLOR_GREEN)Pre-commit checks passed!$(COLOR_RESET)"