import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import proptypes from "prop-types";
import { getUsers } from "../../actions/Users";

export class Users extends Component {
  static proptypes = {
    Users: proptypes.array.isRequired,
    getUsers: proptypes.func.isRequired
  };

  componentDidMount() {
    this.props.getUsers();
  }

  render() {
    return (
      <Fragment>
        <h1>Users list</h1>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>USERNAME</th>
              <th>EMAIL</th>
              <th>DOB</th>
              <th>MOBILE NO</th>
            </tr>
          </thead>
          <tbody>
            {this.props.Users.map(User => (
              <tr key={User.id}>
                <td>{User.user_data.id}</td>
                <td>{User.user_data.username}</td>
                <td>{User.user_data.email}</td>
                <td>{User.dob}</td>
                <td>{User.mobile_no}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  Users: state.Users.Users
});

export default connect(
  mapStateToProps,
  { getUsers }
)(Users);
