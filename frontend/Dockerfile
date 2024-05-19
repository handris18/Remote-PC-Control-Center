# Stage 1: Install dependencies and build TypeScript code
FROM node:22 as node

ENV APP /web-app
RUN mkdir $APP
WORKDIR $APP

COPY . .
RUN npm install

# Install tslib
RUN npm install tslib

RUN npm run ng build -- --output-path=dist

# Stage 2: Create the production image
FROM nginx:1.25.5

ENV APP /web-app

RUN apt-get install bash

COPY ./nginx.conf /etc/nginx/conf.d/
RUN rm -rf /usr/share/nginx/html/*

# Copy built files from the previous stage
COPY --from=node $APP/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
