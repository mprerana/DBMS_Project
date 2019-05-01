module.exports = {
    create: `
            CREATE TABLE IF NOT EXISTS outstanding_tokens (
            "token" BIGINT PRIMARY KEY,
            user_id INT,
            is_valid BOOLEAN DEFAULT TRUE,
            expires_on TIMESTAMP WITH TIME ZONE
            )
            `,
    exists: `
            SELECT * FROM information_schema.tables 
            WHERE table_schema='public' 
            AND table_name='outstanding_tokens'
            `,
    drop:`
            DROP TABLE IF EXISTS outstanding_tokens RESTRICT
            `,
    dropCascade:`
            DROP TABLE IF EXISTS outstanding_tokens CASCADE
            `,
    findAll:`
            SELECT * FROM outstanding_tokens
            `
};
