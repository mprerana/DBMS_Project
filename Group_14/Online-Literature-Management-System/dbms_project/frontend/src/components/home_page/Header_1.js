import React, { Component, Fragment } from "react";
import { Link } from "react-router-dom";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { logout } from "../../actions/auth";
import "./Header_1.css";

export class Header extends Component {
  static propTypes = {
    auth: PropTypes.object.isRequired,
    logout: PropTypes.func.isRequired
  };

  state = {
    isTop: true
  };

  componentDidMount() {
    document.addEventListener("scroll", () => {
      const isTop = window.scrollY < 75;
      if (isTop !== this.state.isTop) {
        this.setState({ isTop });
      }
    });
  }

  render() {
    const { isAuthenticated, user } = this.props.auth;

    return (
      <Fragment>
        <nav
          id="navscroll"
          className="navbar navbar-expand-sm fixed-top"
          style={{ backgroundColor: this.state.isTop ? "none" : "#e6e6e6ef" }}
        >
          <Link className="navbar-brand" to="/home">
            <img
              src="https://i.ibb.co/BZhz7K2/logo-text.png"
              className="d-inline-block align-top animated flipInX slow"
              width="120"
              height="50"
            />
          </Link>
          <button
            className="navbar-toggler fas fa-caret-square-down"
            type="button"
            data-toggle="collapse"
            data-target="#navbarNavDropdown"
            aria-controls="navbarNavDropdown"
            aria-expanded="false"
            aria-label="Toggle navigation"
          />
          <div
            className="collapse navbar-collapse justify-content-end"
            id="navbarNavDropdown"
          >
            <ul className="navbar-nav">
              <li className="nav-item dropdown">
                <Link
                  className="nav-link animated fadeIn slow"
                  id="appDropdown"
                  role="button"
                  data-toggle="dropdown"
                  aria-haspopup="true"
                  aria-expanded="false"
                  onMouseEnter={this.handleHover}
                  onMouseLeave={this.handleHover}
                >
                  CATALOG
                </Link>
                <div
                  style={{
                    backgroundColor: this.state.isTop ? "none" : "#e6e6e6ef"
                  }}
                  className="dropdown-menu dropdown-menu-center"
                  aria-labelledby="appDropdown"
                >
                  <Link className="dropdown-item" to="/full_list">
                    Full List (A-Z)
                  </Link>
                  <div className="dropdown-divider" />
                  <Link className="dropdown-item" to="/search">
                    Advanced Search
                  </Link>
                  <div className="dropdown-divider" />
                  <Link className="dropdown-item" to="/my_uploads">
                    My Books
                  </Link>
                  <div className="dropdown-divider" />
                  <Link className="dropdown-item" to="/reading_lists">
                    My Reading Lists
                  </Link>
                </div>
              </li>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <li className="nav-item">
                <Link to="/upload" className="nav-link animated fadeIn slow">
                  UPLOAD
                </Link>
              </li>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <li className="nav-item">
                <Link to="/about" className="nav-link animated fadeIn slow">
                  ABOUT
                </Link>
              </li>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <li className="nav-item dropdown">
                <Link
                  className="nav-link animated fadeIn slow"
                  id="profileDropdown"
                  role="button"
                  data-toggle="dropdown"
                  aria-haspopup="true"
                  aria-expanded="false"
                >
                  <i className="fas fa-user-circle" />
                </Link>
                <div
                  style={{
                    backgroundColor: this.state.isTop ? "none" : "#e6e6e6ef"
                  }}
                  className="dropdown-menu dropdown-menu-center"
                  aria-labelledby="profileDropdown"
                >
                  <Link className="dropdown-item" to="/profile">
                    {user ? `Hello ${user.username}!` : ""}
                  </Link>
                  {/* <div className="dropdown-divider" />
                  <Link to="/profile_edit" className="dropdown-item">
                    Edit Profile
                  </Link> */}
                  <div className="dropdown-divider" />
                  <Link to="/follower" className="dropdown-item">
                    Followers
                  </Link>
                  <div className="dropdown-divider" />
                  <Link className="dropdown-item" to="/bloglist">
                    My Blog
                  </Link>
                  <div className="dropdown-divider" />
                  <button onClick={this.props.logout} className="dropdown-item">
                    Logout
                  </button>
                </div>
              </li>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <li className="nav-item">
                <Link to="/search" className="nav-link animated fadeIn slow">
                  <i className="fas fa-search" />
                </Link>
              </li>
              {/* <li className="nav-item">
                <Link to="/follower" className="nav-link">
                  Followers
                </Link>
              </li>
              <li className="nav-item">
                <Link to="/literature" className="nav-link">
                  ReadingList
                </Link>
              </li>
              <li className="nav-item">
                <Link to="/upload" className="nav-link">
                  Upload Book
                </Link>
              </li> */}
            </ul>
          </div>
          {/* {isAuthenticated ? authLinks : guestLinks} */}
        </nav>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  auth: state.auth
});

export default connect(
  mapStateToProps,
  { logout }
)(Header);
