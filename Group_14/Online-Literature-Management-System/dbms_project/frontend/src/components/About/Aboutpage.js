import React, { Component, Fragment } from "react";
import "./Aboutpage.css";
export default class Aboutpage extends Component {
  render() {
    return (
      <Fragment>
        <div className="card">
          <div
            className="card-header"
            style={{ textAlign: "center", fontFamily: "Oswald" }}
          >
            <h1>ABOUT US</h1>
          </div>
          <div
            className="card-body"
            style={{ fontFamily: "Quicksand", fontSize: "large" }}
          >
            This web application was initiated as a project for ‘Database
            Management Systems’ course of{" "}
            <a href="http://www.iiits.ac.in/" target="_blank">
              Indian Institute of Information Technology Sri City{" "}
              <i className="fa fa-external-link-square-alt" />
            </a>
            {"  "}
            under the supervision of{" "}
            <a
              href="https://mprerana.github.io/DrPreranaMukherjee/"
              target="_blank"
              style={{ color: "#eb1c3a" }}
            >
              <strong>Dr. Prerana Mukherjee</strong>{" "}
              <i className="fa fa-external-link-square-alt" />
            </a>
            <br />
            <br />
            <hr className="about" />
            <h3 style={{ textAlign: "center" }}>Group Members</h3>
            <br />
            <div className="row" style={{ textAlign: "center" }}>
              <div className="col-4">
                <img
                  src="https://i.ibb.co/3kkXHWH/profile-img.jpg"
                  alt="profile_photo"
                  id="profile_photo"
                  height="120"
                  width="120"
                />
              </div>
              <div className="col-4">
                <img
                  src="https://i.ibb.co/3kkXHWH/profile-img.jpg"
                  alt="profile_photo"
                  id="profile_photo"
                  height="120"
                  width="120"
                />
              </div>
              <div className="col-4">
                <img
                  src="https://i.ibb.co/3kkXHWH/profile-img.jpg"
                  alt="profile_photo"
                  id="profile_photo"
                  height="120"
                  width="120"
                />
              </div>
            </div>
            <div className="row" style={{ textAlign: "center" }}>
              <div className="col-4">Ajith Nagelli</div>
              <div className="col-4">Bharath John</div>
              <div className="col-4">Bhavani Shankar</div>
            </div>
            <br />
            <hr className="about" />
            <br />
            <div className="row" style={{ textAlign: "center" }}>
              <div className="col-4">
                <img
                  src="https://i.ibb.co/3kkXHWH/profile-img.jpg"
                  alt="profile_photo"
                  id="profile_photo"
                  height="120"
                  width="120"
                />
              </div>
              <div className="col-4">
                <img
                  src="https://i.ibb.co/3kkXHWH/profile-img.jpg"
                  alt="profile_photo"
                  id="profile_photo"
                  height="120"
                  width="120"
                />
              </div>
              <div className="col-4">
                <img
                  src="https://i.ibb.co/3kkXHWH/profile-img.jpg"
                  alt="profile_photo"
                  id="profile_photo"
                  height="120"
                  width="120"
                />
              </div>
            </div>
            <div className="row" style={{ textAlign: "center" }}>
              <div className="col-4">Moosa Mohammed</div>
              <div className="col-4">Nikhil Sampangi</div>
              <div className="col-4">Nischal Talluri</div>
            </div>
            <br />
            <br />
            <hr className="about" />
            <br />
            <h3 style={{ textAlign: "center" }}>Links</h3>
            <div className="list-group" style={{ textAlign: "center" }}>
              <a
                href="https://github.com/psvnbhavanishankar/Online-Literature-Management-System"
                target="_blank"
                class="list-group-item list-group-item-action"
              >
                &nbsp;&nbsp;
                <i className="fab fa-github-square" />
                &nbsp;&nbsp;Git Hub
              </a>
              <a
                href="#"
                target="_blank"
                class="list-group-item list-group-item-action"
              >
                &nbsp;&nbsp;
                <i className="fab fa-youtube" />
                &nbsp;&nbsp;Video
              </a>
            </div>
            <br />
            <hr className="about" />
            <br />
            <br />
            <br />
          </div>
        </div>
      </Fragment>
    );
  }
}
