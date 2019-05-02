import React, { Fragment } from "react";
import Works from "./works";
import Header_1 from "../home_page/Header_1";

export default function Dashboard() {
  return (
    <Fragment>
      <Header_1 />
      <br />
      <br />
      <br />
      <div className="container-fluid">
        <Works />
      </div>
    </Fragment>
  );
}
