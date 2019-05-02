import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getUserProfile, UpdateUserProfile } from "../../actions/userprofile";
import { createMessage } from "../../actions/messages";
import "./editprofile.css";

export class EditProfile extends Component {
  state = {
    showProfileChangeInfo: true,
    email: "",
    first_name: "",
    last_name: "",
    dob: "",
    city: "",
    phone: "",
    image: ""
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onShowClick = e => {
    this.setState({
      showProfileChangeInfo: !this.state.showProfileChangeInfo
    });

    this.setState({
      email: this.props.userprofile.email,
      first_name: this.props.userprofile.first_name,
      last_name: this.props.userprofile.last_name,
      dob: this.props.userprofile.dob,
      city: this.props.userprofile.city,
      phone: this.props.userprofile.phone,
      image: ""
    });
  };

  onSubmit = e => {
    e.preventDefault();
    console.log("submit");

    const {
      email,
      first_name,
      last_name,
      dob,
      city,
      phone,
      image
    } = this.state;

    if (dob === "") {
      this.props.createMessage({ dobEmpty: "DOB field is required" });
      return;
    } else if (city === "") {
      this.props.createMessage({ cityEmpty: "City field is required" });
      return;
    } else if (phone === "") {
      this.props.createMessage({ phoneEmpty: "Phone field is required" });
      return;
    } else {
      const updatedUser = {
        newdetails: {
          email: email,
          first_name: first_name,
          last_name: last_name,
          dob: dob,
          city: city,
          phone: phone,
          image: null
        }
      };

      console.log(updatedUser);

      this.props.UpdateUserProfile(this.props.auth.user.id, updatedUser);

      this.setState({
        showProfileChangeInfo: !this.state.showProfileChangeInfo
      });
    }
  };

  static propTypes = {
    userprofile: PropTypes.object.isRequired,
    auth: PropTypes.object.isRequired,
    getUserProfile: PropTypes.func.isRequired,
    UpdateUserProfile: PropTypes.func.isRequired
  };

  componentDidMount() {
    const { auth } = this.props.auth;

    if (this.props.auth.user) {
      this.props.getUserProfile(this.props.auth.user.id);
    }
  }

  render() {
    const { showProfileChangeInfo } = this.state;
    const {
      email,
      first_name,
      last_name,
      dob,
      city,
      phone,
      image
    } = this.state;

    return (
      <div className="background3">
        <div
          className="container"
          style={{ paddingTop: "150px", paddingBottom: "150px" }}
        >
          <div className="profile-main2">
            <h1
              style={{
                textAlign: "center",
                paddingTop: "10px",
                paddingBottom: "20px"
              }}
            >
              Edit Profile &nbsp;&nbsp;
              <i onClick={this.onShowClick} className="fas fa-user-edit" />
            </h1>

            {showProfileChangeInfo ? (
              <div className="container">
                <div className="row">
                  <div className="col-lg-6">
                    <div
                      className="profileimg"
                      style={{ textAlign: "center", paddingTop: "12%" }}
                    >
                      {this.props.userprofile.image ? (
                        <img
                          src={`http://127.0.0.1:8000/media/${
                            this.props.userprofile.image
                          }`}
                          className="avatar img-circle"
                          style={{
                            width: "28%",
                            height: "150px",
                            borderRadius: "10px"
                          }}
                        />
                      ) : (
                        <img
                          className="avatar img-circle"
                          style={{
                            width: "28%",
                            height: "150px",
                            borderRadius: "10px"
                          }}
                          src="http://127.0.0.1:8000/media/profile_image/img_avatar.png"
                        />
                      )}
                    </div>
                  </div>
                  <div className="col-lg-6">
                    <ul className="list-group" style={{ color: "black" }}>
                      <li className="list-group-item">
                        Username:
                        {this.props.userprofile.username}
                      </li>
                      <li className="list-group-item">
                        Email: {this.props.userprofile.email}
                      </li>
                      <li className="list-group-item">
                        Firstname:
                        {this.props.userprofile.first_name}
                      </li>
                      <li className="list-group-item">
                        Lastname:
                        {this.props.userprofile.last_name}
                      </li>
                      <li className="list-group-item">
                        {" "}
                        Dob:{this.props.userprofile.dob}
                      </li>
                      <li className="list-group-item">
                        City: {this.props.userprofile.city}
                      </li>

                      <li className="list-group-item">
                        Phone:{this.props.userprofile.phone}
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            ) : (
              <div className="container">
                <form onSubmit={this.onSubmit}>
                  <div className="row">
                    <div className="col-sm-5" style={{ paddingLeft: "20px" }}>
                      <div
                        className="card card-body mt-5"
                        style={{ background: "transparent" }}
                      >
                        <div class="text-center">
                          {this.props.userprofile.image ? (
                            <img
                              src={`http://127.0.0.1:8000/media/${
                                this.props.userprofile.image
                              }`}
                              className="avatar img-circle"
                              style={{
                                width: "35%",
                                height: "150px",
                                borderRadius: "10px"
                              }}
                            />
                          ) : (
                            <img
                              className="avatar img-circle"
                              style={{
                                width: "35%",
                                height: "150px",
                                borderRadius: "10px"
                              }}
                              src="http://127.0.0.1:8000/media/profile_image/img_avatar.png"
                            />
                          )}
                          <h6 style={{ marginTop: "10px" }}>
                            Upload a different photo...
                          </h6>

                          <input type="file" />
                        </div>

                        {/* <div className="form-group">
                  <label>Image</label>
                  <input
                    type="file"
                    className="form-control"
                    name="image"
                    onChange={this.onChange}
                    value={image}
                  />
                </div> */}
                      </div>
                    </div>
                    <div className="col-sm-7" style={{ paddingLeft: "20px" }}>
                      <div
                        className="card card-body mt-5"
                        style={{ background: "transparent" }}
                      >
                        {/* <h2 className="text-center">Update Profile</h2> */}

                        <div className="form-group">
                          <label>Email</label>
                          <input
                            type="email"
                            className="qbox"
                            name="email"
                            onChange={this.onChange}
                            value={email}
                            spellCheck="false"
                          />
                        </div>
                        <div className="form-group">
                          <label>First name</label>
                          <input
                            type="text"
                            className=" qbox"
                            name="first_name"
                            onChange={this.onChange}
                            value={first_name}
                            spellCheck="false"
                          />
                        </div>
                        <div className="form-group">
                          <label>Last name</label>
                          <input
                            type="text"
                            className=" qbox"
                            name="last_name"
                            onChange={this.onChange}
                            value={last_name}
                            spellCheck="false"
                          />
                        </div>

                        <div className="form-group">
                          <label>Date of Birth</label>
                          <input
                            type="date"
                            className=" qbox"
                            name="dob"
                            onChange={this.onChange}
                            value={dob}
                          />
                        </div>
                        <div className="form-group">
                          <label>City</label>
                          <input
                            type="text"
                            className=" qbox"
                            name="city"
                            onChange={this.onChange}
                            value={city}
                            spellCheck="false"
                          />
                        </div>

                        <div className="form-group">
                          <label>Phone</label>
                          <input
                            type="number"
                            className=" qbox"
                            name="phone"
                            onChange={this.onChange}
                            value={phone}
                            spellCheck="false"
                          />
                        </div>
                      </div>
                    </div>
                  </div>
                  <div className="row" style={{ textAlign: "center" }}>
                    <div className="col-lg-12">
                      <button type="submit" className="button button-q">
                        Update Profile
                      </button>
                    </div>
                  </div>
                </form>
              </div>
            )}
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  userprofile: state.userprofile.userprofile,
  auth: state.auth
});

export default connect(
  mapStateToProps,
  { getUserProfile, UpdateUserProfile, createMessage }
)(EditProfile);
