import React, { Component } from 'react';


import Paypal from "../../components/Paypal/Paypal";

import { Modal } from 'antd';

import classes from './CheckIn.module.css';


import SeatRow from '../../components/SeatRow/SeatRow';
import Seat from '../../components/SeatRow/Seat/Seat';
import axios from 'axios';

class checkIn extends Component {

    state = {
        priceToPay: 0,
        visible: false,
        seats: []
    }

    componentDidMount() {
        axios.post("http://localhost:5000/flights/get_seats/" , { flightNo: 1}, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(res => {
            res.data.seats[3].is_booked = true; 
            res.data.seats[8].is_booked = true;
            res.data.seats[21].is_booked = true;
            this.setState({ seats: res.data.seats.slice(0, 42) });
        });
    }   

    showModalCustom = (isBooked, isSpecial) => {
        if (isBooked) {
            alert('This place is already booked');
            return;
        }
        if (isSpecial) {
            this.setState({ priceToPay: 300 }, this.showModal);
        }
        else {
            this.setState({ priceToPay: 100 }, this.showModal);
        }
    }

    showModal = () => {
        this.setState({
          visible: true
        });
    };
    
    handleOk = e => {
        console.log(e);
        this.setState({
          visible: false
        });
    };
    
    handleCancel = e => {
        console.log(e);
        this.setState({
          visible: false
        });
    };

    render() {

        

        // * List of List of seats
        let seatList = [];

        // * Inner List (Made 0 after rowLengthCounter)
        let miniList = [];
        let rowLengthCounter = 0;
        const rowLength = 6;

        for (let i = 0; i < this.state.seats.length; i++) {
            if (rowLengthCounter === rowLength) {
                seatList.push(miniList);
                rowLengthCounter = 0;
                miniList = [];
            }
            // Last Iteration
            if (i === this.state.seats.length - 1) {
                seatList.push(miniList);
            }

            rowLengthCounter += 1;
            miniList.push(this.state.seats[i]);
        }

        return (  

            <React.Fragment>

                <div>
                    <Modal
                        title="Basic Modal"
                        visible={this.state.visible}
                        onOk={this.handleOk}
                        onCancel={this.handleCancel}
                    >
                        <h1>Your Total Amount is {this.state.priceToPay}</h1>
                        <Paypal
                            toPay={300}
                            transactionError={err => this.transactionError(err)}
                            transactionCancelled={data => this.transactionCancelled(data)}
                            transactionSuccess={payment => this.transactionSuccess(payment)}
                        />
                    </Modal>
                </div>

                <div className={classes.Page}>
                    <div className={classes.Plane}>
                        <div className={classes.Cockpit}>
                            &nbsp;
                        </div>

                        <div className={classes.Body}>
                            {
                                seatList.map((seat, index) => <SeatRow onClick={this.showModalCustom} key={index} seat={seat}/>)
                            }
                        </div>

                    </div>
                    <div className={classes.Reference}>
                        <div className={classes.BlockInfo}>
                            <Seat isBooked={false} special={false} className={classes.RefBlock}/>
                            <div>AVAILABLE</div>
                        </div>
                        <div className={classes.BlockInfo}>
                            <Seat isBooked={false} special={true} className={classes.RefBlock}/> 
                            <div>AVAILABLE - SPECIAL</div>
                        </div>
                        <div className={classes.BlockInfo}>
                            <Seat isBooked={true} special={false} className={classes.RefBlock}/>
                            <div>FILLED</div>
                        </div>
                    </div>
                </div>

            </React.Fragment>

        );
    }
}

export default checkIn;