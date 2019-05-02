import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
import {
  HashRouter as Router,
  Route,
  Switch,
  Redirect
} from "react-router-dom";
import { Provider as AlertProvider } from "react-alert";
import AlertTemplate from "react-alert-template-oldschool-dark";
import Header from "./layout/Header";
import Dashboard from "./Users/Dashboard";
import Follower_Dashboard from "./Followers/Follower_Dashboard";
import AllBlogs from "./AllBlogs/allblogs";
import Blog_Dashboard from "./Blog/Blog_Dashboard";
import Literature from "./Literature/Literature_Dashboard";
import Listworks from "./Listworks/Listworks_Dashboard";
import Workdetails from "./workdetails/workdetails";
import Allworks from "./allworks/allworks";
import Upload from "./Upload/Upload_dashboard";
import My_uploads from "./Upload/My_uploads";
import Profile from "./Profile/Profile_Dashboard";
import Alerts from "./layout/Alerts";
import Login from "./accounts/Login";
import Register from "./accounts/Register";
import PrivateRoute from "./common/PrivateRoute";
import { Provider } from "react-redux";

import store from "../store";
import { loadUser } from "../actions/auth";
import search from "./search/search";
import FrontPage from "./front_page/FrontPage";
import Home_page from "./home_page/Home_page";
import Profile_page from "./Profile/Profile_page";
import Full_list from "./Upload/Full_list";
import PDFViewer_1 from "./PDFViewer/PDFViewer_1";
import About from "./About/About_dashboard";
//alert options

const alertOptions = {
  timeout: 3000,
  position: "bottom right"
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
              <Alerts />
              <Switch>
                <Route exact path="/" component={FrontPage} />
                <Route exact path="/login" component={Login} />
                <Route exact path="/register" component={Register} />
                <PrivateRoute exact path="/home" component={Home_page} />
                <PrivateRoute exact path="/profile" component={Profile_page} />
                <PrivateRoute exact path="/profile_edit" component={Profile} />
                <PrivateRoute exact path="/my_uploads" component={My_uploads} />
                <PrivateRoute exact path="/full_list" component={Full_list} />
                <PrivateRoute exact path="/allblogs" component={AllBlogs} />
                <PrivateRoute
                  exact
                  path="/pdfview/:bookLink"
                  component={PDFViewer_1}
                />
                <PrivateRoute exact path="/search" component={search} />
                <PrivateRoute exact path="/about" component={About} />
                <PrivateRoute
                  exact
                  path="/reading_lists"
                  component={Literature}
                />
                <PrivateRoute exact path="/upload" component={Upload} />
                <PrivateRoute
                  exact
                  path="/follower"
                  component={Follower_Dashboard}
                />
                <PrivateRoute
                  exact
                  path="/literature/readinglist/:id"
                  component={Listworks}
                />
                <PrivateRoute
                  exact
                  path="/literature/workdetails/:id"
                  component={Workdetails}
                />
                <PrivateRoute
                  exact
                  path="/bloglist"
                  component={Blog_Dashboard}
                />
              </Switch>
            </Fragment>
          </Router>
        </AlertProvider>
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
