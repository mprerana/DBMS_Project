import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getlists, deletelist } from "../../actions/lists";
import { getworks, deletework } from "../../actions/works";
import { Link } from "react-router-dom";

export class myreadingliststable extends Component {
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
        <table className="table table-striped">
          <thead>
            <tr id="wtext1">
              <th>ID</th>
              <th>TITLE</th>
              {/* <th>USER</th> */}
              <th> </th>
            </tr>
          </thead>
          <tbody>
            {this.props.lists.map(list => (
              <tr key={list.id}>
                <td>{list.id}</td>
                <td onClick={this.props.getworks.bind(this, list.id)}>
                  <Link to={`/literature/readinglist/${list.id}`}>
                    {" "}
                    {list.r_list_name}
                  </Link>
                </td>
                {/* <td>{list.related_user_id}</td> */}
                <td>
                  {/* <button
                    //   onClick={this.props.deletelist.bind(this, list.id)}
                    className="btn btn-outline-primary btn-sm"
                  > */}
                    {/* <i className="fa fa-pen" />
                    &nbsp;Edit */}
                  {/* </button> */}
                  &nbsp;&nbsp;&nbsp;
                  <button
                    onClick={this.props.deletelist.bind(this, list.id)}
                    className="btn btn-outline-danger btn-sm"
                  >
                    <i className="fa fa-trash-alt" />
                    &nbsp;Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
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
)(myreadingliststable);
