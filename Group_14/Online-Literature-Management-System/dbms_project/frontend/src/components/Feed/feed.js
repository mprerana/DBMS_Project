import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import proptypes from "prop-types";

import { getfeed } from "../../actions/feed";
import { getworkdetails } from "../../actions/workdetails";
import { Link } from "react-router-dom";


export class Feed extends Component {
  static proptypes = {
    feed: proptypes.object.isRequired,
    getfeed: proptypes.func.isRequired,
    auth: proptypes.object.isRequired
  };

  componentDidMount() {
    const { user } = this.props.auth;
    this.props.getfeed(user.id);
    this.interval = setInterval(() => this.props.getfeed(user.id), 1000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  render() {
    return (
      <Fragment>
        {this.props.feed.map(work => (
          <div
            className="col-4"
            key={work.timestamp}
            style={{ paddingTop: "3vh", paddingBottom: "3vh" }}
          >
            <img
              src={work.thumbnail}
              alt="thumbnail"
              style={{
                borderTopLeftRadius: "7px",
                borderTopRightRadius: "7px",
                width: "100%"
              }}
            />
            <div
              style={{
                borderBottomLeftRadius: "7px",
                borderBottomRightRadius: "7px",
                backgroundColor: "#e6e6e6",
                paddingLeft: "7px",
                paddingBottom: "20px"
              }}
            >
              <a
                className="booktitle"
                onClick={this.props.getworkdetails.bind(this, work.id)}
                style={{
                  color: "black",
                  border: "none",
                  backgroundColor: "#e6e6e6"
                }}
                href={`#/literature/workdetails/${work.id}/`}
              >
                {work.work_title}
              </a>
              <div className="bauthor" style={{ textAlign: "right" }}>
                -{work.author}&nbsp;&nbsp;
              </div>
              <div className="buploader">Uploaded by {work.user}</div>
              {/* <div className="btime">time: {work.timestamp}</div> */}
              {/* file: {work.file} */}
            </div>
          </div>
        ))}

      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  feed: state.feed.feed,
  auth: state.auth,
  workdetails: state.workdetails.workdetails
});

export default connect(
  mapStateToProps,
  { getfeed, getworkdetails }
)(Feed);
