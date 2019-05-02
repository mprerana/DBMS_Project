function hbsHelpers(hbs) {
  return hbs.create({
    helpers: { // This was missing
      inc: function(value, options) {
        console.log('reading it');
        return parseInt(value) + 1;
      }

      // More helpers...
    }

  });
}

module.exports = hbsHelpers;
