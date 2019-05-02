import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { adduploads } from "../../actions/uploads";
import { Link } from "react-router-dom";
import "./upload_form.css";

export class Upload_Form extends Component {
  state = {
    work_title: "",
    author: "",
    description: "",
    genre: "",
    thumbnail: "",
    file: "",
    file_content : "",
    thumbnail_content:""
  };

  static propTypes = {
    adduploads: PropTypes.func.isRequired,
    auth: PropTypes.object.isRequired
  };

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value })


  };

  onChange2 = e => {

    this.setState({[e.target.name]: e.target.value});

    console.log(e.target.value );

    // if (e.target.name == "thumbnail")
    //   {
    //     this.setState({"thumbnail": e.target.files[0]})
    //   }
    //
    //   else if (e.target.name == "file")
    //   {
    //     this.setState({"file": e.target.files[0]})
    //   }


    //console.log()

    let files= e.target.files;
    //console.log("data file",files);

    let reader = new FileReader();
    reader.readAsDataURL(files[0]);

    reader.onload=(e)=>{
      //console.log("img data", e.target.result)
      this.setState({thumbnail_content: e.target.result});
     console.log(this.state.thumbnail_content)
    }
  };

  onChange3 = e => {

    this.setState({[e.target.name]: e.target.value});

    //console.log(e.target.value );

    // if (e.target.name == "thumbnail")
    //   {
    //     this.setState({"thumbnail": e.target.files[0]})
    //   }
    //
    //   else if (e.target.name == "file")
    //   {
    //     this.setState({"file": e.target.files[0]})
    //   }


    //console.log()

    let files= e.target.files;
    //console.log("data file",files);

    let reader = new FileReader();
    reader.readAsDataURL(files[0]);

    reader.onload=(e)=>{
     // console.log("file data", e.target.result)
     this.setState({file_content: e.target.result});
     console.log(this.state.file_content)
    }
  };

  

  onSubmit = e => {
    e.preventDefault();
    // console.log("submit");
    // const { isAuthenticated, user } = this.props.auth;
    // console.log(user.id);
    // //
    // const userid = user.id;
    // console.log(" userid", userid);
    // this.setState({ uploader: userid });
    // console.log(this.state.uploader)
    const {
      work_title,
      author,
      description,
      genre,
      thumbnail_content,
      file_content
    } = this.state;
    const upload = {
      work_title,
      author,
      description,
      genre,
      thumbnail:thumbnail_content,
      file:file_content}
    console.log(upload);
    //
    this.props.adduploads(upload, this.props.auth.user.id);
  };
  render() {
    const {
      work_title,
      author,
      description,
      genre,
      thumbnail,
      file
    } = this.state;

    return (
      <Fragment>
        <div className="container">
          <div className="card" style={{ padding: "2%" }}>
            <div className="card-body">
              <div className="row" style={{ textAlign: "center" }}>
                <h4 className="col-12">
                  UPLOAD &nbsp;
                  <i className="fa fa-cloud-upload-alt " />
                </h4>
              </div>
              <br />
              <form onSubmit={this.onSubmit}>
                <div className="form-group row">
                  <label className="col-2" id="ut">
                    TITLE :
                  </label>
                  <input
                    type="text"
                    className="form-control col-10"
                    name="work_title"
                    onChange={this.onChange}
                    value={work_title}
                  />
                </div>
                <div className="form-group row">
                  <label className="col-2" id="ut">
                    AUTHOR :
                  </label>
                  <input
                    type="text"
                    className="form-control col-10"
                    name="author"
                    onChange={this.onChange}
                    value={author}
                  />
                </div>
                <div className="form-group row">
                  <label className="col-2" id="ut">
                    DESCRIPTION :
                  </label>
                  <textarea
                    rows={10}
                    className="form-control col-10"
                    name="description"
                    onChange={this.onChange}
                    value={description}
                  />
                </div>
                <div className="form-group row">
                  <label className="col-2" id="ut">
                    GENRE :
                  </label>
                  <select
                    className="form-control col-10"
                    name="genre"
                    onChange={this.onChange}
                    value={genre}
                  >
                    <option value="novel">Novel</option>
                    <option value="poetry">Poetry</option>
                    <option value="sci_fi">Science Fiction</option>
                    <option value="drama">Drama</option>
                    <option value="horror">Horror</option>
                    <option value="fiction">Fiction</option>
                    <option value="non_fiction">Non-Fiction</option>
                    <option value="thriller">Thriller</option>
                    <option value="biography">Biography</option>
                    <option value="mystery">Mystery</option>
                    <option value="history">History</option>
                    <option value="auto_biography">Auto-Biography</option>
                    <option value="tragedy">Tragedy</option>
                    <option value="fantasy">Fantasy</option>
                    <option value="fairy_tale">Fairy Tale</option>
                    <option value="kids">Children Stories</option>
                    <option value="graphic_novel">Graphic Novel</option>
                    <option value="philosophy">Philosophy</option>
                    <option value="myth">Mythology</option>
                    <option value="comedy">Comedy</option>
                    <option value="textbook">TextBook</option>
                    <option value="encyclopedia">Encyclopedia</option>
                    <option value="academic_journal">Academic Journal</option>
                  </select>
                </div>
                <div className="form-group row">
                  <label className="col-2" id="ut">
                    THUMBNAIL :
                  </label>
                  <div className="col-10">
                    <i className="fa fa-file-image fa-2x" />
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <input
                      type="file"
                      name="thumbnail"
                      accept="image/jpeg, image/jpg, image/png"
                      onChange={this.onChange2}
                      value={thumbnail}
                    />
                  </div>
                </div>
                <div className="form-group row">
                  <label className="col-2" id="ut">
                    FILE :
                  </label>
                  <div className="col-10">
                    <i className="fa fa-book-open fa-2x" />
                    &nbsp;&nbsp;
                    <input
                      type="file"
                      name="file"
                      onChange={this.onChange3}
                      value={file}
                    />
                  </div>
                </div>
                <br />
                <button
                  className="btn btn-outline-info btn-block"
                  type="submit"
                >
                  Upload
                </button>
              </form>
            </div>
          </div>
        </div>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  auth: state.auth
});

export default connect(
  mapStateToProps,
  { adduploads }
)(Upload_Form);
