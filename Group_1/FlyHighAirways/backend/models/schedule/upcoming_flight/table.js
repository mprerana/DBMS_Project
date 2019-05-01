module.exports = {
    create: `
            CREATE TABLE IF NOT EXISTS upcoming_flights (
            id SERIAL PRIMARY KEY,
            schedule_id INT,
            flight_no SERIAL,
            aircraft_id INT NOT NULL,
            source VARCHAR(100) NOT NULL,
            destination VARCHAR(100) NOT NULL,
            start_date DATE NOT NULL,
            end_date DATE NOT NULL,
            price BIGINT,
            start_time TIME WITH TIME ZONE DEFAULT NOW(),
            end_time TIME WITH TIME ZONE DEFAULT NOW(),
            pilot INT ARRAY,
            crew INT ARRAY            
            )
            `,
    exists: `
            SELECT * FROM information_schema.tables 
            WHERE table_schema='public' 
            AND table_name='upcoming_flights'
            `,
    drop:`
            DROP TABLE IF EXISTS upcoming_flights RESTRICT
            `,
    dropCascade:`
            DROP TABLE IF EXISTS upcoming_flights CASCADE
            `,
    findAll:`
            SELECT * FROM upcoming_flights
            `
};
