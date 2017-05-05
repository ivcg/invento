const path = require('path');
const webpack = require('webpack');
const fs = require('fs');

module.exports = {
  entry: './static/app/index.jsx',
  output: {
    filename: 'build/bundle.js'
  },
  // To have a fallback mechanism for ``React Routes`` so that if it hits a
  // 404 webpack-dev-server knows which file to serve
  devServer: {
    historyApiFallback: {
      index: 'html/index.html'
    }
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        query: {
          presets: ['es2015', 'react']
        }
      }, {
        test: /\.css$/,
        use: [
          {
            loader: "style-loader"
          }, {
            loader: "css-loader"
          }
        ]
      }, {
        test: /\.sass$/,
        use: [
          {
            loader: "style-loader"
          }, {
            loader: "css-loader"
          }, {
            loader: "sass-loader",
            options: {
              strictMath: true,
              noIeCompat: true
            }
          }
        ]
      }, {
        test: /\.(eot|svg|ttf|woff|woff2)$/,
        use: {
          loader: 'file-loader?name=../fonts/[name].[ext]'
        }
      }
    ]
  },
  resolve: {
    extensions: [
      '.js', '.jsx'
    ],
    modules: [
      path.resolve(__dirname, './static/app'),
      'node_modules'
    ]
  }
};

