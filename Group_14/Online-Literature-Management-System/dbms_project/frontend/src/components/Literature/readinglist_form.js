import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addlist } from "../../actions/lists";
import { Link } from "react-router-dom";
import "./readinglist_form.css";

export class List_Form extends Component {
  state = {
    r_list_name: "",
    related_user: ""
  };

  static propTypes = {
    addlist: PropTypes.func.isRequired,
    auth: PropTypes.object.isRequired
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmit = e => {
    e.preventDefault();
    const { isAuthenticated, user } = this.props.auth;
    const { r_list_name } = this.state;
    //const list = { r_list_name, related_user: user.id };
    //console.log(list);
    this.props.addlist(r_list_name, user.id);
  };

  render() {
    const { r_list_name } = this.state;
    return (
      <Fragment>
        <div className="container">
          <div className="card" style={{ padding: "2%" }}>
            <div className="card-body">
              <h4 className="row" style={{ textAlign: "center" }}>
                Create a new read-list
              </h4>
              <br />
              <form
                onSubmit={this.onSubmit}
                className="text-center form-group"
                style={{ fontFamily: "Quicksand" }}
              >
                <div className="input-group">
                  <input
                    type="text"
                    className="form-control "
                    placeholder="Enter read-list name"
                    name="r_list_name"
                    onChange={this.onChange}
                    value={r_list_name}
                    style={{
                      borderColor: "#17a2b8"
                    }}
                  />
                  <div className="input-group-append">
                    <button className="btn btn-outline-info" type="submit">
                      Create
                    </button>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  auth: state.auth
});

export default connect(
  mapStateToProps,
  { addlist }
)(List_Form);
