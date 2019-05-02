import React, { Component } from "react";
/* import signupimg from "../images/signup-image.jpg"; */
import { error } from "util";
// import RadioButtonGroup from "./RadioButtonGroup";
import PropTypes from "prop-types";
import {
  withStyles,
  MuiThemeProvider,
  createMuiTheme
} from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";
import Paper from "@material-ui/core/Paper";
import signupimg from "./images/signup-image.jpg";
// import "./css/style.css";
import "materialize-css";
import "typeface-roboto";
import Typography from "@material-ui/core/Typography";
import AccountCircle from "@material-ui/icons/AccountCircle";
import TextField from "@material-ui/core/TextField";
import InputField from "./InputField";
import blue from "@material-ui/core/colors/blue";

const styles = theme => ({
  root: {
    display: "flex"
  },
  container: {
    background: "#fff",
    paddingLeft: "20%",
    paddingRight: "20%"
  },
  margin: {
    margin: theme.spacing.unit
  }
});

const theme = createMuiTheme({
  palette: {
    primary: blue,
    secondary: {
      main: "#f44336"
    }
  }
});

class Signup extends Component {
  state = {
    oldusers: this.props.users,
    name: "",
    email: "",
    password: "",
    confPassword: "",
    validData: true
  };

  sendData = async (url, data) => {
    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
      });
      const responseJson = await response.json();
      return responseJson.success;
    } catch (error) {
      console.error(error);
    }
  };

  handleSubmit = e => {
    e.preventDefault(); //prevents reload when submit
    var regExpEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var regExpName = /^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$/u;

    //valid email
    if (regExpEmail.test(this.state.email)) {
      console.log("valid email");
    } else {
      console.log("invalid email");
      this.setState({
        validData: false
      });
    }

    //valid password
    if (
      this.state.password.length > 0 &&
      this.state.password.length <= 30 &&
      this.state.password === this.state.confPassword
    ) {
      console.log("Password valid");
      console.log(this.state.password, this.state.confPassword);
    } else {
      console.log("Password Invalid");
      this.setState({
        validData: false
      });
      console.log(this.state.password, this.state.confPassword);
    }

    //valid name
    if (
      regExpName.test(this.state.name) &&
      this.state.name.length > 0 &&
      this.state.name.length <= 50
    ) {
      console.log("Name valid");
    } else {
      console.log("Name Invalid");
      console.log(this.state.name);
      this.setState({
        validData: false
      });
    }
    console.log(this.props.users);
    console.log(
      this.state.name,
      this.state.email,
      this.state.password,
      this.state.confPassword
    );

    //email must be unique
    for (var i = 0; i < this.state.oldusers.length; i++) {
      console.log(this.state.oldusers[i]["email"], this.state.email);
      var emailCheck = this.state.oldusers[i]["email"] === this.state.email;
      console.log(emailCheck);
      if (emailCheck) {
        this.setState(
          {
            validData: false
          },
          () => {
            console.log(this.state.validData);
          }
        );
        break;
      }
    }
    if (this.state.validData) {
      this.props.addUser({
        name: this.state.name,
        email: this.state.email,
        password: this.state.password
      });
      this.sendData("http://10.0.36.104:8000/api/auth/register", this.state);
    }
  };

  handleChange = e => {
    //console.log(e.target.id);
    this.setState(
      {
        [e.target.id]: e.target.value
      },
      () => {
        //console.log(this.state);
      }
    );
  };

  render() {
    const { classes } = this.props;

    return (
      <section>
        <div className={classes.container}>
          <div className="signup-content">
            <div className="signup-form">
              <Typography component="h2" variant="display2" gutterBottom>
                Sign Up
                {/* <h2 className="form-title">Sign up</h2> */}
              </Typography>
              <form
                method="POST"
                className="register-form"
                id="register-form"
                onSubmit={this.handleSubmit}
              >
                <div className="form-group">
                  <MuiThemeProvider theme={theme}>
                    <div className={classes.margin}>
                      <Grid container spacing={8} alignItems="flex-end">
                        <Grid item>
                          <AccountCircle />
                        </Grid>
                        <Grid item>
                          <TextField
                            id="input-with-icon-grid"
                            label="With a grid"
                          />
                        </Grid>
                      </Grid>
                    </div>
                  </MuiThemeProvider>
                  {/* <label for="name">
                    <i className="zmdi zmdi-account material-icons-name" />
                  </label>
                  <input
                    type="text"
                    name="name"
                    id="name"
                    placeholder="Your Name"
                    onChange={this.handleChange}
                  /> */}
                </div>
                <div className="form-group">
                  <label for="email">
                    <i className="zmdi zmdi-email" />
                  </label>
                  <input
                    type="email"
                    name="email"
                    id="email"
                    placeholder="Your Email"
                    onChange={this.handleChange}
                  />
                </div>
                <div className="form-group">
                  <label for="pass">
                    <i className="zmdi zmdi-lock" />
                  </label>
                  <input
                    type="password"
                    name="password"
                    id="password"
                    placeholder="Password"
                    onChange={this.handleChange}
                  />
                </div>
                <div className="form-group">
                  <label for="re-pass">
                    <i className="zmdi zmdi-lock-outline" />
                  </label>
                  <input
                    type="password"
                    name="confPassword"
                    id="confPassword"
                    placeholder="Repeat your password"
                    onChange={this.handleChange}
                  />
                </div>
                <div className="form-group" />
                <div className="form-group">
                  <input
                    type="checkbox"
                    name="agree-term"
                    id="agree-term"
                    className="agree-term"
                  />
                  <label for="agree-term" className="label-agree-term">
                    <span>
                      <span />
                    </span>
                    I agree all statements in{" "}
                    <a href="#" className="term-service">
                      Terms of service
                    </a>
                  </label>
                </div>
                <div className="form-group form-button">
                  <input
                    type="submit"
                    name="signup"
                    id="signup"
                    className="form-submit"
                    value="Register"
                  />
                </div>
              </form>
            </div>
            <div class="signup-image">
              <figure>
                <img src={signupimg} alt="sing up image" />
              </figure>
              <a href="#" class="signup-image-link">
                I am already member
              </a>
            </div>
          </div>
        </div>
      </section>
    );
  }
}

Signup.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(Signup);
