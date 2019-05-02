import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getallworks } from "../../actions/allworks";
import { Link } from "react-router-dom";
import Header_1 from "../home_page/Header_1";
import "./search.css";

export class Search extends Component {
  static PropTypes = {
    allworks: PropTypes.array.isRequired,
    getallworks: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getallworks();
  }

  constructor() {
    super();
    this.state = {
      search: "",
      sci_fi: false,
      horror: false,
      thriller: false,
      drama: false,
      fiction: false,
      novel: false,
      non_fiction: false,
      biography: false,
      history: false,
      auto_biography: false,
      mystery: false,
      tragedy: false,
      satire: false,
      fantasy: false,
      fairy_tale: false,
      kids: false,
      graphic_novel: false,
      philosophy: false,
      myth: false,
      poetry: false,
      comedy: false,
      textbook: false,
      encyclopedia: false,
      academic_journals: false
    };
  }

  updateSearch(event) {
    this.setState({ search: event.target.value });
  }

  filterByGenre = e => {
    let p = false;
    console.log(e.target.value);
    if (e.target.value == "false") {
      p = false;
    }
    if (e.target.value == "true") {
      p = true;
    }
    this.setState({ [e.target.name]: p });
  };

  render() {
    let filteredBooks = [];

    if (this.props.allworks) {
      for (let i = 0; i < this.props.allworks.length; i++) {
        if (this.state[this.props.allworks[i].genre.toLowerCase()]) {
          filteredBooks = [...filteredBooks, this.props.allworks[i]];
        }
      }
    }

    if (filteredBooks.length === 0) {
      filteredBooks = this.props.allworks.filter(allwork => {
        return (
          allwork.work_title.toLocaleLowerCase().indexOf(this.state.search) !==
            -1 ||
          allwork.author.toLocaleLowerCase().indexOf(this.state.search) !== -1
        );
      });
    }

    if (filteredBooks.length) {
      filteredBooks = filteredBooks.filter(allwork => {
        return (
          allwork.work_title.toLocaleLowerCase().indexOf(this.state.search) !==
            -1 ||
          allwork.author.toLocaleLowerCase().indexOf(this.state.search) !== -1
        );
      });
    }
    return (
      <Fragment>
        <Header_1 />
        <br />
        <br />
        <br />
        <br />
        <br />
        <input
          type="text"
          placeholder="Search for any Name/Author...."
          value={this.state.search}
          onChange={this.updateSearch.bind(this)}
          className="form-control "
          style={{
            fontFamily: "QuickSand",
            fontSize: "x-large",
            color: "rgb(59,190,182)",
            border: "3px solid rgb(59 , 190, 182)",
            borderRadius: "30px",
            paddingLeft: "25px"
          }}
        />
        <br />
        <div style={{ marginLeft: "25px" }}>
          <div className="dropright">
            <button
              className="btn btn-info dropdown-toggle"
              type="button"
              id="dropdownMenuButton"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              Select Category
            </button>
            <div
              className="dropdown-menu scrollable-menu"
              aria-labelledby="dropdownMenuButton"
            >
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="novel"
                  value={!this.state["novel"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; novel
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="sci_fi"
                  value={!this.state["sci_fi"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; Sci-Fi
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="horror"
                  value={!this.state["horror"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; horror
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="thriller"
                  value={!this.state["thriller"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; thriller
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="drama"
                  value={!this.state["drama"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; Drama
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="non_fiction"
                  value={!this.state["non_fiction"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; non fiction
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="biography"
                  value={!this.state["biography"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; biography
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="history"
                  value={!this.state["history"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; history
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="auto_biography"
                  value={!this.state["auto_biography"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; Auto biography
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="mystery"
                  value={!this.state["mystery"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; mystery
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="tragedy"
                  value={!this.state["tragedy"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; tragedy
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="satire"
                  value={!this.state["satire"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; satire
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="fantasy"
                  value={!this.state["fantasy"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; fantasy
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="fairy_tale"
                  value={!this.state["fairy_tale"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; fairy tale
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="kids"
                  value={!this.state["kids"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; kids
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="graphic_novel"
                  value={!this.state["graphic_novel"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; graphic novel
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="philosophy"
                  value={!this.state["philosophy"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; philosophy
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="myth"
                  value={!this.state["myth"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; myth
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="poetry"
                  value={!this.state["poetry"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; poetry
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="comedy"
                  value={!this.state["comedy"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; comedy
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="textbook"
                  value={!this.state["textbook"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; textbook
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="encyclopedia"
                  value={!this.state["encyclopedia"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; encyclopedia
              </div>
              <div className="dropdown-divider" />
              <div className="dropdown-item">
                <input
                  type="checkbox"
                  name="academic_journals"
                  value={!this.state["academic_journals"]}
                  onChange={this.filterByGenre}
                />
                &nbsp; academic_journals
              </div>
            </div>
          </div>
        </div>
        <br />
        {/* {filteredBooks.map(allwork => (
          <tr key={allwork.id}>
            <td>
              <img
                src={allwork.thumbnail}
                width="200"
                alt="thumbnail"
                style={{
                  border: "2px solid #3bbeb6",
                  borderRadius: "5%"
                }}
              />
            </td>
            <td>{allwork.id}</td>
            <td>
              <Link to={`/literature/workdetails/${allwork.id}/`}>
                {allwork.work_title}
              </Link>
              3
            </td>
            <td>{allwork.uploader_id}</td>
            <td>{allwork.author}</td>
          </tr>
        ))} */}
        {filteredBooks.map(allwork => (
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
                    href="#/home"
                    style={{ color: "black" }}
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
              </div>
              <div className="col-2">
                <div className="buploader">
                  Uploaded by {allwork.username}
                  {/* {upload.id} */}
                </div>
                <div className="btime">{allwork.timestamp}</div>
              </div>
              <div className="col-3">
                <button className="btn btn-primary btn-sm col-5">
                  <i className="fa fa-book-open" /> Read
                </button>
                &nbsp;|&nbsp;
                <button className="btn btn-success btn-sm col-5">
                  <i className="fa fa-save " /> Download
                </button>
                <br />
                <br />
                <button
                  // onClick={}
                  className="btn btn-outline-info col-10 btn-sm"
                >
                  <i className="fa fa-plus" />
                  &nbsp;Add to Read-list
                </button>
              </div>
            </div>
          </div>
        ))}
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  allworks: state.allworks.allworks
});

export default connect(
  mapStateToProps,
  { getallworks }
)(Search);
