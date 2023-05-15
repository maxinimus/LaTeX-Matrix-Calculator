const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/matrix',
    createProxyMiddleware({
      target: 'https://latex-matrix-calculator.herokuapp.com/',
      changeOrigin: true,
    })
  );
};