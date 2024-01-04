/** @type {import('next').NextConfig} */
const nextConfig = {
    distDir: 'build',
    serverRuntimeConfig: {
      // Will only be available on the server side
      apiUrl: 'http://localhost:3000'
    },
    publicRuntimeConfig: {
      // Will be available on both server and client
      apiUrl: 'http://localhost:3000'
    }
  }

module.exports = nextConfig
