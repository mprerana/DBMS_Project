import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import proptypes from "prop-types";
import { getUsers } from "../../actions/Users";
import {
    getFollowing,
  addFollowing
} from "../../actions/Following";
import "./User_suggestions.css";
import { getFollowers } from "../../actions/Followers";
import { createMessage } from "../../actions/messages";

export class Users extends Component {
  static proptypes = {
    Users: proptypes.array.isRequired,
    getUsers: proptypes.func.isRequired,
   //Following: propTypes.object.isRequired,
    //addFollowing: proptypes.func.isRequired
  }; 

  componentDidMount() {
    const { user } = this.props.auth;
    this.props.getUsers();
    this.props.getFollowers(user.id);
    this.props.getFollowing(user.id);
  }

  OnFollow = (id, name) => {
    const { user } = this.props.auth;
    let flag = 0;
    for (var i = 0; i < this.props.Following.following.length; i++) {
      if (
        user.id ===
        id
      ) {
        flag = 1;
        break;
      }
    }

    for (var i = 0; i < this.props.Following.following.length; i++) {
      if (id === this.props.Following.following[i].following_id) {
        flag = 2;
        break;
      }
    }

    if (flag == 1) {
      this.props.createMessage({
        cannotfollow: "You cannot follow yourself"
      });

      return;
    }

    if (flag == 2) {
      this.props.createMessage({
        alreadyFollowing: "Already following"
      });

      return;
    }

  
    const follow = {
      follow: {}
    };
  
    console.log(id);
    console.log(name);
  
    this.props.addFollowing(id, this.props.Following.id, follow);
  
    this.setState({ flag: 1 });
  
    // const currentfollowing = {
    //   id: 2345432,
    //   following_id: id,
    //   user: name
    // };
  
    // console.log(this.props.Following.following);
  
    // this.props.Following.following = [
    //   ...this.props.Following.following,
    //   currentfollowing
    // ];
  
    // this.setState({
    //   flag: 0
    // });
  };

  render() {
    let nooffollowers = 0;
    
    {
        this.props.Followers.followers
            ? this.props.Followers.followers.forEach((followers) => {
    
                nooffollowers = nooffollowers + 1;
            })
            : null;
    }


    return (
      <Fragment>
        <div className="container-fluid animated fadeInDown">
          {this.props.Users.map(User => (
            <div>
              <div
                className="row"
                style={{
                  padding: "1%",
                  borderRadius: "50px",
                  border: "4px",
                  backgroundColor: "#e6e6e6"
                }}
                key={User.id}
              >
                <div
                  className="col-1"
                  style={{
                    borderRight: "2px solid #3ebeb6",
                    padding: "0"
                  }}
                >
                  <img
                    src="https://i.ibb.co/3kkXHWH/profile-img.jpg"
                    alt="profile_photo"
                    id="profile_photo"
                    height="45"
                    width="45"
                    style={{
                      marginLeft: "auto",
                      marginRight: "auto",
                      display: "block"
                    }}
                  />
                </div>
                <div
                  className="col-6"
                  style={{
                    borderRight: "2px solid #3ebeb6",
                    marginTop: "auto",
                    marginBottom: "auto"
                  }}
                >
                  <span id="usname">
                    {User.user_data.first_name}
                    &nbsp;
                    {User.user_data.last_name}
                  </span>
                  &nbsp;&nbsp;&nbsp;
                  <span id="ususername">@{User.user_data.username}</span>
                </div>
                {/* <div
                  className="col-3"
                  style={{
                    borderRight: "2px solid #3ebeb6",
                    marginTop: "auto",
                    marginBottom: "auto"
                  }}
                >
                  <span id="usnumbers">{nooffollowers}</span>
                  <span id="usft"> Followers</span>
                </div> */}
                <div
                  className="col-2"
                  style={{ marginTop: "auto", marginBottom: "auto" }}
                >
                  <button
                    onClick={this.OnFollow.bind(
                        this,
                        User.id,
                        User.user_data.username
                      )}
                    className="btn btn-info btn-sm"
                  >
                    <i className="fa fa-plus fa-sm" />
                    &nbsp; Follow
                  </button>
                </div>
              </div>
              <br />
            </div>
            // {User.user_data.id}
            // {User.user_data.email}
            // {User.dob}
            // {User.mobile_no}
          ))}
        </div>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  Users: state.Users.Users,
  Followers: state.Followers.Followers,
  Following: state.Following.Following,
  auth: state.auth
});

export default connect(
  mapStateToProps,
   { getUsers, addFollowing, getFollowing, getFollowers, createMessage }
)(Users);
