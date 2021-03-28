FROM node:12.20.1-alpine as builder

RUN mkdir /app
WORKDIR /app

COPY code/package.json code/package-lock.json /app/code/
RUN npm install --prefix code

COPY . /app
RUN npm run build --prefix code -- --output-path=./dist/out


FROM nginx:1.15.7-alpine

RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app/code/dist/out /usr/share/nginx/html
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
