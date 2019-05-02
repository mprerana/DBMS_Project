module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },

      {
        test: /.jsx?$/,
        loader: "babel-loader",
        exclude: /node_modules/
      },

      {
        test: /\.css$/,
        loader: "style-loader!css-loader"
      },

      {
        test: /\.(jpe?g|png|gif|woff|woff2|eot|ttf|svg)(\?[a-z0-9=.]+)?$/,
        loader: "url-loader?limit=100000"
      }
    ]
  },
  resolve: {
    alias: {
      jquery: "jquery/src/jquery"
    }
  }
};
