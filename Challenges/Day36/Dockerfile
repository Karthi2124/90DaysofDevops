FROM node:20-alpine

WORKDIR /app

COPY app/package*.json ./

RUN npm install --omit=dev

COPY app .

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

USER appuser

EXPOSE 5000

CMD ["npm", "start"]