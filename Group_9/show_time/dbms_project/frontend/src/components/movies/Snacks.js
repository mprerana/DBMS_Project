import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getSnacks } from "../../actions/snacks";
import { bookaSeat } from "../../actions/seatsbooked";
import { postTicketHistory } from "../../actions/tickethistory";
import { Link } from "react-router-dom";
import Paypal from "../pages/Paypal";
import "./snacks.css";

/// AUWnNkRkdwNKiee-zgU8NF7Zs6OTt-c6zcCNeAM89mHWRHr_DrCjqyyu-qTZGYyJzJ2aTA2wsi4Aq6HK

export class Snacks extends Component {
  static propTypes = {
    snacks: PropTypes.array.isRequired
  };

  state = {
    totalmoviecost: 600.0,
    totalcost: 0.0,
    samosa: 0,
    popcorn: 0,
    sandwich: 0,
    Nachos: 0,
    Icecream: 0,
    Burger: 0,
    coke: 0,
    Frenchfries: 0,
    Pizza: 0,
    ColdCoffee: 0
  };

  componentDidMount() {
    this.props.getSnacks();

    const { ticket_price } = this.props.match.params;

    this.setState({ totalmoviecost: parseFloat(ticket_price) });
  }

  addItems = (name, price) => {
    if (name == "samosa") {
      this.setState({ samosa: this.state.samosa + 1 });
    }
    if (name == "popcorn") {
      this.setState({ popcorn: this.state.popcorn + 1 });
    }
    if (name == "sandwich") {
      this.setState({ sandwich: this.state.sandwich + 1 });
    }

    if (name == "Nachos") {
      this.setState({ Nachos: this.state.Nachos + 1 });
    }
    if (name == "Icecream") {
      this.setState({ Icecream: this.state.Icecream + 1 });
    }
    if (name == "Burger") {
      this.setState({ Burger: this.state.Burger + 1 });
    }

    if (name == "coke") {
      this.setState({ coke: this.state.coke + 1 });
    }
    if (name == "Frenchfries") {
      this.setState({ Frenchfries: this.state.Frenchfries + 1 });
    }
    if (name == "Pizza") {
      this.setState({ Pizza: this.state.Pizza + 1 });
    }

    if (name == "ColdCoffee") {
      this.setState({ ColdCoffee: this.state.ColdCoffee + 1 });
    }

    this.setState({ totalcost: this.state.totalcost + parseFloat(price) });
    this.setState({
      totalmoviecost: this.state.totalmoviecost + parseFloat(price)
    });
  };

  subtractItems = (name, price) => {
    if (name == "samosa") {
      if (this.state.samosa > 0) {
        this.setState({ samosa: this.state.samosa - 1 });
        this.setState({ totalcost: this.state.totalcost - parseFloat(price) });
        this.setState({
          totalmoviecost: this.state.totalmoviecost - parseFloat(price)
        });
      }
    }
    if (name == "popcorn") {
      if (this.state.popcorn > 0) {
        this.setState({ popcorn: this.state.popcorn - 1 });
        this.setState({ totalcost: this.state.totalcost - parseFloat(price) });
        this.setState({
          totalmoviecost: this.state.totalmoviecost - parseFloat(price)
        });
      }
    }
    if (name == "sandwich") {
      if (this.state.sandwich > 0) {
        this.setState({ sandwich: this.state.sandwich - 1 });
        this.setState({ totalcost: this.state.totalcost - parseFloat(price) });
        this.setState({
          totalmoviecost: this.state.totalmoviecost - parseFloat(price)
        });
      }
    }

    if (name == "Nachos") {
      if (this.state.Nachos > 0) {
        this.setState({ Nachos: this.state.Nachos - 1 });
        this.setState({ totalcost: this.state.totalcost - parseFloat(price) });
        this.setState({
          totalmoviecost: this.state.totalmoviecost - parseFloat(price)
        });
      }
    }

    if (name == "Icecream") {
      if (this.state.Icecream > 0) {
        this.setState({ Icecream: this.state.Icecream - 1 });
        this.setState({ totalcost: this.state.totalcost - parseFloat(price) });
        this.setState({
          totalmoviecost: this.state.totalmoviecost - parseFloat(price)
        });
      }
    }

    if (name == "Burger") {
      if (this.state.Burger > 0) {
        this.setState({ Burger: this.state.Burger - 1 });
        this.setState({ totalcost: this.state.totalcost - parseFloat(price) });
        this.setState({
          totalmoviecost: this.state.totalmoviecost - parseFloat(price)
        });
      }
    }

    if (name == "coke") {
      if (this.state.coke > 0) {
        this.setState({ coke: this.state.coke - 1 });
        this.setState({ totalcost: this.state.totalcost - parseFloat(price) });
        this.setState({
          totalmoviecost: this.state.totalmoviecost - parseFloat(price)
        });
      }
    }

    if (name == "Frenchfries") {
      if (this.state.Frenchfries > 0) {
        this.setState({ Frenchfries: this.state.Frenchfries - 1 });
        this.setState({ totalcost: this.state.totalcost - parseFloat(price) });
        this.setState({
          totalmoviecost: this.state.totalmoviecost - parseFloat(price)
        });
      }
    }

    if (name == "Pizza") {
      if (this.state.Pizza > 0) {
        this.setState({ Pizza: this.state.Pizza - 1 });
        this.setState({ totalcost: this.state.totalcost - parseFloat(price) });
        this.setState({
          totalmoviecost: this.state.totalmoviecost - parseFloat(price)
        });
      }
    }

    if (name == "ColdCoffee") {
      if (this.state.ColdCoffee > 0) {
        this.setState({ ColdCoffee: this.state.ColdCoffee - 1 });
        this.setState({ totalcost: this.state.totalcost - parseFloat(price) });
        this.setState({
          totalmoviecost: this.state.totalmoviecost - parseFloat(price)
        });
      }
    }
  };

