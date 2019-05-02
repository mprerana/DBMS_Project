import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getallworks, addworktolist } from "../../actions/allworks";
import { getworkdetails } from "../../actions/workdetails";
import { Link } from "react-router-dom";

export class Allworks extends Component {
  static PropTypes = {
    allworks: PropTypes.array.isRequired,
    getallworks: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getallworks();
  }

  render() {
    return (
      <Fragment>
        <div
          className="container-fluid"
          style={{ paddingLeft: "5%", paddingRight: "5%" }}
        >
          <div className="row">
            <h4 id="wtext1">All Uploads :</h4>
          </div>

          {this.props.allworks.map(allwork => (
            <div
              className="card"
              style={{ padding: "2%", marginTop: "2%", marginBottom: "2%" }}
            >
              <div className="card-body row">
                <div
                  className="col-2"
                  style={{ borderRight: "2px solid #3bbeb6" }}
                >
                  <img
                    src={allwork.thumbnail}
                    alt="thumbnail"
                    height="240"
                    style={{
                      border: "2px solid #3bbeb6",
                      borderRadius: "5%"
                    }}
                  />
                </div>
                <div className="col-5">
                  <blockquote class="blockquote">
                    {/* link title to ratings page */}
                    <a
                      className="booktitle"
                      onClick={this.props.getworkdetails.bind(this, allwork.id)}
                      style={{ color: "black" }}
                      href={`#/literature/workdetails/${allwork.id}/`}
                    >
                      <i className="fa fa-book fa-sm" />
                      &nbsp;&nbsp;{allwork.work_title}
                    </a>
                    <div className="bauthor blockquote-footer">
                      <i className="fa fa-pen-nib" />
                      &nbsp;&nbsp;{allwork.author}
                    </div>
                  </blockquote>
                  <div className="bgenre">Genre: {allwork.genre}</div>
                  <br />
                  <div
                    className=" card card-body bbio"
                    style={{ borderRadius: "5%", backgroundColor: "#e6e6e6" }}
                  >
                    {allwork.description}
                  </div>
                </div>
                <div className="col-2">
                  <div className="buploader">
                    Uploaded by {allwork.username}
                    {/* {upload.id} */}
                  </div>
                  <div className="btime">{allwork.timestamp}</div>
                </div>
                <div className="col-3">
                <a
                href={allwork.file}
                target="_blank"
                className="btn btn-success btn-sm col-5"
                >
                  
                    <i className="fa fa-book-open" /> Read
                    </a> 
                  &nbsp;|&nbsp;
                  <a
                href={allwork.file}
                target="_blank"
                className="btn btn-success btn-sm col-5"
                >
                    <i className="fa fa-save " /> Download
                    </a>
                  <br />
                  <br />
                  {/* <button
                    // onClick={}
                    className="btn btn-outline-info col-10 btn-sm"
                  >
                    <i className="fa fa-plus" />
                    &nbsp;Add to Read-list
                  </button> */}
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* <h1>All Works</h1>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>TITLE</th>
              <th>UPLOADER</th>
              <th>AUTHOR</th>
              <th>ADD</th>
            </tr>
          </thead>
          <tbody>
            {this.props.allworks.map(allwork => (
              <tr key={allwork.id}>
                <td>{allwork.id}</td>
                <td>{allwork.work_title}</td>
                <td>{allwork.uploader_id}</td>
                <td>{allwork.author}</td>
                <td>
                  <button
                    onClick={this.props.addworktolist.bind(this, allwork.id)}
                    className="btn btn-success"
                  >
                    <span className="fa fa-plus" />
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table> */}
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  allworks: state.allworks.allworks,
  workdetails: state.workdetails.workdetails
});

export default connect(
  mapStateToProps,
  { getallworks, addworktolist, getworkdetails }
)(Allworks);
