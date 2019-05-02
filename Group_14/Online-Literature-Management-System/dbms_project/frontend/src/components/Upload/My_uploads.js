import React, { Component, Fragment } from "react";
import Uploads from "./uploads";
import Header_1 from "../home_page/Header_1";

export default class My_uploads extends Component {
  render() {
    return (
      <Fragment>
        <Header_1 />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <div className="container-fluid animated fadeInUp">
          <div
            className="container-fluid"
            style={{ paddingLeft: "5%", paddingRight: "5%" }}
          >
            <div className="row">
              <h4 id="wtext1">Your Uploads :</h4>
            </div>

            <Uploads />
          </div>
        </div>
      </Fragment>
    );
  }
}
