import React from 'react';

import Seat from './Seat/Seat';
import classes from './SeatRow.module.css';

const seatRow = (props) => {


    return (
        <div className={classes.SeatRow}>  
            <div className={classes.SeatSide}>
                <Seat
                    onClick={props.onClick} 
                    name={props.seat[0].seat_number} 
                    special={props.seat[0].special}
                    isBooked={props.seat[0].is_booked}    
                />
                <Seat
                    onClick={props.onClick} 
                    name={props.seat[1].seat_number} 
                    special={props.seat[1].special}
                    isBooked={props.seat[1].is_booked}    
                />
                <Seat
                    onClick={props.onClick} 
                    name={props.seat[2].seat_number} 
                    special={props.seat[2].special}
                    isBooked={props.seat[2].is_booked}                    
                />
            </div>
            <div className={classes.SeatSide}>
                <Seat
                    onClick={props.onClick} 
                    name={props.seat[3].seat_number} 
                    special={props.seat[3].special}
                    isBooked={props.seat[3].is_booked}    
                />
                <Seat
                    onClick={props.onClick} 
                    name={props.seat[4].seat_number} 
                    special={props.seat[4].special}
                    isBooked={props.seat[4].is_booked}    
                />
                <Seat
                    onClick={props.onClick} 
                    name={props.seat[5].seat_number} 
                    special={props.seat[5].special}
                    isBooked={props.seat[5].is_booked}    
                />
            </div>
        </div>
    );
}
 
export default seatRow;