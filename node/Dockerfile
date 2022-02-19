FROM node:latest

ENV WORKDIR /workspace
RUN mkdir $WORKDIR
COPY ./package.json $WORKDIR

WORKDIR $WORKDIR
RUN npm install

CMD npm run serve