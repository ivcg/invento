var path = require('path'),
  fs = require('fs'),
  webpack = require('webpack');

var entry = {
  'app': './app/index.jsx',
  'invento': './sass/invento.sass'
}

var config = {
  entry: entry,
  context: path.join(__dirname, 'static/'),
  module: {
    rules: [{
      test: /\.sass$/,
      use: [{
        loader: "style-loader",
        loader: "css-loader",
        loader: "sass-loader",
        options: {
          includePaths: [
            path.join(__dirname, 'node_modules/bootstrap/scss/'),
          ]
        }
      }]
    }, {
      test: /\.jsx$/,
      use: [{
        loader: "babel-loader",
        query: {
          presets: ['es2015', 'react']
        }
      }]
    }]
  },
  output: {
    filename: '[name].bundle.js',
    path: __dirname + '/build'
  }
}

module.exports = config;
