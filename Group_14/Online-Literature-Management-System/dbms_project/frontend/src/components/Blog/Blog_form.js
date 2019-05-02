import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addBlog } from "../../actions/Blog";

export class Blog extends Component {
  state = {
    blog_title: "",
    blog_content: ""
  };

  static propTypes = {
    addBlog: PropTypes.func.isRequired,
    auth: PropTypes.object.isRequired
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmit = e => {
    e.preventDefault();
    const { isAuthenticated, user } = this.props.auth;
    const { blog_title, blog_content } = this.state;
    this.props.addBlog(blog_title, blog_content, user.id);
  };

  render() {
    const { blog_title, blog_content } = this.state;
    return (
      <Fragment>
        <div className="container">
          <div className="card">
            <div className="card-header">
              <div className="row" style={{ textAlign: "center" }}>
                <h4 className="col-12">
                  WRITE BLOG&nbsp;
                  <i className="fa fa-pen-alt" />
                </h4>
              </div>
            </div>
            <br />
            <div className="card-body">
              <form onSubmit={this.onSubmit}>
                <div className="form-group row">
                  <label className="col-2" id="ut">
                    TITLE :
                  </label>
                  <input
                    type="text"
                    className="form-control col-10"
                    name="blog_title"
                    placeholder="Enter blog title"
                    onChange={this.onChange}
                    value={blog_title}
                  />
                </div>
                <br />
                <div className="row">
                  <label className="col-2" id="ut">
                    CONTENT :
                  </label>
                  <textarea
                    rows={10}
                    className="form-control col-10"
                    name="blog_content"
                    placeholder="Enter blog content"
                    onChange={this.onChange}
                    value={blog_content}
                  />
                </div>

                <div className="row" style={{ padding: "2%" }}>
                  <button
                    className="form-control btn btn-outline-info"
                    type="submit"
                  >
                    Create
                  </button>
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
  Blog: state.Blog.Blog,
  auth: state.auth
});

export default connect(
  mapStateToProps,
  { addBlog }
)(Blog);
