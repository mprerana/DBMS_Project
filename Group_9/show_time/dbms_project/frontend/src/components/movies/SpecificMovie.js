import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getSpecificMovie, addComment } from "../../actions/specificmovie";
import { createMessage } from "../../actions/messages";
import { NavLink, Link } from "react-router-dom";
import moviesReducer from "../../reducers/moviesReducer";
import "./trash.css";
import StarRatings from "react-star-ratings";
import Rating from "react-star-rating-lite";
import InfiniteScroll from "react-infinite-scroll-component";

export class SpecificMovie extends Component {
  static propTypes = {
    specificmovie: PropTypes.object.isRequired,
    getSpecificMovie: PropTypes.func.isRequired,
    addComment: PropTypes.func.isRequired,
    createMessage: PropTypes.func.isRequired
  };

  state = {
    rating: 1,
    comment: "",
    flag: 0,
    summary: true,
    allreviews: false,
    yourreview: false,
    hasMore: false
  };

  showSummary = e => {
    this.setState({
      summary: true,
      allreviews: false,
      yourreview: false
    });
  };

  showAllReviews = e => {
    this.setState({
      summary: false,
      allreviews: true,
      yourreview: false
    });
  };

  showYourReview = e => {
    if (!this.props.auth.isAuthenticated) {
      this.props.createMessage({
        notloggedin: "Please Login to review a movie"
      });
      return;
    }

    this.setState({
      summary: false,
      allreviews: false,
      yourreview: true
    });

    this.setState({ flag: 1 });
  };

  componentDidMount() {
    const { id } = this.props.match.params;
    this.props.getSpecificMovie(id);
  }

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  rateStar = ratedVal => {
    console.log(ratedVal);
    this.setState({ rating: ratedVal });
    console.log(this.state.rating);
  };

  onSubmit = e => {
    e.preventDefault();

    const { rating, comment } = this.state;

    if (!this.props.auth.isAuthenticated) {
      this.props.createMessage({ notloggedin: "Please Login to comment" });
      return;
    }

    let flag = 0;
    for (var i = 0; i < this.props.specificmovie.allcomments.length; i++) {
      if (
        this.props.auth.user.username ===
        this.props.specificmovie.allcomments[i].user
      ) {
        flag = 1;
        console.log(`hi ${flag}`);
        break;
      }
    }

    if (flag) {
      this.props.createMessage({
        alreadyReviewed: "You have already reviewed"
      });

      return;
    }

    const ratings = {
      rating: {
        title: this.props.specificmovie.id,
        user: this.props.auth.user.id,
        rating: rating,
        comment: comment
      }
    };

    this.props.addComment(ratings);

    this.setState({ flag: 1 });

    const currentrating = {
      id: 2225645,
      user: this.props.auth.user.username,
      likestatus: 1,
      ratestatus: 1,
      rating: rating,
      comment: comment
    };

    this.setState({
      rating: 1,
      comment: "",
      flag: 0
    });

    this.props.specificmovie.allcomments = [
      ...this.props.specificmovie.allcomments,
      currentrating
    ];
  };

