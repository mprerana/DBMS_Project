module.exports = {
    create: `
            CREATE TABLE IF NOT EXISTS cron_logs (
                id SERIAL PRIMARY KEY,
                started_on TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                total INTEGER DEFAULT 0,
                errored INTEGER DEFAULT 0
                );
                `,
    exists: `
            SELECT * FROM information_schema.tables 
            WHERE table_schema='public' 
            AND table_name='cron_logs'
            `,
    drop: `
            DROP TABLE IF EXISTS cron_logs RESTRICT
            `,
    dropCascade: `
            DROP TABLE IF EXISTS cron_logs CASCADE
            `,
    findAll: `
            SELECT * FROM cron_logs
            `
};
