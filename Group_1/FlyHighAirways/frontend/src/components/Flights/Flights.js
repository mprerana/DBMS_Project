import React from 'react';

import Flight from './Flight/Flight';

import classes from './Flights.module.css';

const flights = (props) => {
    return (  
        <div className={classes.FlightList}>
            <Flight {...props}/>
        </div>
    );
}
 
export default flights;