import React, { Fragment } from "react";
import Blog from "./Blog";
import Form from "./Blog_form"
import Header_1 from "../home_page/Header_1";

export default function Dashboard() {
  return (
    <Fragment>
      <Header_1 />
      <br />
      <br />
      <br />
      <br />
      <Form />
      <br />
      <Blog />
    </Fragment>
  );
}