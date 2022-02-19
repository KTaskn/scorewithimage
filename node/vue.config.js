const { defineConfig } = require('@vue/cli-service')
const HtmlInlineScriptPlugin = require('html-inline-script-webpack-plugin');
// const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = defineConfig({
  transpileDependencies: [
    'vuetify'
  ],
  configureWebpack: {
    plugins: [
      // new HtmlWebpackPlugin(),
      new HtmlInlineScriptPlugin(),
    ],
  },
  css: {
    extract: false,
  }
})
