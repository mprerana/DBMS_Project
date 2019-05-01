module.exports = {
    create: `
            CREATE TABLE IF NOT EXISTS aircrafts (
            model_id INT PRIMARY KEY,
            no_of_aircrafts INT NOT NULL,
            date_of_purchase TIMESTAMP WITH TIME ZONE DEFAULT NOW()
            )
            `,
    exists: `
            SELECT * FROM information_schema.tables 
            WHERE table_schema='public' 
            AND table_name='aircrafts'
            `,
    drop:`
            DROP TABLE IF EXISTS aircrafts RESTRICT
            `,
    dropCascade:`
            DROP TABLE IF EXISTS aircrafts CASCADE
            `,
    findAll:`
            SELECT * FROM aircrafts
            `
};
