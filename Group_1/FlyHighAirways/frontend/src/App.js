import React, { Component } from "react";
import { Route, Switch, withRouter, BrowserRouter } from "react-router-dom";

import { Provider } from "react-redux";
import { createStore, applyMiddleware, compose } from "redux";
import thunk from "redux-thunk";
import { connect } from "react-redux";

import { authCheckStatus } from "./store/actions/index";

import "antd/dist/antd.css";

import FlightSearch from "./containers/FlightSearch/FlightSearch";
import Auth from "./containers/Auth/Auth";
import CheckIn from "./containers/CheckIn/CheckIn";
import FlightBook from "./containers/FlightBook/FlightBook";
import HomePage from "./containers/Homepage/Hompage";
import Navbar from "./components/Header/Header";
import Footer from "./components/Footer/Footer";

import { APIKEY } from "./Keys/GoogleApiKey";
import axios from "axios";
import DashBoard from "./containers/DashBoard/DashBoard";

// import Navbar from "./components/UI/Navbar/navbar";

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const store = createStore(
  composeEnhancers,
  composeEnhancers(applyMiddleware(thunk))
);

class App extends Component {
  state = {
    flightInfo: {
      source: "",
      destination: "",
      date: ""
    },
    selectedFlight: null,
    auth: {
      tokenId: null,
      email: null
    }
  };

  componentDidMount() {
    this.props.autoSignUpHandler();
  }

  onFormSubmit = data => {
    this.setState({ flightInfo: data });
  };

  onFlightSelect = data => {
    console.log(data);
    this.setState({ selectedFlight: data });
  };

  onAuthSubmit = data => {
    // let url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=";

    let url = "http://localhost:5000/auth/login";

    if (data.isSignUp) {
      // url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=";

      url = "http://localhost:5000/auth/register";
    }

    axios
      .post(`${url}`, data.auth)
      .then(response => {
        const expirationTime = new Date(
          new Date().getTime() + response.data.expiresIn * 1000
        );

        const authData = {
          idToken: response.data.tokens.access,
          email: data.auth.email
        };
        this.setState({ auth: authData });

        // localStorage.setItem("token", response.data.idToken);
        // localStorage.setItem("expirationTime", expirationTime);
        // localStorage.setItem("userId", response.data.localId);
      })
      .catch(err => {
        console.log(err.response);
      });
  };

  render() {
    //*   This are components with props used only to pass in Route

    const HomePageWithProps = props => {
      return <HomePage origin="homepage" formFill={this.onFormSubmit} />;
    };

    const FlightSearchWithProps = props => {
      return (
        <FlightSearch
          auth={this.state.auth}
          flightInfo={this.state.flightInfo}
          flightSelect={this.onFlightSelect}
          formFill={this.onFormSubmit}
        />
      );
    };

    const FlightFormWithProps = props => {
      return (
        <FlightBook
          selectedFlight={this.state.selectedFlight}
          auth={this.state.auth}
        />
      );
    };

    const AuthFormWithProps = props => {
      return <Auth onAuthSubmit={this.onAuthSubmit} />;
    };

    const onLogout = props => {
      this.setState({ auth: null });
    };

    //* This is components with props

    return (
      <React.Fragment>
        <Provider store={store}>
          <BrowserRouter>
            <Navbar isAuth={this.state.auth.email} onLogout={this.onLogout} />
            <Switch>
              <Route path="/" exact render={HomePageWithProps} />
              <Route path="/flights" render={FlightSearchWithProps} />
              <Route path="/book-flight" render={FlightFormWithProps} />
              <Route path="/authenticate" render={AuthFormWithProps} />
              <Route path="/checkIn" component={CheckIn} />
              <Route path="/dashboard" component={DashBoard} />
            </Switch>
            <Footer />
          </BrowserRouter>
        </Provider>
      </React.Fragment>
    );
  }
}

const mapDispatchToProps = dispatch => {
  return {
    autoSignUpHandler: () => dispatch(authCheckStatus())
  };
};

const mapStateToProps = state => {
  return {
    isAuthenticated: state.auth.token !== null
  };
};

export default withRouter(
  connect(
    mapStateToProps,
    mapDispatchToProps
  )(App)
);
