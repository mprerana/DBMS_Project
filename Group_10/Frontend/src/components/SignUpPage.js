import React from "react";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogContentText from "@material-ui/core/DialogContentText";
import DialogTitle from "@material-ui/core/DialogTitle";
import {
  withStyles,
  createMuiTheme,
  MuiThemeProvider
} from "@material-ui/core/styles";
import PropTypes from "prop-types";
import Typography from "@material-ui/core/Typography";
import { grey } from "@material-ui/core/colors";
import InputLabel from "@material-ui/core/InputLabel";
import Input from "@material-ui/core/Input";
import { MenuItem } from "@material-ui/core";
import MaskedInput from "react-text-mask";
import Switch from "@material-ui/core/Switch";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import axios from "axios";
import { Redirect } from 'react-router-dom'
//TODO: Add login success as a snackbar
//TODO: add login fail as a snackbar

const theme = createMuiTheme({
  palette: {
    primary: grey,
    secondary: {
      main: "#f44336"
    }
  },
  cssLabel: {
    "&$cssFocused": {
      color: "#212121"
    }
  },
  cssFocused: {},
  cssUnderline: {
    "&:after": {
      borderBottomColor: "#212121"
    }
  }
});

const styles = theme => ({
  button: {
    margin: theme.spacing.unit
  },
  subtext: {
    paddingBottom: "2%"
  },
  text: {
    paddingTop: "1%",
    paddingBottom: "1%"
  },
  email: {
    color: "#212121"
  },
  switch: {
    paddingLeft: "-1%",
    float: "right"
  }
});

class SignUpPage extends React.Component {
  state = {
    signUpSuccess:false,
    open: false,
    ageError: false,
    validUsername: true,
    validEmail: true,
    validName: true,
    user: {
      username: "",
      name: "",
      password: "",
      passwordConf: "",
      email: "",
      age: 0,
      isTeacher: false
    }
  };

  register = () => {
    const url = "http://10.0.36.104:8000/api/auth/register";
    var self = this;
    axios
      .post(url, this.state.user)
      .then(function(response) {
        self.completeRegister(response);
        // self.completeLogin.bind(response);
        console.log(response.status);
        if (response.status == 200) {
          console.log("object");
          localStorage.setItem('auth-token',response.data.token)
          self.setState({
            signUpSuccess: true})
        } else {
          console.log("Sign up unsuccessfull");
          this.setState({
            loginTryFail: true
          });
        }
        console.log(response);
      })
      .catch(function(error) {
        console.log(error);
      });
  };

  completeRegister = response => {
    if (response.status == 201) {
      console.log("Sign up successfull");
    }
  };

  handleOpen = () => {
    this.setState({
      open: true
    });
  };

  handleClose = () => {
    this.setState({
      open: false
    });
    if (this.props.buttonClicked == "sign up") {
      console.log("sign up closing");
      return this.props.handleMenuClose();
    }
  };

  handleChange = e => {
    this.setState(
      {
        user: { ...this.state.user, [e.target.id]: e.target.value }
      },
      () => {
        // console.log(this.state);
      }
    );
  };

  handleSignUp = e => {
    console.log(this.state.user);
    this.register();
    if (
      !this.state.ageError &&
      this.state.validEmail &&
      this.state.validName &&
      this.state.validUsername &&
      this.state.user.password == this.state.user.passwordConf
    ) {
      console.log("form valid");
    } else {
      console.log("form invalid");
    }
  };

  handleAge = e => {
    this.handleChange(e);
    console.log(e.target.value);
    if (isNaN(e.target.value) || Number(e.target.value) < 0) {
      this.setState({
        ageError: true
      });
    } else {
      this.setState({
        ageError: false
      });
    }
  };

  handlePassword = e => {
    this.handleChange(e);
    if (this.state.user.password != this.state.user.passwordConf) {
      console.log("not equal");
      this.setState({
        passwordConfError: true
      });
    } else {
      console.log("equal");
      this.setState({
        passwordConfError: false
      });
    }
  };

  handleUsername = e => {
    this.handleChange(e);
    if (e.target.value.match(/^[A-Za-z\d_]*$/)) {
      console.log("username valid");
      if (!this.state.validUsername) {
        this.setState({
          validUsername: true
        });
      }
    } else {
      console.log("username invalid");
      if (this.state.validUsername) {
        this.setState({
          validUsername: false
        });
      }
    }
  };

