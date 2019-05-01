module.exports = {
    create: `
            CREATE TABLE IF NOT EXISTS flight_bookings (
            id SERIAL PRIMARY KEY,
            booker INT NOT NULL,
            pnr_no VARCHAR(300),
            flight_no INT NOT NULL,
            amount DOUBLE PRECISION NOT NULL,
            status VARCHAR(20) NOT NULL,
            booked_on TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            passengers JSON NOT NULL
            )
            `,
    exists: `
            SELECT * FROM information_schema.tables 
            WHERE table_schema='public' 
            AND table_name='flight_bookings'
            `,
    drop:`
            DROP TABLE IF EXISTS flight_bookings RESTRICT
            `,
    dropCascade:`
            DROP TABLE IF EXISTS flight_bookings CASCADE
            `,
    findAll:`
            SELECT * FROM flight_bookings
            `
};
