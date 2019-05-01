module.exports = {
    unique: {
        email:`
                  ALTER TABLE users
                  ADD CONSTRAINT unique_email
                  UNIQUE(email)
                  `
    },
    check:{
        password: `
                    ALTER TABLE users
                    ADD CONSTRAINT check_password_length_gte_8
                    CHECK ( LENGTH(password) >=8 )
                    `,
        email: `
                    ALTER TABLE users
                    ADD CONSTRAINT check_email_format
                    CHECK (
                        email = lower(email) AND
                        email LIKE '%@%.%'
                        )
                    `
    },
    index:{
        email:`
                    CREATE UNIQUE INDEX email_btree ON users 
                    USING btree
                    ( email ASC NULLS FIRST)
                    WITH (FILLFACTOR = 80)
                `
        /* NULLS FIRST puts all nulls at the start of the tree. (doesnt matter here as email is NOT NULL)
        FILLFACTOR determines till what percentage each leaf
         of btree is filled before split operation is performed (
         */
    }
};
