FROM node:22 as node

ENV APP /web-app
RUN mkdir $APP
WORKDIR $APP

COPY . .
RUN npm install
RUN npm run ng build -- --output-path=dist


FROM nginx:1.25.5
