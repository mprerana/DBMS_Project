module.exports = {
    create: `
            CREATE TABLE IF NOT EXISTS schedules (
            id SERIAL PRIMARY KEY,
            departure TIME WITH TIME ZONE,
            arrival TIME WITH TIME ZONE,
            aircraft_id INT NOT NULL,
            source VARCHAR(100) NOT NULL,
            price BIGINT,
            destination VARCHAR(100) NOT NULL
            )
            `,
    exists: `
            SELECT * FROM information_schema.tables 
            WHERE table_schema='public' 
            AND table_name='schedules'
            `,
    drop:`
            DROP TABLE IF EXISTS schedules RESTRICT
            `,
    dropCascade:`
            DROP TABLE IF EXISTS schedules CASCADE
            `,
    findAll:`
            SELECT * FROM schedules
            `
};
