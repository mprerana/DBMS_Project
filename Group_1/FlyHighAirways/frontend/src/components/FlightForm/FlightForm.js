import React, { Component } from "react";

import { connect } from "react-redux";
import { withRouter } from "react-router";
import { Select, Popover, Button, Calendar, Input } from "antd";

import classes from "./FlightForm.module.css";
import { Alert } from "antd";

const Option = Select.Option;

class flightForm extends Component {
  state = {
    calendarPopUp: false,
    formData: {
      source: "",
      destination: "",
      date: ""
    },
    flightFormError: null,
    validity: {
      source: false,
      destination: false,
      time: false
    },
    isValid: false
  };

  // Whether to display the calendar
  onVisibleHandler = () => {
    this.setState(prevState => {
      return { calendarPopUp: !prevState.calendarPopUp };
    });
  };

  // Whether to display the calendar
  onVisibleHandler = () => {
    this.setState(prevState => {
      return { calendarPopUp: !prevState.calendarPopUp };
    });
  };

  // location ==> Source or destination
  onCitySelectHandler = (cityData, location) => {
    const updatedFormData = { ...this.state.formData };
    updatedFormData[location] = cityData;

    const updatedValidity = { ...this.state.validity };
    updatedValidity[location] = cityData == "" ? false : true;

    this.setState({ formData: updatedFormData, validity: updatedValidity });
  };

  // After selecting the date
  onDateSelectHandler = data => {
    this.onVisibleHandler();

    const updatedFormData = { ...this.state.formData };
    updatedFormData.time = data.format("L");

    const updatedValidity = { ...this.state.validity };
    updatedValidity.time = true;

    if (data == "") {
      updatedValidity.time = false;
    }

    this.setState({ formData: updatedFormData, validity: updatedValidity });
  };

  // Utility function to check if date is valid (After current time)
  checkDateValidation = date => {
    const currentDate = new Date();

    const selectedDate = date.split("/");
    let updatedDate = [];
    selectedDate.forEach(element => {
      updatedDate.push(parseInt(element));
    });

    let validation = true;

    if (updatedDate[2] < currentDate.getUTCFullYear()) {
      validation = false;
      return validation;
    } else if (updatedDate[2] === currentDate.getUTCFullYear()) {
      if (updatedDate[0] < currentDate.getUTCMonth() + 1) {
        validation = false;
        return validation;
      } else if (updatedDate[0] === currentDate.getUTCMonth() + 1) {
        if (updatedDate[1] < currentDate.getUTCDate()) {
          validation = false;
          return validation;
        }
      }
    }
    return validation;
  };

  onSubmitHandler = (event, data) => {
    event.preventDefault();

    let isError = false;
    let errorString = null;

    if (!this.state.validity.time) {
      isError = true;
      errorString = "Date Selected is Not Valid";
    } else if (!this.state.validity.source) {
      isError = true;
      errorString = "Please Select A Source";
    } else if (!this.state.validity.destination) {
      isError = true;
      errorString = "Please Select A Destination";
    }

    this.setState({ flightFormError: errorString });
    if (isError) {
      return;
    }
    this.props.formFill(data);

    this.props.history.push("/flights");
  };

  render() {
    const popUpCalendar = (
      <div style={{ width: 300, border: "1px solid #d9d9d9", borderRadius: 4 }}>
        <Calendar
          fullscreen={false}
          onSelect={date => this.onDateSelectHandler(date)}
        />
      </div>
    );

    const data = {
      ...this.state.formData
    };

    // Checks from where this Form component is rendered
    let homePageSearch = this.props.origin === "search" ? false : true;

    return (
      <React.Fragment>
        {this.state.flightFormError ? (
          <Alert
            banner
            message={
              this.state.flightFormError ? this.state.flightFormError : null
            }
            type="warning"
          />
        ) : null}
        <form
          className={homePageSearch ? classes.FormDiv : classes.FormDivMain2}
          onSubmit={e => this.onSubmitHandler(e, data)}
        >
          <div className={homePageSearch ? null : classes.FormDiv2}>
            <div
              className={
                homePageSearch ? classes.optionWrapper : classes.optionWrapper2
              }
            >
              <h6>Select Source: </h6>
              <Select
                showSearch
                style={{ width: "200px", marginLeft: "20px" }}
                placeholder="Source Airport"
                optionFilterProp="children"
                onSelect={cityName =>
                  this.onCitySelectHandler(cityName, "source")
                }
                filterOption={(input, option) =>
                  option.props.children
                    .toLowerCase()
                    .indexOf(input.toLowerCase()) >= 0
                }
              >
                <Option value="chennai">Chennai</Option>
                <Option value="kolkata">Kolkata</Option>
                <Option value="mumbai">Mumbai</Option>
                <Option value="pune">Pune</Option>
                <Option value="indore">Indore</Option>
                <Option value="delhi">Delhi</Option>
              </Select>
            </div>

            <div
              className={
                homePageSearch ? classes.optionWrapper : classes.optionWrapper2
              }
            >
              <h6>Select Destination: </h6>
              <Select
                showSearch
                style={{ width: "200px", marginLeft: "20px" }}
                placeholder="Destination Airport"
                optionFilterProp="children"
                onSelect={cityName =>
                  this.onCitySelectHandler(cityName, "destination")
                }
                filterOption={(input, option) =>
                  option.props.children
                    .toLowerCase()
                    .indexOf(input.toLowerCase()) >= 0
                }
              >
                <Option value="chennai">Chennai</Option>
                <Option value="kolkata">Kolkata</Option>
                <Option value="mumbai">Mumbai</Option>
                <Option value="pune">Pune</Option>
                <Option value="indore">Indore</Option>
                <Option value="delhi">Delhi</Option>
              </Select>
            </div>

            <div
              className={
                homePageSearch ? classes.dateWrapper : classes.dateWrapper2
              }
            >
              <Input
                type="text"
                value={this.state.formData.time}
                placeholder="Date"
              />
              <Popover
                content={popUpCalendar}
                title="Please Select the date of flight"
                trigger="click"
                visible={this.state.calendarPopUp}
              >
                <Button
                  type="primary"
                  onClick={this.onVisibleHandler}
                  style={{ marginLeft: "20px", marginTop: "0px" }}
                >
                  Select A Date
                </Button>
              </Popover>
            </div>
          </div>

          <div className={classes.SearchBtn}>
            <Button
              style={{ marginTop: "0px" }}
              type="primary"
              htmlType="submit"
              size="large"
            >
              Search Flights
            </Button>
          </div>
        </form>
      </React.Fragment>
    );
  }
}

const mapDispatchToProps = dispatch => {
  return {
    onFlightFormAdded: flightData =>
      dispatch({ type: "ADD_FLIGHT_FORM", flightData })
  };
};

export default withRouter(
  connect(
    null,
    mapDispatchToProps
  )(flightForm)
);
