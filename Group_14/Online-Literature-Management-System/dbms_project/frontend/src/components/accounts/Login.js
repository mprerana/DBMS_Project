import React, { Component, Fragment } from "react";
import { Link, Redirect } from "react-router-dom";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { login } from "../../actions/auth";

import "./Login.css";
import Header_0 from "./Header_0";

function change_bg_3() {
  document
    .getElementById("app")
    .classList.remove(document.getElementById("app").classList[0]);
  document.getElementById("app").classList.add("lp");
}

export class Login extends Component {
  state = {
    username: "",
    password: ""
  };

  static propTypes = {
    login: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool
  };

  onSubmit = e => {
    e.preventDefault();
    this.props.login(this.state.username, this.state.password);
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  render() {
    if (this.props.isAuthenticated) {
      return <Redirect to="/home" />;
    }

    const { username, password } = this.state;
    return (
      <Fragment onLoad={change_bg_3()}>
        <Header_0 />
        <div className="row">
          <div className="col-7" id="c1" />
          <div className="col-5 log_form" id="c3">
            <div className="signin">Sign In</div>
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
                  type="password"
                  id="materialLoginFormPassword"
                  className="form-control"
                  name="password"
                  placeholder="Password"
                  onChange={this.onChange}
                  value={password}
                />
              </div>
              <button
                className="btn btn-outline-info btn-rounded btn-block my-4 waves-effect z-depth-0"
                type="submit"
              >
                Login
              </button>
              <p>
                Don't have an account?
                <br />
                <Link to="/register">Register</Link>
              </p>
            </form>
          </div>
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
  { login }
)(Login);
