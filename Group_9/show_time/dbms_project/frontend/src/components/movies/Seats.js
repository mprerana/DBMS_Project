import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getShowDetails } from "../../actions/showdetails";
import { getSeatsBooked } from "../../actions/seatsbooked";
import { getSelectedSeats } from "../../actions/selectedseats";
import { createMessage } from "../../actions/messages";
import { Route, Redirect } from "react-router-dom";
import ReactTimeout from "react-timeout";
import { Link } from "react-router-dom";
import "./seat.css";

export class seats extends Component {
  static propTypes = {
    showdetails: PropTypes.object.isRequired,
    getShowDetails: PropTypes.func.isRequired,
    getShowDetails: PropTypes.func.isRequired,
    seatsbooked: PropTypes.array.isRequired,
    selectedseats: PropTypes.array.isRequired,
    getSelectedSeats: PropTypes.func.isRequired
  };

  changeStatusseatsBooked = id => {
    if (this.props.seatsbooked) {
      for (var i = 0; i < this.props.seatsbooked.length; i++) {
        console.log(this.props.seatsbooked[i]);
        let row = "row" + String(this.props.seatsbooked[i]["seatno"][0]);
        this.props.seatsbooked[i]["seatno"] = String(
          this.props.seatsbooked[i]["seatno"]
        );
        let seat_no = this.props.seatsbooked[i]["seatno"].slice(
          1,
          this.props.seatsbooked[i].length
        );

        console.log(seat_no);
        seat_no = parseInt(seat_no, 10);

        let a = this.state.seatplan1;
        a[row][seat_no]["status"] = 2;
        a[row][seat_no]["bgColor"] = "rgb(141, 137, 25)";

        this.setState({ seatplan1: a });

        console.log("I am not laxman");
      }
    } else {
      console.log("I am Laxman");
    }
  };

  componentDidMount() {
    const { show_id, theatre_id, city, theatre_name } = this.props.match.params;
    this.props.getShowDetails(show_id);
    this.props.getSeatsBooked(show_id);
    this.props.setTimeout(this.changeStatusseatsBooked.bind(this, 23), 200);
    this.changeStatusseatsBooked.bind(this, 23);
  }

