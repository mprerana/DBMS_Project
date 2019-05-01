const tasks = require('../../../utils/database/scheduled_tasks/tasks');
const sequelize = require('../../../utils/database/connect');
const queryWrappers = require('../../../utils/query-wrappers');

// Create Procedures
exports.createFunctions = async function () {
    for (task of tasks) {
        createFunctionQuery = `
                                CREATE OR REPLACE FUNCTION ${task.procedureName}()
                                RETURNS BOOLEAN AS
                                $$
                                    DECLARE
                                        ${task.procedure.declarations}
                                    BEGIN
                                        ${task.procedure.statements}
                                        RETURN TRUE;
                                    END;
                                $$
                                LANGUAGE PLPGSQL;
                                `;

        let result = await sequelize.query(createFunctionQuery);
        console.log(createFunctionQuery);
    }
};


exports.createScheduleEntries = async function () {
    for (task of tasks) {
        insertQuery = `
                        INSERT INTO scheduled_tasks 
                        ("name","repeats_in","procedure")
                        VALUES
                        (
                            ${queryWrappers.wrapValue(task.name)},
                            ${queryWrappers.wrapValue(task.timeDelta)},
                            ${queryWrappers.wrapValue(task.procedureName)}
                        )    
                      `;

        let result = await sequelize.query(insertQuery);
        console.log(insertQuery);
    }
};

