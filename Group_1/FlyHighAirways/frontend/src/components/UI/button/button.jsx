import React, { Component } from "react";
import { Button } from "antd";

class button extends Component {
  state = { size: "small" };
  handleSizeChange = e => {
    this.setState({ size: e.target.value });
  };
  render() {
    const size = this.state.size;
    return (
      <div>
        <Button type="danger" size={size}>
          Danger
        </Button>
      </div>
    );
  }
}

export default button;
