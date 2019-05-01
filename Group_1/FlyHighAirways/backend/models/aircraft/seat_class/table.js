module.exports = {
    create: `
            CREATE TABLE IF NOT EXISTS seat_classes (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            )
            `,
    exists: `
            SELECT * FROM information_schema.tables 
            WHERE table_schema='public' 
            AND table_name='seat_classes'
            `,
    drop:`
            DROP TABLE IF EXISTS seat_classes RESTRICT
            `,
    dropCascade:`
            DROP TABLE IF EXISTS seat_classes CASCADE
            `,
    findAll:`
            SELECT * FROM seat_classes
            `
};
