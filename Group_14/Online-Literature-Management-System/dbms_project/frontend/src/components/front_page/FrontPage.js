import React, { Component } from "react";
import { Link, Redirect } from "react-router-dom";
import "./FrontPage.css";

function change_bg_1() {
  document
    .getElementById("app")
    .classList.remove(document.getElementById("app").classList[0]);
  document.getElementById("app").classList.add("fp");
}
export default class FrontPage extends Component {
  render() {
    return (
      <div className="row" onLoad={change_bg_1()}>
        <div className="fpregrow col-3">
          <div className="fixed1 animated bounceInDown delay-1s slow fpregtab">
            First time?
            <br />
            Join the hoot community
            <br />
            now!
            <br />
            <br />
            <Link
              className="btn btn-sm animated-button thar-two"
              to="/register"
            >
              Sign Up
            </Link>
          </div>
        </div>
        <div className="marigins col-6 animated fadeIn slow">
          Welcome to
          <br />
          <img
            src="https://i.ibb.co/b3Yg08S/logo-animated.gif"
            className="l1"
            alt="logo"
          />
          <br />
          <br />
          An online community of literature lovers
        </div>
        <div className="fixed2 col-3 animated bounceInRight delay-2s slow fplogtab">
          <div className="fplogtext">
            Already a member?
            <br />
            <br />
            <Link className="btn btn-sm animated-button thar-four" to="/login">
              Hoot me in
            </Link>
          </div>
        </div>
      </div>
    );
  }
}
