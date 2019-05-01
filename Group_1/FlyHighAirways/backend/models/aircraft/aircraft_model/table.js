module.exports = {
    create: `
            CREATE TABLE IF NOT EXISTS aircraft_models (
            id SERIAL PRIMARY KEY,
            manufacturer_name VARCHAR(50),
            model_name VARCHAR(50) NOT NULL,
            no_of_seats INT NOT NULL,
            name VARCHAR(50),
            max_weight FLOAT,
            manufactured_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            maintenance_date TIMESTAMP WITH TIME ZONE DEFAULT NOW()
            )
            `,
    exists: `
            SELECT * FROM information_schema.tables 
            WHERE table_schema='public' 
            AND table_name='aircraft_models'
            `,
    drop:`
            DROP TABLE IF EXISTS aircraft_models RESTRICT
            `,
    dropCascade:`
            DROP TABLE IF EXISTS aircraft_models CASCADE
            `,
    findAll:`
            SELECT * FROM aircraft_models
            `
};
