model = require('./model');

const tableName = model.getTableName();


module.exports = {
    check:{
        status:`
                ALTER TABLE ${tableName}
                ADD CONSTRAINT ${tableName}_check_status_choices
                CHECK (status IN ('confirmed','completed','cancelled'))
                `
    },
    fk:{
        booker:`
                    ALTER TABLE ${tableName}
                    ADD CONSTRAINT ${tableName}_fk_booker
                    FOREIGN KEY (booker) REFERENCES users
                    ON DELETE CASCADE
                    `,
    }
};