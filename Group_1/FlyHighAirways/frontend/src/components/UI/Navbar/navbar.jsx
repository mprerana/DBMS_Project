import React, { Component } from "react";
import { NavLink } from "react-router-dom";
import { withRouter } from 'react-router-dom';
import { connect } from 'react-redux';

import { logout } from '../../../store/actions/index';

class NavBar extends Component {
  
  state = {
      isAuthenticated: null
  }

  onLogoutHandler = () => {
    this.props.onLogout();
  }


  render() {
  

    return (
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <NavLink className="navbar-brand" to="/">
          FLyHigh
        </NavLink>
        <button
          className="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon" />
        </button>

        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav mr-auto">
            <li className="nav-item">
              <NavLink className="nav-link" to="/movies">
                Flights
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/checkIn">
                CheckIN
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/rentals">
                Contact
              </NavLink>
            </li>
            <li className="nav-item">
              {this.props.isAuth 
                  ? (
                      <NavLink 
                        className="nav-link" 
                        to="/logout"
                        onClick={this.onLogoutHandler}>
                        LogOut
                      </NavLink>
                  )
                  : (
                      <NavLink className="nav-link" to="/authenticate">
                        Login
                      </NavLink>
                  )    
              }
            </li>
          </ul>
        </div>
      </nav>
    );

  }
};


const mapDispatchToProps = dispatch => {
  return {
    onLogout: () => dispatch(logout())
  };
};


export default withRouter(connect(null, mapDispatchToProps)(NavBar));
