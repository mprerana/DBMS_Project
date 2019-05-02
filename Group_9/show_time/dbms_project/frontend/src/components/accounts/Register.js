import React, { Component } from "react";
import { Link, Redirect } from "react-router-dom";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { register } from "../../actions/auth";
import './register.css';
import { createMessage } from "../../actions/messages";

export class Register extends Component {
  state = {
    username: "",
    email: "",
    first_name: "",
    last_name: "",
    password: "",
    password2: "",
    dob: "",
    city: "",
    phone: "",
    image: ""
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmit = e => {
    e.preventDefault();

    const {
      username,
      email,
      first_name,
      last_name,
      password,
      password2,
      dob,
      city,
      phone,
      image
    } = this.state;

    if (password !== password2) {
      this.props.createMessage({ passwordNotMatch: "Passwords do not match" });
      return;
    } else if (city === "") {
      this.props.createMessage({ cityEmpty: "City field is required" });
      return;
    } else if (phone === "") {
      this.props.createMessage({ phoneEmpty: "Phone field is required" });
      return;
    } else {
      const newUser = {
        username,
        password,
        email,
        first_name,
        last_name,
        dob,
        city,
        phone,
        image: null
      };

      this.props.register(newUser);
    }
  };

  static propTypes = {
    register: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool
  };

  render() {
    if (this.props.isAuthenticated) {
      return <Redirect to="/" />;
    }

    const {
      username,
      email,
      first_name,
      last_name,
      password,
      password2,
      dob,
      city,
      phone,
      image
    } = this.state;

    return (
      <div className='background2'>
      <div className='container' style={{paddingTop:'150px',paddingBottom:'150px'}}>
        <div className="profile-main1">

          <form onSubmit={this.onSubmit}>
          <p style={{fontSize: '30px',color:'#e19536',marginLeft:'130px',marginTop:'30px',fontFamily:'open sans',fontWeight:'bolder'}}>Register </p> <br />

            <div className="form-group">
              <label style={{color:'#e19536'}}>Username</label>
              <input
                type="text"
                className="form-control"
                name="username"
                onChange={this.onChange}
                value={username}
                placeholder="Username" style={{backgroundColor: 'transparent',color:'white'}}
              />
            </div>
            <div className="form-group">
              <label style={{color:'#e19536'}}>Email</label>
              <input
                type="email"
                className="form-control"
                name="email"
                onChange={this.onChange}
                value={email}
                placeholder="Enter email" style={{backgroundColor: 'transparent',color:'white'}}
                spellCheck='false'
              />
            </div>
            <div className="form-group">
              <label style={{color:'#e19536'}}>First name</label>
              <input
                type="text"
                className="form-control"
                name="first_name"
                onChange={this.onChange}
                value={first_name}
                placeholder="First Name" style={{backgroundColor: 'transparent',color:'white'}}
                spellCheck='false'
              />
            </div>
            <div className="form-group">
              <label style={{color:'#e19536'}}>Last name</label>
              <input
                type="text"
                className="form-control"
                name="last_name"
                onChange={this.onChange}
                value={last_name}
                placeholder="Last Name" style={{backgroundColor: 'transparent',color:'white'}}
                spellCheck='false'
              />
            </div>
            <div className="form-group">
              <label style={{color:'#e19536'}}>Password</label>
              <input
                type="password"
                className="form-control"
                name="password"
                onChange={this.onChange}
                value={password}
                placeholder="Enter password" style={{backgroundColor: 'transparent',color:'white'}}
                spellCheck='false'
              />
            </div>
            <div className="form-group">
              <label style={{color:'#e19536'}}>Confirm Password</label>
              <input
                type="password"
                className="form-control"
                name="password2"
                onChange={this.onChange}
                value={password2}
                placeholder="Confirm password" style={{backgroundColor: 'transparent',color:'white'}}
                spellCheck='false'
              />
            </div>

            <div className="form-group">
              <label style={{color:'#e19536'}}>Date of Birth</label>
              <input
                type="date"
                className="form-control"
                name="dob"
                onChange={this.onChange}
                value={dob}
                placeholder="Enter Date of Birth" style={{backgroundColor: 'transparent',color:''}}
              />
            </div>
            <div className="form-group">
              <label style={{color:'#e19536'}}>City</label>
              <input
                type="text"
                className="form-control"
                name="city"
                onChange={this.onChange}
                value={city}
                placeholder="Enter city" style={{backgroundColor: 'transparent',color:'white'}}
                spellCheck='false'
              />
            </div>

            <div className="form-group">
              <label style={{color:'#e19536'}}>Phone</label>
              <input
                type="number"
                className="form-control"
                name="phone"
                onChange={this.onChange}
                value={phone}
                placeholder="Enter Phone Number" style={{backgroundColor: 'transparent',color:'white'}}
              />
            </div>

            <div className="form-group">
              <label style={{color:'#e19536'}}>Image</label>
              <input
                type="file"
                className="form-control"
                name="image"
                onChange={this.onChange}
                value={image}
                placeholder="Enter Phone Number" style={{backgroundColor: 'transparent',color:'white'}}
              />
            </div>

            <p style={{marginLeft: '25%',marginTop: '2%',}}>
              <button type="submit" className="button button-q">
                Register
              </button></p>
            
            <p style={{marginRight:'20px'}}>
            Already have an account? <Link to="/login"><span style={{fontFamily:' Raleway',fontSize:'18px'}}>Login</span></Link>
            </p>
          </form>
          </div>
</div>
</div>

    );
  }
}

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated
});

export default connect(
  mapStateToProps,
  { register, createMessage }
)(Register);
