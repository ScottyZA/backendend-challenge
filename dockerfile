FROM python:3.10 as base

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1


FROM base AS runtime

WORKDIR /usr/app/

RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY . .
RUN pipenv install --system --deploy

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]