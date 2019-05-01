import React from "react";
import { Row, Col } from "antd";
// import classes from "./Footer.module.css";
import "./footer.css";
function Footer() {
  return (
    <footer
      id="footer"
      className="dark"
      style={{
        backgroundImage: "linear-gradient(to left, #74ebd5, #ACB6E5)",
        WebkitTextFillColor: "black"
      }}
    >
      <div className="footer-wrap">
        <Row>
          <Col lg={4} sm={24} xs={24}>
            <div className="footer-center">
              <h1 style={{ WebkitTextFillColor: "black" }}>Get to know us</h1>
              <div>
                <a
                  target="_blank "
                  href="/"
                  style={{ WebkitTextFillColor: "black" }}
                >
                  About Us
                </a>
              </div>
              <div>
                <a
                  target="_blank "
                  href="/"
                  style={{ WebkitTextFillColor: "black" }}
                >
                  Information
                </a>
              </div>
              <div>
                <a href="/" style={{ WebkitTextFillColor: "black" }}>
                  Destinations
                </a>
              </div>
            </div>
          </Col>
          <Col lg={4} sm={24} xs={24}>
            <div className="footer-center">
              <h1 style={{ WebkitTextFillColor: "black" }}>Services</h1>
              <div>
                <a href="/" style={{ WebkitTextFillColor: "black" }}>
                  Flight Schedule
                </a>
              </div>
              <div>
                <a
                  target="_blank"
                  rel="noopener"
                  href="/"
                  style={{ WebkitTextFillColor: "black" }}
                >
                  Web-Checkin
                </a>
              </div>
              <div>
                <a
                  target="_blank"
                  rel="noopener"
                  href="/"
                  style={{ WebkitTextFillColor: "black" }}
                >
                  Flights
                </a>
              </div>
            </div>
          </Col>
          <Col lg={4} sm={24} xs={24}>
            <div className="footer-center">
              <h1 style={{ WebkitTextFillColor: "black" }}>
                Create An Account
              </h1>
              <div>
                <a href="/" style={{ WebkitTextFillColor: "black" }}>
                  Signup
                </a>
              </div>
              <div>
                <a
                  target="_blank"
                  rel="noopener"
                  href="/"
                  style={{ WebkitTextFillColor: "black" }}
                >
                  Profile
                </a>
              </div>
              <div>
                <a
                  target="_blank"
                  rel="noopener"
                  href="/"
                  style={{ WebkitTextFillColor: "black" }}
                >
                  Logout
                </a>
              </div>
            </div>
          </Col>

          <Col lg={8} sm={24} xs={24}>
            <div className="footer-center">
              <h1 style={{ WebkitTextFillColor: "black" }}>FlyHighways</h1>
              <div>
                <a
                  target="_blank"
                  rel="noopener noreferrer"
                  href="http://ant.design/"
                >
                  Come Visit Us
                </a>
              </div>
            </div>
          </Col>
        </Row>
      </div>
      <Row className="bottom-bar">
        <Col lg={6} sm={24} />
        <Col lg={18} sm={24}>
          <span
            style={{
              lineHeight: "16px",
              paddingRight: 12,
              marginRight: 11,
              borderRight: "1px solid rgba(255, 255, 255, 0.55)"
            }}
          >
            <a
              href="https://docs.alipay.com/policies/privacy/antfin"
              rel="noopener noreferrer"
              target="_blank"
            >
              FlyHighways
            </a>
          </span>

          <span style={{ marginRight: 12 }}>Copyright © Flyhighways</span>
        </Col>
      </Row>
    </footer>
  );
}

export default Footer;
