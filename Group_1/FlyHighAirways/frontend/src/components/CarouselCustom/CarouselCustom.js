import React, { Component } from "react";
import { Carousel, Icon } from "antd";
import FlightForm from "../FlightForm/FlightForm";
import classes from "./CarouselCustom.module.css";
import { Button } from "antd";

export default class CarouselComponent extends Component {
  constructor(props) {
    super(props);
    this.next = this.next.bind(this);
    this.previous = this.previous.bind(this);
    this.carousel = React.createRef();
  }

  next() {
    this.carousel.next();
  }

  previous() {
    this.carousel.prev();
  }

  onFormSubmitHandler = e => {
    e.preventDefault();
    console.log("hi there");
  };

  render() {
    const props = {
      dots: true,
      infinite: true,
      speed: 500,
      slidesToShow: 1,
      slidesToScroll: 1
    };
    return (
      <div style={{ position: "relative" }}>
        <Icon
          type="left-circle"
          theme="filled"
          onClick={this.previous}
          style={{
            position: "absolute",
            zIndex: "190",
            top: "50%",
            left: "45%",
            fontSize: "40px"
          }}
        />
        <div>
          <Carousel ref={node => (this.carousel = node)} {...props} autoplay>
            <div className={classes.antCarousel}>
              <img
                alt="<temporary>"
                src="https://us-east.manta.joyent.com/condenast/public/cnt-services/production/2015/11/24/5654d90d5e7aeb7a6e217ebf_cappadocia-turkey-hot-air-balloons-cr-getty.jpg"
              />
            </div>
            <div
              style={{ position: "relative" }}
              className={classes.antCarousel}
            >
              <img
                alt="<temporary>"
                src="http://www.liveenhanced.com/wp-content/uploads/2018/03/B-Ocean-Resort-most-beautiful-places-To-visit-In-florida.jpg"
              />
            </div>
            <div className={classes.antCarousel}>
              <img
                alt="<temporary>"
                src="http://www.jetwayz.com/wp-content/uploads/2012/11/Tourist-Attractions-in-Italy.jpg"
              />
            </div>
          </Carousel>
          <div className={classes.rightChild}>
            <h1>Flyhigh to Delhi </h1>

            <h5>
              Introducing daily, non-stop flights between Kolkata and Mumbai,
            </h5>
            <h5>W.E.F 5 June 2019.</h5>
            <h5>Starting from Rs 4590. </h5>
            <Button>Book Now</Button>
          </div>
        </div>
        <div className={classes.childDiv} style={{paddingTop: '4rem'}}>
          <FlightForm {...this.props} />
        </div>
        <Icon
          type="right-circle"
          theme="filled"
          onClick={this.next}
          style={{
            position: "absolute",
            zIndex: "190",
            top: "50%",
            left: "96%",
            fontSize: "40px"
          }}
        />
      </div>
    );
  }
}
