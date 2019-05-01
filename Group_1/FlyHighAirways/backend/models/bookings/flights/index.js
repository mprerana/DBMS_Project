const sequelize = require('../../../utils/database/connect');

const FlightBooking = require('./model');
const table = require('./table');
const constraints = require('./constraints');
// const triggers = require('./triggers');
// const procedures = require('./procedures');
const methods = require('./methods');
const queryWrappers = require('../../../utils/query-wrappers');


FlightBooking.sqlCommands = {
    table: table,
    constraints: constraints,
    // triggers: triggers,
    // procedures: procedures,
};

const seeds = require('./seeds');
FlightBooking.seeds = seeds;

FlightBooking.createTable = async function (options) {
    const {table} = this.sqlCommands;
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

FlightBooking.createConstraints = async function (options) {
    const {constraints} = this.sqlCommands;
    const all_queries = [];
    for (type in constraints){
        all_queries.push(...Object.values(constraints[type]))
    }

    let queryResult;
    try {
        for (q of all_queries) {
            console.log(q);
            queryResult = await sequelize.query(q);
        }
    } catch (error){
        console.log(error);

    }
};


/*

FlightBooking.createTriggers = async function(options){
    const {triggers} = this.sqlCommands;
    Object.keys(triggers).map(async key=>{

        console.log(triggers[key].procedure);
        let result = await sequelize.query(triggers[key].procedure);

        console.log(triggers[key].trigger);
        result = await sequelize.query(triggers[key].trigger);
    });
};
*/

FlightBooking.createBookedSeatsTable = async function (options){
    const Query =   `
                            DROP TABLE IF EXISTS booked_seats;
                            CREATE TABLE IF NOT EXISTS booked_seats (
                            id SERIAL PRIMARY KEY,
                            booking_id INT,
                            flight_no INT,
                            seat_no VARCHAR(10)
                            )
                            
                        `;
    console.log(Query);

    await sequelize.query(Query);
};

FlightBooking.createPassengerView = async function (options){
    query = `
            CREATE MATERIALIZED VIEW passengers
            AS
            SELECT email AS booker_email, F.flight_no, F.id AS booking_id,
            passengers->0->>'fullName' AS passenger_name,
            passengers->0->>'age' AS passenger_age,
            passengers->0->>'gender' AS passenger_gender,
            passengers->0->>'seat' AS passenger_seat
            from flight_bookings AS F INNER JOIN upcoming_flights AS U ON F.flight_no=U.flight_no INNER JOIN users ON F.booker=users.id
            WITH DATA;
            CREATE UNIQUE INDEX booking_id ON passengers (booking_id);

            `;
    console.log(query);
    await sequelize.query(query);
}
FlightBooking.createAll = async function (options){
    await this.createTable(options);
    await this.createConstraints(options);
    await this.createBookedSeatsTable(options);
    await this.createPassengerView(options)
    // await this.createTriggers(options);
};
/* Set all method prototypes */
// FlightBooking.prototype.x = methods.x;

FlightBooking.seedTable = async function (options) {
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
module.exports = FlightBooking;