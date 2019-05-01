import React, { Component } from "react";
import { Icon, Input, Button, Row, Col } from "antd";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import axios from "axios";

import classes from "./Auth.module.css";

import * as actions from "../../store/actions/index";

// AeCP7XjbY68kPoHkF4cqS2LWBZ83t1wSFRy6jbEdbGFG4c_m3qI6j_qozn84D8xpTN3ML6opD6XanSgO

class AuthenticateForm extends Component {
  state = {
    authForm: {
      email: {
        elementType: "input",
        elementConfig: {
          type: "email",
          placeholder: "Enter Your Email"
        },
        value: "",
        validation: {
          required: true,
          shouldContain: "@"
        },
        valid: false,
        touched: false
      },
      password: {
        elementType: "input",
        elementConfig: {
          type: "password",
          placeholder: "Enter Your Password"
        },
        value: "",
        validation: {
          required: true,
          minLength: 8
        },
        valid: false,
        touched: false
      }
      // firstName: {
      //     elementType: 'input',
      //     elementConfig: {
      //         type: 'text',
      //         placeholder: 'Enter Your First Name'
      //     },
      //     value: '',
      //     validation: {
      //         required: false,
      //         minLength: 8,
      //     },
      //     valid: false,
      //     touched: false
      // },
      // lastName: {
      //     elementType: 'input',
      //     elementConfig: {
      //         type: 'text',
      //         placeholder: 'Enter Your Last Name'
      //     },
      //     value: '',
      //     validation: {
      //         required: false,
      //         minLength: 8,
      //     },
      //     valid: false,
      //     touched: false
      // }
    },
    isSignUp: true,
    valid: false
  };

  authHandler = event => {
    event.preventDefault();
    // this.props.onAuth(
    //   this.state.authForm.email.value,
    //   this.state.authForm.password.value,
    //   this.state.isSignUp
    // );

    let data = {
      auth: {}
    };
    data.isSignUp = this.state.isSignUp;

    for (const formElement in this.state.authForm) {
      if (this.state.authForm[formElement].valid === false) {
        alert("form can't be submitted!");
        return;
      }
      data.auth[formElement] = this.state.authForm[formElement].value;
    }
    data.auth.returnSecureToken = true;

    this.props.onAuthSubmit(data);
    this.props.history.replace("/");

    this.props.history.push("/");
  };
  // chennai, Indore, Chennai, Kolkata
  //chennai kokllata punnaei  deli indore

  componentDidMount() {
    const flight = {
      source: "Indore",
      destination: "Chennai",
      start_time: "08:00",
      end_time: "10:05",
      date: "22/04/2019",
      logo: "some 2",
      business: {
        fare: 3956,
        seats_remaining: 0
      },
      economy: {
        fare: 4963,
        seats_remaining: 6
      },
      nonStop: true
    };

    // axios.post('https://flyhighairways-2cfb4.firebaseio.com/flight.json', flight)
    //     .then(res => console.log(res))
    //     .catch(err => console.log('there was an ', err));
  }

  switchAuthModeHandler = () => {
    this.setState(prevState => {
      return {
        isSignUp: !prevState.isSignUp
      };
    });

    // Making all values empty

    const updatedAuthForm = { ...this.state.authForm };

    const updatedEmailForm = { ...this.state.authForm.email };
    updatedEmailForm.value = "";
    updatedEmailForm.touched = false;

    updatedAuthForm.email = updatedEmailForm;

    const updatedPassForm = { ...this.state.authForm.password };
    updatedPassForm.value = "";
    updatedPassForm.touched = false;

    updatedAuthForm.password = updatedPassForm;

    this.setState({ authForm: updatedAuthForm });
  };

  checkValidation = (value, rules) => {
    let isValid = true;

    if (rules.required) {
      isValid = isValid && value.trim() !== "";
    }

    if (rules.minLength) {
      isValid = isValid && value.length >= rules.minLength;
    }

    if (rules.shouldContain) {
      isValid = isValid && value.includes(rules.shouldContain);
    }

    return isValid;
  };

