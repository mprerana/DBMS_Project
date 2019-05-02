import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getBlog, deleteBlog } from "../../actions/Blog";

export class Blog extends Component {
  static PropTypes = {
    Blog: PropTypes.array.isRequired,
    getBlog: PropTypes.func.isRequired,
    auth: PropTypes.object.isRequired,
    deleteBlog: PropTypes.func.isRequired
  };

  componentDidMount() {
    const { user } = this.props.auth;
    //console.log(user.id);

    this.props.getBlog(user.id);
  }

  render() {
    return (
      <Fragment>
        <div className="container">
          <div className="card" style={{ padding: "2%" }}>
            <div className="card-body">
              <h4>Blogs :</h4>
              <br />
              {this.props.Blog.map(Blog => (
                <div
                  className="card"
                  key={Blog.id}
                  style={{ marginBottom: "30px" }}
                >
                  <div className="card-header">
                    <div className="row">
                      <div className="col-11">{Blog.blog_title}</div>
                      <div className="col-11">{Blog.timestamp}</div>
                      <div className="col-1">
                        <button
                          onClick={this.props.deleteBlog.bind(this, Blog.id)}
                          className="btn btn-outline-danger"
                        >
                          <i className="fa fa-trash-alt " />
                        </button>
                      </div>
                    </div>
                  </div>
                  {/* {Blog.id} */}
                  <div className="card-body">
                    {Blog.blog_content}
                    {/* {Blog.timestamp} */}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  Blog: state.Blog.Blog,
  auth: state.auth
});

export default connect(
  mapStateToProps,
  { getBlog, deleteBlog }
)(Blog);
