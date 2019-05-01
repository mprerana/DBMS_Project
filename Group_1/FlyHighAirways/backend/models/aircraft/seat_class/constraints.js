module.exports = {
    unique: {
        seat_class_name:`
                  ALTER TABLE seat_classes
                  ADD CONSTRAINT unique_name
                  UNIQUE(name)
                  `
    },
};
