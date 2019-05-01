import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { Col, Row, Button } from 'antd';
import classes from './Flight.module.css';

class Flight extends  Component {

    onFlightSelectHandler = () => {
        this.props.history.push('/book-flight');
        this.props.onFlightSelect(this.props);
    }

    render() {

        return (
            <Row type="flex" className={classes.Flight}>
                <Col lg={12}>
                    <div className={classes.TimingBoxHeader}>
                        <div className={classes.ToCenter}>
                            <h2>{this.props.startTime}</h2>
                            <h4>{this.props.source.toUpperCase()}</h4>
                        </div>
                        <div className={classes.ToCenter}>
                            <h3>{this.props.nonStop ? 'NON STOP' : '1 STOP'}</h3>
                            <h5>1h 55m</h5>
                        </div>
                        <div className={classes.ToCenter}>
                            <h2>{this.props.endTime}</h2>
                            <h4>{this.props.destination.toUpperCase()}</h4>
                        </div>
                    </div>
                </Col>
                <Col lg={8}>
                    <div className={classes.Class}>
                        <h4>INR <span className={classes.ClassPrice}>{this.props.economy.fare}</span></h4>
                    </div>
                </Col>
                <Col lg={4}>
                    <div className={classes.BookNow}>
                        <Button 
                            type="primary"
                            onClick={() => this.onFlightSelectHandler()}
                            disabled={this.props.auth.email || this.props.economy.seats_remaining <= 0 ? false : true}
                        >Book Now</Button>
                    </div>
                </Col>
            </Row>
        )
    }


    
}
 
export default withRouter(Flight);