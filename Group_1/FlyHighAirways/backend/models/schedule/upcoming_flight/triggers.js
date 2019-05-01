module.exports = {
    check_flight_no_not_in_logs: {
        procedure: `
                    CREATE OR REPLACE FUNCTION check_flight_no_not_in_logs()
                    RETURNS TRIGGER AS
                    $$
                    BEGIN
                        IF EXISTS (
                                    SELECT 1 FROM flight_logs
                                    WHERE flight_logs.flight_no=OLD.flight_no
                                    )
                        THEN         
                            -- This means no already exists. Can't allow to happen!
                            
                            RAISE EXCEPTION '% already exists in past flight logs', OLD.flight_no;
                        END IF;
                        
                        RETURN NEW;
                    END;
                    $$
                    LANGUAGE PLPGSQL;        
                  `,
        trigger: `
                    DROP TRIGGER IF EXISTS check_flight_no_not_in_logs ON upcoming_flights;
                    CREATE TRIGGER check_flight_no_not_in_logs
                    BEFORE INSERT
                    ON upcoming_flights
                    FOR EACH ROW
                    EXECUTE PROCEDURE check_flight_no_not_in_logs();
                `
    }
};