import React, { Component } from "react";
import { Carousel, Icon } from "antd";
import classes from "./Carousal.module.css";
import FlightForm from "../../FlightForm/FlightForm";

class Carousal extends Component {
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

  render() {
    return (
      <div className={classes.parentDiv}>
        <Carousel effect="fade">
          <div className={[classes.antCarousel, classes.slickSlide].join(" ")}>
            <img src="https://mdbootstrap.com/img/Photos/Slides/img%20(15).jpg" />
          </div>
          <div className={[classes.antCarousel, classes.slickSlide].join(" ")}>
            <img src="https://mdbootstrap.com/img/Photos/Slides/img%20(16).jpg" />
          </div>
          <div className={[classes.antCarousel, classes.slickSlide].join(" ")}>
            <img src="https://mdbootstrap.com/img/Photos/Slides/img%20(17).jpg" />
          </div>
          <div className={[classes.antCarousel, classes.slickSlide].join(" ")}>
            <img src="https://mdbootstrap.com/img/Photos/Slides/img%20(18).jpg" />
          </div>
        </Carousel>

        <h1 className={classes.childDiv}>
          <FlightForm />
        </h1>
        <h1 className={classes.childDiv1}>
          <Icon type="left-circle" onClick={this.previous} />
        </h1>
        <h1 className={classes.childDiv2}>
          <Icon type="left-circle" onClick={this.next} />
        </h1>
      </div>
    );
  }
}

export default Carousal;