  bookTickets = () => {
    let showdetailsid = this.props.showdetails.id;

    for (var i = 0; i < this.props.selectedseats.length; i++) {
      let data = {
        seatno: this.props.selectedseats[i],
        show_time_no_id: showdetailsid
      };

      let seat = {
        posting: data
      };

      this.props.bookaSeat(seat);
    }

    const { city, theatre_name } = this.props.match.params;

    let ticket = {
      booking_id: "PAYPAL$%123",
      title: this.props.showdetails.title,
      city: city,
      theatre: theatre_name,
      cost: this.state.totalmoviecost,
      language: this.props.showdetails.language,
      dimension: this.props.showdetails.format,
      category: "A",
      seat_no: String(this.props.selectedseats),
      timings: this.props.showdetails.show_timings,
      snacks: "samosa",
      user_id: this.props.auth.user.id
    };

    let poster = {
      posting: ticket
    };

    this.props.postTicketHistory(poster);
  };

  transactionError = () => {};

  transactionCanceled = () => {};

  transactionSuccess = () => {};

  render() {
    const useridbook = 36;

    const { city, theatre_name } = this.props.match.params;

    let state = this.state;

    return (
      <Fragment>
        <div className="backgroundsnacks">
          <div className="container-fluid">
            <div className="row">
              <div
                className="col-sm-8"
                style={{ paddingLeft: "5%", paddingRight: "5%" }}
              >
                <div className="headerimg">
                  <img
                    src="//in.bmscdn.com/bmsin/fnb/offerbanner/web/web-offerbanner.jpg"
                    style={{
                      width: "93%",
                      height: "auto",
                      maxWidth: "inherit"
                    }}
                  />
                </div>

                <div className="snacksbody">
                  <div className="container" style={{ maxWidth: "inherit" }}>
                    <div className="row ">
                      <div className="col-sm-12 snackshead">
                        <p className="snackshead1">
                          {" "}
                          Grab a <span style={{ color: "red" }}>Bite!</span>
                        </p>
                        <p className="snackshead2">
                          {" "}
                          Prebook Your Meal and{" "}
                          <span style={{ color: "red" }}>save more!</span>
                        </p>
                      </div>
                    </div>
                    <div className="row ">
                      <div className="col-sm-12 snackslist">
                        {this.props.snacks.map(snack => (
                          <div
                            className="card "
                            key={snack.id}
                            style={{ width: "30%" }}
                          >
                            <img
                              className="card-img-top"
                              src={snack.image}
                              alt="Card image"
                              style={{ width: "100 %", height: "150px" }}
                            />
                            <div className="card-body">
                              <h6 className="card-title">{snack.snacks}</h6>
                              <p className="card-text">
                                {snack.price}/- per plate / unit{" "}
                              </p>
                              <p className="card-text">
                                <span>
                                  &nbsp;&nbsp;
                                  <div
                                    className="btn btn-primary "
                                    onClick={this.addItems.bind(
                                      this,
                                      snack.snacks,
                                      snack.price
                                    )}
                                  >
                                    Add
                                  </div>
                                </span>
                                <span>
                                  &nbsp;&nbsp; {this.state[snack.snacks]}{" "}
                                </span>
                                <span>
                                  &nbsp;&nbsp;
                                  <div
                                    className="btn btn-danger"
                                    onClick={this.subtractItems.bind(
                                      this,
                                      snack.snacks,
                                      snack.price
                                    )}
                                  >
                                    Remove
                                  </div>
                                </span>
                              </p>
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                    <div className="row ">
                      <div className="col-sm-12 snacksfooter">
                        Note:
                        <ol style={{ fontSize: "small" }}>
                          <li>Images are for representation purposes only</li>
                          <li>Prices inclusive of taxes</li>
                        </ol>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div className="col-sm-4">
                <div className="bookingsummary">
                  <div className="bookingsummaryrates">
                    <table width="100%">
                      <tbody>
                        <tr>
                          <td style={{ padding: "16px", color: "aliceblue" }}>
                            Movie:
                          </td>
                          <td
                            style={{
                              textAlign: "right",
                              padding: "16px",
                              color: "aliceblue"
                            }}
                          >
                            {" "}
                            {this.props.showdetails.title}
                          </td>
                        </tr>
                        <tr>
                          <td style={{ padding: "16px", color: "aliceblue" }}>
                            Theatre:
                          </td>
                          <td
                            style={{
                              textAlign: "right",
                              padding: "16px",
                              color: "aliceblue"
                            }}
                          >
                            {" "}
                            {theatre_name}
                          </td>
                        </tr>
                        <tr>
                          <td style={{ padding: "16px", color: "aliceblue" }}>
                            Language:
                          </td>
                          <td
                            style={{
                              textAlign: "right",
                              padding: "16px",
                              color: "aliceblue"
                            }}
                          >
                            {" "}
                            {this.props.showdetails.language}
                          </td>
                        </tr>
                        <tr>
                          <td style={{ padding: "16px", color: "aliceblue" }}>
                            Format:
                          </td>
                          <td
                            style={{
                              textAlign: "right",
                              padding: "16px",
                              color: "aliceblue"
                            }}
                          >
                            {" "}
                            {this.props.showdetails.format}
                          </td>
                        </tr>
                        <tr>
                          <td style={{ padding: "16px", color: "aliceblue" }}>
                            Show_Timings:
                          </td>
                          <td
                            style={{
                              textAlign: "right",
                              padding: "16px",
                              color: "aliceblue"
                            }}
                          >
                            {" "}
                            {this.props.showdetails.show_timings}
                          </td>
                        </tr>
                        <tr>
                          <td style={{ padding: "16px", color: "aliceblue" }}>
                            City:
                          </td>
                          <td
                            style={{
                              textAlign: "right",
                              padding: "16px",
                              color: "aliceblue"
                            }}
                          >
                            {" "}
                            {city}
                          </td>
                        </tr>
                        <tr>
                          <td style={{ padding: "16px", color: "aliceblue" }}>
                            {" "}
                            <span style={{ fontSize1: "16px" }}>
                              Seats: &nbsp;
                              {this.props.selectedseats.map(seat => (
                                <span style={{ fontSize1: "12px" }}>
                                  {seat}&nbsp;&nbsp;
                                </span>
                              ))}
                            </span>
                          </td>
                          <td
                            style={{
                              textAlign: "right",
                              padding: "16px",
                              color: "aliceblue"
                            }}
                          >
                            {" "}
                            {`${this.state.totalmoviecost -
                              this.state.totalcost}`}
                            /-
                          </td>
                        </tr>
                        <tr>
                          <td style={{ color: "aliceblue" }}> Snacks</td>
                          <td
                            style={{
                              textAlign: "right",
                              padding: "16px",
                              color: "aliceblue"
                            }}
                          >
                            {this.state.totalcost}
                          </td>
                        </tr>

                        {/* here */}
                        {this.props.snacks.map(snack => (
                          <div key={snack.id}>
                            {this.state[snack.snacks] ? (
                              <tr>
                                <td style={{ color: "aliceblue" }}>
                                  {snack.snacks} * {this.state[snack.snacks]}
                                </td>

                                <td
                                  style={{
                                    textAlign: "right",
                                    padding: "16px",
                                    color: "aliceblue"
                                  }}
                                >
                                  {snack.price * this.state[snack.snacks]}
                                </td>
                              </tr>
                            ) : null}
                          </div>
                        ))}
                      </tbody>
                    </table>
                  </div>
                  <div className="bookingsummarytotalamount">
                    <table width="100%">
                      <tbody>
                        <tr>
                          <td>
                            {" "}
                            <span
                              style={{
                                fontSize1: "18px",
                                padding: "16px",
                                color: "aliceblue"
                              }}
                            >
                              Total
                            </span>
                          </td>
                          <td
                            style={{
                              textAlign: "right",
                              padding: "16px",
                              color: "aliceblue"
                            }}
                          >
                            {" "}
                            {this.state.totalmoviecost}
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                  <div className="bookingsummarysubmit">
                    <Paypal
                      style={{ width: "100%" }}
                      toPay={this.state.totalmoviecost}
                      transactionError={data => this.transactionError(data)}
                      transactionCanceled={data =>
                        this.transactionCanceled(data)
                      }
                      onSuccess={data => this.transactionSuccess(data)}
                      className="btn btn-danger"
                    />
                  </div>
                  <div>
                    <Link
                      to={`/history/${this.props.auth.user.id}`}
                      className="btn btn-dark"
                      style={{
                        height: "50px",
                        width: "187px",
                        padding: "10px",
                        backgroundColor: "#f57a15",
                        color: "white",
                        fontWeight: "bolder",
                        borderRadius: "7px"
                      }}
                      onClick={this.bookTickets}
                    >
                      Book Tickets
                    </Link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  snacks: state.snacks.snacks,
  selectedseats: state.selectedseats.selectedseats,
  showdetails: state.showdetails.showdetails,
  auth: state.auth
});

export default connect(
  mapStateToProps,
  { getSnacks, bookaSeat, postTicketHistory }
)(Snacks);
