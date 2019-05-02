import React, { Component, Fragment } from "react";
import Header_1 from "../home_page/Header_1";
import About_page from "./Aboutpage";

export default class About_dashboard extends Component {
  render() {
    return (
      <Fragment>
        <Header_1 />
        <br />
        <br />
        <br />
        <br />
        <div className="container">
          <About_page />
        </div>
      </Fragment>
    );
  }
}