  // Function to use ternary operator and find which one of the two (cross/tick) to use
  validSignHandler = inputField => {
    return !this.state.authForm[inputField].touched ? (
      <Icon
        type="check-circle"
        theme="twoTone"
        twoToneColor="#fff"
        className={classes.validateIcon}
      />
    ) : this.state.authForm[inputField].valid ? (
      <Icon
        type="check-circle"
        theme="twoTone"
        twoToneColor="#52c41a"
        className={classes.validateIcon}
      />
    ) : (
      <Icon
        type="close-circle"
        theme="twoTone"
        twoToneColor="#eb2f96"
        className={classes.validateIcon}
      />
    );
  };

  inputChangedHandler = (event, inputIdentifier) => {
    const updatedForm = { ...this.state.authForm };
    const updatedFormElement = { ...updatedForm[inputIdentifier] };
    updatedFormElement.value = event.target.value;
    updatedForm[inputIdentifier] = updatedFormElement;
    updatedForm[inputIdentifier].valid = this.checkValidation(
      event.target.value,
      updatedForm[inputIdentifier].validation
    );
    updatedForm[inputIdentifier].touched = true;

    this.setState({ authForm: updatedForm });
  };

  render() {
    const { authForm } = this.state;

    // LOGIN FORM
    let form = (
      <div className={classes.container}>
        {this.state.isSignUp ? (
          <h4 className={classes.FormText}>Sign Up To Proceed</h4>
        ) : (
          <h4 className={classes.FormText}>Login To Proceed</h4>
        )}
        <form onSubmit={e => this.authHandler(e)}>
          <div className={classes.formDiv}>
            <Input
              className={classes.InputElement}
              prefix={<Icon type="user" style={{ color: "rgba(0,0,0,.25)" }} />}
              type={authForm.email.elementConfig.type}
              placeholder={authForm.email.elementConfig.placeholder}
              value={authForm.email.value}
              onChange={e =>
                this.inputChangedHandler(e, authForm.email.elementConfig.type)
              }
            />
            {this.validSignHandler("email")}
          </div>

          <div className={classes.formDiv}>
            <Input
              className={classes.InputElement}
              prefix={<Icon type="lock" style={{ color: "rgba(0,0,0,.25)" }} />}
              type="password"
              placeholder="Password"
              value={authForm.password.value}
              onChange={e =>
                this.inputChangedHandler(
                  e,
                  authForm.password.elementConfig.type
                )
              }
            />
            {this.validSignHandler("password")}
          </div>
          <div style={{ width: "90%" }}>
            <Button
              htmlType="submit"
              size="default"
              style={{ backgroundColor: "#bdc3c7", border: "none" }}
              block
              shape="round"
            >
              {this.state.isSignUp ? "SIGN UP" : "LOG IN"}
            </Button>
          </div>
        </form>
        {this.state.isSignUp ? (
          <div>
            <h3
              style={{
                paddingTop: "2rem",
                paddingLeft: "4.5rem",
                fontWeight: "bold"
              }}
            >
              Already have an Account ?
            </h3>
          </div>
        ) : (
          <div>
            <h3
              style={{
                paddingTop: "2rem",
                paddingLeft: "5rem",
                fontWeight: "bold"
              }}
            >
              Don't Have an Account ?
            </h3>
          </div>
        )}
        <Button
          size="large"
          className={classes.switchBtn}
          onClick={this.switchAuthModeHandler}
        >
          {this.state.isSignUp ? "LogIn" : "Sign Up"}
        </Button>
      </div>
    );

    return (
      <div className={classes.BigDiv}>
        <div className={classes.LoginCard}>
          <Row style={{ height: "100%" }}>
            <Col lg={12} className={classes.makeHeightFull}>
              <div
                className={[classes.makeHeightFull, classes.planeImg].join(" ")}
              />
            </Col>
            <Col lg={12} className={classes.makeHeightFull}>
              {form}
            </Col>
          </Row>
        </div>
      </div>
    );
  }
}

const mapDispatchToProps = dispatch => {
  return {
    onAuth: (email, password, method) =>
      dispatch(actions.auth(email, password, method))
  };
};

export default withRouter(
  connect(
    null,
    mapDispatchToProps
  )(AuthenticateForm)
);
