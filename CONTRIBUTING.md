# Contributing to graph-atlas

Thanks for your interest in contributing.

## Development Setup

1. Create a virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate

2. Install in editable mode:

    pip install -e .
    pip install pytest

3. Run tests:

    pytest -q

## Guidelines

- Keep functions small and readable.
- Prefer clarity over micro-optimizations.
- Add tests for new behavior.
- Maintain type hints where possible.
- Keep public API stable.

## Code Style

- Follow PEP8.
- Use descriptive variable names.
- Keep algorithm implementations easy to reason about.

## Pull Requests

- Describe the change clearly.
- Include tests if applicable.
- Avoid breaking public APIs unless discussed.