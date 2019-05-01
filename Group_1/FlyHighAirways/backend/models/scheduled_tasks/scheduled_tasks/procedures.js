module.exports = {

    cronProcedure: {
        drop: `
                    DROP PROCEDURE IF EXISTS run_all_scheduled_tasks;
                `,

        create: `
                    CREATE PROCEDURE run_all_scheduled_tasks()
                    LANGUAGE plpgsql
                    AS
                    $$
                    DECLARE
                        rec RECORD;
                        res BOOLEAN;
                        stat VARCHAR(100);
                    BEGIN
                        RAISE INFO 'Starting scheduled tasks at %', NOW();
                        INSERT INTO cron_logs (started_on) VALUES (NOW());

                        FOR 
                            rec in SELECT * FROM scheduled_tasks 
                            WHERE active=TRUE AND
                            next_run_on <= NOW()
                        LOOP
                            BEGIN
                                -- compose query in variable stat
                                stat := 'SELECT ' || rec.procedure || '()';
                                RAISE INFO 'Executing: %',stat;
                                
                                EXECUTE stat INTO res;
                                
                                -- update next_run_time in scheduled tasks table
                                UPDATE scheduled_tasks 
                                    SET "next_run_on" = NOW()+repeats_in
                                    WHERE id=rec.id;

                                EXCEPTION
                                    WHEN others THEN
                                        RAISE NOTICE 'Exception Occured: Code: %, Messege: %', sqlstate, sqlerrm;
                                        ROLLBACK;
                                END;
                            COMMIT;
                        END LOOP;
                        
                        RAISE INFO 'Scheduled Tasks Completed at %', NOW();
                    END;
                    $$;    
                `
    }
};