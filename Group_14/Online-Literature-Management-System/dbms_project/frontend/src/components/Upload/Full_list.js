import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getallworks } from "../../actions/allworks";
import "./uploads.css";
import Header_1 from "../home_page/Header_1";
import Allworkslist from "../allworks/allworks";

export class Full_list extends Component {
  static PropTypes = {
    allworks: PropTypes.array.isRequired,
    getallworks: PropTypes.func.isRequired,
    auth: PropTypes.object.isRequired
  };

  componentDidMount() {
    const { user } = this.props.auth;
    this.props.getallworks();
  }

  render() {
    return (
      <Fragment>
        <Header_1 />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <Allworkslist />
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  allworks: state.allworks.allworks,

  auth: state.auth
});

export default connect(
  mapStateToProps,
  { getallworks }
)(Full_list);
