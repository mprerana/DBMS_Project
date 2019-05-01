module.exports = {
    revokeRefreshTokens:{
        procedure:`
                    CREATE OR REPLACE FUNCTION invalidate_outstanding_tokens_on_password_change()
                    RETURNS TRIGGER AS
                    $$
                    BEGIN
                        IF NEW.password != OLD.password THEN
                            UPDATE outstanding_tokens
                            SET is_valid = FALSE
                            WHERE user_id = OLD.id;
                        END IF;
                        
                        RETURN NEW;
                    END;
                    $$
                    LANGUAGE PLPGSQL;        
                  `,
        trigger:`
                    DROP TRIGGER IF EXISTS invalidate_outstanding_tokens_on_password_change ON users;
                    CREATE TRIGGER invalidate_outstanding_tokens_on_password_change
                    AFTER UPDATE
                    ON users
                    FOR EACH ROW
                    EXECUTE PROCEDURE invalidate_outstanding_tokens_on_password_change();
                `
    }
};