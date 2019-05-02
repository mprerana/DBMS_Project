import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import {
  getworkdetails,
  addRating,
  addReview
} from "../../actions/workdetails";
import { createMessage } from "../../actions/messages";
import "./workdetails.css";
import Header_1 from "../home_page/Header_1";
//import PDFJSBackend from '../../backends/pdfjs';
//import PDFViewer from '../PDFViewer/PDFViewer';

export class Workdetails extends Component {
  static PropTypes = {
    workdetails: PropTypes.object.isRequired,
    getworkdetails: PropTypes.func.isRequired,
    addRating: PropTypes.func.isRequired,
    addReview: PropTypes.func.isRequired,
    createMessage: PropTypes.func.isRequired
  };

  state = {
    rating: 0,
    review: "",
    flag: 0,
    allreviews: false,
    allratings: false,
    yourreview: false,
    yourrating: false,
    showBook: false
  };

  showAllRatings = e => {
    this.setState({
      allratings: true,
      yourrating: false,
      allreviwes: false,
      yourreview: false
    });

    this.setState({ flag: 1 });
  };

  showYourRating = e => {
    this.setState({
      allratings: false,
      yourrating: true,
      allreviwes: false,
      yourreview: false
    });

    this.setState({ flag: 1 });
  };

  showAllReviews = e => {
    this.setState({
      allratings: false,
      yourrating: false,
      allreviews: true,
      yourreview: false
    });

    this.setState({ flag: 1 });
  };

  showYourReview = e => {
    this.setState({
      allratings: false,
      yourrating: false,
      allreviews: false,
      yourreview: true
    });

    this.setState({ flag: 1 });
  };

  componentDidMount() {}

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmitRating = e => {
    e.preventDefault();

    const { rating } = this.state;
    console.log(rating);

    if (rating > 5 || rating < 0) {
      this.props.createMessage({
        invalidrating: "Invalid Rating"
      });

      return;
    }

    let flag = 0;
    for (var i = 0; i < this.props.workdetails.allratings.length; i++) {
      if (
        this.props.auth.user.username ===
        this.props.workdetails.allratings[i].user
      ) {
        flag = 1;
        break;
      }
    }

    if (flag) {
      this.props.createMessage({
        alreadyRated: "You have already rated"
      });

      return;
    }

    const ratings = {
      addrating: {
        rating: rating,
        book_id: this.props.workdetails.id
      }
    };

    this.props.addRating(this.props.auth.user.id, ratings);

    this.setState({ flag: 1 });

    const currentrating = {
      id: 2234645,
      rating: rating,
      user: this.props.auth.user.username
    };

    this.setState({
      rating: 0,
      flag: 0
    });

    this.props.workdetails.allratings = [
      ...this.props.workdetails.allratings,
      currentrating
    ];

    console.log(this.props.workdetails.allratings);
  };

  onSubmitReview = e => {
    e.preventDefault();

    const { review } = this.state;

    let flag = 0;

    for (var i = 0; i < this.props.workdetails.allreviews.length; i++) {
      if (
        this.props.auth.user.username ===
        this.props.workdetails.allreviews[i].user
      ) {
        flag = 1;
        break;
      }
    }

    if (flag) {
      this.props.createMessage({
        alreadyReviewed: "You have already reviewed"
      });

      return;
    }

    const reviews = {
      addreview: {
        content: review,
        book_id: this.props.workdetails.id
      }
    };

    this.props.addReview(this.props.auth.user.id, reviews);
    this.setState({ flag: 1 });

    const currentreview = {
      id: 2637675,
      content: review,
      user: this.props.auth.user.username
    };

    this.setState({
      review: "",
      flag: 0
    });

    this.props.workdetails.allreviews = [
      ...this.props.workdetails.allreviews,
      currentreview
    ];
  };

