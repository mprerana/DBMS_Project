import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getUserProfile, UpdateUserProfile } from "../../actions/userprofile";
import { createMessage } from "../../actions/messages";

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
      <div style={{ width: "70%", paddingLeft: "30%" }}>
        <div>
          <h1>
            Edit Profile View &nbsp;&nbsp;
            <i
              onClick={this.onShowClick}
              className="fas fa-user-edit"
              style={{ cursor: "pointer" }}
            />
          </h1>
        </div>
        <div>
          {showProfileChangeInfo ? (
            <ul className="list-group">
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
              <li className="list-group-item">
                Image:{this.props.userprofile.image}
              </li>
            </ul>
          ) : (
            <div className="card card-body mt-5">
              <h2 className="text-center">Update Profile</h2>
              <form onSubmit={this.onSubmit}>
                <div className="form-group">
                  <label>Email</label>
                  <input
                    type="email"
                    className="form-control"
                    name="email"
                    onChange={this.onChange}
                    value={email}
                  />
                </div>
                <div className="form-group">
                  <label>First name</label>
                  <input
                    type="text"
                    className="form-control"
                    name="first_name"
                    onChange={this.onChange}
                    value={first_name}
                  />
                </div>
                <div className="form-group">
                  <label>Last name</label>
                  <input
                    type="text"
                    className="form-control"
                    name="last_name"
                    onChange={this.onChange}
                    value={last_name}
                  />
                </div>

                <div className="form-group">
                  <label>Date of Birth</label>
                  <input
                    type="date"
                    className="form-control"
                    name="dob"
                    onChange={this.onChange}
                    value={dob}
                  />
                </div>
                <div className="form-group">
                  <label>City</label>
                  <input
                    type="text"
                    className="form-control"
                    name="city"
                    onChange={this.onChange}
                    value={city}
                  />
                </div>

                <div className="form-group">
                  <label>Phone</label>
                  <input
                    type="number"
                    className="form-control"
                    name="phone"
                    onChange={this.onChange}
                    value={phone}
                  />
                </div>

                <div className="form-group">
                  <label>Image</label>
                  <input
                    type="file"
                    className="form-control"
                    name="image"
                    onChange={this.onChange}
                    value={image}
                  />
                </div>

                <div className="form-group">
                  <button type="submit" className="btn btn-primary">
                    Update Profile
                  </button>
                </div>
              </form>
            </div>
          )}
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
