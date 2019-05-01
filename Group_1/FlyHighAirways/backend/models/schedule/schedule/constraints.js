model = require('./model');

const tableName = model.getTableName();


module.exports = {
    check:{
        source_destination: `
                    ALTER TABLE ${tableName}
                    ADD CONSTRAINT ${tableName}check_different_source_destination
                    CHECK ( source <> destination )
                    `
    },
    fk:{
        aircraft_id:`
                    ALTER TABLE ${tableName}
                    ADD CONSTRAINT ${tableName}foreign_key_aircraft
                    FOREIGN KEY (aircraft_id) REFERENCES aircrafts
                    ON DELETE RESTRICT
                    `,

        source:`
                    ALTER TABLE ${tableName}
                    ADD CONSTRAINT ${tableName}foreign_key_dest_city
                    FOREIGN KEY (source) REFERENCES cities
                    ON DELETE RESTRICT
                `,

        destination:`
                    ALTER TABLE ${tableName}
                    ADD CONSTRAINT ${tableName}foreign_key_source_city
                    FOREIGN KEY (destination) REFERENCES cities
                    ON DELETE RESTRICT
                    `
    }
};