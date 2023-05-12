const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/matrix',
    createProxyMiddleware({
      target: 'https://desolate-coast-38022.herokuapp.com/',
      changeOrigin: true,
    })
  );
};