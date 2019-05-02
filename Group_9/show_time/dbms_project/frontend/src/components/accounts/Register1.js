import React, { Component } from "react";
import { Link, Redirect } from "react-router-dom";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { register } from "../../actions/auth";
import { createMessage } from "../../actions/messages";

export class Register extends Component {
  state = {
    username: "",
    email: "",
    first_name: "",
    last_name: "",
    password: "",
    password2: "",
    dob: "",
    city: "",
    phone: "",
    image: ""
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmit = e => {
    e.preventDefault();

    const {
      username,
      email,
      first_name,
      last_name,
      password,
      password2,
      dob,
      city,
      phone,
      image
    } = this.state;

    if (password !== password2) {
      this.props.createMessage({ passwordNotMatch: "Passwords do not match" });
      return;
    } else if (city === "") {
      this.props.createMessage({ cityEmpty: "City field is required" });
      return;
    } else if (phone === "") {
      this.props.createMessage({ phoneEmpty: "Phone field is required" });
      return;
    } else {
      const newUser = {
        username,
        password,
        email,
        first_name,
        last_name,
        dob,
        city,
        phone,
        image: null
      };

      this.props.register(newUser);
    }
  };

  static propTypes = {
    register: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool
  };

  render() {
    if (this.props.isAuthenticated) {
      return <Redirect to="/" />;
    }

    const {
      username,
      email,
      first_name,
      last_name,
      password,
      password2,
      dob,
      city,
      phone,
      image
    } = this.state;

    return (
      <div className="col-md-6 m-auto">
        <div className="card card-body mt-5">
          <h2 className="text-center">Register</h2>
          <form onSubmit={this.onSubmit}>
            <div className="form-group">
              <label>Username</label>
              <input
                type="text"
                className="form-control"
                name="username"
                onChange={this.onChange}
                value={username}
              />
            </div>
            <div className="form-group">
              <label>Email</label>
              <input
                type="email"
                className="form-control"
                name="email"
                onChange={this.onChange}
                value={email}
              />
            </div>
            <div className="form-group">
              <label>First name</label>
              <input
                type="text"
                className="form-control"
                name="first_name"
                onChange={this.onChange}
                value={first_name}
              />
            </div>
            <div className="form-group">
              <label>Last name</label>
              <input
                type="text"
                className="form-control"
                name="last_name"
                onChange={this.onChange}
                value={last_name}
              />
            </div>
            <div className="form-group">
              <label>Password</label>
              <input
                type="password"
                className="form-control"
                name="password"
                onChange={this.onChange}
                value={password}
              />
            </div>
            <div className="form-group">
              <label>Confirm Password</label>
              <input
                type="password"
                className="form-control"
                name="password2"
                onChange={this.onChange}
                value={password2}
              />
            </div>

            <div className="form-group">
              <label>Date of Birth</label>
              <input
                type="date"
                className="form-control"
                name="dob"
                onChange={this.onChange}
                value={dob}
              />
            </div>
            <div className="form-group">
              <label>City</label>
              <input
                type="text"
                className="form-control"
                name="city"
                onChange={this.onChange}
                value={city}
              />
            </div>

            <div className="form-group">
              <label>Phone</label>
              <input
                type="number"
                className="form-control"
                name="phone"
                onChange={this.onChange}
                value={phone}
              />
            </div>

            <div className="form-group">
              <label>Image</label>
              <input
                type="file"
                className="form-control"
                name="image"
                onChange={this.onChange}
                value={image}
              />
            </div>

            <div className="form-group">
              <button type="submit" className="btn btn-primary">
                Register
              </button>
            </div>
            <p>
              Already have an account? <Link to="/login">Login</Link>
            </p>
          </form>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated
});

export default connect(
  mapStateToProps,
  { register, createMessage }
)(Register);
