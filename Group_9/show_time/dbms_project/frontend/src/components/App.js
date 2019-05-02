import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";

import { Provider as AlertProvider } from "react-alert";
import AlertTemplate from "react-alert-template-basic";
import {
  HashRouter as Router,
  BrowserRouter as bRouter,
  Route,
  Switch,
  Redirect
} from "react-router-dom";

import Header from "./layout/Header";
import Alerts from "./layout/Alerts";
import List from "./movies/List1";
import SpecificMovie from "./movies/SpecificMovie";
import Seats from "./movies/Seats";
import Snacks from "./movies/Snacks";
import Login from "./accounts/Login";
import Register from "./accounts/Register";
import EditProfile from "./accounts/EditProfile";
import PrivateRoute from "./common/PrivateRoute";
import Payment from "./pages/Payment";
import { loadUser } from "../actions/auth";
import TicketHistoryPage from "./ticketbookinghistory/history";
import TheatrePage from "./bookingpage/theatrepage";

import { Provider } from "react-redux";

import store from "../store";

//Alert Options
const alertOptions = {
  timeout: 3000,
  position: "top center"
};

class App extends Component {
  componentDidMount() {
    store.dispatch(loadUser());
  }

  render() {
    return (
      <Provider store={store}>
        <AlertProvider template={AlertTemplate} {...alertOptions}>
          <Router>
            <Fragment>
              <Header />
              <Alerts />
              <div>
                <Switch>
                  <Route exact path="/" component={List} />
                  <PrivateRoute exact path="/pay" component={Payment} />
                  <Route exact path="/register" component={Register} />
                  <Route exact path="/login" component={Login} />
                  <Route
                    exact
                    path="/specifics/:id/:city_id"
                    component={SpecificMovie}
                  />

                  <Route
                    exact
                    path="/snacks/:city/:theatre_name/:ticket_price"
                    component={Snacks}
                  />
                  <PrivateRoute
                    exact
                    path="/editprofile"
                    component={EditProfile}
                  />
                  <Route
                    exact
                    path="/theatre/:movie_id/:city_id"
                    component={TheatrePage}
                  />
                  <Route
                    exact
                    path="/theatre/seats/:show_id/:theatre_id/:city/:theatre_name"
                    component={Seats}
                  />
                  <Route
                    exact
                    path="/history/:user_id"
                    component={TicketHistoryPage}
                  />
                </Switch>
              </div>
            </Fragment>
          </Router>
        </AlertProvider>
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
