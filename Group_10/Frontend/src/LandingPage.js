import React from "react";
import "./LandingPage.css";
import styled from "styled-components";
import PropTypes from "prop-types";
import logo from "./components/images/Logo2.png";
import {
  withStyles,
  MuiThemeProvider,
  createMuiTheme
} from "@material-ui/core/styles";
import { blue } from "@material-ui/core/colors";
import Button from "@material-ui/core/Button";

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
      main: "#f44336"
    }
  },
  shadows: ["none"]
});

const styles = theme => ({
  button: { margin: theme.spacing.unit }
});

const LandingPage = props => {
  const { classes } = props;

  return (
    <MuiThemeProvider theme={theme}>
      <div
        style={{
          textAlign: "center"
        }}
      >
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
          style={{
            fontFamily: "Roboto",
            textAlign: "center",
            fontSize: "40px",
            fontWeight: "300",
            color: "#2196f3",
            letterSpacing: "6px",
            paddingLeft: "10px",
            paddingTop: "3%"
          }}
        >
          QUIZAPP
        </div>
        <div
          style={{
            fontFamily: "Roboto",
            textAlign: "center",
            paddingLeft: "35%",
            paddingRight: "35%",
            fontSize: "25px",
            fontWeight: "100",
            color: "#2196f3",
            paddingTop: "2%"
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
          <Button variant="outlined" color="primary" className={classes.button} href="/login">
            Get Started
          </Button>
        </div>
        <div
          style={{
            paddingTop: "5%",
            color: "#2196f3"
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
};

LandingPage.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(LandingPage);
