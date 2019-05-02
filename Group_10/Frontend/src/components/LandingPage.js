import React from "react";
import "./LandingPage.css";
import styled from "styled-components";
import PropTypes from "prop-types";

import {
  withStyles,
  MuiThemeProvider,
  createMuiTheme
} from "@material-ui/core/styles";
import { blue } from "@material-ui/core/colors";
import Button from "@material-ui/core/Button";
import backgroundImg from "./images/thumb-1920-306638.jpg";
import logo from "./images/LogoWhiteTransparent.png";
import LoginPage from "./LoginPage";
import BackgroundImage from "react-background-image-loader";
import Navbar from "./Navbar";

const wiseWords = {
  quote:
    "An app designed to make you better at understanding what you have learned"
};

const show = () => {
  // const logo = document.getElementById("logo");
  const footer = document.getElementById("footer");
  // logo.classList.add("animated", "fadeOut", 'slow');
  footer.classList.add("animated", "fadeOut", "slow");
};

const hide = () => {
  // const logo = document.getElementById("logo");
  const footer = document.getElementById("footer");
  // logo.classList.remove("animated", "fadeOut", 'slow');
  footer.classList.remove("animated", "fadeOut", "slow");
  // logo.classList.add("animated", "fadeIn", 'slow');
  footer.classList.add("animated", "fadeIn", "slow");
};

const theme = createMuiTheme({
  palette: {
    primary: blue,
    secondary: {
      main: "#fff"
    }
  },
  shadows: ["none"]
});
let url = "./images/bible-biblia-book-bindings-1112048.jpg";
const styles = theme => ({
  root: {
    backgroundImage: "url(" + url + ")",
    backgroundSize: "cover",
    overflow: "hidden"
  },
  button: { margin: theme.spacing.unit }
});
const loadAnimation = () => {
  const logo = document.getElementById("logo");
  logo.classList.add("animated", "fadeIn", "slower");
};

class LandingPage extends React.Component{
 
  componentDidMount() {
    var navLogo = document.getElementById('navLogo');
    navLogo.innerHTML= '';
  }

  render() {
  const { classes } = this.props;
  const sectionStyle = {
    position: 'absolute',
    top: 0,
    left: 0,
    bottom: 0,
    right: 0,
    overflow: "auto",
    width: "100%",
    height: "auto",/* 
    marginLeft: "-10px",
    marginRight: "-10px",
    marginBottom: "-20px", */
    backgroundImage: `url(${backgroundImg})`
  };
  return (
      <MuiThemeProvider theme={theme}>
      <img src={backgroundImg} 
      className='kenburns-right'
      style={{
        position:'fixed',
        top:0,
        right:0,
        bottom:0,
        overflow:'hidden',
        zIndex: '-1',
        marginTop: '-10px',
        marginLeft: '-30px',
        objectFit: 'cover'
      }}></img>
        <div
          className={`${classes.root} back`}
          style={{
            position:'fixed',
            top: 0,
            left:0,
            right:0,
          }}
          onLoad={loadAnimation}
        >
          <Navbar />
          <figure
            id="logo"
            style={{
              width: "200px",
              height: "120px",
              display: "inline-block",
              paddingTop: "2%"
            }}
          >
            <img
              src={logo}
              alt="Logo"
              style={{
                height: "auto",
                width: "100%"
              }}
            />
          </figure>
          <div
            id="logo"
            className="tracking-in-expand"
            style={{
              fontFamily: "Roboto",
              textAlign: "center",
              fontSize: "40px",
              fontWeight: "300",
              color: "#fff",
              letterSpacing: "6px",
              paddingLeft: "10px",
              paddingTop: "3%"
            }}
          >
            QUAZAPP
          </div>
          <div
            style={{
              fontFamily: "Roboto",
              textAlign: "center",
              paddingLeft: "35%",
              paddingRight: "35%",
              fontSize: "25px",
              fontWeight: "100",
              color: "#fff",
              paddingTop: "2%",
            }}
            onMouseOver={hide}
            onMouseOut={show}
          >
            {wiseWords.quote}
          </div>
          <div
            style={{
              paddingTop: "3%"
            }}
          >
            <LoginPage buttonClicked="getStarted" />
          </div>
          <div
            style={{
              paddingTop: "5%",
              color: "#fff"
            }}
            id="footer"
          >
            <span
              style={{
                fontFamily: "Titillium Web",
                fontStyle: "normal",
                fontWeight: 200,
                fontSize: "15px",
                paddingRight: "3px"
              }}
            >
              | be
            </span>
            <span
              style={{
                fontFamily: "Titillium Web",
                fontStyle: "normal",
                fontWeight: "normal",
                fontSize: "15px",
                paddingRight: "3px"
              }}
            >
              smart
            </span>
            <span
              style={{
                fontFamily: "Titillium Web",
                fontStyle: "normal",
                fontWeight: 200,
                fontSize: "15px"
              }}
            >
              at learning |
            </span>
          </div>
        </div>
      </MuiThemeProvider>
  );
  }
}


LandingPage.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(LandingPage);
