import React from "react";
import { Row, Col } from "antd";
import "./styles.scss";

class NewsHeaderBackground extends React.Component {
  render() {
    let { thumbnail, imgUrl } = this.props;
    return (
      <div className="news-header-background">
        <div className="overlay" />

        <div className="thumbnail">
          <div
            style={{
              backgroundImage: `url(${imgUrl})`
            }}
          />
        </div>
      </div>
    );
  }
}

export default NewsHeaderBackground;
