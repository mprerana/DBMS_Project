const models = require('../models');
// const sequelize = require('./database/connect');

/*
sequelize.sync({ "force": true }).then(result => {
    console.log(result);
    console.log("Models synced!", result.models);
    console.log("db synced!");
}).catch(err => {
    console.log(err);
    console.log("Sync Failed!");
});
*/

const orderedModels = [
    models.auth.User,
    models.auth.OutstandingToken,

    models.scheduledTask.ScheduledTask,
    models.scheduledTask.CronLog,

    models.aircraft.AircraftModel,
    models.aircraft.Aircraft,

    models.others.City,
    models.others.Payment,

    models.schedule.Schedule,
    models.schedule.FlightLog,
    models.schedule.UpcomingFlight,

    models.bookings.FlightBooking

];

async function createAndSeedAllTables(options) {
    try {
        let result;

        for (let model of orderedModels) {
            console.log("\n\n\n\n Creating ", model.getTableName(), "\n\n\n");
            result = await model.createAll(options);
        }

        for (let model of orderedModels) {
            console.log("\n\n\n\n Seeding", model.getTableName(), "\n\n\n");
            result = await model.seedTable(options);
        }

        // await models.aircraft.AircraftModel.seedTable({});
        // await models.aircraft.Aircraft.seedTable({});

    } catch (err) {
        console.log(err);
        console.log("Errored!");
    }
}

createAndSeedAllTables({"force": true});
