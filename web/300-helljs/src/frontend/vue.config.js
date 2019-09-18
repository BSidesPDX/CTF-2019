const webpack = require('webpack');

module.exports = {
  configureWebpack: {
    plugins: [
      new webpack.DefinePlugin({
        'process.env': {
          SECURE_API_URL: JSON.stringify(process.env.SECURE_API_URL),
          VULNERABLE_API_URL: JSON.stringify(process.env.VULNERABLE_API_URL),
        },
      }),
    ],
  },
};
