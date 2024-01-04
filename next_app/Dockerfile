# syntax=docker/dockerfile:1

ARG NODE_VERSION=20

FROM node:${NODE_VERSION}-alpine as base
WORKDIR /next_app


FROM base as dev
RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
    --mount=type=cache,target=/root/.npm \
    npm ci --include=dev

COPY . .
#RUN addgroup --system --gid 1001 nodejs
#RUN adduser --system --uid 1001 nextjs

#RUN chown nextjs:nodejs .next

RUN npm run build

#USER node
EXPOSE 3000
CMD npm run dev
