module.exports = {
    unique: {
        name:`
                  ALTER TABLE payments
                  ADD CONSTRAINT payments_unique_reference_string
                  UNIQUE(reference_string)
                  `,
    },
    fk:{
        user_id:`
                    ALTER TABLE payments
                    ADD CONSTRAINT payments_fk_user
                    FOREIGN KEY (user_id) REFERENCES users
                    ON DELETE CASCADE
                `
    }
    
};