import React, { Component } from "react";
import classes from "./homepage.module.css";
import "font-awesome/css/font-awesome.css";
import CarouselComponent from "../../components/CarouselCustom/CarouselCustom";
import MenuBar from "../../components/HorizontalScrollBar/ScrollBar";
import Footer from "../../components/Footer/Footer";
import Cards from "../../components/UI/Cards/cards";
import NewsHeaderCard from "../../components/UI/NewsHeaderCard";
import { Divider } from "antd";

const styles = {
  fontFamily: "sans-serif",
  textAlign: "center",
  paddingTop: "50px"
};
class HomePage extends Component {
  state = {};

  render() {
    const popularFlights = [
      {
        source: "CHENNAI",
        destination: "MUMBAI",
        img1:
          "https://scoutmytrip.com/blog/wp-content/uploads/2016/12/Road-Trips-from-Delhi-Blog-Feature.jpg"
      },
      {
        source: "DELHI",
        destination: "KOLKATA",
        img1:
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxK7-eHcmEmTrN8pqPwbPbsyPt_8MqjNB3syiX8Z1gahgesEsh"
      },
      {
        source: "CHENNAI",
        destination: "DELHI",
        img1:
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWh2iBRsGwyW1q0OPcPq_aopkAfJh-NHNEp59pjW8QgBSRPdzIFw"
      },
      {
        source: "KOLKATA",
        destination: "DARJEELING",
        img1:
          "https://scoutmytrip.com/blog/wp-content/uploads/2018/05/Hill-stations-South-India-Featured.jpg"
      }
    ];
    const destinations = [
      {
        destination: "Manali",
        img:
          "http://alldatmatterz.com/img/article/764/%E0%A4%95%E0%A5%81%E0%A4%B2%E0%A5%8D%E0%A4%B2%E0%A5%82%20%E0%A4%AE%E0%A4%A8%E0%A4%BE%E0%A4%B2%E0%A5%80.jpg"
      },
      {
        destination: "Shillong",
        img:
          "https://scoutmytrip.com/blog/wp-content/uploads/2018/05/Hill-stations-in-India-Featured.jpg"
      },
      {
        destination: "Rajasthan",
        img:
          "https://i.pinimg.com/originals/71/41/ff/7141fff9e2dfc82f159c9496dac3747b.jpg"
      },
      {
        destination: "Darjeeling",
        img:
          "https://scoutmytrip.com/blog/wp-content/uploads/2018/04/Places-to-visit-in-Darjeeling-Featured.jpg"
      }
    ];

    return (
      <React.Fragment>
        <CarouselComponent {...this.props} />
        <div style={styles}>
          <MenuBar />
          <br />
          <br />
          <br />
          <Divider />
          <NewsHeaderCard
            title="Travel with our Airlines"
            flightList={destinations}
          />
          <br />
          <br />
          <br />
          <Divider />
          <NewsHeaderCard title="Popular Flights" flightList={popularFlights} />
        </div>

        {/* <Carousal /> */}
        {/* <Carousal /> */}
        {/* <FlightForm /> */}

        {/* <Footer /> */}
      </React.Fragment>
    );
  }
}

export default HomePage;
