module.exports = {
    updateTimestamp:{
        procedure:`
                  CREATE OR REPLACE FUNCTION update_user_modified_stamp()
                  RETURNS TRIGGER AS
                  $$
                  BEGIN
                    NEW.updated_at = NOW();
                    RETURN NEW;
                  END;
                  $$
                  LANGUAGE PLPGSQL;  
                  `,

        trigger:`
                DROP TRIGGER IF EXISTS update_user_modified_stamp ON users;
                CREATE TRIGGER update_user_modified_stamp
                BEFORE UPDATE
                ON users
                FOR EACH ROW
                EXECUTE PROCEDURE update_user_modified_stamp();
                `
    }
};