  state = {
    stateplanning: 0,
    totalprice: 0,
    noofseatsbooked: 0,

    seatplan1: {
      rowA: [
        { seatno: "A1", status: 0, bgColor: "#404048de" },
        { seatno: "A2", status: 0, bgColor: "#404048de" },
        { seatno: "A3", status: 0, bgColor: "#404048de" },
        { seatno: "A4", status: 0, bgColor: "#404048de" },
        { seatno: "A5", status: 0, bgColor: "#404048de" },
        { seatno: "A6", status: 0, bgColor: "#404048de" },
        { seatno: "A7", status: 0, bgColor: "#404048de" },
        { seatno: "A8", status: 0, bgColor: "#404048de" },
        { seatno: "A9", status: 0, bgColor: "#404048de" },
        { seatno: "A10", status: 0, bgColor: "#404048de" },
        { seatno: "A11", status: 0, bgColor: "#404048de" },
        { seatno: "A12", status: 0, bgColor: "#404048de" },
        { seatno: "A13", status: 0, bgColor: "#404048de" },
        { seatno: "A14", status: 0, bgColor: "#404048de" },
        { seatno: "A15", status: 0, bgColor: "#404048de" },
        { seatno: "A16", status: 0, bgColor: "#404048de" },
        { seatno: "A17", status: 0, bgColor: "#404048de" },
        { seatno: "A18", status: 0, bgColor: "#404048de" },
        { seatno: "A19", status: 0, bgColor: "#404048de" },
        { seatno: "A20", status: 0, bgColor: "#404048de" },
        { seatno: "A21", status: 0, bgColor: "#404048de" },
        { seatno: "A22", status: 0, bgColor: "#404048de" },
        { seatno: "A23", status: 0, bgColor: "#404048de" },
        { seatno: "A24", status: 0, bgColor: "#404048de" },
        { seatno: "A25", status: 0, bgColor: "#404048de" },
        { seatno: "A26", status: 0, bgColor: "#404048de" },
        { seatno: "A27", status: 0, bgColor: "#404048de" },
        { seatno: "A28", status: 0, bgColor: "#404048de" },
        { seatno: "A29", status: 0, bgColor: "#404048de" },
        { seatno: "A30", status: 0, bgColor: "#404048de" }
      ],

      rowB: [
        { seatno: "B1", status: 0, bgColor: "#404048de" },
        { seatno: "B2", status: 0, bgColor: "#404048de" },
        { seatno: "B3", status: 0, bgColor: "#404048de" },
        { seatno: "B4", status: 0, bgColor: "#404048de" },
        { seatno: "B5", status: 0, bgColor: "#404048de" },
        { seatno: "B6", status: 0, bgColor: "#404048de" },
        { seatno: "B7", status: 0, bgColor: "#404048de" },
        { seatno: "B8", status: 0, bgColor: "#404048de" },
        { seatno: "B9", status: 0, bgColor: "#404048de" },
        { seatno: "B10", status: 0, bgColor: "#404048de" },
        { seatno: "B11", status: 0, bgColor: "#404048de" },
        { seatno: "B12", status: 0, bgColor: "#404048de" },
        { seatno: "B13", status: 0, bgColor: "#404048de" },
        { seatno: "B14", status: 0, bgColor: "#404048de" },
        { seatno: "B15", status: 0, bgColor: "#404048de" },
        { seatno: "B16", status: 0, bgColor: "#404048de" },
        { seatno: "B17", status: 0, bgColor: "#404048de" },
        { seatno: "B18", status: 0, bgColor: "#404048de" },
        { seatno: "B19", status: 0, bgColor: "#404048de" },
        { seatno: "B20", status: 0, bgColor: "#404048de" },
        { seatno: "B21", status: 0, bgColor: "#404048de" },
        { seatno: "B22", status: 0, bgColor: "#404048de" },
        { seatno: "B23", status: 0, bgColor: "#404048de" },
        { seatno: "B24", status: 0, bgColor: "#404048de" }
      ],
      rowC: [
        { seatno: "C1", status: 0, bgColor: "#404048de" },
        { seatno: "C2", status: 0, bgColor: "#404048de" },
        { seatno: "C3", status: 0, bgColor: "#404048de" },
        { seatno: "C4", status: 0, bgColor: "#404048de" },
        { seatno: "C5", status: 0, bgColor: "#404048de" },
        { seatno: "C6", status: 0, bgColor: "#404048de" },
        { seatno: "C7", status: 0, bgColor: "#404048de" },
        { seatno: "C8", status: 0, bgColor: "#404048de" },
        { seatno: "C9", status: 0, bgColor: "#404048de" },
        { seatno: "C10", status: 0, bgColor: "#404048de" },
        { seatno: "C11", status: 0, bgColor: "#404048de" },
        { seatno: "C12", status: 0, bgColor: "#404048de" },
        { seatno: "C13", status: 0, bgColor: "#404048de" },
        { seatno: "C14", status: 0, bgColor: "#404048de" },
        { seatno: "C15", status: 0, bgColor: "#404048de" },
        { seatno: "C16", status: 0, bgColor: "#404048de" },
        { seatno: "C17", status: 0, bgColor: "#404048de" },
        { seatno: "C18", status: 0, bgColor: "#404048de" },
        { seatno: "C19", status: 0, bgColor: "#404048de" },
        { seatno: "C20", status: 0, bgColor: "#404048de" },
        { seatno: "C21", status: 0, bgColor: "#404048de" },
        { seatno: "C22", status: 0, bgColor: "#404048de" },
        { seatno: "C23", status: 0, bgColor: "#404048de" },
        { seatno: "C24", status: 0, bgColor: "#404048de" }
      ],
      rowD: [
        { seatno: "D1", status: 0, bgColor: "#404048de" },
        { seatno: "D2", status: 0, bgColor: "#404048de" },
        { seatno: "D3", status: 0, bgColor: "#404048de" },
        { seatno: "D4", status: 0, bgColor: "#404048de" },
        { seatno: "D5", status: 0, bgColor: "#404048de" },
        { seatno: "D6", status: 0, bgColor: "#404048de" },
        { seatno: "D7", status: 0, bgColor: "#404048de" },
        { seatno: "D8", status: 0, bgColor: "#404048de" },
        { seatno: "D9", status: 0, bgColor: "#404048de" },
        { seatno: "D10", status: 0, bgColor: "#404048de" },
        { seatno: "D11", status: 0, bgColor: "#404048de" },
        { seatno: "D12", status: 0, bgColor: "#404048de" },
        { seatno: "D13", status: 0, bgColor: "#404048de" },
        { seatno: "D14", status: 0, bgColor: "#404048de" },
        { seatno: "D15", status: 0, bgColor: "#404048de" },
        { seatno: "D16", status: 0, bgColor: "#404048de" },
        { seatno: "D17", status: 0, bgColor: "#404048de" },
        { seatno: "D18", status: 0, bgColor: "#404048de" },
        { seatno: "D19", status: 0, bgColor: "#404048de" },
        { seatno: "D20", status: 0, bgColor: "#404048de" },
        { seatno: "D21", status: 0, bgColor: "#404048de" },
        { seatno: "D22", status: 0, bgColor: "#404048de" },
        { seatno: "D23", status: 0, bgColor: "#404048de" },
        { seatno: "D24", status: 0, bgColor: "#404048de" }
      ],
      rowE: [
        { seatno: "E1", status: 0, bgColor: "#404048de" },
        { seatno: "E2", status: 0, bgColor: "#404048de" },
        { seatno: "E3", status: 0, bgColor: "#404048de" },
        { seatno: "E4", status: 0, bgColor: "#404048de" },
        { seatno: "E5", status: 0, bgColor: "#404048de" },
        { seatno: "E6", status: 0, bgColor: "#404048de" },
        { seatno: "E7", status: 0, bgColor: "#404048de" },
        { seatno: "E8", status: 0, bgColor: "#404048de" },
        { seatno: "E9", status: 0, bgColor: "#404048de" },
        { seatno: "E10", status: 0, bgColor: "#404048de" },
        { seatno: "E11", status: 0, bgColor: "#404048de" },
        { seatno: "E12", status: 0, bgColor: "#404048de" },
        { seatno: "E13", status: 0, bgColor: "#404048de" },
        { seatno: "E14", status: 0, bgColor: "#404048de" },
        { seatno: "E15", status: 0, bgColor: "#404048de" },
        { seatno: "E16", status: 0, bgColor: "#404048de" },
        { seatno: "E17", status: 0, bgColor: "#404048de" },
        { seatno: "E18", status: 0, bgColor: "#404048de" },
        { seatno: "E19", status: 0, bgColor: "#404048de" },
        { seatno: "E20", status: 0, bgColor: "#404048de" },
        { seatno: "E21", status: 0, bgColor: "#404048de" },
        { seatno: "E22", status: 0, bgColor: "#404048de" },
        { seatno: "E23", status: 0, bgColor: "#404048de" },
        { seatno: "E24", status: 0, bgColor: "#404048de" }
      ],
      rowF: [
        { seatno: "F1", status: 0, bgColor: "#404048de" },
        { seatno: "F2", status: 0, bgColor: "#404048de" },
        { seatno: "F3", status: 0, bgColor: "#404048de" },
        { seatno: "F4", status: 0, bgColor: "#404048de" },
        { seatno: "F5", status: 0, bgColor: "#404048de" },
        { seatno: "F6", status: 0, bgColor: "#404048de" },
        { seatno: "F7", status: 0, bgColor: "#404048de" },
        { seatno: "F8", status: 0, bgColor: "#404048de" },
        { seatno: "F9", status: 0, bgColor: "#404048de" },
        { seatno: "F10", status: 0, bgColor: "#404048de" },
        { seatno: "F11", status: 0, bgColor: "#404048de" },
        { seatno: "F12", status: 0, bgColor: "#404048de" },
        { seatno: "F13", status: 0, bgColor: "#404048de" },
        { seatno: "F14", status: 0, bgColor: "#404048de" },
        { seatno: "F15", status: 0, bgColor: "#404048de" },
        { seatno: "F16", status: 0, bgColor: "#404048de" },
        { seatno: "F17", status: 0, bgColor: "#404048de" },
        { seatno: "F18", status: 0, bgColor: "#404048de" },
        { seatno: "F19", status: 0, bgColor: "#404048de" },
        { seatno: "F20", status: 0, bgColor: "#404048de" },
        { seatno: "F21", status: 0, bgColor: "#404048de" },
        { seatno: "F22", status: 0, bgColor: "#404048de" },
        { seatno: "F23", status: 0, bgColor: "#404048de" },
        { seatno: "F24", status: 0, bgColor: "#404048de" }
      ],
      rowG: [
        { seatno: "G1", status: 0, bgColor: "#404048de" },
        { seatno: "G2", status: 0, bgColor: "#404048de" },
        { seatno: "G3", status: 0, bgColor: "#404048de" },
        { seatno: "G4", status: 0, bgColor: "#404048de" },
        { seatno: "G5", status: 0, bgColor: "#404048de" },
        { seatno: "G6", status: 0, bgColor: "#404048de" },
        { seatno: "G7", status: 0, bgColor: "#404048de" },
        { seatno: "G8", status: 0, bgColor: "#404048de" },
        { seatno: "G9", status: 0, bgColor: "#404048de" },
        { seatno: "G10", status: 0, bgColor: "#404048de" },
        { seatno: "G11", status: 0, bgColor: "#404048de" },
        { seatno: "G12", status: 0, bgColor: "#404048de" },
        { seatno: "G13", status: 0, bgColor: "#404048de" },
        { seatno: "G14", status: 0, bgColor: "#404048de" },
        { seatno: "G15", status: 0, bgColor: "#404048de" },
        { seatno: "G16", status: 0, bgColor: "#404048de" },
        { seatno: "G17", status: 0, bgColor: "#404048de" },
        { seatno: "G18", status: 0, bgColor: "#404048de" },
        { seatno: "G19", status: 0, bgColor: "#404048de" },
        { seatno: "G20", status: 0, bgColor: "#404048de" },
        { seatno: "G21", status: 0, bgColor: "#404048de" },
        { seatno: "G22", status: 0, bgColor: "#404048de" },
        { seatno: "G23", status: 0, bgColor: "#404048de" },
        { seatno: "G24", status: 0, bgColor: "#404048de" }
      ],
      rowH: [
        { seatno: "H1", status: 0, bgColor: "#404048de" },
        { seatno: "H2", status: 0, bgColor: "#404048de" },
        { seatno: "H3", status: 0, bgColor: "#404048de" },
        { seatno: "H4", status: 0, bgColor: "#404048de" },
        { seatno: "H5", status: 0, bgColor: "#404048de" },
        { seatno: "H6", status: 0, bgColor: "#404048de" },
        { seatno: "H7", status: 0, bgColor: "#404048de" },
        { seatno: "H8", status: 0, bgColor: "#404048de" },
        { seatno: "H9", status: 0, bgColor: "#404048de" },
        { seatno: "H10", status: 0, bgColor: "#404048de" },
        { seatno: "H11", status: 0, bgColor: "#404048de" },
        { seatno: "H12", status: 0, bgColor: "#404048de" },
        { seatno: "H13", status: 0, bgColor: "#404048de" },
        { seatno: "H14", status: 0, bgColor: "#404048de" },
        { seatno: "H15", status: 0, bgColor: "#404048de" },
        { seatno: "H16", status: 0, bgColor: "#404048de" },
        { seatno: "H17", status: 0, bgColor: "#404048de" },
        { seatno: "H18", status: 0, bgColor: "#404048de" },
        { seatno: "H19", status: 0, bgColor: "#404048de" },
        { seatno: "H20", status: 0, bgColor: "#404048de" },
        { seatno: "H21", status: 0, bgColor: "#404048de" },
        { seatno: "H22", status: 0, bgColor: "#404048de" },
        { seatno: "H23", status: 0, bgColor: "#404048de" },
        { seatno: "H24", status: 0, bgColor: "#404048de" }
      ],

      rowI: [
        { seatno: "I1", status: 0, bgColor: "#404048de" },
        { seatno: "I2", status: 0, bgColor: "#404048de" },
        { seatno: "I3", status: 0, bgColor: "#404048de" },
        { seatno: "I4", status: 0, bgColor: "#404048de" },
        { seatno: "I5", status: 0, bgColor: "#404048de" },
        { seatno: "I6", status: 0, bgColor: "#404048de" },
        { seatno: "I7", status: 0, bgColor: "#404048de" },
        { seatno: "I8", status: 0, bgColor: "#404048de" },
        { seatno: "I9", status: 0, bgColor: "#404048de" },
        { seatno: "I10", status: 0, bgColor: "#404048de" },
        { seatno: "I11", status: 0, bgColor: "#404048de" },
        { seatno: "I12", status: 0, bgColor: "#404048de" },
        { seatno: "I13", status: 0, bgColor: "#404048de" },
        { seatno: "I14", status: 0, bgColor: "#404048de" },
        { seatno: "I15", status: 0, bgColor: "#404048de" },
        { seatno: "I16", status: 0, bgColor: "#404048de" },
        { seatno: "I17", status: 0, bgColor: "#404048de" },
        { seatno: "I18", status: 0, bgColor: "#404048de" },
        { seatno: "I19", status: 0, bgColor: "#404048de" },
        { seatno: "I20", status: 0, bgColor: "#404048de" },
        { seatno: "I21", status: 0, bgColor: "#404048de" },
        { seatno: "I22", status: 0, bgColor: "#404048de" },
        { seatno: "I23", status: 0, bgColor: "#404048de" },
        { seatno: "I24", status: 0, bgColor: "#404048de" }
      ],

      rowJ: [
        { seatno: "J1", status: 0, bgColor: "#404048de" },
        { seatno: "J2", status: 0, bgColor: "#404048de" },
        { seatno: "J3", status: 0, bgColor: "#404048de" },
        { seatno: "J4", status: 0, bgColor: "#404048de" },
        { seatno: "J5", status: 0, bgColor: "#404048de" },
        { seatno: "J6", status: 0, bgColor: "#404048de" },
        { seatno: "J7", status: 0, bgColor: "#404048de" },
        { seatno: "J8", status: 0, bgColor: "#404048de" },
        { seatno: "J9", status: 0, bgColor: "#404048de" },
        { seatno: "J10", status: 0, bgColor: "#404048de" },
        { seatno: "J11", status: 0, bgColor: "#404048de" },
        { seatno: "J12", status: 0, bgColor: "#404048de" },
        { seatno: "J13", status: 0, bgColor: "#404048de" },
        { seatno: "J14", status: 0, bgColor: "#404048de" },
        { seatno: "J15", status: 0, bgColor: "#404048de" },
        { seatno: "J16", status: 0, bgColor: "#404048de" },
        { seatno: "J17", status: 0, bgColor: "#404048de" },
        { seatno: "J18", status: 0, bgColor: "#404048de" },
        { seatno: "J19", status: 0, bgColor: "#404048de" },
        { seatno: "J20", status: 0, bgColor: "#404048de" },
        { seatno: "J21", status: 0, bgColor: "#404048de" },
        { seatno: "J22", status: 0, bgColor: "#404048de" },
        { seatno: "J23", status: 0, bgColor: "#404048de" },
        { seatno: "J24", status: 0, bgColor: "#404048de" }
      ],

      rowK: [
        { seatno: "K1", status: 0, bgColor: "#404048de" },
        { seatno: "K2", status: 0, bgColor: "#404048de" },
        { seatno: "K3", status: 0, bgColor: "#404048de" },
        { seatno: "K4", status: 0, bgColor: "#404048de" },
        { seatno: "K5", status: 0, bgColor: "#404048de" },
        { seatno: "K6", status: 0, bgColor: "#404048de" },
        { seatno: "K7", status: 0, bgColor: "#404048de" },
        { seatno: "K8", status: 0, bgColor: "#404048de" },
        { seatno: "K9", status: 0, bgColor: "#404048de" },
        { seatno: "K10", status: 0, bgColor: "#404048de" },
        { seatno: "K11", status: 0, bgColor: "#404048de" },
        { seatno: "K12", status: 0, bgColor: "#404048de" },
        { seatno: "K13", status: 0, bgColor: "#404048de" },
        { seatno: "K14", status: 0, bgColor: "#404048de" },
        { seatno: "K15", status: 0, bgColor: "#404048de" },
        { seatno: "K16", status: 0, bgColor: "#404048de" },
        { seatno: "K17", status: 0, bgColor: "#404048de" },
        { seatno: "K18", status: 0, bgColor: "#404048de" },
        { seatno: "K19", status: 0, bgColor: "#404048de" },
        { seatno: "K20", status: 0, bgColor: "#404048de" },
        { seatno: "K21", status: 0, bgColor: "#404048de" },
        { seatno: "K22", status: 0, bgColor: "#404048de" },
        { seatno: "K23", status: 0, bgColor: "#404048de" },
        { seatno: "K24", status: 0, bgColor: "#404048de" }
      ],
      rowL: [
        { seatno: "L1", status: 0, bgColor: "#404048de" },
        { seatno: "L2", status: 0, bgColor: "#404048de" },
        { seatno: "L3", status: 0, bgColor: "#404048de" },
        { seatno: "L4", status: 0, bgColor: "#404048de" },
        { seatno: "L5", status: 0, bgColor: "#404048de" },
        { seatno: "L6", status: 0, bgColor: "#404048de" },
        { seatno: "L7", status: 0, bgColor: "#404048de" },
        { seatno: "L8", status: 0, bgColor: "#404048de" },
        { seatno: "L9", status: 0, bgColor: "#404048de" },
        { seatno: "L10", status: 0, bgColor: "#404048de" },
        { seatno: "L11", status: 0, bgColor: "#404048de" },
        { seatno: "L12", status: 0, bgColor: "#404048de" },
        { seatno: "L13", status: 0, bgColor: "#404048de" },
        { seatno: "L14", status: 0, bgColor: "#404048de" },
        { seatno: "L15", status: 0, bgColor: "#404048de" },
        { seatno: "L16", status: 0, bgColor: "#404048de" },
        { seatno: "L17", status: 0, bgColor: "#404048de" },
        { seatno: "L18", status: 0, bgColor: "#404048de" },
        { seatno: "L19", status: 0, bgColor: "#404048de" },
        { seatno: "L20", status: 0, bgColor: "#404048de" },
        { seatno: "L21", status: 0, bgColor: "#404048de" },
        { seatno: "L22", status: 0, bgColor: "#404048de" },
        { seatno: "L23", status: 0, bgColor: "#404048de" },
        { seatno: "L24", status: 0, bgColor: "#404048de" }
      ]
    },

    seatplan2: [
      { seatno: "A1", status: 0 },
      { seatno: "A2", status: 0 },
      { seatno: "A3", status: 0 },
      { seatno: "A4", status: 0 },
      { seatno: "A5", status: 0 },
      { seatno: "A6", status: 0 },
      { seatno: "A7", status: 0 },
      { seatno: "A8", status: 0 },
      { seatno: "A9", status: 0 },
      { seatno: "A10", status: 0 },
      { seatno: "A11", status: 0 },
      { seatno: "A12", status: 0 },
      { seatno: "A13", status: 0 },
      { seatno: "A14", status: 0 },
      { seatno: "A15", status: 0 },
      { seatno: "A16", status: 0 },
      { seatno: "A17", status: 0 },
      { seatno: "A18", status: 0 },
      { seatno: "A19", status: 0 },
      { seatno: "A20", status: 0 },
      { seatno: "A21", status: 0 },
      { seatno: "A22", status: 0 },
      { seatno: "A23", status: 0 },
      { seatno: "A24", status: 0 },
      { seatno: "A25", status: 0 },
      { seatno: "A26", status: 0 },
      { seatno: "A27", status: 0 },
      { seatno: "A28", status: 0 },
      { seatno: "A29", status: 0 },
      { seatno: "A30", status: 0 },
      { seatno: "A31", status: 0 },
      { seatno: "A32", status: 0 },
      { seatno: "A33", status: 0 },
      { seatno: "A34", status: 0 },
      { seatno: "A35", status: 0 },
      { seatno: "A36", status: 0 },
      { seatno: "A37", status: 0 },
      { seatno: "A38", status: 0 },
      { seatno: "A39", status: 0 },
      { seatno: "A40", status: 0 },
      { seatno: "B1", status: 0 },
      { seatno: "B2", status: 0 },
      { seatno: "B3", status: 0 },
      { seatno: "B4", status: 0 },
      { seatno: "B5", status: 0 },
      { seatno: "B6", status: 0 },
      { seatno: "B7", status: 0 },
      { seatno: "B8", status: 0 },
      { seatno: "B9", status: 0 },
      { seatno: "B10", status: 0 },
      { seatno: "B11", status: 0 },
      { seatno: "B12", status: 0 },
      { seatno: "B13", status: 0 },
      { seatno: "B14", status: 0 },
      { seatno: "B15", status: 0 },
      { seatno: "B16", status: 0 },
      { seatno: "B17", status: 0 },
      { seatno: "B18", status: 0 },
      { seatno: "B19", status: 0 },
      { seatno: "B20", status: 0 },
      { seatno: "B21", status: 0 },
      { seatno: "B22", status: 0 },
      { seatno: "B23", status: 0 },
      { seatno: "B24", status: 0 },
      { seatno: "B25", status: 0 },
      { seatno: "B26", status: 0 },
      { seatno: "B27", status: 0 },
      { seatno: "B28", status: 0 },
      { seatno: "B29", status: 0 },
      { seatno: "B30", status: 0 },
      { seatno: "B1", status: 0 },
      { seatno: "B32", status: 0 },
      { seatno: "B33", status: 0 },
      { seatno: "B34", status: 0 },
      { seatno: "B35", status: 0 },
      { seatno: "B36", status: 0 },
      { seatno: "B37", status: 0 },
      { seatno: "B38", status: 0 },
      { seatno: "B39", status: 0 },
      { seatno: "B40", status: 0 },
      { seatno: "C1", status: 0 },
      { seatno: "C2", status: 0 },
      { seatno: "C3", status: 0 },
      { seatno: "C4", status: 0 },
      { seatno: "C5", status: 0 },
      { seatno: "C6", status: 0 },
      { seatno: "C7", status: 0 },
      { seatno: "C8", status: 0 },
      { seatno: "C9", status: 0 },
      { seatno: "C10", status: 0 },
      { seatno: "C11", status: 0 },
      { seatno: "C12", status: 0 },
      { seatno: "C13", status: 0 },
      { seatno: "C14", status: 0 },
      { seatno: "C15", status: 0 },
      { seatno: "C16", status: 0 },
      { seatno: "C17", status: 0 },
      { seatno: "C18", status: 0 },
      { seatno: "C19", status: 0 },
      { seatno: "C20", status: 0 },
      { seatno: "C21", status: 0 },
      { seatno: "C22", status: 0 },
      { seatno: "C23", status: 0 },
      { seatno: "C24", status: 0 },
      { seatno: "C25", status: 0 },
      { seatno: "C26", status: 0 },
      { seatno: "C27", status: 0 },
      { seatno: "C28", status: 0 },
      { seatno: "C29", status: 0 },
      { seatno: "C30", status: 0 },
      { seatno: "C31", status: 0 },
      { seatno: "C32", status: 0 },
      { seatno: "C33", status: 0 },
      { seatno: "C34", status: 0 },
      { seatno: "C35", status: 0 },
      { seatno: "C36", status: 0 },
      { seatno: "C37", status: 0 },
      { seatno: "C38", status: 0 },
      { seatno: "C39", status: 0 },
      { seatno: "C40", status: 0 },
      { seatno: "D1", status: 0 },
      { seatno: "D2", status: 0 },
      { seatno: "D3", status: 0 },
      { seatno: "D4", status: 0 },
      { seatno: "D5", status: 0 },
      { seatno: "D6", status: 0 },
      { seatno: "D7", status: 0 },
      { seatno: "D8", status: 0 },
      { seatno: "D9", status: 0 },
      { seatno: "D10", status: 0 },
      { seatno: "D11", status: 0 },
      { seatno: "D12", status: 0 },
      { seatno: "D13", status: 0 },
      { seatno: "D14", status: 0 },
      { seatno: "D15", status: 0 },
      { seatno: "D16", status: 0 },
      { seatno: "D17", status: 0 },
      { seatno: "D18", status: 0 },
      { seatno: "D19", status: 0 },
      { seatno: "D20", status: 0 },
      { seatno: "D21", status: 0 },
      { seatno: "D22", status: 0 },
      { seatno: "D23", status: 0 },
      { seatno: "D24", status: 0 },
      { seatno: "D25", status: 0 },
      { seatno: "D26", status: 0 },
      { seatno: "D27", status: 0 },
      { seatno: "D28", status: 0 },
      { seatno: "D29", status: 0 },
      { seatno: "D30", status: 0 },
      { seatno: "D31", status: 0 },
      { seatno: "D32", status: 0 },
      { seatno: "D33", status: 0 },
      { seatno: "D34", status: 0 },
      { seatno: "D35", status: 0 },
      { seatno: "D36", status: 0 },
      { seatno: "D37", status: 0 },
      { seatno: "D38", status: 0 },
      { seatno: "D39", status: 0 },
      { seatno: "D40", status: 0 },
      { seatno: "E1", status: 0 },
      { seatno: "E2", status: 0 },
      { seatno: "E3", status: 0 },
      { seatno: "E4", status: 0 },
      { seatno: "E5", status: 0 },
      { seatno: "E6", status: 0 },
      { seatno: "E7", status: 0 },
      { seatno: "E8", status: 0 },
      { seatno: "E9", status: 0 },
      { seatno: "E10", status: 0 },
      { seatno: "E11", status: 0 },
      { seatno: "E12", status: 0 },
      { seatno: "E13", status: 0 },
      { seatno: "E14", status: 0 },
      { seatno: "E15", status: 0 },
      { seatno: "E16", status: 0 },
      { seatno: "E17", status: 0 },
      { seatno: "E18", status: 0 },
      { seatno: "E19", status: 0 },
      { seatno: "E20", status: 0 },
      { seatno: "E21", status: 0 },
      { seatno: "E22", status: 0 },
      { seatno: "E23", status: 0 },
      { seatno: "E24", status: 0 },
      { seatno: "E25", status: 0 },
      { seatno: "E26", status: 0 },
      { seatno: "E27", status: 0 },
      { seatno: "E28", status: 0 },
      { seatno: "E29", status: 0 },
      { seatno: "E30", status: 0 },
      { seatno: "E31", status: 0 },
      { seatno: "E32", status: 0 },
      { seatno: "E33", status: 0 },
      { seatno: "E34", status: 0 },
      { seatno: "E35", status: 0 },
      { seatno: "E36", status: 0 },
      { seatno: "E37", status: 0 },
      { seatno: "E38", status: 0 },
      { seatno: "E39", status: 0 },
      { seatno: "E40", status: 0 },
      { seatno: "F1", status: 0 },
      { seatno: "F2", status: 0 },
      { seatno: "F3", status: 0 },
      { seatno: "F4", status: 0 },
      { seatno: "F5", status: 0 },
      { seatno: "F6", status: 0 },
      { seatno: "F7", status: 0 },
      { seatno: "F8", status: 0 },
      { seatno: "F9", status: 0 },
      { seatno: "F10", status: 0 },
      { seatno: "F11", status: 0 },
      { seatno: "F12", status: 0 },
      { seatno: "F13", status: 0 },
      { seatno: "F14", status: 0 },
      { seatno: "F15", status: 0 },
      { seatno: "F16", status: 0 },
      { seatno: "F17", status: 0 },
      { seatno: "F18", status: 0 },
      { seatno: "F19", status: 0 },
      { seatno: "F20", status: 0 },
      { seatno: "F21", status: 0 },
      { seatno: "F22", status: 0 },
      { seatno: "F23", status: 0 },
      { seatno: "F24", status: 0 },
      { seatno: "F25", status: 0 },
      { seatno: "F26", status: 0 },
      { seatno: "F27", status: 0 },
      { seatno: "F28", status: 0 },
      { seatno: "F29", status: 0 },
      { seatno: "F30", status: 0 },
      { seatno: "G1", status: 0 },
      { seatno: "G2", status: 0 },
      { seatno: "G3", status: 0 },
      { seatno: "G4", status: 0 },
      { seatno: "G5", status: 0 },
      { seatno: "G6", status: 0 },
      { seatno: "G7", status: 0 },
      { seatno: "G8", status: 0 },
      { seatno: "G9", status: 0 },
      { seatno: "G10", status: 0 },
      { seatno: "G11", status: 0 },
      { seatno: "G12", status: 0 },
      { seatno: "G13", status: 0 },
      { seatno: "G14", status: 0 },
      { seatno: "G15", status: 0 },
      { seatno: "G16", status: 0 },
      { seatno: "G17", status: 0 },
      { seatno: "G18", status: 0 },
      { seatno: "G19", status: 0 },
      { seatno: "G20", status: 0 },
      { seatno: "G21", status: 0 },
      { seatno: "G22", status: 0 },
      { seatno: "G23", status: 0 },
      { seatno: "G24", status: 0 },
      { seatno: "G25", status: 0 },
      { seatno: "G26", status: 0 },
      { seatno: "G27", status: 0 },
      { seatno: "G28", status: 0 },
      { seatno: "G29", status: 0 },
      { seatno: "G30", status: 0 },
      { seatno: "H1", status: 0 },
      { seatno: "H2", status: 0 },
      { seatno: "H3", status: 0 },
      { seatno: "H4", status: 0 },
      { seatno: "H5", status: 0 },
      { seatno: "H6", status: 0 },
      { seatno: "H7", status: 0 },
      { seatno: "H8", status: 0 },
      { seatno: "H9", status: 0 },
      { seatno: "H10", status: 0 },
      { seatno: "H11", status: 0 },
      { seatno: "H12", status: 0 },
      { seatno: "H13", status: 0 },
      { seatno: "H14", status: 0 },
      { seatno: "H15", status: 0 },
      { seatno: "H16", status: 0 },
      { seatno: "H17", status: 0 },
      { seatno: "H18", status: 0 },
      { seatno: "H19", status: 0 },
      { seatno: "H20", status: 0 },
      { seatno: "H21", status: 0 },
      { seatno: "H22", status: 0 },
      { seatno: "H23", status: 0 },
      { seatno: "H24", status: 0 },
      { seatno: "H25", status: 0 },
      { seatno: "H26", status: 0 },
      { seatno: "H27", status: 0 },
      { seatno: "H28", status: 0 },
      { seatno: "H29", status: 0 },
      { seatno: "H30", status: 0 },
      { seatno: "I1", status: 0 },
      { seatno: "I2", status: 0 },
      { seatno: "I3", status: 0 },
      { seatno: "I4", status: 0 },
      { seatno: "I5", status: 0 },
      { seatno: "I6", status: 0 },
      { seatno: "I7", status: 0 },
      { seatno: "I8", status: 0 },
      { seatno: "I9", status: 0 },
      { seatno: "I10", status: 0 },
      { seatno: "I11", status: 0 },
      { seatno: "I12", status: 0 },
      { seatno: "I13", status: 0 },
      { seatno: "I14", status: 0 },
      { seatno: "I15", status: 0 },
      { seatno: "I16", status: 0 },
      { seatno: "I17", status: 0 },
      { seatno: "I18", status: 0 },
      { seatno: "I19", status: 0 },
      { seatno: "I20", status: 0 },
      { seatno: "I21", status: 0 },
      { seatno: "I22", status: 0 },
      { seatno: "I23", status: 0 },
      { seatno: "I24", status: 0 },
      { seatno: "I25", status: 0 },
      { seatno: "I26", status: 0 },
      { seatno: "I27", status: 0 },
      { seatno: "I28", status: 0 },
      { seatno: "I29", status: 0 },
      { seatno: "I30", status: 0 },
      { seatno: "J1", status: 0 },
      { seatno: "J2", status: 0 },
      { seatno: "J3", status: 0 },
      { seatno: "J4", status: 0 },
      { seatno: "J5", status: 0 },
      { seatno: "J6", status: 0 },
      { seatno: "J7", status: 0 },
      { seatno: "J8", status: 0 },
      { seatno: "J9", status: 0 },
      { seatno: "J10", status: 0 },
      { seatno: "J11", status: 0 },
      { seatno: "J12", status: 0 },
      { seatno: "J13", status: 0 },
      { seatno: "J14", status: 0 },
      { seatno: "J15", status: 0 },
      { seatno: "J16", status: 0 },
      { seatno: "J17", status: 0 },
      { seatno: "J18", status: 0 },
      { seatno: "J19", status: 0 },
      { seatno: "J20", status: 0 },
      { seatno: "J21", status: 0 },
      { seatno: "J22", status: 0 },
      { seatno: "J23", status: 0 },
      { seatno: "J24", status: 0 },
      { seatno: "J25", status: 0 },
      { seatno: "K1", status: 0 },
      { seatno: "K2", status: 0 },
      { seatno: "K3", status: 0 },
      { seatno: "K4", status: 0 },
      { seatno: "K5", status: 0 },
      { seatno: "K6", status: 0 },
      { seatno: "K7", status: 0 },
      { seatno: "K8", status: 0 },
      { seatno: "K9", status: 0 },
      { seatno: "K10", status: 0 },
      { seatno: "K11", status: 0 },
      { seatno: "K12", status: 0 },
      { seatno: "K13", status: 0 },
      { seatno: "K14", status: 0 },
      { seatno: "K15", status: 0 },
      { seatno: "K16", status: 0 },
      { seatno: "K17", status: 0 },
      { seatno: "K18", status: 0 },
      { seatno: "K19", status: 0 },
      { seatno: "K20", status: 0 },
      { seatno: "K21", status: 0 },
      { seatno: "K22", status: 0 },
      { seatno: "K23", status: 0 },
      { seatno: "K24", status: 0 },
      { seatno: "K25", status: 0 },
      { seatno: "L1", status: 0 },
      { seatno: "L2", status: 0 },
      { seatno: "L3", status: 0 },
      { seatno: "L4", status: 0 },
      { seatno: "L5", status: 0 },
      { seatno: "L6", status: 0 },
      { seatno: "L7", status: 0 },
      { seatno: "L8", status: 0 },
      { seatno: "L9", status: 0 },
      { seatno: "L10", status: 0 },
      { seatno: "L11", status: 0 },
      { seatno: "L12", status: 0 },
      { seatno: "L13", status: 0 },
      { seatno: "L14", status: 0 },
      { seatno: "L15", status: 0 },
      { seatno: "L16", status: 0 },
      { seatno: "L17", status: 0 },
      { seatno: "L18", status: 0 },
      { seatno: "L19", status: 0 },
      { seatno: "L20", status: 0 },
      { seatno: "L21", status: 0 },
      { seatno: "L22", status: 0 },
      { seatno: "L23", status: 0 },
      { seatno: "L24", status: 0 },
      { seatno: "L25", status: 0 },
      { seatno: "M1", status: 0 },
      { seatno: "M2", status: 0 },
      { seatno: "M3", status: 0 },
      { seatno: "M4", status: 0 },
      { seatno: "M5", status: 0 },
      { seatno: "M6", status: 0 },
      { seatno: "M7", status: 0 },
      { seatno: "M8", status: 0 },
      { seatno: "M9", status: 0 },
      { seatno: "M10", status: 0 },
      { seatno: "M11", status: 0 },
      { seatno: "M12", status: 0 },
      { seatno: "M13", status: 0 },
      { seatno: "M14", status: 0 },
      { seatno: "M15", status: 0 },
      { seatno: "M16", status: 0 },
      { seatno: "M17", status: 0 },
      { seatno: "M18", status: 0 },
      { seatno: "M19", status: 0 },
      { seatno: "M20", status: 0 },
      { seatno: "M21", status: 0 },
      { seatno: "M22", status: 0 },
      { seatno: "M23", status: 0 },
      { seatno: "M24", status: 0 },
      { seatno: "M25", status: 0 },
      { seatno: "N1", status: 0 },
      { seatno: "N2", status: 0 },
      { seatno: "N3", status: 0 },
      { seatno: "N4", status: 0 },
      { seatno: "N5", status: 0 },
      { seatno: "N6", status: 0 },
      { seatno: "N7", status: 0 },
      { seatno: "N8", status: 0 },
      { seatno: "N9", status: 0 },
      { seatno: "N10", status: 0 },
      { seatno: "N11", status: 0 },
      { seatno: "N12", status: 0 },
      { seatno: "N13", status: 0 },
      { seatno: "N14", status: 0 },
      { seatno: "N15", status: 0 },
      { seatno: "N16", status: 0 },
      { seatno: "N17", status: 0 },
      { seatno: "N18", status: 0 },
      { seatno: "N19", status: 0 },
      { seatno: "N20", status: 0 },
      { seatno: "N21", status: 0 },
      { seatno: "N22", status: 0 },
      { seatno: "N23", status: 0 },
      { seatno: "N24", status: 0 },
      { seatno: "N25", status: 0 },
      { seatno: "O1", status: 0 },
      { seatno: "O2", status: 0 },
      { seatno: "O3", status: 0 },
      { seatno: "O4", status: 0 },
      { seatno: "O5", status: 0 },
      { seatno: "O6", status: 0 },
      { seatno: "O7", status: 0 },
      { seatno: "O8", status: 0 },
      { seatno: "O9", status: 0 },
      { seatno: "O10", status: 0 },
      { seatno: "O11", status: 0 },
      { seatno: "O12", status: 0 },
      { seatno: "O13", status: 0 },
      { seatno: "O14", status: 0 },
      { seatno: "O15", status: 0 },
      { seatno: "O16", status: 0 },
      { seatno: "O17", status: 0 },
      { seatno: "O18", status: 0 },
      { seatno: "O19", status: 0 },
      { seatno: "O20", status: 0 },
      { seatno: "O21", status: 0 },
      { seatno: "O22", status: 0 },
      { seatno: "O23", status: 0 },
      { seatno: "O24", status: 0 },
      { seatno: "O25", status: 0 },
      { seatno: "P1", status: 0 },
      { seatno: "P2", status: 0 },
      { seatno: "P3", status: 0 },
      { seatno: "P4", status: 0 },
      { seatno: "P5", status: 0 },
      { seatno: "P6", status: 0 },
      { seatno: "P7", status: 0 },
      { seatno: "P8", status: 0 },
      { seatno: "P9", status: 0 },
      { seatno: "P10", status: 0 },
      { seatno: "P11", status: 0 },
      { seatno: "P12", status: 0 },
      { seatno: "P13", status: 0 },
      { seatno: "P14", status: 0 },
      { seatno: "P15", status: 0 },
      { seatno: "P16", status: 0 },
      { seatno: "P17", status: 0 },
      { seatno: "P18", status: 0 },
      { seatno: "P19", status: 0 },
      { seatno: "P20", status: 0 },
      { seatno: "P21", status: 0 },
      { seatno: "P22", status: 0 },
      { seatno: "P23", status: 0 },
      { seatno: "P24", status: 0 },
      { seatno: "P25", status: 0 }
    ],

    seatplan3: [
      { seatno: "A1", status: 0 },
      { seatno: "A2", status: 0 },
      { seatno: "A3", status: 0 },
      { seatno: "A4", status: 0 },
      { seatno: "A5", status: 0 },
      { seatno: "A6", status: 0 },
      { seatno: "A7", status: 0 },
      { seatno: "A8", status: 0 },
      { seatno: "A9", status: 0 },
      { seatno: "A10", status: 0 },
      { seatno: "A11", status: 0 },
      { seatno: "A12", status: 0 },
      { seatno: "A13", status: 0 },
      { seatno: "A14", status: 0 },
      { seatno: "A15", status: 0 },
      { seatno: "A16", status: 0 },
      { seatno: "A17", status: 0 },
      { seatno: "A18", status: 0 },
      { seatno: "A19", status: 0 },
      { seatno: "A20", status: 0 },
      { seatno: "A21", status: 0 },
      { seatno: "A22", status: 0 },
      { seatno: "A23", status: 0 },
      { seatno: "A24", status: 0 },
      { seatno: "A25", status: 0 },
      { seatno: "A26", status: 0 },
      { seatno: "A27", status: 0 },
      { seatno: "A28", status: 0 },
      { seatno: "A29", status: 0 },
      { seatno: "A30", status: 0 },
      { seatno: "A31", status: 0 },
      { seatno: "A32", status: 0 },
      { seatno: "A33", status: 0 },
      { seatno: "A34", status: 0 },
      { seatno: "A35", status: 0 },
      { seatno: "A36", status: 0 },
      { seatno: "A37", status: 0 },
      { seatno: "A38", status: 0 },
      { seatno: "A39", status: 0 },
      { seatno: "A40", status: 0 },
      { seatno: "B1", status: 0 },
      { seatno: "B2", status: 0 },
      { seatno: "B3", status: 0 },
      { seatno: "B4", status: 0 },
      { seatno: "B5", status: 0 },
      { seatno: "B6", status: 0 },
      { seatno: "B7", status: 0 },
      { seatno: "B8", status: 0 },
      { seatno: "B9", status: 0 },
      { seatno: "B10", status: 0 },
      { seatno: "B11", status: 0 },
      { seatno: "B12", status: 0 },
      { seatno: "B13", status: 0 },
      { seatno: "B14", status: 0 },
      { seatno: "B15", status: 0 },
      { seatno: "B16", status: 0 },
      { seatno: "B17", status: 0 },
      { seatno: "B18", status: 0 },
      { seatno: "B19", status: 0 },
      { seatno: "B20", status: 0 },
      { seatno: "B21", status: 0 },
      { seatno: "B22", status: 0 },
      { seatno: "B23", status: 0 },
      { seatno: "B24", status: 0 },
      { seatno: "B25", status: 0 },
      { seatno: "B26", status: 0 },
      { seatno: "B27", status: 0 },
      { seatno: "B28", status: 0 },
      { seatno: "B29", status: 0 },
      { seatno: "B30", status: 0 },
      { seatno: "B1", status: 0 },
      { seatno: "B32", status: 0 },
      { seatno: "B33", status: 0 },
      { seatno: "B34", status: 0 },
      { seatno: "B35", status: 0 },
      { seatno: "B36", status: 0 },
      { seatno: "B37", status: 0 },
      { seatno: "B38", status: 0 },
      { seatno: "B39", status: 0 },
      { seatno: "B40", status: 0 },
      { seatno: "C1", status: 0 },
      { seatno: "C2", status: 0 },
      { seatno: "C3", status: 0 },
      { seatno: "C4", status: 0 },
      { seatno: "C5", status: 0 },
      { seatno: "C6", status: 0 },
      { seatno: "C7", status: 0 },
      { seatno: "C8", status: 0 },
      { seatno: "C9", status: 0 },
      { seatno: "C10", status: 0 },
      { seatno: "C11", status: 0 },
      { seatno: "C12", status: 0 },
      { seatno: "C13", status: 0 },
      { seatno: "C14", status: 0 },
      { seatno: "C15", status: 0 },
      { seatno: "C16", status: 0 },
      { seatno: "C17", status: 0 },
      { seatno: "C18", status: 0 },
      { seatno: "C19", status: 0 },
      { seatno: "C20", status: 0 },
      { seatno: "C21", status: 0 },
      { seatno: "C22", status: 0 },
      { seatno: "C23", status: 0 },
      { seatno: "C24", status: 0 },
      { seatno: "C25", status: 0 },
      { seatno: "C26", status: 0 },
      { seatno: "C27", status: 0 },
      { seatno: "C28", status: 0 },
      { seatno: "C29", status: 0 },
      { seatno: "C30", status: 0 },
      { seatno: "C31", status: 0 },
      { seatno: "C32", status: 0 },
      { seatno: "C33", status: 0 },
      { seatno: "C34", status: 0 },
      { seatno: "C35", status: 0 },
      { seatno: "C36", status: 0 },
      { seatno: "C37", status: 0 },
      { seatno: "C38", status: 0 },
      { seatno: "C39", status: 0 },
      { seatno: "C40", status: 0 },
      { seatno: "D1", status: 0 },
      { seatno: "D2", status: 0 },
      { seatno: "D3", status: 0 },
      { seatno: "D4", status: 0 },
      { seatno: "D5", status: 0 },
      { seatno: "D6", status: 0 },
      { seatno: "D7", status: 0 },
      { seatno: "D8", status: 0 },
      { seatno: "D9", status: 0 },
      { seatno: "D10", status: 0 },
      { seatno: "D11", status: 0 },
      { seatno: "D12", status: 0 },
      { seatno: "D13", status: 0 },
      { seatno: "D14", status: 0 },
      { seatno: "D15", status: 0 },
      { seatno: "D16", status: 0 },
      { seatno: "D17", status: 0 },
      { seatno: "D18", status: 0 },
      { seatno: "D19", status: 0 },
      { seatno: "D20", status: 0 },
      { seatno: "D21", status: 0 },
      { seatno: "D22", status: 0 },
      { seatno: "D23", status: 0 },
      { seatno: "D24", status: 0 },
      { seatno: "D25", status: 0 },
      { seatno: "D26", status: 0 },
      { seatno: "D27", status: 0 },
      { seatno: "D28", status: 0 },
      { seatno: "D29", status: 0 },
      { seatno: "D30", status: 0 },
      { seatno: "D31", status: 0 },
      { seatno: "D32", status: 0 },
      { seatno: "D33", status: 0 },
      { seatno: "D34", status: 0 },
      { seatno: "D35", status: 0 },
      { seatno: "D36", status: 0 },
      { seatno: "D37", status: 0 },
      { seatno: "D38", status: 0 },
      { seatno: "D39", status: 0 },
      { seatno: "D40", status: 0 },
      { seatno: "E1", status: 0 },
      { seatno: "E2", status: 0 },
      { seatno: "E3", status: 0 },
      { seatno: "E4", status: 0 },
      { seatno: "E5", status: 0 },
      { seatno: "E6", status: 0 },
      { seatno: "E7", status: 0 },
      { seatno: "E8", status: 0 },
      { seatno: "E9", status: 0 },
      { seatno: "E10", status: 0 },
      { seatno: "E11", status: 0 },
      { seatno: "E12", status: 0 },
      { seatno: "E13", status: 0 },
      { seatno: "E14", status: 0 },
      { seatno: "E15", status: 0 },
      { seatno: "E16", status: 0 },
      { seatno: "E17", status: 0 },
      { seatno: "E18", status: 0 },
      { seatno: "E19", status: 0 },
      { seatno: "E20", status: 0 },
      { seatno: "E21", status: 0 },
      { seatno: "E22", status: 0 },
      { seatno: "E23", status: 0 },
      { seatno: "E24", status: 0 },
      { seatno: "E25", status: 0 },
      { seatno: "E26", status: 0 },
      { seatno: "E27", status: 0 },
      { seatno: "E28", status: 0 },
      { seatno: "E29", status: 0 },
      { seatno: "E30", status: 0 },
      { seatno: "E31", status: 0 },
      { seatno: "E32", status: 0 },
      { seatno: "E33", status: 0 },
      { seatno: "E34", status: 0 },
      { seatno: "E35", status: 0 },
      { seatno: "E36", status: 0 },
      { seatno: "E37", status: 0 },
      { seatno: "E38", status: 0 },
      { seatno: "E39", status: 0 },
      { seatno: "E40", status: 0 },
      { seatno: "F1", status: 0 },
      { seatno: "F2", status: 0 },
      { seatno: "F3", status: 0 },
      { seatno: "F4", status: 0 },
      { seatno: "F5", status: 0 },
      { seatno: "F6", status: 0 },
      { seatno: "F7", status: 0 },
      { seatno: "F8", status: 0 },
      { seatno: "F9", status: 0 },
      { seatno: "F10", status: 0 },
      { seatno: "F11", status: 0 },
      { seatno: "F12", status: 0 },
      { seatno: "F13", status: 0 },
      { seatno: "F14", status: 0 },
      { seatno: "F15", status: 0 },
      { seatno: "F16", status: 0 },
      { seatno: "F17", status: 0 },
      { seatno: "F18", status: 0 },
      { seatno: "F19", status: 0 },
      { seatno: "F20", status: 0 },
      { seatno: "F21", status: 0 },
      { seatno: "F22", status: 0 },
      { seatno: "F23", status: 0 },
      { seatno: "F24", status: 0 },
      { seatno: "F25", status: 0 },
      { seatno: "F26", status: 0 },
      { seatno: "F27", status: 0 },
      { seatno: "F28", status: 0 },
      { seatno: "F29", status: 0 },
      { seatno: "F30", status: 0 },
      { seatno: "F31", status: 0 },
      { seatno: "F32", status: 0 },
      { seatno: "F33", status: 0 },
      { seatno: "F34", status: 0 },
      { seatno: "F35", status: 0 },
      { seatno: "F36", status: 0 },
      { seatno: "F37", status: 0 },
      { seatno: "F38", status: 0 },
      { seatno: "F39", status: 0 },
      { seatno: "F40", status: 0 },

      { seatno: "G1", status: 0 },
      { seatno: "G2", status: 0 },
      { seatno: "G3", status: 0 },
      { seatno: "G4", status: 0 },
      { seatno: "G5", status: 0 },
      { seatno: "G6", status: 0 },
      { seatno: "G7", status: 0 },
      { seatno: "G8", status: 0 },
      { seatno: "G9", status: 0 },
      { seatno: "G10", status: 0 },
      { seatno: "G11", status: 0 },
      { seatno: "G12", status: 0 },
      { seatno: "G13", status: 0 },
      { seatno: "G14", status: 0 },
      { seatno: "G15", status: 0 },
      { seatno: "G16", status: 0 },
      { seatno: "G17", status: 0 },
      { seatno: "G18", status: 0 },
      { seatno: "G19", status: 0 },
      { seatno: "G20", status: 0 },
      { seatno: "G21", status: 0 },
      { seatno: "G22", status: 0 },
      { seatno: "G23", status: 0 },
      { seatno: "G24", status: 0 },
      { seatno: "G25", status: 0 },
      { seatno: "G26", status: 0 },
      { seatno: "G27", status: 0 },
      { seatno: "G28", status: 0 },
      { seatno: "G29", status: 0 },
      { seatno: "G30", status: 0 },
      { seatno: "G31", status: 0 },
      { seatno: "G32", status: 0 },
      { seatno: "G33", status: 0 },
      { seatno: "G34", status: 0 },
      { seatno: "G35", status: 0 },
      { seatno: "G36", status: 0 },
      { seatno: "G37", status: 0 },
      { seatno: "G38", status: 0 },
      { seatno: "G39", status: 0 },
      { seatno: "G40", status: 0 },

      { seatno: "H1", status: 0 },
      { seatno: "H2", status: 0 },
      { seatno: "H3", status: 0 },
      { seatno: "H4", status: 0 },
      { seatno: "H5", status: 0 },
      { seatno: "H6", status: 0 },
      { seatno: "H7", status: 0 },
      { seatno: "H8", status: 0 },
      { seatno: "H9", status: 0 },
      { seatno: "H10", status: 0 },
      { seatno: "H11", status: 0 },
      { seatno: "H12", status: 0 },
      { seatno: "H13", status: 0 },
      { seatno: "H14", status: 0 },
      { seatno: "H15", status: 0 },
      { seatno: "H16", status: 0 },
      { seatno: "H17", status: 0 },
      { seatno: "H18", status: 0 },
      { seatno: "H19", status: 0 },
      { seatno: "H20", status: 0 },
      { seatno: "H21", status: 0 },
      { seatno: "H22", status: 0 },
      { seatno: "H23", status: 0 },
      { seatno: "H24", status: 0 },
      { seatno: "H25", status: 0 },
      { seatno: "H26", status: 0 },
      { seatno: "H27", status: 0 },
      { seatno: "H28", status: 0 },
      { seatno: "H29", status: 0 },
      { seatno: "H30", status: 0 },
      { seatno: "H31", status: 0 },
      { seatno: "H32", status: 0 },
      { seatno: "H33", status: 0 },
      { seatno: "H34", status: 0 },
      { seatno: "H35", status: 0 },
      { seatno: "H36", status: 0 },
      { seatno: "H37", status: 0 },
      { seatno: "H38", status: 0 },
      { seatno: "H39", status: 0 },
      { seatno: "H40", status: 0 },
      { seatno: "I1", status: 0 },
      { seatno: "I2", status: 0 },
      { seatno: "I3", status: 0 },
      { seatno: "I4", status: 0 },
      { seatno: "I5", status: 0 },
      { seatno: "I6", status: 0 },
      { seatno: "I7", status: 0 },
      { seatno: "I8", status: 0 },
      { seatno: "I9", status: 0 },
      { seatno: "I10", status: 0 },
      { seatno: "I11", status: 0 },
      { seatno: "I12", status: 0 },
      { seatno: "I13", status: 0 },
      { seatno: "I14", status: 0 },
      { seatno: "I15", status: 0 },
      { seatno: "I16", status: 0 },
      { seatno: "I17", status: 0 },
      { seatno: "I18", status: 0 },
      { seatno: "I19", status: 0 },
      { seatno: "I20", status: 0 },
      { seatno: "I21", status: 0 },
      { seatno: "I22", status: 0 },
      { seatno: "I23", status: 0 },
      { seatno: "I24", status: 0 },
      { seatno: "I25", status: 0 },
      { seatno: "I26", status: 0 },
      { seatno: "I27", status: 0 },
      { seatno: "I28", status: 0 },
      { seatno: "I29", status: 0 },
      { seatno: "I30", status: 0 },
      { seatno: "I31", status: 0 },
      { seatno: "I32", status: 0 },
      { seatno: "I33", status: 0 },
      { seatno: "I34", status: 0 },
      { seatno: "I35", status: 0 },
      { seatno: "I36", status: 0 },
      { seatno: "I37", status: 0 },
      { seatno: "I38", status: 0 },
      { seatno: "I39", status: 0 },
      { seatno: "I40", status: 0 },
      { seatno: "J1", status: 0 },
      { seatno: "J2", status: 0 },
      { seatno: "J3", status: 0 },
      { seatno: "J4", status: 0 },
      { seatno: "J5", status: 0 },
      { seatno: "J6", status: 0 },
      { seatno: "J7", status: 0 },
      { seatno: "J8", status: 0 },
      { seatno: "J9", status: 0 },
      { seatno: "J10", status: 0 },
      { seatno: "J11", status: 0 },
      { seatno: "J12", status: 0 },
      { seatno: "J13", status: 0 },
      { seatno: "J14", status: 0 },
      { seatno: "J15", status: 0 },
      { seatno: "J16", status: 0 },
      { seatno: "J17", status: 0 },
      { seatno: "J18", status: 0 },
      { seatno: "J19", status: 0 },
      { seatno: "J20", status: 0 },
      { seatno: "J21", status: 0 },
      { seatno: "J22", status: 0 },
      { seatno: "J23", status: 0 },
      { seatno: "J24", status: 0 },
      { seatno: "J25", status: 0 },
      { seatno: "J26", status: 0 },
      { seatno: "J27", status: 0 },
      { seatno: "J28", status: 0 },
      { seatno: "J29", status: 0 },
      { seatno: "J30", status: 0 },
      { seatno: "J31", status: 0 },
      { seatno: "J32", status: 0 },
      { seatno: "J33", status: 0 },
      { seatno: "J34", status: 0 },
      { seatno: "J35", status: 0 },
      { seatno: "J36", status: 0 },
      { seatno: "J37", status: 0 },
      { seatno: "J38", status: 0 },
      { seatno: "J39", status: 0 },
      { seatno: "J40", status: 0 },

      { seatno: "K1", status: 0 },
      { seatno: "K2", status: 0 },
      { seatno: "K3", status: 0 },
      { seatno: "K4", status: 0 },
      { seatno: "K5", status: 0 },
      { seatno: "K6", status: 0 },
      { seatno: "K7", status: 0 },
      { seatno: "K8", status: 0 },
      { seatno: "K9", status: 0 },
      { seatno: "K10", status: 0 },
      { seatno: "K11", status: 0 },
      { seatno: "K12", status: 0 },
      { seatno: "K13", status: 0 },
      { seatno: "K14", status: 0 },
      { seatno: "K15", status: 0 },
      { seatno: "K16", status: 0 },
      { seatno: "K17", status: 0 },
      { seatno: "K18", status: 0 },
      { seatno: "K19", status: 0 },
      { seatno: "K20", status: 0 },
      { seatno: "K21", status: 0 },
      { seatno: "K22", status: 0 },
      { seatno: "K23", status: 0 },
      { seatno: "K24", status: 0 },
      { seatno: "K25", status: 0 },
      { seatno: "K26", status: 0 },
      { seatno: "K27", status: 0 },
      { seatno: "K28", status: 0 },
      { seatno: "K29", status: 0 },
      { seatno: "K30", status: 0 },
      { seatno: "K31", status: 0 },
      { seatno: "K32", status: 0 },
      { seatno: "K33", status: 0 },
      { seatno: "K34", status: 0 },
      { seatno: "K35", status: 0 },
      { seatno: "K36", status: 0 },
      { seatno: "K37", status: 0 },
      { seatno: "K38", status: 0 },
      { seatno: "K39", status: 0 },
      { seatno: "K40", status: 0 },

      { seatno: "L1", status: 0 },
      { seatno: "L2", status: 0 },
      { seatno: "L3", status: 0 },
      { seatno: "L4", status: 0 },
      { seatno: "L5", status: 0 },
      { seatno: "L6", status: 0 },
      { seatno: "L7", status: 0 },
      { seatno: "L8", status: 0 },
      { seatno: "L9", status: 0 },
      { seatno: "L10", status: 0 },
      { seatno: "L11", status: 0 },
      { seatno: "L12", status: 0 },
      { seatno: "L13", status: 0 },
      { seatno: "L14", status: 0 },
      { seatno: "L15", status: 0 },
      { seatno: "L16", status: 0 },
      { seatno: "L17", status: 0 },
      { seatno: "L18", status: 0 },
      { seatno: "L19", status: 0 },
      { seatno: "L20", status: 0 },
      { seatno: "L21", status: 0 },
      { seatno: "L22", status: 0 },
      { seatno: "L23", status: 0 },
      { seatno: "L24", status: 0 },
      { seatno: "L25", status: 0 },
      { seatno: "L26", status: 0 },
      { seatno: "L27", status: 0 },
      { seatno: "L28", status: 0 },
      { seatno: "L29", status: 0 },
      { seatno: "L30", status: 0 },
      { seatno: "L31", status: 0 },
      { seatno: "L32", status: 0 },
      { seatno: "L33", status: 0 },
      { seatno: "L34", status: 0 },
      { seatno: "L35", status: 0 },
      { seatno: "L36", status: 0 },
      { seatno: "L37", status: 0 },
      { seatno: "L38", status: 0 },
      { seatno: "L39", status: 0 },
      { seatno: "L40", status: 0 },

      { seatno: "M1", status: 0 },
      { seatno: "M2", status: 0 },
      { seatno: "M3", status: 0 },
      { seatno: "M4", status: 0 },
      { seatno: "M5", status: 0 },
      { seatno: "M6", status: 0 },
      { seatno: "M7", status: 0 },
      { seatno: "M8", status: 0 },
      { seatno: "M9", status: 0 },
      { seatno: "M10", status: 0 },
      { seatno: "M11", status: 0 },
      { seatno: "M12", status: 0 },
      { seatno: "M13", status: 0 },
      { seatno: "M14", status: 0 },
      { seatno: "M15", status: 0 },
      { seatno: "M16", status: 0 },
      { seatno: "M17", status: 0 },
      { seatno: "M18", status: 0 },
      { seatno: "M19", status: 0 },
      { seatno: "M20", status: 0 },
      { seatno: "M21", status: 0 },
      { seatno: "M22", status: 0 },
      { seatno: "M23", status: 0 },
      { seatno: "M24", status: 0 },
      { seatno: "M25", status: 0 },
      { seatno: "M26", status: 0 },
      { seatno: "M27", status: 0 },
      { seatno: "M28", status: 0 },
      { seatno: "M29", status: 0 },
      { seatno: "M30", status: 0 },
      { seatno: "M31", status: 0 },
      { seatno: "M32", status: 0 },
      { seatno: "M33", status: 0 },
      { seatno: "M34", status: 0 },
      { seatno: "M35", status: 0 },
      { seatno: "M36", status: 0 },
      { seatno: "M37", status: 0 },
      { seatno: "M38", status: 0 },
      { seatno: "M39", status: 0 },
      { seatno: "M40", status: 0 },

      { seatno: "N1", status: 0 },
      { seatno: "N2", status: 0 },
      { seatno: "N3", status: 0 },
      { seatno: "N4", status: 0 },
      { seatno: "N5", status: 0 },
      { seatno: "N6", status: 0 },
      { seatno: "N7", status: 0 },
      { seatno: "N8", status: 0 },
      { seatno: "N9", status: 0 },
      { seatno: "N10", status: 0 },
      { seatno: "N11", status: 0 },
      { seatno: "N12", status: 0 },
      { seatno: "N13", status: 0 },
      { seatno: "N14", status: 0 },
      { seatno: "N15", status: 0 },
      { seatno: "N16", status: 0 },
      { seatno: "N17", status: 0 },
      { seatno: "N18", status: 0 },
      { seatno: "N19", status: 0 },
      { seatno: "N20", status: 0 },
      { seatno: "N21", status: 0 },
      { seatno: "N22", status: 0 },
      { seatno: "N23", status: 0 },
      { seatno: "N24", status: 0 },
      { seatno: "N25", status: 0 },
      { seatno: "N26", status: 0 },
      { seatno: "N27", status: 0 },
      { seatno: "N28", status: 0 },
      { seatno: "N29", status: 0 },
      { seatno: "N30", status: 0 },
      { seatno: "N31", status: 0 },
      { seatno: "N32", status: 0 },
      { seatno: "N33", status: 0 },
      { seatno: "N34", status: 0 },
      { seatno: "N35", status: 0 },
      { seatno: "N36", status: 0 },
      { seatno: "N37", status: 0 },
      { seatno: "N38", status: 0 },
      { seatno: "N39", status: 0 },
      { seatno: "N40", status: 0 }
    ]
  };

