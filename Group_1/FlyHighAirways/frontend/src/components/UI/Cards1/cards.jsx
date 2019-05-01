import React, { Component } from "react";
import { Card, Button } from "antd";
import { Row, Col } from "antd";
import classes from "./Cards.module.css";
import { NavLink } from "react-router-dom";
import flights from "../../Flights/Flights";
import { func, object, string } from "prop-types";

class Cards1 extends Component {
  constructor(props) {
    super(props);
  }
  state = { key: "Booking1" };
  onTabChange = (key, type) => {
    console.log(key, type);
    this.setState({ [type]: key });
  };
  render() {
    const flights_ = this.props.flightList;

    let contentList = {};
    const ListFligts = flights_.map(
      (booking, index) =>
        (contentList[`Booking ${index + 1}`] = (
          <div style={{ fontSize: "20px", fontWeight: "bolder" }}>
            <p>
              {booking.source} - {booking.destination}
            </p>
            <p> Date : {booking.Date} </p>
            <p>Departure Time : {booking.departureTime}</p>
            <div
              style={{ float: "right" }}
              className={[classes.stamp, classes.isApproved].join(" ")}
            >
              Scheduled
            </div>
            <React.Fragment>
              <div style={{ padding: "5px", float: "left" }}>
                <Button style={{ fontSize: "17px" }}>
                  <NavLink className="nav-link" to="/checkIn">
                    Check In
                  </NavLink>
                </Button>
              </div>
              <div style={{ padding: "5px", float: "left" }}>
                <Button style={{ fontSize: "17px" }}>
                  <NavLink to="/" className="nav-link">Cancel</NavLink>
                </Button>
              </div>
            </React.Fragment>
          </div>
        ))
    );
    let tabList = [];
    for (var i = 0; i < flights_.length; i++) {
      tabList.push({
        key: `Booking ${i + 1}`,
        tab: `Booking ${i + 1}`
      });
    }

    const { Meta } = Card;
    console.log(this.props.flightList);
    return (
      <React.Fragment>
        <div>
          <Card
            style={{ width: "50%", height: "40%" }}
            tabList={tabList}
            extra={<a href="#">More</a>}
            activeTabKey={this.state.key}
            onTabChange={key => {
              this.onTabChange(key, "key");
            }}
          >
            {contentList[this.state.key]}
          </Card>
        </div>
      </React.Fragment>
    );
  }
}

export default Cards1;
