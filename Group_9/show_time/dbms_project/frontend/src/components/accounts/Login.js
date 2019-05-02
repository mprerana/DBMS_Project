import React, { Component } from "react";
import { Link, Redirect } from "react-router-dom";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import 'bootstrap/dist/css/bootstrap.min.css';
import './login.css';
import { login } from "../../actions/auth";

export class Login extends Component {
  state = {
    username: "",

    password: ""
  };

  onSubmit = e => {
    e.preventDefault();
    const { username, password } = this.state;
    this.props.login(this.state.username, this.state.password);
  };

  static propTypes = {
    login: PropTypes.func.isRequired,
    isAuthenticated: PropTypes.bool
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });
  render() {
    if (this.props.isAuthenticated) {
      return <Redirect to="/" />;
    }

    const { username, password } = this.state;
    return (
      <div className='background1'>
      <div className='container' style={{paddingTop:'150px',paddingBottom:'150px'}}>
      <div className="profile-main">

          
          <form onSubmit={this.onSubmit}>
          <p style={{fontSize: '30px',color:'#e19536',marginLeft:'130px',marginTop:'30px',fontFamily:'open sans'}}>Log in </p> <br />
            <div className="form-group">
              <label style={{color:" #e19536"}}>Username</label>
              <input
                type="text"
                className="form-control"
                name="username"
                onChange={this.onChange}
                value={username} 
                style={{backgroundColor:'transparent',color:'white'}}
                spellCheck='false'
              />
            </div>

            <div className="form-group">
              <label style={{color:" #e19536"}}>Password</label>
              <input
                type="password"
                className="form-control"
                name="password"
                onChange={this.onChange}
                value={password}
                style={{backgroundColor:'transparent',color:'white'}}
                spellCheck='false'
              />
            </div>
            <div className="form-group form-check">
              <label className="form-check-label">
                <input className="form-check-input" type="checkbox" name="remember" style={{width: '20px',backgroundColor:' rgba(255,255,255,0.9)'}} /><span style={{color: '#e19536'}}>Remember me</span> 
            </label><br /><br />
            </div>
            


            <p>
              Don't Have an account? <Link to="/register"><span style={{fontFamily:' Raleway',fontSize:'18px',fontSize:'17px',color:'#84d5d9'}}>Register</span></Link>
            </p>
            <p style={{marginLeft: '29%',marginTop: '2%',}}>
              <button type="submit" className="button button-q" >
                Login
              </button></p><br />
            
            
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
  { login }
)(Login);
