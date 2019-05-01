import React from 'react';
import classes from './Seat.module.css';

const seat = (props) => {

    let backgroundColor = null;
    if (props.isBooked) {
        backgroundColor = "#4169E1"
    }
    else if (props.special) {
        backgroundColor = "#00BFFF"
    }
    else {
        backgroundColor = "#FF8C00"
    }



    return (  
        <span 
            className={classes.Seat} 
            style={{backgroundColor}}
            onClick={() => props.onClick(props.isBooked, props.special)}    
        >
            {props.name}
        </span>
    );
}
 
export default seat;