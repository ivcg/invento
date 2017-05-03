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
        loader: "sass-loader",
        options: {}
      }]
    }, {
      test: /\.jsx$/,
      use: [{
        loader: "babel-loader",
        options: {}
      }]
    }]
  },
  output: {
    filename: '[name].bundle.js',
    path: __dirname + '/build'
  }
}

module.exports = config;
