import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getworks, deletework } from "../../actions/works";
import { getallworks, addworktolist } from "../../actions/allworks";
import { getworkdetails } from "../../actions/workdetails";
import { Link } from "react-router-dom";
import "./works.css";
import { createMessage } from "../../actions/messages";

export class Works extends Component {
  static PropTypes = {
    works: PropTypes.object.isRequired,
    getworks: PropTypes.func.isRequired,
    deletework: PropTypes.func.isRequired,
    allworks: PropTypes.array.isRequired,
    getallworks: PropTypes.func.isRequired,
    createMessage: PropTypes.func.isRequired
  };

  state = {
    flag: 0
  };
  OnClickAdd = (work_id, readlist_id, title, author, uploader, name) => {
    let flag = 0;

    for (var i = 0; i < this.props.works.works.length; i++) {
      if (work_id === this.props.works.works[i].id) {
        flag = 1;
        break;
      }
    }

    if (flag === 1) {
      this.props.createMessage({
        alreadyinthelist: "Book already exists in your ReadingList "
      });

      return;
    }

    const work = {
      addworktolist: {
        work_id: work_id
      }
    };
    this.props.addworktolist(readlist_id, work);
    this.setState({ flag: 1 });

    const currentwork = {
      id: 2345432,
      work_title: title,
      author: author,
      username: name
    };

    this.props.works.works = [...this.props.works.works, currentwork];

    this.setState({
      flag: 0
    });
  };

  OnDelete = (work_id, list_id) => {
    this.props.deletework(work_id, list_id);

    for (var i = 0; i < this.props.works.works.length; i++) {
      if (this.props.works.works[i]["id"] == work_id) {
        this.props.works.works.splice(i, 1);
      }
    }

    this.setState({ flag: 1 });
  };

  componentDidMount() {
    //const {id}= this.props.match.params;
    this.props.getallworks();
  }

  render() {
    console.log(this.props);
    return (
      <Fragment>
        <div className="container">
          <div className="card card-body" style={{ padding: "3%" }}>
            <h4 id="wtext1">BOOKS IN YOUR READINGLIST</h4>
            <table className="table table-striped">
              <thead>
                <tr id="wtext1">
                  <th>TITLE</th>
                  <th>UPLOADER</th>
                  <th>AUTHOR</th>
                  <th> </th>
                </tr>
              </thead>
              <tbody>
                {this.props.works.works
                  ? this.props.works.works.map(work => (
                      <tr key={work.id}>
                        <td
                          onClick={this.props.getworkdetails.bind(
                            this,
                            work.id
                          )}
                        >
                          <Link to={`/literature/workdetails/${work.id}/`}>
                            {work.work_title}
                          </Link>
                        </td>
                        <td>{work.username}</td>
                        <td>{work.author}</td>
                        <td>
                          <button
                            onClick={this.OnDelete.bind(
                              this,
                              work.id,
                              this.props.works.id
                            )}
                            className="btn btn-danger btn-sm"
                          >
                            <i className="fa fa-trash-alt" />
                            &nbsp;Delete
                          </button>{" "}
                        </td>
                      </tr>
                    ))
                  : null}
              </tbody>
            </table>
          </div>
          <br />
          <div className="card card-body" style={{ padding: "3%" }}>
            <h4 id="wtext1">ADD TO LIST</h4>
            <table className="table table-striped">
              <thead>
                <tr id="wtext1">
                  <th>ID</th>
                  <th>TITLE</th>
                  <th>UPLOADER</th>
                  <th>AUTHOR</th>
                  <th> </th>
                </tr>
              </thead>
              <tbody>
                {this.props.allworks.map(allwork => (
                  <tr key={allwork.id}>
                    <td>{allwork.id}</td>
                    <td>{allwork.work_title}</td>
                    <td>{allwork.username}</td>
                    <td>{allwork.author}</td>

                    <td>
                      <button
                        onClick={this.OnClickAdd.bind(
                          this,
                          allwork.id,
                          this.props.works.id,
                          allwork.work_title,
                          allwork.author,
                          allwork.uploader_id,
                          allwork.username
                        )}
                        className="btn btn-success"
                      >
                        <i className="fa fa-plus" />
                        &nbsp; Add
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  works: state.works.works,
  allworks: state.allworks.allworks,
  workdetails: state.workdetails.workdetails
});

export default connect(
  mapStateToProps,
  {
    getworks,
    deletework,
    getallworks,
    addworktolist,
    getworkdetails,
    createMessage
  }
)(Works);
