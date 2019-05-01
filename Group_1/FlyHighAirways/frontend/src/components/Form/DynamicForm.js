import React from "react";
import ReactDOM from "react-dom";

import "./style.css";

import { Button } from 'antd';

class DynamicForm extends React.Component {
  constructor() {
    super();
    this.state = {
      name: "",
      Passengers: [{ name: "", age: "", email: "", sex: "" }]
    };
  }

  handleNameChange = evt => {
    this.setState({ name: evt.target.value });
  };
  handleEmailChange = evt => {
    this.setState({ email: evt.target.value });
  };
  handleAgeChange = evt => {
    this.setState({ age: evt.target.value });
  };

  handlePassengerNameChange = idx => evt => {
    const newPassengers = this.state.Passengers.map((Passenger, sidx) => {
      if (idx !== sidx) return Passenger;
      return { ...Passenger, name: evt.target.value };
    });

    this.setState({ Passengers: newPassengers });
  };

  handlePassengerEmailChange = idx => evt => {
    const newPassengers = this.state.Passengers.map((Passenger, sidx) => {
      if (idx !== sidx) return Passenger;
      return { ...Passenger, email: evt.target.value };
    });

    this.setState({ Passengers: newPassengers });
  };
  handlePassengerAgeChange = idx => evt => {
    const newPassengers = this.state.Passengers.map((Passenger, sidx) => {
      if (idx !== sidx) return Passenger;
      return { ...Passenger, age: evt.target.value };
    });

    this.setState({ Passengers: newPassengers });
  };
  handleSubmit = e => {
    e.preventDefault();

    this.props.onSubmit(this.state.Passengers);

    const { name, Passengers } = this.state;
    // alert(`Incorporated: ${name} with ${shareholders.length} shareholders`);
  };

  handleAddPassenger = () => {
    this.setState({
      Passengers: this.state.Passengers.concat([
        { name: "", age: "", email: "", sex: "" }
      ])
    });
    this.props.onAdd(this.state.Passengers.length + 1);
  };

  handleRemovePassenger = idx => () => {
    this.setState({
      Passengers: this.state.Passengers.filter((s, sidx) => idx !== sidx)
    });
    this.props.onAdd(this.state.Passengers.length - 1);
  };

  render() {
    // console.log(this.state.Passengers);

    return (
      <form onSubmit={this.handleSubmit}>
        <h4>Passengers</h4>

        {this.state.Passengers.map((Passenger, idx) => (
          <div className="shareholder" key={idx}>
            <input
              type="text"
              placeholder={`#${idx + 1} name`}
              value={Passenger.name}
              onChange={this.handlePassengerNameChange(idx)}
              style={{ backgroundColor: "white" }}
            />
            <input
              type="text"
              placeholder={`#${idx + 1} Email`}
              value={Passenger.email}
              onChange={this.handlePassengerEmailChange(idx)}
              style={{ backgroundColor: "white" }}
            />
            <input
              type="number"
              placeholder={`#${idx + 1} age`}
              value={Passenger.age}
              onChange={this.handlePassengerAgeChange(idx)}
              style={{ backgroundColor: "white" }}
            />
            <button
              type="button"
              onClick={this.handleRemovePassenger(idx)}
              className="small"
            >
              -
            </button>
          </div>
        ))}
        <button
          type="button"
          onClick={this.handleAddPassenger}
          className="small"
        >
          Add Passenger
        </button>
        <Button
          type="primary"
          htmlType="submit"
          disabled={
            !(
              this.props.isFlightSelected[0] !== null &&
              this.props.isFlightSelected[1] > 0 &&
              this.props.isFlightSelected[2].email !== null
            )
          }
        >
          Submit
        </Button>
      </form>
    );
  }
}
export default DynamicForm;
