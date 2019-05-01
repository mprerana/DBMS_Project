import React from "react";
import ComponentSlider from "@kapost/react-component-slider";
import { Card } from "antd";

import "./customstyle.css";
const renderLeftArrow = () => <i className="fa fa-caret-left" />;
const renderRightArrow = () => <i className="fa fa-caret-right" />;

class MenuBar extends React.Component {
  render() {
    return (
      <Card className="menu-bar" style={{ lineHeight: "1.5" }}>
        <div>
          <ComponentSlider
            renderLeftArrow={renderLeftArrow}
            renderRightArrow={renderRightArrow}
          >
            <div className="menu-item">
              <Card.Grid style={{ width: "300px", display: "inline-block" }}>
                Web check in
              </Card.Grid>
            </div>
            <div className="menu-item">
              <Card.Grid className="menu-item">Book a Flight </Card.Grid>
            </div>
            <div className="menu-item">
              <Card.Grid className="menu-item">Edit a Booking</Card.Grid>
            </div>
            <div className="menu-item">
              <Card.Grid className="menu-item">Group Booking </Card.Grid>
            </div>
            <div className="menu-item">
              <Card.Grid className="menu-item">Plan B </Card.Grid>
            </div>
            <div className="menu-item">
              <Card.Grid className="menu-item">Flight Status </Card.Grid>
            </div>
          </ComponentSlider>
        </div>
      </Card>
    );
  }
}

export default MenuBar;
