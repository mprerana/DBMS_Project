module.exports = {
    unique: {
        name:`
                  ALTER TABLE cities
                  ADD CONSTRAINT unique_name
                  UNIQUE(name)
                  `,
        short_form:`
                  ALTER TABLE cities
                  ADD CONSTRAINT unique_short_form
                  UNIQUE(short_form)
                  `
    },
    
}