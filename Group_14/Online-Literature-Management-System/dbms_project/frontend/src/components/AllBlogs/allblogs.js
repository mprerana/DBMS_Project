import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getallblogs } from "../../actions/allblogs";
import { Link } from "react-router-dom";

export class Search extends Component {
  static PropTypes = {
    allblogs: PropTypes.array.isRequired,
    getallblogs: PropTypes.func.isRequired
  };

  componentDidMount() {
    const { user } = this.props.auth;
    this.props.getallblogs(user.id);
  }

  render() {
    return (
      <Fragment>
        {this.props.allblogs.map(allblog => (
          // <tr key={allblog.id}>
          //   <td />
          //   <td>{allblog.id}</td>
          //   <td>
          //     {allblog.blog_title}
          //     {/* <Link to={`/literature/workdetails/${allwork.id}/`} />3 */}
          //   </td>
          //   <td>{allblog.blog_content}</td>
          //   <td>{allblog.timestamp}</td>
          //   <td>{allblog.uploader_id}</td>
          // </tr>
          <div
            className="card"
            key={allblog.id}
            style={{ marginBottom: "30px", border: "none" }}
          >
            <div
              className="card-header"
              style={{ backgroundColor: "#27bedb", color: "white" }}
            >
              <div className="row">
                <div className="col-6">{allblog.blog_title}</div>
                &nbsp;&nbsp;&nbsp;&nbsp;
                By <div className="col-2">{allblog.username}</div>
                at <div className="col-4">{allblog.timestamp}</div>
              </div>
            </div>
            {/* {allblog.id} */}
            <div className="card-body" style={{ fontFamily: "Quicksand" }}>
              {allblog.blog_content}
              {/* {Blog.timestamp} */}
            </div>
            <br />
            <br />
          </div>
        ))}
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  allblogs: state.allblogs.allblogs,
  auth: state.auth
});

export default connect(
  mapStateToProps,
  { getallblogs }
)(Search);
