module.exports = {
    check:{
        no_of_seats: `
                    ALTER TABLE rows
                    ADD CONSTRAINT no_of_seats_not_0
                    CHECK (no_of_seats > 0)
                    `
    },
};
