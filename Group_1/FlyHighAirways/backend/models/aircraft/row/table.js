module.exports = {
    create: `
            CREATE TABLE IF NOT EXISTS rows (
            id SERIAL PRIMARY KEY,
            aircraft_model_id REFERENCES aircraft_models(id),
            row_class REFERENCES seat_class(id),
            no_of_seats INT NOT NULL,
            specials VARCHAR(150) NOT NULL
            )
            `,
    exists: `
            SELECT * FROM information_schema.tables 
            WHERE table_schema='public' 
            AND table_name='rows'
            `,
    drop:`
            DROP TABLE IF EXISTS rows RESTRICT
            `,
    dropCascade:`
            DROP TABLE IF EXISTS rows CASCADE
            `,
    findAll:`
            SELECT * FROM rows
            `
};
