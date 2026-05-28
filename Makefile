.PHONY: help install test test-unit test-integration test-stress benchmark lint format typecheck notebooks clean dashboard

help:
	@echo ""
	@echo "  DSA-Python — Available Commands"
	@echo "  ================================"
	@echo "  make install         Install all dependencies"
	@echo "  make test            Run all tests with coverage"
	@echo "  make test-unit       Run unit tests only"
	@echo "  make test-integration Run integration tests"
	@echo "  make test-stress     Run stress tests"
	@echo "  make benchmark       Run all benchmarks"
	@echo "  make lint            Flake8 lint check"
	@echo "  make format          Format with black + isort"
	@echo "  make typecheck       Run mypy type checker"
	@echo "  make notebooks       Launch Jupyter notebooks"
	@echo "  make clean           Remove build artifacts"
	@echo "  make dashboard       Launch Streamlit dashboard"
	@echo ""

install:
	pip install -r requirements.txt
	pip install -e .
	find src -type d -exec touch {}/__init__.py \;
	find tests -type d -exec touch {}/__init__.py \;

test:
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term-missing

test-unit:
	pytest tests/unit/ -v

test-integration:
	pytest tests/integration/ -v

test-stress:
	pytest tests/stress/ -v --timeout=60

benchmark:
	@echo "Running sorting benchmark..."
	python benchmarks/sorting_benchmark.py
	@echo "Running graph benchmark..."
	python benchmarks/graph_benchmark.py
	@echo "Running DP benchmark..."
	python benchmarks/dp_benchmark.py

benchmark-sort:
	python benchmarks/sorting_benchmark.py

benchmark-graph:
	python benchmarks/graph_benchmark.py

lint:
	flake8 src/ tests/ benchmarks/ --max-line-length=88 --extend-ignore=E203,W503,E501

format:
	black src/ tests/ benchmarks/ problems/ solutions/ --line-length=88
	isort src/ tests/ benchmarks/ problems/ solutions/

typecheck:
	mypy src/ --ignore-missing-imports

notebooks:
	jupyter notebook notebooks/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	find . -name ".coverage" -delete 2>/dev/null || true
	rm -rf htmlcov/ dist/ build/ *.egg-info/ 2>/dev/null || true

dashboard:
	streamlit run src/dashboard/app.py

cli:
	python -m src.cli.main
