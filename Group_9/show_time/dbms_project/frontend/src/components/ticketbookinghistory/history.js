import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getTicketHistory } from "../../actions/tickethistory";
import "./history.css";

export class TicketHistoryPage extends Component {
  static propTypes = {
    ticketbookinghistory: PropTypes.object.isRequired
  };

  componentDidMount() {
    this.props.getTicketHistory(this.props.match.params.user_id);
  }

  render() {
    const ticketlist = this.props.ticketbookinghistory["tickets"];
    console.log(ticketlist);

    if (!ticketlist) {
      return <h1>Not Found.</h1>;
    }
    ticketlist.map(ticket =>
      console.log(ticket.movie, ticket.booking_id, ticket.theatre)
    );
    return (
      <div style={{ backgroundColor: "rgb(36, 37, 43)", minHeight: "1080px" }}>
        <div className="container">
          <div className="row">
            <div className="col-sm-12 bodyy">
              <div
                className="row"
                style={{ paddingLeft: "20px", paddingRight: "20px" }}
              >
                <div
                  className="col-sm-12"
                  style={{
                    textAlign: "center",
                    fontSize: "47px",
                    fontWeight: "bolder",
                    borderBottom: "4px solid #dbdf99",
                    padding: "20px"
                  }}
                >
                  <span style={{ color: "#dcf836" }}> Booking History</span>
                </div>
              </div>
              <div className="row">
                <div className="col-sm-12" style={{ paddingLeft: "9%" }}>
                  {ticketlist.map(ticket => (
                    <table
                      className="table table-striped"
                      key={ticket.id}
                      style={{
                        width: "35%",
                        backgroundColor: "rgb(255, 254, 211)",
                        float: "left",
                        margin: "5%",
                        border: "11px double ",
                        borderRadius: "4px"
                      }}
                    >
                      <tbody>
                        <tr>
                          <td>Movie</td>
                          <td>{ticket.movie}</td>
                        </tr>
                        <tr>
                          <td>Booking Id</td>
                          <td>{ticket.booking_id}</td>
                        </tr>
                        <tr>
                          <td>City</td>
                          <td>{ticket.city}</td>
                        </tr>
                        <tr>
                          <td>Theatre</td>
                          <td>{ticket.theatre}</td>
                        </tr>
                        <tr>
                          <td>Timings</td>
                          <td>{ticket.timings}</td>
                        </tr>
                        <tr>
                          <td>Cost</td>
                          <td>{ticket.cost}</td>
                        </tr>

                        <tr>
                          <td>Seat No</td>
                          <td>{ticket.seat_no}</td>
                        </tr>
                        <tr>
                          <td>Category</td>
                          <td>{ticket.category}</td>
                        </tr>
                        <tr>
                          <td>Dimension</td>
                          <td>{ticket.dimension}</td>
                        </tr>
                        <tr>
                          <td>Language</td>
                          <td>{ticket.language}</td>
                        </tr>
                        <tr>
                          <td>Snakcs</td>
                          <td>{ticket.snacks}</td>
                        </tr>
                      </tbody>
                    </table>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  ticketbookinghistory: state.ticketbookinghistory.ticketbookinghistory
});

export default connect(
  mapStateToProps,
  { getTicketHistory }
)(TicketHistoryPage);