  render() {
    const { specificmovie } = this.props;
    const { comment } = this.state;

    var rating = 0;

    let totalrating = 0;
    let noofratings = 0;

    {
      this.props.specificmovie.allcomments
        ? this.props.specificmovie.allcomments.forEach((comment, index) => {
            totalrating = totalrating + comment.rating;
            noofratings = noofratings + 1;
          })
        : null;
    }

    let avgrating = 0;

    if (this.props.specificmovie.allcomments) {
      avgrating = totalrating / noofratings;
    }

    avgrating = Math.round(avgrating * 100) / 100;

    let currentuserreview =
      this.props.specificmovie.allcomments && this.props.auth.user
        ? this.props.specificmovie.allcomments.filter(
            comment => comment.user === this.props.auth.user.username
          )
        : null;

    console.log(currentuserreview);

    if (currentuserreview) {
      console.log(currentuserreview.length);
    }

    return (
      <div>
        <div className="hero mv-single-hero">
          <div className="container">
            <div className="row">
              <div className="col-md-12" />
            </div>
          </div>
        </div>
        <div className="page-single movie-single movie_single">
          <div className="container">
            <div className="row ipad-width2">
              <div className="col-md-4 col-sm-12 col-xs-12">
                <div className="movie-img sticky-sb">
                  <img src={specificmovie.image_source} alt="" />
                  <div className="movie-btn">
                    <div className="btn-transform  buyticketbutton1">
                      <div />
                      <div>
                        <a
                          style={{ textDecoration: "none", color: "white" }}
                          href={specificmovie.trailer_link}
                        >
                          Watch Trailer
                        </a>
                      </div>
                    </div>
                    <div className="btn-transform  buyticketbutton">
                      <div>
                        {" "}
                        <i className="ion-card " />{" "}
                        <a
                          style={{ textDecoration: "none", color: "white" }}
                          href={`http://127.0.0.1:8000/frontend/#/theatre/${
                            specificmovie.id
                          }/3`}
                        >
                          Buy ticket
                        </a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div className="col-md-8 col-sm-12 col-xs-12">
                <div
                  className="movie-single-ct main-content"
                  style={{ paddingTop: "75px" }}
                >
                  <h1 className="bd-hd" style={{ textAlign: "left" }}>
                    {specificmovie.title} <span>2018</span>
                  </h1>
                  <div className="movie-rate">
                    <div className="rate">
                      <i className="ion-android-star" />
                      <p>
                        <span>{avgrating / 1}</span> /5
                        <br />
                        <span className="rv">{noofratings} Reviews</span>
                      </p>
                    </div>
                    {specificmovie.allcomments ? (
                      specificmovie.allcomments.length ? (
                        <div className="rate-star">
                          <p>Total Rating: </p>
                          <StarRatings
                            rating={avgrating}
                            starRatedColor="yellow"
                            starDimension="30px"
                            starSpacing="5px"
                          />
                        </div>
                      ) : (
                        <div className="rate-star">
                          <p>Total Rating: </p>
                          <StarRatings
                            rating={0}
                            starRatedColor="yellow"
                            starDimension="30px"
                            starSpacing="5px"
                          />
                        </div>
                      )
                    ) : null}
                  </div>
                  <div className="movie-tabs">
                    <div className="tabs">
                      <ul className="tab-links tabs-mv">
                        {this.state.summary ? (
                          <li
                            className="active"
                            style={{ cursor: "pointer" }}
                            onClick={this.showSummary}
                          >
                            <a style={{ textDecoration: "None" }}>overview</a>
                          </li>
                        ) : (
                          <li
                            style={{ cursor: "pointer" }}
                            onClick={this.showSummary}
                          >
                            <a style={{ textDecoration: "None" }}>overview</a>
                          </li>
                        )}

                        {this.state.allreviews ? (
                          <li
                            className="active"
                            style={{ cursor: "pointer" }}
                            onClick={this.showAllReviews}
                          >
                            <a style={{ textDecoration: "None" }}>Reviews</a>
                          </li>
                        ) : (
                          <li
                            style={{ cursor: "pointer" }}
                            onClick={this.showAllReviews}
                          >
                            <a style={{ textDecoration: "None" }}>Reviews</a>
                          </li>
                        )}

                        {this.state.yourreview ? (
                          <li
                            className="active"
                            style={{ cursor: "pointer" }}
                            onClick={this.showYourReview}
                          >
                            <a style={{ textDecoration: "None" }}>
                              Your Review
                            </a>
                          </li>
                        ) : (
                          <li
                            style={{ cursor: "pointer" }}
                            onClick={this.showYourReview}
                          >
                            <a style={{ textDecoration: "None" }}>
                              Your Review
                            </a>
                          </li>
                        )}
                      </ul>

                      <div className="tab-content">
                        {this.state.summary ? (
                          <div id="overview" className="tab active">
                            <div className="row">
                              <div className="col-md-8 col-sm-12 col-xs-12">
                                <div className="title-hd-sm">
                                  <h4>synopsis</h4>
                                </div>
                                <p>{specificmovie.synopsis}</p>

                                <div className="mvsingle-item ov-item" />
                                <div className="title-hd-sm">
                                  <h4>cast and crew</h4>
                                </div>

                                <div className="mvcast-item">
                                  {specificmovie.completecast
                                    ? specificmovie.completecast.length
                                      ? specificmovie.completecast.map(cast => (
                                          <div
                                            key={cast.id}
                                            className="cast-it"
                                          >
                                            <div className="cast-left">
                                              <img
                                                src={cast.image}
                                                alt=""
                                                style={{
                                                  maxHeight: "20%",
                                                  maxWidth: "30%"
                                                }}
                                              />
                                            </div>
                                            <p> {cast.cast}</p>
                                          </div>
                                        ))
                                      : null
                                    : null}
                                </div>
                              </div>
                              <div
                                className="col-md-4 col-xs-12 col-sm-12"
                                style={{ fontSize: "18px" }}
                              >
                                <div
                                  style={{
                                    border: "1px solid white",
                                    borderRadius: "7px",
                                    height: "auto",
                                    padding: "21px",
                                    marginTop: "100px",
                                    paddingTop: "26px"
                                  }}
                                >
                                  <div className="sb-it">
                                    <h6>Genre: </h6>
                                    <p>
                                      {specificmovie.allgenre
                                        ? specificmovie.allgenre.map(genre => (
                                            <span key={genre.id}>
                                              {genre.genre} &nbsp; &nbsp;
                                            </span>
                                          ))
                                        : null}
                                    </p>
                                  </div>
                                  <div className="sb-it">
                                    <h6>Languages: </h6>
                                    <p>
                                      {specificmovie.allanguages
                                        ? specificmovie.allanguages.map(
                                            language => (
                                              <span key={language.id}>
                                                {language.language} &nbsp;
                                                &nbsp;
                                              </span>
                                            )
                                          )
                                        : null}
                                    </p>
                                  </div>
                                  <div
                                    className="sb-it"
                                    style={{ marginBottom: "0px" }}
                                  >
                                    <h6>Available in Formats: </h6>
                                    <p>
                                      {specificmovie.allformats
                                        ? specificmovie.allformats.map(
                                            format => (
                                              <span key={format.id}>
                                                {format.format} &nbsp; &nbsp;
                                              </span>
                                            )
                                          )
                                        : null}
                                    </p>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                        ) : null}
                        {this.state.allreviews ? (
                          <div className="row">
                            <div
                              className="topbar-filter"
                              style={{ width: "100%" }}
                            >
                              <p>Found {noofratings} reviews in total</p>
                            </div>

                            {specificmovie.allcomments ? (
                              <InfiniteScroll
                                dataLength={specificmovie.allcomments.length}
                                hasMore={this.state.hasMore}
                                loader={<h4>Loading...</h4>}
                                height={400}
                                style={{ width: "100%" }}
                                endMessage={
                                  <p style={{ textAlign: "center" }}>
                                    <b>
                                      That's all folks you have seen all the
                                      comments
                                    </b>
                                  </p>
                                }
                              >
                                {specificmovie.allcomments.map(comment => (
                                  <div key={comment.id} className="col-sm-12">
                                    <Rating
                                      value={String(comment.rating)}
                                      weight="20"
                                      color="yellow"
                                      readonly
                                    />
                                    <span style={{ color: "white" }}> by</span>{" "}
                                    &nbsp;&nbsp;
                                    <span
                                      style={{
                                        color: "white",
                                        fontWeight: "bold"
                                      }}
                                    >
                                      {comment.user}
                                    </span>
                                    <p style={{ wordWrap: "break-word" }}>
                                      {comment.comment}
                                    </p>
                                  </div>
                                ))}
                              </InfiniteScroll>
                            ) : null}
                          </div>
                        ) : null}

                        {this.state.yourreview ? (
                          <div
                            style={{
                              width: "100%",

                              color: "white"
                            }}
                          >
                            Your Review
                            <br />
                            <br />
                            {currentuserreview ? (
                              currentuserreview.length ? (
                                currentuserreview.map(userreview => (
                                  <div
                                    key={userreview.id}
                                    style={{ width: "50%" }}
                                  >
                                    <div>
                                      <Rating
                                        value={String(userreview.rating)}
                                        weight="20"
                                        color="yellow"
                                        readonly
                                      />
                                      {userreview.comment} by{" "}
                                      <strong> {userreview.user}</strong>{" "}
                                      &nbsp;&nbsp;
                                    </div>
                                    <br />
                                    <br />
                                  </div>
                                ))
                              ) : (
                                <strong>
                                  You haven't reviewed yet
                                  <br />
                                  <br />
                                </strong>
                              )
                            ) : null}
                            <Rating
                              value="1"
                              weight="30"
                              onClick={this.rateStar}
                              color="yellow"
                            />
                            <form action="" onSubmit={this.onSubmit}>
                              <div className="form-group">
                                <label htmlFor="name"> Review </label>
                                <textarea
                                  type="message"
                                  name="comment"
                                  style={{ height: "120px" }}
                                  placeholder="Enter your review...."
                                  className="form-control form-control-lg"
                                  value={comment}
                                  onChange={this.onChange}
                                />
                              </div>
                              <input
                                type="submit"
                                value="Post Your Review"
                                className="btn btn-dark btn-block"
                              />
                            </form>
                          </div>
                        ) : null}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  specificmovie: state.specificmovie.specificmovie,
  auth: state.auth
});

export default connect(
  mapStateToProps,
  { getSpecificMovie, addComment, createMessage }
)(SpecificMovie);
