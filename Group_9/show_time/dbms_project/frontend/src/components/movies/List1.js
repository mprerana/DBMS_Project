import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getMovies } from "../../actions/movies";
import { getGenres } from "../../actions/genres";
import { getLanguages } from "../../actions/languages";
import { getFormats } from "../../actions/formats";
import { getCities } from "../../actions/cities";
import { Link } from "react-router-dom";
import "./list1.css";
import { Card, CardImg, CardBody, CardTitle, CardText } from "reactstrap";

export class List extends Component {
  state = {
    intheatre: 1,
    city: "chennai",
    search: ""
  };

  movie = [];
  movie_bygenre = [];
  movie_bylanguage = [];
  movie_byformats = [];

  genre_select = 0;
  language_select = 0;
  format_select = 0;

  updateSearch(event) {
    this.setState({ search: event.target.value });
  }

  static propTypes = {
    movies: PropTypes.array.isRequired,
    genres: PropTypes.array.isRequired,
    languages: PropTypes.array.isRequired,
    formats: PropTypes.array.isRequired,
    cities: PropTypes.array.isRequired,
    getMovies: PropTypes.func.isRequired,
    getGenres: PropTypes.func.isRequired,
    getLanguages: PropTypes.func.isRequired,
    getFormats: PropTypes.func.isRequired,
    getCities: PropTypes.func.isRequired
  };

  showInTheatreMovies = e => {
    this.setState({ intheatre: 1 });
  };

