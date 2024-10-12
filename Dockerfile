ARG PYTHON_VERSION=3.13.0-slim-bookworm
ARG POETRY_VERSION=1.8.3

FROM python:${PYTHON_VERSION} AS builder

RUN pip install --upgrade pip wheel

# The ARG command must be repeated in the new stage: https://docs.docker.com/reference/dockerfile/#understand-how-arg-and-from-interact
ARG POETRY_VERSION
RUN pip install poetry==${POETRY_VERSION}

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-cache

########

ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}

WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

ARG ASSETS_DIR

COPY wiigames_categorizer ./wiigames_categorizer/
COPY ./.env ./

ENTRYPOINT ["python", "-m", "wiigames_categorizer"]