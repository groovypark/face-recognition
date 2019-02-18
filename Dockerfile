FROM node:10.15-stretch-slim as spa-build

WORKDIR /spa
COPY ./spa/yarn.lock ./spa/package.json ./
RUN yarn
COPY ./spa/ ./
RUN yarn build

FROM python:3.7.2-slim-stretch
COPY --from=spa-build /spa /spa
COPY ./app/ /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]