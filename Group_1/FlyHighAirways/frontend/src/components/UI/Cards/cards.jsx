import React, { Component } from "react";
import { Card } from "antd";
import { Row, Col } from "antd";
import classes from "./Cards.module.css";
const tabList = [
  {
    key: "Booking1",
    tab: "Booking1"
  },
  {
    key: "Booking2",
    tab: "Booking2"
  }
];

const contentList = {
  Booking1: (
    <div style={{ fontSize: "20px", fontWeight: "bolder" }}>
      <p>Delhi - Mumbai</p>
      <p> Date : 20 March, 2018 </p>
      <p>Departure Time : 13:50 IST</p>
      <div
        style={{ float: "right" }}
        className={[classes.stamp, classes.isApproved].join(" ")}
      >
        Completed
      </div>
    </div>
  ),
  Booking2: (
    <div style={{ fontSize: "20px", fontWeight: "bolder" }}>
      <p>Kolkata - Chennai</p>
      <p> Date : 24 March, 2017 </p>
      <p>Departure Time : 9:35 IST</p>
      <div
        style={{ float: "right" }}
        className={[classes.stamp, classes.isApproved].join(" ")}
      >
        Cancelled
      </div>
    </div>
  )
};

class Cards extends Component {
  constructor(props) {
    super(props);
  }
  state = { key: "Booking1" };
  onTabChange = (key, type) => {
    console.log(key, type);
    this.setState({ [type]: key });
  };
  render() {
    const { Meta } = Card;

    return (
      <React.Fragment>
        <Row gutter={40}>
          {this.props.flightList.map((flight, index) => {
            return <div key={index} />;
          })}
        </Row>
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

export default Cards;
