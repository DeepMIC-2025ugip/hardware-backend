_isort_check:
	PYTHONPATH=src uv run isort --check ./

_black_check:
	PYTHONPATH=src uv run black --check ./

_mypy:
	PYTHONPATH=src uv run mypy ./

lint:
	PYTHONPATH=src make -j _isort_check _black_check _mypy

_isort_apply:
	PYTHONPATH=src uv run isort ./

_black_apply:
	PYTHONPATH=src uv run black ./

fmt:
	PYTHONPATH=src make _isort_apply _black_apply

test:
	PYTHONPATH=src uv run pytest

run:
	./python
