import React from "react";

import Card from "../Card";
import NewsHeader from "./NewsHeader";
import NewsHeaderBackground from "./NewsHeaderBackground";
import { Row, Col } from "antd";
import "./styles.scss";

class NewsHeaderCard extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    let { href, title, author, date, thumbnail, tags } = this.props;
    return (
      <div className="card1">
        <h1
          style={{
            textAlign: "left",
            fontFamily: "Sans",
            fontWeight: "bolder",
            paddingTop: "100px",
            paddingBottom: "30px",
            paddingLeft: "60px",
            paddingRight: "30px",
            fontSize: "40px"
          }}
        >
          {title}
        </h1>
        <Row gutter={40}>
          {this.props.flightList.map((flight, index) => {
            return (
              <div className="space" key={index}>
                <Col span={6}>
                  <Card className="news-header-card">
                    <NewsHeaderBackground
                      thumbnail={thumbnail}
                      imgUrl={
                        flight.source == null
                          ? `${flight.img}`
                          : `${flight.img1}`
                      }
                    />

                    <NewsHeader
                      title={
                        flight.source == null
                          ? `${flight.destination}`
                          : `${flight.source} - ${flight.destination}`
                      }
                      author={author}
                      date={date}
                      tags={tags}
                    />
                  </Card>
                </Col>
              </div>
            );
          })}
        </Row>
      </div>
    );
  }
}

export default NewsHeaderCard;
