module.exports = {
    check:{
        no_of_flights: `
                    ALTER TABLE aircrafts
                    ADD CONSTRAINT no_of_aircrafts_gte_0
                    CHECK (no_of_aircrafts > -1)
                `
    },
    // fk:{
    //     model_id:   `
    //                 ALTER TABLE aircrafts
    //                 ADD CONSTRAINT foreign_key_aircraft_model
    //                 FOREIGN KEY (model_id) REFERENCES aircraft_models
    //                 ON DELETE RESTRICT
    //                 `
    // }
};
