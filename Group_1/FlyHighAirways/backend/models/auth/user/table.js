module.exports = {
    create: `
            CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(50) NOT NULL,
            password VARCHAR(500) NOT NULL,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            last_login TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            has_password BOOLEAN NOT NULL DEFAULT TRUE,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
            )
            `,
    exists: `
            SELECT * FROM information_schema.tables 
            WHERE table_schema='public' 
            AND table_name='users'
            `,
    drop:`
            DROP TABLE IF EXISTS users RESTRICT
            `,
    dropCascade:`
            DROP TABLE IF EXISTS users CASCADE
            `,
    findAll:`
            SELECT * FROM users
            `
};
