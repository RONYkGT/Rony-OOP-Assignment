# Using alpine for smaller size python base
FROM python:3.8-alpine

WORKDIR /app
# Copy two directories at once to minimize layers
COPY src ./src
COPY tests ./tests