  handleEmail = e => {
    this.handleChange(e);
    console.log(e.target.value);
    if (
      e.target.value.match(
        /^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/
      )
    ) {
      console.log("valid email");
      if (!this.state.validEmail) {
        this.setState({
          validEmail: true
        });
      }
    } else {
      console.log("invalid email");
      if (this.state.validEmail) {
        this.setState({
          validEmail: false
        });
      }
    }
  };

  handleIsTeacher = e => {
    this.setState(
      {
        user: { ...this.state.user, isTeacher: !this.state.user.isTeacher }
      },
      () => {
        console.log(this.state.user);
      }
    );
  };

  handleName = e => {
    this.handleChange(e);
    if (e.target.value.match(/^[a-z ,.'-]+$/i)) {
      if (!this.state.validName) {
        this.setState({
          validName: true
        });
      }
    } else {
      if (this.state.validName) {
        this.setState({
          validName: false
        });
      }
    }
  };

  render() {
    const { classes } = this.props;
    if(this.state.signUpSuccess){
      return <Redirect to='/profile' />
    }
    return (
      <div>
        <MenuItem
          variant="outlined"
          color="inherit"
          className={classes.button}
          onClick={this.handleOpen}
        >
          Sign Up
        </MenuItem>
        <Dialog
          open={this.state.open}
          onClose={this.handleClose}
          aria-labelledby="form-dialog-title"
        >
          <DialogTitle id="form-dialog-title">
            <Typography variant="h5" component="h5">
              Sign Up
            </Typography>
          </DialogTitle>
          <DialogContent>
            <DialogContentText className={classes.subtext}>
              To start your journey login here.
            </DialogContentText>
            <MuiThemeProvider theme={theme}>
              <TextField
                className={[classes.margin, classes.text].join(" ")}
                error={!this.state.validUsername}
                label="Username"
                id="username"
                autoFocus
                fullWidth
                type="name"
                onChange={this.handleUsername}
                placeholder="Only alphabets, numbers and underscore allowed"
              />
              <TextField
                className={[classes.margin, classes.text].join(" ")}
                error={!this.state.validName}
                label="Name"
                id="name"
                autoFocus
                fullWidth
                type="name"
                onChange={this.handleName}
              />
              <TextField
                className={[classes.margin, classes.text].join(" ")}
                error={!this.state.validEmail}
                label="Email"
                id="email"
                autoFocus
                fullWidth
                type="email"
                onChange={this.handleEmail}
              />
              <TextField
                className={[classes.margin, classes.text].join(" ")}
                label="Password"
                id="password"
                autoFocus
                fullWidth
                type="password"
                onChange={this.handlePassword}
              />
              <TextField
                error={this.state.user.passwordConf != this.state.user.password}
                className={[classes.margin, classes.text].join(" ")}
                label=" Repeat Password"
                id="passwordConf"
                autoFocus
                fullWidth
                type="password"
                onChange={this.handlePassword}
              />
              <TextField
                error={this.state.ageError}
                className={[classes.margin, classes.text].join(" ")}
                label="Age"
                id="age"
                autoFocus
                fullWidth
                type="text"
                onChange={this.handleAge}
              />
              <FormControlLabel
                label="Create account as a teacher"
                control={
                  <Switch
                    checked={this.state.user.isTeacher}
                    color="secondary"
                    id="isTeacher"
                    onChange={this.handleIsTeacher}
                    className={classes.switch}
                  />
                }
              />
              {/* <Typography
                className={classes.text}
                style={{
                  color: "#616161"
                }}
              >
                 <Switch
                  checked={this.state.user.isTeacher}
                  color="secondary"
                  id="isTeacher"
                  onChange={this.handleIsTeacher}
                  className={classes.switch}
                />
              </Typography> */}
            </MuiThemeProvider>
          </DialogContent>
          <DialogActions>
            <Button onClick={this.handleClose} color="default">
              Cancel
            </Button>
            <Button
              // onClick={this.handleClose}
              color="default"
              onClick={this.handleSignUp}
            >
              Sign Up
            </Button>
          </DialogActions>
        </Dialog>
      </div>
    );
  }
}
SignUpPage.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(SignUpPage);
