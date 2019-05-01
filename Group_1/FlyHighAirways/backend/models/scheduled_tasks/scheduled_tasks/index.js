const ScheduledTask = require('./model');

const sequelize = require('../../../utils/database/connect');

const tasks = require('../../../utils/database/scheduled_tasks/tasks');

const procedures = require('./procedures');

const seed = require('./seed');
const table = require('./table');

ScheduledTask.sqlCommands = {
    table: table,
    // constraints: constraints,
    // triggers: triggers,
    procedures: procedures,
};

const seeds = require('./seeds');
ScheduledTask.seeds = seeds;


ScheduledTask.createTable = async function (options) {
    const { table } = this.sqlCommands;
    const force = (options && options.force) || false;
    let queryResult;
    try {
        if (force) {
            console.log(table.dropCascade);
            queryResult = await sequelize.query(table.dropCascade);
        } else {
            console.log(table.drop);
            queryResult = await sequelize.query(table.drop);
        }

        queryResult = await sequelize.query(table.exists);

        if (queryResult[0].length > 0) {
            throw new Error("Drop Failed!. force was set to " + force);
        }

        console.log(table.create);
        queryResult = await sequelize.query(table.create);
        // console.log(queryResult);
    } catch (error) {
        console.log(error);
    }
};

/*
ScheduledTask.createConstraints = async function (options) {
    const {constraints} = this.sqlCommands;
    const all_queries = [];
    for (type in constraints){
        all_queries.push(...Object.values(constraints[type]))
    }

    let queryResult;
    try {
        for (q of all_queries) {
            queryResult = await sequelize.query(q);
            console.log(q);
        }
    } catch (error){
        console.log(error);

    }
};



ScheduledTask.createTriggers = async function(options){
    const {triggers} = this.sqlCommands;
    Object.keys(triggers).map(async key=>{

        console.log(triggers[key].procedure);
        let result = await sequelize.query(triggers[key].procedure);

        console.log(triggers[key].trigger);
        result = await sequelize.query(triggers[key].trigger);
    });
};
*/

ScheduledTask.seed = async function (options) {
    await seed.createFunctions();
    await seed.createScheduleEntries();
};

ScheduledTask.createProcedures = async function (options) {
    console.log(this.sqlCommands.procedures.cronProcedure.drop);
    let result = await sequelize.query(this.sqlCommands.procedures.cronProcedure.drop);

    console.log(this.sqlCommands.procedures.cronProcedure.create);
    result = await sequelize.query(this.sqlCommands.procedures.cronProcedure.create);
};

ScheduledTask.createAll = async function (options) {
    await this.createTable(options);
    await this.seed(options);
    await this.createProcedures(options);
    // await this.createConstraints(options);
    // await this.createTriggers(options);
};

ScheduledTask.seedTable = async function (options) {
    for (record of this.seeds) {
        let keys = Object.keys(record);
        let fields = keys.map(key => queryWrappers.wrapField(key));
        fieldsString = fields.join(',');

        let values = keys.map(key => {
            let val = record[key];
            if (typeof (val) === "string") return queryWrappers.wrapValue(val);
            else return val;
        });

        valuesString = values.join(',');

        insertQuery = `INSERT INTO ${this.getTableName()} (${fieldsString}) VALUES (${valuesString})`;
        console.log(insertQuery);
        await sequelize.query(insertQuery).then(result=>{

        }).catch(err=>{
            console.log(err);
            console.log(`Insert Failed for fields: ${fieldsString} values: ${valuesString}`);
        })
    }
};
/* Set all method prototypes */
// User.prototype.x = methods.x;


module.exports = ScheduledTask;