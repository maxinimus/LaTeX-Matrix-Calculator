const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/matrix',
    createProxyMiddleware({
      target: 'localhost:5000/',
      changeOrigin: true,
    })
  );
};