  showUpcomingMovies = e => {
    this.setState({ intheatre: 0 });
  };

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });

    let id = 79;

    for (var i = 0; i < this.props.cities.length; i++) {
      if (this.props.cities[i]["city"] == e.target.value) {
        id = this.props.cities[i]["id"];
        this.props.getMovies(id);
        break;
      }
    }
  };

  doFormatFilter = e => {
    let p = false;
    if (e.target.value == "false") {
      p = false;
    } else if (e.target.value == "true") {
      p = true;
    }

    this.setState({ [e.target.name]: p });
  };

  doGenreFilter = e => {
    let p = false;
    if (e.target.value == "false") {
      p = false;
    } else if (e.target.value == "true") {
      p = true;
    }

    this.setState({ [e.target.name]: p });
  };

  doLanguageFilter = e => {
    let p = false;
    if (e.target.value == "false") {
      p = false;
    } else if (e.target.value == "true") {
      p = true;
    }

    this.setState({ [e.target.name]: p });
  };

  componentDidMount() {
    this.props.getGenres();
    this.props.getLanguages();
    this.props.getFormats();
    this.props.getCities();
    this.props.getMovies(3);
  }

  render() {
    let movies = this.props.movies;

    let flag = 0;

    let city_id = 0;

    for (var i = 0; i < this.props.cities.length; i++) {
      if (this.props.cities[i]["city"] == this.state.city) {
        city_id = this.props.cities[i]["id"];
        console.log(city_id);
        break;
      }
    }

    if (this.props.genres.length) {
      for (i = 0; i < this.props.genres.length; i++) {
        if (this.state[this.props.genres[i]["genre"]]) {
          this.genre_select = 1;
          console.log(this.genre_select);
          break;
        } else if (i == this.props.genres.length - 1) {
          this.genre_select = 0;
        }
      }
    }

    if (this.props.languages.length) {
      for (i = 0; i < this.props.languages.length; i++) {
        if (this.state[this.props.languages[i]["language"]]) {
          this.language_select = 1;
          console.log(this.language_select);
          break;
        } else if (i == this.props.languages.length - 1) {
          this.language_select = 0;
        }
      }
    }

    if (this.props.formats.length) {
      for (i = 0; i < this.props.formats.length; i++) {
        if (this.state[this.props.formats[i]["format"]]) {
          this.format_select = 1;
          console.log(this.format_select);
          break;
        } else if (i == this.props.formats.length - 1) {
          this.format_select = 0;
        }
      }
    }

    if (this.props.movies.length) {
      //console.log(this.props.movies);
      this.movie = [];
      this.movie_bygenre = [];
      this.movie_bylanguage = [];
      this.movie_byformats = [];

      if (this.genre_select) {
        for (var i = 0; i < this.props.movies.length; i++) {
          if (this.props.movies[i]["allgenre"]) {
            for (var j = 0; j < this.props.movies[i]["allgenre"].length; j++) {
              if (this.state[this.props.movies[i]["allgenre"][j]["genre"]]) {
                flag = 1;
                break;
              }
            }
            if (flag) {
              this.movie_bygenre = [
                ...this.movie_bygenre,
                this.props.movies[i]
              ];
            }

            flag = 0;
          }
        }
      }

      if (this.language_select) {
        for (var i = 0; i < this.props.movies.length; i++) {
          if (this.props.movies[i]["allanguages"]) {
            for (
              var j = 0;
              j < this.props.movies[i]["allanguages"].length;
              j++
            ) {
              if (
                this.state[this.props.movies[i]["allanguages"][j]["language"]]
              ) {
                flag = 1;
                break;
              }
            }
            if (flag) {
              this.movie_bylanguage = [
                ...this.movie_bylanguage,
                this.props.movies[i]
              ];
            }

            flag = 0;
          }
        }
      }

      if (this.format_select) {
        for (var i = 0; i < this.props.movies.length; i++) {
          if (this.props.movies[i]["allformats"]) {
            for (
              var j = 0;
              j < this.props.movies[i]["allformats"].length;
              j++
            ) {
              if (this.state[this.props.movies[i]["allformats"][j]["format"]]) {
                flag = 1;
                break;
              }
            }
            if (flag) {
              this.movie_byformats = [
                ...this.movie_byformats,
                this.props.movies[i]
              ];
            }

            flag = 0;
          }
        }
      }
    }

    if (this.genre_select || this.language_select || this.format_select) {
      this.movie = [];
      if (this.genre_select && !this.language_select && !this.format_select) {
        for (i = 0; i < this.movie_bygenre.length; i++) {
          this.movie = [...this.movie, this.movie_bygenre[i]];
        }
      } else if (
        !this.genre_select &&
        this.language_select &&
        !this.format_select
      ) {
        for (i = 0; i < this.movie_bylanguage.length; i++) {
          this.movie = [...this.movie, this.movie_bylanguage[i]];
        }
      } else if (
        !this.genre_select &&
        !this.language_select &&
        this.format_select
      ) {
        for (i = 0; i < this.movie_byformats.length; i++) {
          this.movie = [...this.movie, this.movie_byformats[i]];
        }
      } else if (
        this.genre_select &&
        this.language_select &&
        !this.format_select
      ) {
        for (var i = 0; i < this.movie_bygenre.length; i++) {
          for (var j = 0; j < this.movie_bylanguage.length; j++) {
            if (
              this.movie_bygenre[i]["title"] ==
              this.movie_bylanguage[j]["title"]
            ) {
              this.movie = [...this.movie, this.movie_bygenre[i]];
            }
          }
          // this.movie = [...this.movie, this.movie_byformats[i]];
        }
      } else if (
        this.genre_select &&
        !this.language_select &&
        this.format_select
      ) {
        for (var i = 0; i < this.movie_bygenre.length; i++) {
          for (var j = 0; j < this.movie_byformats.length; j++) {
            if (
              this.movie_bygenre[i]["title"] == this.movie_byformats[j]["title"]
            ) {
              this.movie = [...this.movie, this.movie_bygenre[i]];
            }
          }
          // this.movie = [...this.movie, this.movie_byformats[i]];
        }
      } else if (
        !this.genre_select &&
        this.language_select &&
        this.format_select
      ) {
        for (var i = 0; i < this.movie_bylanguage.length; i++) {
          for (var j = 0; j < this.movie_byformats.length; j++) {
            if (
              this.movie_bylanguage[i]["title"] ==
              this.movie_byformats[j]["title"]
            ) {
              this.movie = [...this.movie, this.movie_bylanguage[i]];
            }
          }
          // this.movie = [...this.movie, this.movie_byformats[i]];
        }
      } else if (
        this.genre_select &&
        this.language_select &&
        this.format_select
      ) {
        for (var i = 0; i < this.movie_bylanguage.length; i++) {
          for (var j = 0; j < this.movie_byformats.length; j++) {
            for (var k = 0; k < this.movie_bygenre.length; k++) {
              if (
                this.movie_bylanguage[i]["title"] ==
                this.movie_byformats[j]["title"] &&
                this.movie_bygenre[k]["title"] ==
                this.movie_byformats[j]["title"] &&
                this.movie_bylanguage[i]["title"] ==
                this.movie_bygenre[k]["title"]
              ) {
                this.movie = [...this.movie, this.movie_bylanguage[i]];
              }
            }
            // this.movie = [...this.movie, this.movie_byformats[i]];
          }
        }
      }
    }

    if (this.genre_select || this.language_select || this.format_select) {
      movies = this.movie;
      console.log(`hi iam ok ${this.genre_select}`);
    }

    movies.sort((a, b) => b.likes - a.likes);

    movies = movies.filter(movie => {
      return movie.title.toLocaleLowerCase().indexOf(this.state.search) !== -1;
    });

    return (
      <Fragment>
        <div className="slider movie-items">
          <div
            className="container-fluid"
            style={{ marginLeft: "500px", marginRight: "125px" }}
          >
            <div className="row">
              <div
                className="slick-multiItemSlider"
                style={{ padddingLeft: "100px" }}
              >
                <div className="movie-item" style={{ float: "left" }}>
                  <div className="mv-img">
                    <Link to="#">
                      <img
                        src="http://127.0.0.1:8000/media/profile_image/alexander-andrews-340055-unsplash_zRvaz6g.jpg"
                        alt=""
                        width="285"
                        height="437"
                      />
                    </Link>
                  </div>
                  <div className="title-in">
                    <div className="cate">
                      <span className="blue">
                        <Link to="#">Sci-fi</Link>
                      </span>
                    </div>
                    <h6>
                      <Link to="#">Interstellar</Link>
                    </h6>
                    <p>
                      <i className="ion-android-star" />
                      <span>7.4</span> /10
                    </p>
                  </div>
                </div>
                <div className="movie-item" style={{ float: "left" }}>
                  <div className="mv-img">
                    <Link to="#">
                      <img
                        src="http://127.0.0.1:8000/media/profile_image/avengers.jpg"
                        alt=""
                        width="285"
                        height="437"
                      />
                    </Link>
                  </div>
                  <div className="title-in">
                    <div className="cate">
                      <span className="blue">
                        <Link to="#">Sci-fi</Link>
                      </span>
                    </div>
                    <h6>
                      <Link to="#">Avengers:Endgame</Link>
                    </h6>
                    <p>
                      <i className="ion-android-star" />
                      <span>7.4</span> /10
                    </p>
                  </div>
                </div>
                <div className="movie-item" style={{ float: "left" }}>
                  <div className="mv-img">
                    <Link to="#">
                      <img
                        src="http://127.0.0.1:8000/media/profile_image/movie-single.jpg"
                        alt=""
                        width="285"
                        height="437"
                      />
                    </Link>
                  </div>
                  <div className="title-in">
                    <div className="cate">
                      <span className="blue">
                        <Link to="#">Sci-fi</Link>
                      </span>
                    </div>
                    <h6>
                      <Link to="#">Skyfall</Link>
                    </h6>
                    <p>
                      <i className="ion-android-star" />
                      <span>7.4</span> /10
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        {/* style=
        {{
          paddingLeft: "83%",
          backgroundColor: "#020d18",
          paddingTop: "30px"
        }} */}
        <div
          className="row"
          style={{ backgroundColor: "#020d18", paddingTop: "30px" }}
        >
          <div className="col-sm-3" />
          <div className="col-sm-7">
            <input
              className="searchbar"
              type="text"
              placeholder="search movies"
              value={this.state.search}
              onChange={this.updateSearch.bind(this)}
            />
          </div>

          <div className="col-sm-2">
            <select
              name="city"
              className="btn btn-dark dropdown-toggle"
              onChange={this.onChange}
            >
              <option value="chennai">chennai</option>
              <option value="hyderabad">Hyderabad</option>
              <option value="mumbai">Mumbai</option>
            </select>
          </div>
        </div>
        <div className="movie-items">
          <div className="container-fluid" style={{}}>
            <div className="row ipad-width">
              <div
                className="col-md-3"
                style={{
                  paddingLeft: "5%",
                  paddingRight: "5%",
                  color: "white"
                }}
              >
                {/* <!-- <img src="images/uploads/ads1.png" alt="" width="336" height="296"> --> */}
                <div className="row" style={{ paddingLeft: "10%" }}>
                  <div
                    className="col-sm-12"
                    style={{
                      border: "1px solid gray",
                      borderRadius: "10px"
                    }}
                  >
                    <p style={{ fontSize: "25px" }}>Genres</p>

                    {this.props.genres.map(genre => (
                      <span key={genre.id}>
                        <input
                          type="checkbox"
                          name={genre.genre}
                          value={!this.state[genre.genre]}
                          onChange={this.doGenreFilter}
                        />
                        {genre.genre}
                        <br />
                      </span>
                    ))}
                  </div>
                </div>

                <div
                  className="row"
                  style={{ paddingLeft: "10%", marginTop: "2%" }}
                >
                  <div
                    className="col-sm-12"
                    style={{
                      border: "1px solid gray",
                      borderRadius: "10px"
                    }}
                  >
                    <p style={{ fontSize: "25px" }}>Languages</p>

                    {this.props.languages.map(language => (
                      <span key={language.id}>
                        <input
                          type="checkbox"
                          name={language.language}
                          value={!this.state[language.language]}
                          onChange={this.doLanguageFilter}
                        />
                        {language.language}
                        <br />
                      </span>
                    ))}
                  </div>
                </div>
                <div
                  className="row"
                  style={{ paddingLeft: "10%", marginTop: "2%" }}
                >
                  <div
                    className="col-sm-12"
                    style={{
                      border: "1px solid gray",
                      borderRadius: "10px"
                    }}
                  >
                    <p style={{ fontSize: "25px" }}>Formats</p>

                    {this.props.formats.map(format => (
                      <span key={format.id}>
                        <input
                          type="checkbox"
                          name={format.format}
                          value={!this.state[format.format]}
                          onChange={this.doFormatFilter}
                        />
                        {format.format}
                        <br />
                      </span>
                    ))}
                  </div>
                </div>
              </div>

              <div className="col-md-2" />

              <div
                className="col-md-7"
                style={{ paddingLeft: "20px", paddindRight: "20px" }}
              >
                <div className="movie-tabs">
                  <div className="tabs">
                    <ul className="tab-links tabs-mv">
                      {this.state.intheatre ? (
                        <li
                          className="active"
                          style={{ cursor: "pointer" }}
                          onClick={this.showInTheatreMovies}
                        >
                          <a style={{ textDecoration: "None" }}>
                            #Movies in Theatres
                          </a>
                        </li>
                      ) : (
                          <li
                            style={{ cursor: "pointer" }}
                            onClick={this.showInTheatreMovies}
                          >
                            <a style={{ textDecoration: "None" }}>
                              #Movies in Theatres
                          </a>
                          </li>
                        )}

                      {!this.state.intheatre ? (
                        <li
                          className="active"
                          style={{ cursor: "pointer" }}
                          onClick={this.showUpcomingMovies}
                        >
                          <a style={{ textDecoration: "None" }}>#Coming Soon</a>
                        </li>
                      ) : (
                          <li
                            style={{ cursor: "pointer" }}
                            onClick={this.showUpcomingMovies}
                          >
                            <a style={{ textDecoration: "None" }}>#Coming Soon</a>
                          </li>
                        )}
                    </ul>

                    <div className="tab-content">
                      <div id="tab1" className="tab active">
                        {this.state.intheatre
                          ? movies.map(movie =>
                            movie.status ? (
                              <div
                                className="row"
                                key={movie.id}
                                style={{
                                  width: "30%",
                                  float: "left",
                                  padding: "20px"
                                }}
                              >
                                <div className="slick-multiItem">
                                  <Link
                                    to={`/specifics/${movie.id}/${city_id}`}
                                  >
                                    <div className="slide-it">
                                      <div className="movie-item">
                                        <div className="mv-img">
                                          <img
                                            src={movie.image_source}
                                            alt=""
                                            width="185"
                                            height="284"
                                          />

                                          <div className="title-in">
                                            <h6
                                              style={{
                                                color: "#f1e000",
                                                fontSize: "20px"
                                              }}
                                            >
                                              {movie.title}
                                            </h6>
                                            <p>
                                              <i
                                                style={{
                                                  fontSize: "16px",
                                                  color: "red"
                                                }}
                                              >
                                                &#10084;
                                                </i>
                                              <span
                                                style={{
                                                  color: "#f1e000",
                                                  fontSize: "20px"
                                                }}
                                              >
                                                {movie.likes} likes
                                                </span>
                                            </p>
                                          </div>
                                        </div>
                                      </div>
                                    </div>
                                  </Link>
                                </div>
                              </div>
                            ) : null
                          )
                          : null}
                      </div>
                    </div>

                    <div className="tab-content">
                      <div id="tab1" className="tab active">
                        {!this.state.intheatre
                          ? movies.map(movie =>
                            !movie.status ? (
                              <div
                                className="row"
                                key={movie.id}
                                style={{
                                  width: "30%",
                                  float: "left",
                                  padding: "20px"
                                }}
                              >
                                <div className="slick-multiItem">
                                  <Link
                                    to={`/specifics/${movie.id}/${city_id}`}
                                    key={movie.id}
                                  >
                                    <div className="slide-it">
                                      <div className="movie-item">
                                        <div className="mv-img">
                                          <img
                                            src={movie.image_source}
                                            alt=""
                                            width="185"
                                            height="284"
                                          />

                                          <div className="title-in">
                                            <h6
                                              style={{
                                                color: "#f1e000",
                                                fontSize: "20px"
                                              }}
                                            >
                                              {movie.title}
                                            </h6>
                                            <p>
                                              <i
                                                style={{
                                                  fontSize: "16px",
                                                  color: "red"
                                                }}
                                              >
                                                &#10084;
                                                </i>
                                              <span
                                                style={{
                                                  color: "#f1e000",
                                                  fontSize: "20px"
                                                }}
                                              >
                                                {movie.likes} likes
                                                </span>
                                            </p>
                                          </div>
                                        </div>
                                      </div>
                                    </div>
                                  </Link>
                                </div>
                              </div>
                            ) : null
                          )
                          : null}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  movies: state.movies.movies,
  genres: state.genres.genres,
  formats: state.formats.formats,
  languages: state.languages.languages,
  cities: state.cities.cities
});

export default connect(
  mapStateToProps,
  { getMovies, getGenres, getLanguages, getFormats, getCities }
)(List);
