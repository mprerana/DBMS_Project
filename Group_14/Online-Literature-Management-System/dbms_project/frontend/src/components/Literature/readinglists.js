import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getlists, deletelist } from "../../actions/lists";
import { getworks, deletework } from "../../actions/works";
import { Link } from "react-router-dom";
import Rltable from "./myreadingliststable";

export class Lists extends Component {
  static PropTypes = {
    lists: PropTypes.array.isRequired,
    getlists: PropTypes.func.isRequired,
    deletelist: PropTypes.func.isRequired,
    auth: PropTypes.object.isRequired
  };

  componentDidMount() {
    const { user } = this.props.auth;
    //console.log(user.id);

    this.props.getlists(user.id);
  }

  render() {
    return (
      <Fragment>
        <div className="container">
          <div className="card" style={{ padding: "2%" }}>
            <div className="card-body">
              <h4>Your Read-lists</h4>
              <br />
              <Rltable />
            </div>
          </div>
        </div>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  lists: state.lists.lists,
  auth: state.auth,
  works: state.works.works
});

export default connect(
  mapStateToProps,
  { getlists, deletelist, getworks }
)(Lists);
