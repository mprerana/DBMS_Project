module.exports = {
    create: `
            CREATE TABLE IF NOT EXISTS scheduled_tasks (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL UNIQUE,
            active BOOLEAN DEFAULT TRUE,
            starts_on TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            repeats_in INTERVAL,
            next_run_on TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            procedure varchar(100)
            );
            `,
    exists: `
            SELECT * FROM information_schema.tables 
            WHERE table_schema='public' 
            AND table_name='scheduled_tasks'
            `,
    drop: `
            DROP TABLE IF EXISTS scheduled_tasks RESTRICT
            `,
    dropCascade: `
            DROP TABLE IF EXISTS scheduled_tasks CASCADE
            `,
    findAll: `
            SELECT * FROM scheduled_tasks
            `
};
