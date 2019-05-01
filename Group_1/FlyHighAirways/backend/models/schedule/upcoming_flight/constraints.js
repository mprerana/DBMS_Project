model = require('./model');

const tableName = model.getTableName();


module.exports = {
    fk: {
        schedule_id: `
                    ALTER TABLE ${tableName}
                    ADD CONSTRAINT ${tableName}foreign_key_schedule
                    FOREIGN KEY (schedule_id) REFERENCES schedules
                    ON DELETE RESTRICT
                    `,
        aircraft_id: `
                    ALTER TABLE ${tableName}
                    ADD CONSTRAINT ${tableName}foreign_key_aircraft
                    FOREIGN KEY (aircraft_id) REFERENCES aircrafts
                    ON DELETE RESTRICT
                    `,

        source: `
                    ALTER TABLE ${tableName}
                    ADD CONSTRAINT ${tableName}foreign_key_source_city
                    FOREIGN KEY (source) REFERENCES cities
                    ON DELETE RESTRICT
                `,

        destination: `
                    ALTER TABLE ${tableName}
                    ADD CONSTRAINT ${tableName}foreign_key_dest_city
                    FOREIGN KEY (destination) REFERENCES cities
                    ON DELETE RESTRICT
                    `
    },
    check:{
        source_destination: `
                    ALTER TABLE ${tableName}
                    ADD CONSTRAINT ${tableName}check_different_source_destination
                    CHECK ( source <> destination )
                    `
        // start_end_time: `
        //             ALTER TABLE ${tableName}
        //             ADD CONSTRAINT ${tableName}check_different_start_end_time
        //             CHECK (start_time != end_time)
        //             `
        // start_time != end_time because flights can start at night and reach next day.
/*        flight_no_not_in_logs:  `
                                ALTER TABLE ${tableName}
                                ADD CONSTRAINT flight_no_not_in_logs
                                CHECK( EXISTS (
                                    SELECT 1 FROM flight_logs
                                    WHERE flight_logs.flight_no=${tableName}.flight_no
                                    ) = FALSE
                                )
                                `*/
    },
    unique: {
        flight_no:`
                  ALTER TABLE ${tableName}
                  ADD CONSTRAINT ${tableName}unique_flight_no
                  UNIQUE(flight_no)
                  `
    }
};