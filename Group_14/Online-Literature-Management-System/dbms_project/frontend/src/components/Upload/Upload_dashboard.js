import React, { Fragment } from "react";
import Upload_Form from "./upload_form";
import Uploads from "./uploads";
import Header_1 from "../home_page/Header_1";

export default function Dashboard() {
  return (
    <Fragment>
      <Header_1 />
      <br />
      <br />
      <br />
      <br />
      <br />
      <div className="container-fluid animated fadeInUp">
        <Upload_Form />
        <br />
        <br />
        <br />
        <Uploads />
      </div>
    </Fragment>
  );
}
