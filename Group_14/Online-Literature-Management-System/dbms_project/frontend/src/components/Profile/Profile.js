import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getProfile, editProfile } from "../../actions/Profile";
import { Link } from "react-router-dom";
import Header_1 from "../home_page/Header_1";
import "./Profile.css";

export class Profile extends Component {
  state = {
    showProfileInfo: true,
    first_name: "",
    last_name: "",
    email: "",
    dob: "",
    mobile_no: "",
    image: "",
    bio: ""
  };
  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmit = e => {
    e.preventDefault();
    const {
      first_name,
      last_name,
      email,
      dob,
      mobile_no,
      image,
      bio
    } = this.state;

    const updatedUser = {
      newdetails: {
        first_name: first_name,
        last_name: last_name,
        email: email,
        dob: dob,
        mobile_no: mobile_no,
        image: null,
        bio: bio
      }
    };

    const { user } = this.props.auth;

    console.log(updatedUser);

    this.props.editProfile(user.id, updatedUser);

    this.setState({ showProfileInfo: !this.state.showProfileInfo });
  };

  onShowClick = e => {
    this.setState({ showProfileInfo: !this.state.showProfileInfo });

    let dateofbirth = this.props.Profile.dob ? this.props.Profile.dob : null;
    let mobile_number = this.props.Profile.mobile_no
      ? this.props.Profile.mobile_no
      : "";
    let biodata = this.props.Profile.bio ? this.props.Profile.bio : "";

    this.setState({
      first_name: this.props.Profile.first_name,
      last_name: this.props.Profile.last_name,
      email: this.props.Profile.email,
      dob: dateofbirth,
      mobile_no: mobile_number,
      image: "",
      bio: biodata
    });
  };

  static PropTypes = {
    Profile: PropTypes.object.isRequired,
    getProfile: PropTypes.func.isRequired,
    editProfile: PropTypes.func.isRequired,
    auth: PropTypes.object.isRequired
  };

  componentDidMount() {
    const { user } = this.props.auth;
    this.props.getProfile(user.id);
  }

  render() {
    const { showProfileInfo } = this.state;
    const {
      first_name,
      last_name,
      email,
      dob,
      mobile_no,
      image,
      bio
    } = this.state;
    return (
      <Fragment>
        <Header_1 />
        <div
          className="container animated fadeInUp"
          style={{ paddingTop: "120px" }}
        >
          <button
            onClick={this.onShowClick}
            className="btn btn-success btn-block"
          >
            <i className="fas fa-edit" />
            &nbsp; Edit
          </button>
          <br />

          {showProfileInfo ? (
            <div className="card">
              <div className="card-body">
                <div class=" row">
                  <span id="pt" className="col-2">
                    User-Name :
                  </span>
                  <span className="col-10">
                    {this.props.Profile.username}
                    &nbsp;&nbsp;&nbsp;
                    <i
                      className="fas fa-lock  "
                      data-toggle="tooltip"
                      data-placement="top"
                      title="Cannot edit"
                    />
                  </span>
                </div>
                <hr />
                <div class="row">
                  <span id="pt" className="col-2">
                    First Name :
                  </span>
                  <span className="col-10">
                    {this.props.Profile.first_name}
                  </span>
                </div>
                <hr />
                <div class="row">
                  <span id="pt" className="col-2">
                    Last Name :
                  </span>
                  <span className="col-10">{this.props.Profile.last_name}</span>
                </div>
                <hr />
                <div class="row">
                  <span id="pt" className="col-2">
                    E-mail id :
                  </span>
                  <span className="col-10">{this.props.Profile.email}</span>
                </div>
                <hr />
                <div class="row">
                  <span id="pt" className="col-2">
                    Date of Birth :
                  </span>
                  <span className="col-10">{this.props.Profile.dob}</span>
                </div>
                <hr />
                <div class="row">
                  <span id="pt" className="col-2">
                    Phone Number :
                  </span>
                  <span className="col-10">{this.props.Profile.mobile_no}</span>
                </div>
                <hr />
                <div class="row">
                  <span id="pt" className="col-2">
                    Profile Photo :
                  </span>
                  <span className="col-10">
                    <i className="fas fa-file-image " />
                    {this.props.Profile.image}
                  </span>
                </div>
                <hr />
                <div class="row">
                  <span id="pt" className="col-2">
                    Bio :
                  </span>
                  <span className="col-10">{this.props.Profile.bio}</span>
                </div>
              </div>
            </div>
          ) : (
            <div className="card">
              <div className="card-body">
                <form onSubmit={this.onSubmit}>
                  <div className="form-group row">
                    <label for="fn" className="col-2 col-form-label" id="pt">
                      First-Name :
                    </label>
                    <input
                      type="text"
                      id="fn"
                      className="form-control col-10"
                      name="first_name"
                      onChange={this.onChange}
                      value={first_name}
                    />
                  </div>
                  <div className="form-group row">
                    <label for="ln" className="col-2 col-form-label" id="pt">
                      Last-Name :
                    </label>
                    <input
                      type="text"
                      id="ln"
                      className="form-control col-10"
                      name="last_name"
                      onChange={this.onChange}
                      value={last_name}
                    />
                  </div>
                  <div className="form-group row">
                    <label for="em" className="col-2 col-form-label" id="pt">
                      E-mail :
                    </label>
                    <input
                      type="email"
                      id="em"
                      className="form-control col-10"
                      name="email"
                      onChange={this.onChange}
                      value={email}
                    />
                  </div>
                  <div className="form-group row">
                    <label for="dob" className="col-2 col-form-label" id="pt">
                      Date of Birth :
                    </label>
                    <input
                      type="date"
                      id="dob"
                      className="form-control col-10"
                      name="dob"
                      onChange={this.onChange}
                      value={dob}
                    />
                  </div>
                  <div className="form-group row">
                    <label for="phn" className="col-2 col-form-label" id="pt">
                      Phone Number :
                    </label>
                    <input
                      type="text"
                      className="form-control col-10"
                      id="phn"
                      name="mobile_no"
                      onChange={this.onChange}
                      value={mobile_no}
                    />
                  </div>
                  <div className="form-group row">
                    <label for="pimg" className="col-2 col-form-label" id="pt">
                      Profile Photo :
                    </label>
                    <input
                      type="file"
                      id="pimg"
                      name="image"
                      onChange={this.onChange}
                      value={image}
                    />
                  </div>
                  <div className="form-group row">
                    <label for="bio" className="col-2 col-form-label" id="pt">
                      Bio :
                    </label>
                    <input
                      type="text"
                      className="form-control col-10"
                      id="bio"
                      name="bio"
                      onChange={this.onChange}
                      value={bio}
                    />
                  </div>
                  <button className="btn btn-outline-info" type="submit">
                    <i className="fas fa-save" />
                    &nbsp; Save
                  </button>
                </form>
              </div>
            </div>
          )}
        </div>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  auth: state.auth,
  Profile: state.Profile.Profile
});

export default connect(
  mapStateToProps,
  { getProfile, editProfile }
)(Profile);
