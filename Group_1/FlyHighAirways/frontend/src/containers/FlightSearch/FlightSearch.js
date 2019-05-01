import React, { Component } from "react";

import { Row, Col } from "antd";
import axios from "axios";

import Flights from "../../components/Flights/Flights";
import FlightFilter from "../../components/FlightFilter/FlightFilter";

import CustomSkeleton from "../../components/UI/Skeleton/Skeleton";
import { getTimeSlot } from "./utils";

import { withRouter } from "react-router-dom";
import { connect } from "react-redux";

import classes from "./FlightSearch.module.css";

import Paypal from "../../components/Paypal/Paypal";
import FlightForm from "../../components/FlightForm/FlightForm";

class FlightSearch extends Component {
  state = {
    loading: true,
    flights: [
      {
        id: 1,
        date: "21/04/2019",
        source: "Kolkata",
        destination: "Mumbai",
        economy: {
          fare: 4563,
          seats_remaining: 3
        },
        start_time: "03:45",
        end_time: "05:00"
      }
    ],

    filterInfo: {
      flightType: 3,
      priceRange: 9000,
      flightTime: {
        morning: true,
        afternoon: true,
        evening: true,
        night: true
      }
    }
  };

  // Check If user has clicked any of 1)Non-Stop 2)Stop
  onFlightTypeChangeHandler = event => {
    const updatedFilterInfo = { ...this.state.filterInfo };

    updatedFilterInfo.flightType = event.target.value;
    this.setState({ filterInfo: updatedFilterInfo });
  };

  // Utility function to filter Flight Type
  filterType = (flightList, value) => {
    if (value === 1) {
      return flightList.filter(flight => flight.nonStop);
    } else if (value === 2) {
      return flightList.filter(flight => !flight.nonStop);
    }
    return flightList;
  };

  // Utility function to filter by price range
  filterPrice = (flightList, price) => {
    return flightList.filter(flight => flight.economy.fare < price);
  };

  // Utility function to filter by flight time
  filterTime = (flightList, timeListObject) => {
    return flightList.filter(flight => {
      const time = getTimeSlot(flight.start_time.split(":")[0]);
      return timeListObject[time] ? true : false;
    });
  };

  // Utility function to filter by location props
  filterByLocation = (flightList, locations) => {
    return flightList.filter(flight => {
      return (
        (flight.source.toLowerCase() === locations.source.toLowerCase() &&
          flight.destination.toLowerCase() ===
            locations.destination.toLowerCase()) ||
        locations.source === ""
      );
    });
  };

  filterFlights = filterInfo => {
    // const { flights } = this.state;

    let flightArray = this.state.flights;

    // for (let flight in flights) {
    //   flightArray.push(flights[flight]);
    // }

    // Fliter by location
    flightArray = this.filterByLocation(flightArray, this.props.flightInfo);

    // Filter Non-Stop, Stop
    flightArray = this.filterType(flightArray, filterInfo.flightType);

    // Filter By Price
    flightArray = this.filterPrice(flightArray, filterInfo.priceRange);

    // Filter By Time of the Day
    flightArray = this.filterTime(flightArray, filterInfo.flightTime);
    return flightArray;
  };

  onFlightPriceChangeHandler = event => {
    const updatedFilterInfo = { ...this.state.filterInfo };

    updatedFilterInfo.priceRange = event.target.value;
    this.setState({ filterInfo: updatedFilterInfo });
  };

  onFlightTimeChangeHandler = timeSlot => {
    const updatedFilterInfo = { ...this.state.filterInfo };

    const updatedFlightTime = { ...this.state.filterInfo.flightTime };
    updatedFlightTime[timeSlot] = !updatedFlightTime[timeSlot];
    updatedFilterInfo.flightTime = updatedFlightTime;

    this.setState({ filterInfo: updatedFilterInfo });
  };

  componentDidMount() {
    axios
      .post("http://localhost:5000/flights/get_all_flights")
      .then(res => {
        console.log(res);
        this.setState({ loading: false, flights: res.data.flights });
      })
      .catch(err => console.log("there was an ", err));

    setTimeout(() => {
      this.setState({ loading: false });
    }, 500);
  }

  render() {
    let flights = null;
    console.log(this.state);
    if (this.state.flights != null) flights = this.state.flights;

    let flightList = <CustomSkeleton />;
    let flightListArray = [];

    if (!this.state.loading && flights) {
      flightListArray = this.filterFlights(this.state.filterInfo);
    }

    if (flightListArray.length > 0) {
      flightList = [];
      flightList = flightListArray.map((flight, index) => {
        return (
          <Flights
            auth={this.props.auth}
            key={index}
            startTime={flight.start_time}
            endTime={flight.end_time}
            nonStop={flight.nonStop}
            business={flight.business}
            economy={flight.economy}
            source={flight.source}
            destination={flight.destination}
            onFlightSelect={this.props.flightSelect}
            id={flight.flight_id}
          />
        );
      });
    }

    return (
      <React.Fragment>
        <br />
        <br />
        <br />
        <br />
        <Row>
          <FlightForm origin="search" formFill={this.props.formFill} />
        </Row>
        <Row type="flex" className={classes.FlightSearch}>
          <Col md={5}>
            <FlightFilter
              flightStopType={this.onFlightTypeChangeHandler}
              flightPriceType={this.onFlightPriceChangeHandler}
              flightTimeType={this.onFlightTimeChangeHandler}
              filterInfo={this.state.filterInfo}
            />
          </Col>
          <Col md={19}>
            <div style={{ height: "80vh", overflow: "auto" }}>{flightList}</div>
          </Col>
        </Row>
      </React.Fragment>
    );
  }
}

const mapStateToProps = state => {
  return {
    // flightInfo: state.flightSearch.source,
  };
};

export default withRouter(connect(mapStateToProps)(FlightSearch));
