export const inProduction = process.env.NODE_ENV === 'production'
export const isDevelopment = process.env.NODE_ENV === 'development'
export const isStaging = process.env.NODE_ENV === 'staging'
export const inDocker = process.env.DOCKER_STATUS_ENV === 'docker'

export const backendURL = inDocker ? 'http://back:8000' :'http://localhost:8000'