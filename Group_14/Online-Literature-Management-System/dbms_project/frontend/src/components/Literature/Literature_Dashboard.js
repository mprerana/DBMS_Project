import React, { Fragment } from "react";
import List_Form from "./readinglist_form";
import Lists from "./readinglists";
import Header_1 from "../home_page/Header_1";

export default function Dashboard() {
  return (
    <Fragment>
      <Header_1 />
      <br />
      <br />
      <br />
      <div className="container-fluid animated fadeInDown">
        <List_Form />
        <br />
        <Lists />
      </div>
    </Fragment>
  );
}
