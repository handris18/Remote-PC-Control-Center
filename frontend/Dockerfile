FROM node:22 as node

ENV APP /web-app
RUN mkdir $APP
WORKDIR $APP

COPY . .
RUN npm install
RUN npm run ng build -- --output-path=dist


FROM nginx:1.25.5

ENV APP /web-app

RUN apt-get install bash

COPY ./nginx.conf /etc/nginx/conf.d/
RUN rm -rf /usr/share/nginx/html/*

COPY --from=node $APP/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