  render() {
    const { rating, review } = this.state;
    let totalrating = 0;
    let noofratings = 0;

    {
      this.props.workdetails.allratings
        ? this.props.workdetails.allratings.forEach(rating => {
            totalrating = totalrating + rating.rating;
            noofratings = noofratings + 1;
          })
        : null;
    }

    let avgrating = 0;

    if (this.props.workdetails.allratings) {
      avgrating = totalrating / noofratings;
    }
    avgrating = Math.round(avgrating * 100) / 100;

    let currentuserrating =
      this.props.workdetails.allratings && this.props.auth.user
        ? this.props.workdetails.allratings.filter(
            rating => rating.user === this.props.auth.user.username
          )
        : null;

    console.log(`hii ${currentuserrating}`);

    if (currentuserrating) {
      console.log(currentuserrating.length);
    }

    let currentuserreview =
      this.props.workdetails.allreviews && this.props.auth.user
        ? this.props.workdetails.allreviews.filter(
            comment => comment.user === this.props.auth.user.username
          )
        : null;

    if (currentuserreview) {
      console.log(currentuserreview.length);
    }
    const { showBook } = this.state;

    return (
      <Fragment>
        <Header_1 />
        <br />
        <br />
        <br />
        <br />
        <div className="container">
          <div
            className="card"
            style={{ padding: "2%", marginTop: "2%", marginBottom: "2%" }}
          >
            <div className="card-body row">
              <div
                className="col-3"
                style={{ borderRight: "2px solid #3bbeb6" }}
              >
                <img
                  src={this.props.workdetails.thumbnail}
                  //src="http://www.jameshmayfield.com/wp-content/uploads/2015/03/defbookcover-min.jpg"
                  width="200"
                  alt="thumbnail"
                  style={{
                    border: "2px solid #3bbeb6",
                    borderRadius: "5%"
                  }}
                />
              </div>
              <div
                className="col-7"
                style={{ borderRight: "2px solid #3bbeb6" }}
              >
                <blockquote className="blockquote">
                  <div className="booktitle">
                    <i className="fa fa-book fa-sm" />
                    &nbsp;&nbsp;{this.props.workdetails.work_title}
                  </div>
                  <div className="bauthor blockquote-footer">
                    <i className="fa fa-pen-nib" />
                    &nbsp;&nbsp; {this.props.workdetails.author}
                  </div>
                </blockquote>
                <div className="bgenre">
                  Genre: {this.props.workdetails.genre}
                </div>
                <br />
                Description:
                <div
                  className=" card card-body bbio"
                  style={{ borderRadius: "5%", backgroundColor: "#e6e6e6" }}
                >
                  {this.props.workdetails.description}
                </div>
              </div>
              <div className="col-2">
                <div className="buploader">
                  Uploaded by {this.props.workdetails.username}
                </div>
                <div className="btime">{this.props.workdetails.timestamp}</div>
                <br />
                <div className="buploader">
                  Rating: {avgrating} &nbsp;&nbsp; ({noofratings})
                </div>
                <br />
                <div>
                  {/* <Link to={`pdfview/${bookLink}`} > */}
                  <a href={this.props.workdetails.file} target="_blank">
                    <button
                      className="btn btn-block btn-outline-primary"
                      onClick={() =>
                        this.setState({
                          showBook: !this.state.showBook
                        })
                      }
                    >
                      <i className="fa fa-book-open" /> Read
                    </button>
                  </a>
                  {/* </Link> */}
                  {/*{showBook ? (*/}
                  {/*<div style={{width: '50px', height: '50px'}}>*/}
                  {/*{console.log(this.props.workdetails.file)}*/}
                  {/*<iframe src={this.props.workdetails.file}/>*/}
                  {/*</div>*/}
                  {/*) : null}*/}
                </div>
                <br />
                <div>
                <a href={this.props.workdetails.file} target="_blank">
                    <button
                      className="btn btn-block btn-outline-primary"
                      onClick={() =>
                        this.setState({
                          showBook: !this.state.showBook
                        })
                      }
                    >
                    <i className="fa fa-save " /> Download
                  </button>
                  </a>
                </div>
              </div>
            </div>
          </div>

          <div className="card">
            <div className="card-header">
              <div class="btn-group">
                <input
                  type="button"
                  name="options"
                  id="option1"
                  class="btn btn-info"
                  onClick={this.showAllRatings}
                  value="All Ratings"
                />
                <input
                  type="button"
                  id="option2"
                  class="btn btn-success"
                  onClick={this.showYourRating}
                  value="Your Rating"
                />
              </div>
            </div>
            <div className="card-body">
              {this.state.allratings ? (
                <div>
                  {this.props.workdetails.allratings.map(comment => (
                    <div className="row" key={comment.id}>
                      <div
                        className="col-2"
                        style={{ marginRight: "3px solid black" }}
                      >
                        {comment.user}
                      </div>
                      :
                      <div className="col-2">
                        {comment.rating} star(s) &nbsp;&nbsp;
                      </div>
                    </div>
                  ))}
                </div>
              ) : null}

              {this.state.yourrating ? (
                <div className="row">
                  {currentuserrating ? (
                    currentuserrating.length ? (
                      currentuserrating.map(userrating => (
                        <div key={userrating.id} className="col-6">
                          You have rated {userrating.rating} Star(s)
                          {/*<strong> {userrating.user}</strong> &nbsp;&nbsp;*/}
                        </div>
                      ))
                    ) : (
                      <strong className="col-6">
                        You haven't rated yet!
                        <br />
                        <br />
                      </strong>
                    )
                  ) : null}

                  <form onSubmit={this.onSubmitRating} className="col-6">
                    <div className="form-group">
                      Rate (1-5): &nbsp;&nbsp;&nbsp;
                      <input
                        type="number"
                        name="rating"
                        //   className="form-control form-control-sm"
                        value={rating}
                        onChange={this.onChange}
                      />
                      &nbsp;&nbsp;&nbsp;
                      <input
                        type="submit"
                        value="Submit"
                        className="btn btn-outline-dark btn-sm"
                      />
                    </div>
                  </form>
                </div>
              ) : null}
            </div>
            <br />
            <br />
          </div>

          <br />
          <br />
          <div className="card">
            <div className="card-header">
              <div class="btn-group">
                <input
                  type="button"
                  name="options"
                  id="option1"
                  class="btn btn-info"
                  onClick={this.showAllReviews}
                  value="All Reviews"
                />
                <input
                  type="button"
                  id="option2"
                  class="btn btn-success"
                  onClick={this.showYourReview}
                  value="Your Review"
                />
              </div>
            </div>
            <div className="card-body">
              {this.state.allreviews ? (
                <div className="row">
                  {this.props.workdetails.allreviews.map(comment => (
                    <div key={comment.id}>
                      <div>
                        {comment.user} : "{comment.content}" &nbsp;&nbsp;
                      </div>
                    </div>
                  ))}
                </div>
              ) : null}
              {this.state.yourreview ? (
                <div className="row">
                  {currentuserreview ? (
                    currentuserreview.length ? (
                      currentuserreview.map(userreview => (
                        <div key={userreview.id} className="col-6">
                          <div>
                            Your Review: "{userreview.content}"
                            {/*<strong> {userreview.user}</strong> &nbsp;&nbsp;*/}
                          </div>
                          <br />
                          <br />
                        </div>
                      ))
                    ) : (
                      <div className="col-6">
                        You haven't reviewed it yet
                        <br />
                        <br />
                      </div>
                    )
                  ) : null}

                  <form
                    action=""
                    onSubmit={this.onSubmitReview}
                    className="col-6"
                  >
                    <div className="form-group">
                      Write Review :
                      <textarea
                        name="review"
                        className="form-control form-control"
                        value={review}
                        onChange={this.onChange}
                      />
                    </div>
                    <input
                      type="submit"
                      value="Post Your Review"
                      className="btn btn-dark btn-block btn-sm"
                    />
                  </form>
                </div>
              ) : null}
            </div>
          </div>
        </div>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  workdetails: state.workdetails.workdetails,
  auth: state.auth
});

export default connect(
  mapStateToProps,
  { getworkdetails, addRating, addReview, createMessage }
)(Workdetails);
