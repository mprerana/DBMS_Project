import React, { Component, Fragment } from "react";
import { Link, Redirect } from "react-router-dom";
import "./Home_page.css";
import User_suggestions from "../Users/User_suggestions";
import Feed from "../Feed/feed";
import Header_1 from "./Header_1";
import Blog from "../AllBlogs/allblogs";

function change_bg_4() {
  document
    .getElementById("app")
    .classList.remove(document.getElementById("app").classList[0]);
  document.getElementById("app").classList.add("hp");
}

export default class Home_page extends Component {
  render() {
    return (
      <Fragment onLoad={change_bg_4()}>
        <Header_1 />
        <div className="container-fluid row animated fadeInUp fast">
          <div className="col-5">
            <img
              src="https://i.ibb.co/R9SfyZr/half-owl.png"
              alt="owl"
              className="halfowl"
            />
          </div>
          <div className="col-7 quotebox">
            <blockquote className="homepagequotes">
              I used to think my life was a tragedy, Now I realize it's more of
              a comedy
              <span>- Arthur Flick</span>
            </blockquote>
          </div>
        </div>
        <br />
        <br />
        <br />
        <br />
        <div className="container-fluid row hpb2">
          <div
            className="col-4 hpb2t"
            style={{ marginTop: "auto", marginBottom: "auto" }}
          >
            Welcome to Hoot family Explore the{" "}
            <a className="btn btn-outline-light" href="#/full_list">
              CATALOG
            </a>{" "}
            section to find what you need or{" "}
            <a className="btn btn-outline-light" href="#/follower">
              FOLLOW
            </a>{" "}
            fellow bibliophiles to know what they're reading
          </div>
          <div className="col-1" />
          <div
            className="col-7"
            style={{ marginTop: "auto", marginBottom: "auto", padding: "3%" }}
          >
            <img
              src="https://i.ibb.co/WtyXQRk/hpb2.png"
              alt="owl"
              className="hpb2img"
            />
          </div>
        </div>
        <div className="container-fluid row hpb3">
          <div
            className="col-5"
            style={{ marginTop: "auto", marginBottom: "auto" }}
          >
            <img
              src="https://i.ibb.co/CbYd34V/hpb3img.png"
              alt="friends"
              className="friendimg"
            />
          </div>
          <div className="col-1" />
          <div
            className="col-6"
            style={{ marginTop: "auto", marginBottom: "auto", padding: "3%" }}
          >
            <div className="hpb2t">
              It's a fabulous day to make new friends !!
            </div>
            <br />
            <User_suggestions />
          </div>
        </div>
        <div className="container-fluid hpb4">
          <div
            style={{
              marginLeft: "7vw",
              marginRight: "7vw",
              paddingTop: "7vh",
              paddingBottom: "7vh"
            }}
          >
            <div className="row">
              <h1 style={{ fontFamily: "righteous, cursive" }}>Your Feed</h1>
            </div>
            <div className="row">
              <Feed />
            </div>
          </div>
          <br />
          <br />
          <br />
          <br />
        </div>
        <div
          className="container-fluid hpb5"
          style={{ backgroundColor: "#63d2e8" }}
        >
          <div
            style={{
              marginLeft: "7vw",
              marginRight: "7vw",
              paddingTop: "7vh",
              paddingBottom: "7vh"
            }}
          >
          <div className="row">
              <h1 style={{ fontFamily: "righteous, cursive", color: "white" }}>
                Blogs
              </h1>
          </div>
            <br />
            <Blog />
            
          </div>
        </div>
        <br />
        <br />
        <br />
        <br />
      </Fragment>
    );
  }
}
