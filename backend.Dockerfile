FROM python:3.12-alpine

LABEL maintainer="contact@tobias-bayer.dev"
LABEL version="1.0"
LABEL description="Character Planer Django Backend"

WORKDIR /app

COPY . .

# RUN apk update && \
#     apk add --no-cache --upgrade bash && \
#     apk add --no-cache postgresql-client ffmpeg && \
#     apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
#     pip install --upgrade pip && \
#     pip install --no-cache-dir -r requirements.txt && \
#     apk del .build-deps && \
#     chmod +x backend.entrypoint.sh

# EXPOSE 8000

RUN apk update && \
    apk add --no-cache bash && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    chmod +x backend.entrypoint.sh

EXPOSE 8000

ENTRYPOINT [ "./backend.entrypoint.sh" ]
