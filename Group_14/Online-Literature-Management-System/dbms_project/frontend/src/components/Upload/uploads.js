import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getuploads, deleteuploads } from "../../actions/uploads";
import { getworkdetails } from "../../actions/workdetails";
import "./uploads.css";

export class uploads extends Component {
  static PropTypes = {
    uploads: PropTypes.array.isRequired,
    getuploads: PropTypes.func.isRequired,
    deleteuploads: PropTypes.func.isRequired,
    auth: PropTypes.object.isRequired
  };

  componentDidMount() {
    const { user } = this.props.auth;
    //console.log(user.id);
    console.log(user.id);
    this.props.getuploads(user.id);
  }

  render() {
    return (
      <Fragment>
        {this.props.uploads.map(upload => (
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
                  src={upload.thumbnail}
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
                  <a
                    className="booktitle"
                    onClick={this.props.getworkdetails.bind(this, upload.id)}
                    style={{ color: "black" }}
                    href={`#/literature/workdetails/${upload.id}/`}
                  >
                    <i className="fa fa-book fa-sm" />
                    &nbsp;&nbsp;{upload.work_title}
                  </a>
                  <div className="bauthor blockquote-footer">
                    <i className="fa fa-pen-nib" />
                    &nbsp;&nbsp;{upload.author}
                  </div>
                </blockquote>
                <div className="bgenre">Genre: {upload.genre}</div>
                <br />
                <div
                  className=" card card-body bbio"
                  style={{ borderRadius: "5%", backgroundColor: "#e6e6e6" }}
                >
                  {upload.description}
                </div>
              </div>
              <div className="col-2">
                <div className="btime">Date Added: {upload.timestamp}</div>
              </div>
              <div className="col-3">
                <a
                  href={upload.file}
                  target="_blank"
                  className="btn btn-primary btn-sm col-5"
                >
                  <i className="fa fa-book-open" /> Read
                </a>
                &nbsp;|&nbsp;
                <a
                  href={upload.file}
                  target="_blank"
                  className="btn btn-primary btn-sm col-5"
                >
                
                  <i className="fa fa-save " /> Download
                  </a>
                <br />
                <br />
                <button
                  onClick={this.props.deleteuploads.bind(this, upload.id)}
                  className="btn btn-outline-danger col-10 btn-sm"
                >
                  <i className="fa fa-trash-alt" />
                  &nbsp;Delete
                </button>
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
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  uploads: state.uploads.uploads,
  auth: state.auth,
  workdetails: state.workdetails.workdetails
});

export default connect(
  mapStateToProps,
  { getuploads, deleteuploads, getworkdetails }
)(uploads);
