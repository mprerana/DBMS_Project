import React, { Component } from "react";
import { Layout, Menu, Icon, Row, Col, Avatar } from "antd";
import { Form, Modal, Button } from "antd";
import Paypal from "../../components/Paypal/Paypal";

import classes from "./FlightBook.module.css";
import DynamicForm from "../../components/Form/DynamicForm";

const { SubMenu } = Menu;

const { Content, Footer, Sider } = Layout;

class FlightBook extends Component {
  constructor(props) {
    super(props);

    this.handler = this.handler.bind(this);
    // this.state = {
    //   messageShown: false,
    //   id: -1 // initialize new state property with a value
    // };
  }

  state = {
    counts: 1,
    baseFare: 4500,
    luggage: 500,
    gst: 18,
    visible: false,
    passengers: []
  };

  componentDidMount() {
    if (this.props.selectedFlight) {
      this.setState({ baseFare: this.props.selectedFlight.economy.fare });
    }
  }

  totalPriceCalculate = () => {
    if (this.state.counts === 0) {
      return [0, 0];
    }
    let sum = 0;
    sum += this.state.counts * this.state.baseFare;
    sum += this.state.luggage;
    const sumWithoutGST = (sum * this.state.gst) / 100;
    sum += (sum * this.state.gst) / 100;
    return [sum, sumWithoutGST];
  };

  handler(id) {
    this.setState({
      messageShown: true,
      id: id
    });
  }

  showModal = passengers => {

    console.log('former', passengers)

    const newPassengers = [];

    for (let passenger of passengers) {
        const tempPassenger = {
          fullName: passenger.name,
          age: parseInt(passenger.age),
          gender: 'M'
        }
        newPassengers.push(tempPassenger);
    }

    this.setState({ passengers: newPassengers, visible: true })
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

  handleClick = e => {
    console.log(e);
    this.setState({
      counts: e
    });
  };

  render() {


    return (
      <React.Fragment>
        {/* Modal */}
        <div>
          <Modal
            title="Basic Modal"
            visible={this.state.visible}
            onOk={this.handleOk}
            onCancel={this.handleCancel}
          >
            <h1>Your Total Amount is {this.totalPriceCalculate()[0]}</h1>
            <Paypal
              style={{ marginTop: "20px" }}
              toPay={this.totalPriceCalculate()[0]}
              transactionError={err => this.transactionError(err)}
              transactionCancelled={data => this.transactionCancelled(data)}
              transactionSuccess={payment => this.transactionSuccess(payment)}
              bookingData={this.props.selectedFlight}
              token={this.props.auth.idToken}
              passengers={this.state.passengers}
            />
          </Modal>
        </div>

        <Row
          style={{
            width: "80%",
            margin: "auto",
            paddingTop: "38px"
          }}
        >
          <Content
          // style={{ padding: "0 50px" }}
          >
            <Row
              style={{ marginTop: "5rem" }}
              // style={{ padding: "24px 0", background: "rgb(240, 242, 245)" }}
            >
              <Col
                lg={19}
                sm={14}
                style={{
                  padding: "0 24px",
                  minHeight: 280,
                  maxWidth: "75%",
                  borderRight: "1px solid #ebedf0"

                  // background: "rgb(240, 242, 245)"
                }}
              >
                <div
                // style={{ border: " 1px solid #ebedf0", background: "white" }}
                >
                  <Row
                    style={{
                      borderBottom: "1px solid #ebedf0",
                      padding: "10px"
                    }}
                  >
                    <Col sm={2}>
                      <div>
                        <Avatar size={64} icon="user" />
                      </div>
                    </Col>
                    <Col>
                      <h1
                        style={{
                          padding: "16px",
                          fontSize: "22px",
                          paddingLeft: "70px"
                        }}
                      >
                        Aaquib Niaz
                      </h1>
                    </Col>
                  </Row>

                  <Row
                    style={{
                      borderBottom: "1px solid #ebedf0",
                      padding: "10px"
                    }}
                  >
                    <Col
                      sm={24}
                      lg={20}
                      // sm={24}
                      // xs={24}
                      style={
                        {
                          // padding: "15px 85px"
                        }
                      }
                    >
                      {/* <WrappedDynamicFieldSet 
                        onAdd={this.handleClick} 
                        onSubmit={this.showModal}
                        isFlightSelected={[this.props.selectedFlight, this.state.counts]}  
                      /> */}

                      <DynamicForm
                        onSubmit={this.showModal}
                        onAdd={this.handleClick}
                        isFlightSelected={[
                          this.props.selectedFlight,
                          this.state.counts,
                          this.props.auth
                        ]}
                      />
                    </Col>
                  </Row>
                  <Row>
                    <Col>
                      <h1
                        style={{
                          padding: "16px",
                          fontSize: "22px",
                          paddingLeft: "70px"
                        }}
                      >
                        <Icon type="shopping-cart" />
                        &nbsp;&nbsp;Add Aditional Baggage
                      </h1>
                    </Col>
                  </Row>
                  <Row
                    style={{
                      borderBottom: "1px solid #ebedf0",
                      padding: "10px 85px"
                    }}
                  >
                    There is limit of 25 kg luggage per person
                  </Row>
                </div>
              </Col>

              <Col lg={6} style={{ background: "#fff", padding: "0 24px" }}>
                <div
                  style={{
                    background: "black",
                    color: "white",
                    fontSize: "19px",
                    textAlign: "center"
                  }}
                >
                  Pricing Summary
                </div>
                <div style={{ padding: "10px" }}>
                  <div className={classes.location}>
                    <h1>
                      {this.props.selectedFlight
                        ? this.props.selectedFlight.source
                        : "Select"}
                    </h1>
                    <h1>{this.props.selectedFlight ? "TO" : "The"}</h1>
                    <h1>
                      {this.props.selectedFlight
                        ? this.props.selectedFlight.destination
                        : "Locations"}
                    </h1>
                  </div>

                  {this.props.selectedFlight ? (
                    <div className={classes.pricebox}>
                      Base Fare = Rs{" "}
                      <span>
                        <b>
                          {this.state.counts === 0
                            ? 0
                            : this.state.counts * this.state.baseFare}
                        </b>
                      </span>
                      <br />
                      Luggage Charge = Rs <b>{this.state.luggage}</b>
                      <br />
                      GST = Rs <b>{this.totalPriceCalculate()[1]}</b>
                      <div className={classes.hr}>&nbsp;</div>
                      Total Fare= Rs <b>{this.totalPriceCalculate()[0]}</b>
                    </div>
                  ) : null}
                </div>
              </Col>
            </Row>
          </Content>
        </Row>
      </React.Fragment>
    );
  }
}

export default FlightBook;
