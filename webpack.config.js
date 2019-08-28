const path = require('path');
const webpack = require('webpack');
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
  entry: ['babel-polyfill', path.resolve(__dirname, './src/js/index.js')],
  output: {
    path: path.resolve(__dirname, './eastecho/site/static/'),
    filename: 'site.js',
  },
  performance: {hints: false},
  resolve: {
    extensions: ['.js', '.jsx']
  },
  module: {
    noParse: (content) => /jquery|lodash/.test(content),
    rules: [
      {
        test: /\.jsx?/,
        exclude: /node_modules/,
        use: 'babel-loader'
      }
    ]
  },
  // mode: 'production',
  plugins: [
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      'window.jQuery': 'jquery',
      Tether: 'tether',
      "window.Tether": "tether",
      Popper: ['popper.js', 'default'],
    }),
    new CopyWebpackPlugin([
      {
        from: 'node_modules/@fortawesome/fontawesome-free/webfonts/*',
        to: path.resolve(__dirname, './eastecho/site/static/fonts/'),
        flatten: true
      }/*,
      {
        from: 'node_modules/redoc/bundles/redoc.standalone.js',
        to: path.resolve(__dirname, './eastecho/api/static/'),
        flatten: true
      }*/
    ], {})
  ],
  externals: {
    config: JSON.stringify({
      apiUrl: 'http://localhost:8000'
    })
  }
};