  statusChange = (row, seatno) => {
    let p = 0;

    for (var i = 0; i < this.state.seatplan1[row].length; i++) {
      if (this.state.seatplan1[row][i]["seatno"] == seatno) {
        p = i;
        break;
      }
    }

    console.log(p);

    if (this.state.seatplan1[row][p]["status"] == 2) {
    } else if (this.state.seatplan1[row][p]["status"] == 1) {
      let a = this.state.seatplan1;
      a[row][p]["status"] = 0;
      a[row][p]["bgColor"] = "#404048de";
      this.setState({ seatplan1: a });
      this.setState({ totalprice: this.state.totalprice - 150 });
      this.setState({ noofseatsbooked: this.state.noofseatsbooked - 1 });
    } else if (this.state.seatplan1[row][p]["status"] == 0) {
      let a = this.state.seatplan1;
      a[row][p]["status"] = 1;
      a[row][p]["bgColor"] = "rgb(239, 176, 34)";
      this.setState({ seatplan1: a });
      this.setState({ totalprice: this.state.totalprice + 150 });
      this.setState({ noofseatsbooked: this.state.noofseatsbooked + 1 });
    }
  };

  carryForward = () => {
    let rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"];
    let selectedseats = [];

    let count = 0;

    for (var i = 0; i < rows.length; i++) {
      let currow = "row" + rows[i];

      for (var j = 0; j < this.state.seatplan1[currow].length; j++) {
        if (this.state.seatplan1[currow][j]["status"] == 1) {
          count = count + 1;
          selectedseats = [
            ...selectedseats,
            this.state.seatplan1[currow][j]["seatno"]
          ];
        }
      }
    }

    console.log(count);
    console.log(selectedseats);

    if (count == 0) {
      this.props.createMessage({
        noseatselected: "You need to select at least 1 seat to continue booking"
      });
    } else {
      this.props.getSelectedSeats(selectedseats);
    }
  };
  render() {
    let { seatplanning } = this.state.seatplan1;

    let rows = 12;

    console.log(this.props.seatsbooked);
    console.log(this.props.showdetails);

    if (this.props.seatsbooked) {
      this.changeStatusseatsBooked.bind(this, 23);
      console.log("hi");
    }

    // :show_id/:theatre_id/:city/:theatre_name

    let { show_id, theatre_id, city, theatre_name } = this.props.match.params;

    console.log(theatre_name);

    return (
      <div style={{ backgroundColor: "#404048de", height: "1080px" }}>
        <div style={{ float: "left" }}>
          <table className="grid">
            <tr>
              <td>A</td>
            </tr>
            <tr>
              <td>B</td>
            </tr>
            <tr>
              <td>C</td>
            </tr>
            <tr>
              <td>D</td>
            </tr>
            <tr>
              <td>E</td>
            </tr>
            <tr>
              <td>F</td>
            </tr>
            <tr>
              <td>G</td>
            </tr>
            <tr>
              <td>H</td>
            </tr>
            <tr>
              <td>I</td>
            </tr>
            <tr>
              <td>J</td>
            </tr>
            <tr>
              <td>K</td>
            </tr>
            <tr>
              <td>L</td>
            </tr>
          </table>
        </div>
        <div style={{ paddingLeft: "15%" }}>
          <table className="grid">
            <tbody>
              <tr>
                {this.state.seatplan1.rowA.map(seat => (
                  <td
                    key={seat.seatno.slice(1)}
                    style={{ backgroundColor: seat.bgColor }}
                    onClick={this.statusChange.bind(this, "rowA", seat.seatno)}
                  >
                    {seat.seatno.slice(1)}
                  </td>
                ))}
              </tr>
              <center>
                <tr>
                  {this.state.seatplan1.rowB.map(seat => (
                    <td
                      key={seat.seatno.slice(1)}
                      style={{ backgroundColor: seat.bgColor }}
                      onClick={this.statusChange.bind(
                        this,
                        "rowB",
                        seat.seatno
                      )}
                    >
                      {seat.seatno.slice(1)}
                    </td>
                  ))}
                </tr>
              </center>
              <center>
                <tr>
                  {this.state.seatplan1.rowC.map(seat => (
                    <td
                      key={seat.seatno.slice(1)}
                      style={{ backgroundColor: seat.bgColor }}
                      onClick={this.statusChange.bind(
                        this,
                        "rowC",
                        seat.seatno
                      )}
                    >
                      {seat.seatno.slice(1)}
                    </td>
                  ))}
                </tr>
              </center>
              <center>
                <tr>
                  {this.state.seatplan1.rowD.map(seat => (
                    <td
                      key={seat.seatno.slice(1)}
                      style={{ backgroundColor: seat.bgColor }}
                      onClick={this.statusChange.bind(
                        this,
                        "rowD",
                        seat.seatno
                      )}
                    >
                      {seat.seatno.slice(1)}
                    </td>
                  ))}
                </tr>
              </center>
              <center>
                <tr>
                  {this.state.seatplan1.rowE.map(seat => (
                    <td
                      key={seat.seatno.slice(1)}
                      style={{ backgroundColor: seat.bgColor }}
                      onClick={this.statusChange.bind(
                        this,
                        "rowE",
                        seat.seatno
                      )}
                    >
                      {seat.seatno.slice(1)}
                    </td>
                  ))}
                </tr>
              </center>
              <center>
                <tr>
                  {this.state.seatplan1.rowF.map(seat => (
                    <td
                      key={seat.seatno.slice(1)}
                      style={{ backgroundColor: seat.bgColor }}
                      onClick={this.statusChange.bind(
                        this,
                        "rowF",
                        seat.seatno
                      )}
                    >
                      {seat.seatno.slice(1)}
                    </td>
                  ))}
                </tr>
              </center>
              <center>
                <tr>
                  {this.state.seatplan1.rowG.map(seat => (
                    <td
                      key={seat.seatno.slice(1)}
                      style={{ backgroundColor: seat.bgColor }}
                      onClick={this.statusChange.bind(
                        this,
                        "rowG",
                        seat.seatno
                      )}
                    >
                      {seat.seatno.slice(1)}
                    </td>
                  ))}
                </tr>
              </center>
              <center>
                <tr>
                  {this.state.seatplan1.rowH.map(seat => (
                    <td
                      key={seat.seatno.slice(1)}
                      style={{ backgroundColor: seat.bgColor }}
                      onClick={this.statusChange.bind(
                        this,
                        "rowH",
                        seat.seatno
                      )}
                    >
                      {seat.seatno.slice(1)}
                    </td>
                  ))}
                </tr>
              </center>
              <center>
                <tr>
                  {this.state.seatplan1.rowI.map(seat => (
                    <td
                      key={seat.seatno.slice(1)}
                      style={{ backgroundColor: seat.bgColor }}
                      onClick={this.statusChange.bind(
                        this,
                        "rowI",
                        seat.seatno
                      )}
                    >
                      {seat.seatno.slice(1)}
                    </td>
                  ))}
                </tr>
              </center>
              <center>
                <tr>
                  {this.state.seatplan1.rowJ.map(seat => (
                    <td
                      key={seat.seatno.slice(1)}
                      style={{ backgroundColor: seat.bgColor }}
                      onClick={this.statusChange.bind(
                        this,
                        "rowJ",
                        seat.seatno
                      )}
                    >
                      {seat.seatno.slice(1)}
                    </td>
                  ))}
                </tr>
              </center>
              <center>
                <tr>
                  {this.state.seatplan1.rowK.map(seat => (
                    <td
                      key={seat.seatno.slice(1)}
                      style={{ backgroundColor: seat.bgColor }}
                      onClick={this.statusChange.bind(
                        this,
                        "rowK",
                        seat.seatno
                      )}
                    >
                      {seat.seatno.slice(1)}
                    </td>
                  ))}
                </tr>
              </center>
              <center>
                <tr>
                  {this.state.seatplan1.rowL.map(seat => (
                    <td
                      key={seat.seatno.slice(1)}
                      style={{ backgroundColor: seat.bgColor }}
                      onClick={this.statusChange.bind(
                        this,
                        "rowL",
                        seat.seatno
                      )}
                    >
                      {seat.seatno.slice(1)}
                    </td>
                  ))}
                </tr>
              </center>
            </tbody>
          </table>
        </div>
        <div
          className="container"
          style={{ minHeight: "300px", marginTop: "40px", marginLeft: "276px" }}
        >
          <div className="row">
            <div className="col-sm-12 entryexit">
              <table style={{ width: "115%", height: "50px" }}>
                <tbody>
                  <tr>
                    <td style={{ float: "left" }}>
                      <div
                        style={{
                          height: "80px",
                          color: "white",
                          backgroundColor: "grey",
                          width: "40px",
                          textAlign: "center",
                          paddingTop: "30px",
                          fontWeight: "bolder"
                        }}
                      >
                        Exit
                      </div>
                    </td>
                    <td style={{ float: "right" }}>
                      <div
                        style={{
                          height: "80px",
                          color: "white",
                          backgroundColor: "grey",
                          width: "40px",
                          textAlign: "center",
                          paddingTop: "30px",
                          fontWeight: "bolder"
                        }}
                      >
                        Exit
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div className="row " style={{ paddingLeft: "160px" }}>
            <div
              className="col-sm-12 "
              style={{
                height: "20px",
                backgroundColor: "#f1d581",
                textAlign: "center",
                color: "dark",
                fontWeight: "bold"
              }}
            >
              Screen this side
            </div>
          </div>
          <div className="row" style={{ paddingLeft: "160px" }}>
            <div
              className="col-sm-12"
              style={{
                height: "50px",
                backgroundColor: "white",
                textAlign: "center",
                color: "dark",
                fontWeight: "bold",
                marginTop: "50px",
                padding: "15px"
              }}
            >
              totalprice:&nbsp;{this.state.totalprice} &nbsp;&nbsp;&nbsp;
              noofseats:&nbsp;
              {this.state.noofseatsbooked}
            </div>
          </div>
          <div className="row " style={{ paddingLeft: "160px" }}>
            <div
              className="col-sm-12 "
              style={{
                height: "100px",
                textAlign: "center",
                paddingLeft: "2%",
                paddingTop: "30px"
              }}
            >
              <button
                className="submit1"
                style={{
                  height: "50px",
                  width: "187px",
                  padding: "10px",
                  backgroundColor: "#f57a15",
                  color: "white",
                  fontWeight: "bolder",
                  borderRadius: "7px"
                }}
                onClick={this.carryForward}
              >
                <Link
                  to={`/snacks/${city}/${theatre_name}/${
                    this.state.totalprice
                  }`}
                  style={{
                    textDecoration: "none",
                    color: "white",
                    cursor: "pointer"
                  }}
                >
                  Book tickets
                </Link>
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  showdetails: state.showdetails.showdetails,
  seatsbooked: state.seatsbooked.seatsbooked,
  selectedseats: state.selectedseats.selectedseats
});

export default ReactTimeout(
  connect(
    mapStateToProps,
    { getShowDetails, getSeatsBooked, getSelectedSeats, createMessage }
  )(seats)
);
