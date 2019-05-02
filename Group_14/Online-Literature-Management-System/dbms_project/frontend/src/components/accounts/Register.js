import React, { Component, Fragment } from "react";
import { Link, Redirect } from "react-router-dom";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { register } from "../../actions/auth";
import { createMessage } from "../../actions/messages";

import "./Register.css";
import Header_0 from "./Header_0";

function change_bg_2() {
  document
    .getElementById("app")
    .classList.remove(document.getElementById("app").classList[0]);
  document.getElementById("app").classList.add("rp");
  // console.log("fuck yeah! magic!!");
}

export class Register extends Component {
  state = {
    username: "",
    email: "",
    password: "",
    password2: ""
  };

  static propTypes = {
    register: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool
  };

  onSubmit = e => {
    e.preventDefault();
    const { username, email, password, password2 } = this.state;

    if (password !== password2) {
      this.props.createMessage({
        passwordsNotMatch: "Passwords do not match "
      });
    } else {
      const newUser = {
        username,
        email,
        password
      };
      this.props.register(newUser);
    }
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  render() {
    if (this.props.isAuthenticated) {
      return <Redirect to="/" />;
    }
    const { username, email, password, password2 } = this.state;
    return (
      <Fragment onLoad={change_bg_2()}>
        <Header_0 />
        <div className="row">
          <div className="col-5 reg_form">
            <div className="signup">Sign Up</div>
            <br />
            <form
              onSubmit={this.onSubmit}
              className="text-center"
              style={{ color: "#757575" }}
            >
              <div className="md-form">
                <input
                  type="text"
                  id="materialLoginFormEmail"
                  className="form-control"
                  name="username"
                  placeholder="User Name"
                  onChange={this.onChange}
                  value={username}
                />
              </div>
              <br />
              <div className="md-form">
                <input
                  type="email"
                  id="materialLoginFormEmail"
                  className="form-control"
                  name="email"
                  placeholder="E-mail"
                  onChange={this.onChange}
                  value={email}
                />
              </div>
              <br />
              <div className="md-form">
                <input
                  type="password"
                  id="materialLoginFormPassword"
                  className="form-control"
                  name="password"
                  placeholder="Password"
                  onChange={this.onChange}
                  value={password}
                />
              </div>
              <br />
              <div className="md-form">
                <input
                  type="password"
                  id="materialLoginFormPassword"
                  className="form-control"
                  name="password2"
                  placeholder="Confirm Password"
                  onChange={this.onChange}
                  value={password2}
                />
              </div>
              <button
                className="btn btn-outline-info btn-rounded btn-block my-4 waves-effect z-depth-0"
                type="submit"
              >
                Register
              </button>
              <p>
                Already have an account?
                <br />
                <Link to="/login">Login</Link>
              </p>
            </form>
          </div>
          <div className="col-7" />
        </div>
      </Fragment>
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
