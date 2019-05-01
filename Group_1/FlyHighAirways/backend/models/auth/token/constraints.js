module.exports = {
    fk: {
        user_id:`
                  ALTER TABLE outstanding_tokens
                  ADD CONSTRAINT foreign_key_user
                  FOREIGN KEY (user_id) REFERENCES users 
                  ON DELETE CASCADE
                  `
    },

};
