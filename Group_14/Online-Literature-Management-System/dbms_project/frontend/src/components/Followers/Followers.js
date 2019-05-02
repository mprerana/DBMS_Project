import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getFollowers } from "../../actions/Followers";
import {
  getFollowing,
  deleteFollowing,
  addFollowing
} from "../../actions/Following";
import { getUsers } from "../../actions/Users";
import { createMessage } from "../../actions/messages";

export class Followers extends Component {
  static propTypes = {
    Followers: PropTypes.object.isRequired,
    getFollowers: PropTypes.func.isRequired,
    Following: PropTypes.object.isRequired,
    getFollowing: PropTypes.func.isRequired,
    deleteFollowing: PropTypes.func.isRequired,
    auth: PropTypes.object.isRequired,
    Users: PropTypes.array.isRequired,
    getUsers: PropTypes.func.isRequired,
    addFollowing: PropTypes.func.isRequired,
    createMessage: PropTypes.func.isRequired
  };

  state = {
    flag: 0
    //following:false,
  };

  showFollowing = e => {
    this.setState({
      //following:true,
    });

    this.setState({ flag: 1 });
  };

  OnUnFollow = (id1, id2) => {
    //this.setState({flag:1});
    this.props.deleteFollowing(id1, id2);

    for (var i = 0; i < this.props.Following.following.length; i++) {
      if (this.props.Following.following[i]["following_id"] == id1) {
        this.props.Following.following.splice(i, 1);
      }
    }

    this.setState({ flag: 1 });
  };

  componentDidMount() {
    const { user } = this.props.auth;
    //console.log(user.id);

    this.props.getFollowers(user.id);
    this.props.getFollowing(user.id);
    this.props.getUsers();
  }

  // OnDeleteFollow = (id1, id2) => {
  //     this.props.deleteFollowing.bind(this, id1, id2);
  // //     this.setState({
  // //
  // //   flag: 0
  // // });
  // };

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

    this.props.addFollowing(id, user.id, follow);

    this.setState({ flag: 1 });

    const currentfollowing = {
      id: 2345432,
      following_id: id,
      user: name
    };

    // this.setState({
    //
    //   flag: 0
    // });

    console.log(this.props.Following.following);

    this.props.Following.following = [
      ...this.props.Following.following,
      currentfollowing
    ];

    this.setState({
      flag: 0
    });
  };

  render() {
    // let nooffollowers = 0;
    //
    // {
    //     this.props.Followers.followers
    //         ? this.props.Followers.followers.forEach((followers) => {
    //
    //             nooffollowers = nooffollowers + 1;
    //         })
    //         : null;
    // }
    //     //console.log(this.props.Followers.followers);
    //
    // let nooffollowing = 0;
    //
    // {
    //     this.props.Following.following
    //         ? this.props.Following.following.forEach((following) => {
    //
    //             nooffollowing = nooffollowing + 1;
    //         })
    //         : null;
    // }
    //     console.log(this.props.Following.following);

    return (
      <Fragment>
        <div className="container">
          <br />
          <br />
          <div className="row">
            <div className="col">
              <div className="list-group">
                <div
                  className="list-group-item active"
                  style={{
                    backgroundColor: "rgb(62, 190, 182)",
                    borderColor: "rgb(62, 190, 182)"
                  }}
                >
                  <h5 style={{ textAlign: "center" }}>Your Followers</h5>
                </div>

                {this.props.Followers.followers ? (
                  this.props.Followers.followers.map(Follower => (
                    <div className="list-group-item" key={Follower.id}>
                      <span>{Follower.user}</span>
                    </div>
                  ))
                ) : (
                  <div className="list-group-item">No followers yet!</div>
                )}
              </div>
            </div>
            <div className="col-1" />
            <div className="col">
              <div className="list-group">
                <div
                  className="list-group-item active"
                  style={{
                    backgroundColor: "rgb(62, 190, 182)",
                    borderColor: "rgb(62, 190, 182)"
                  }}
                >
                  <h5 style={{ textAlign: "center" }}>
                    People you're following
                  </h5>
                </div>

                {this.props.Following.following ? (
                  this.props.Following.following.map(Following => (
                    <div className="list-group-item" key={Following.id}>
                      <div className="row">
                        <div className="col-8">{Following.user}</div>
                        <div className="col-4">
                          <button
                            onClick={this.OnUnFollow.bind(
                              this,
                              Following.following_id,
                              this.props.Following.id
                            )}
                            className="btn btn-outline-danger btn-sm"
                          >
                            Unfollow
                          </button>
                        </div>
                      </div>
                    </div>
                  ))
                ) : (
                  <div className="list-group-item">
                    You haven't followed anyone yet!
                  </div>
                )}
              </div>
            </div>
          </div>
          <br />
          <div className="card">
            <div className="card-header">
              <h5 style={{ textAlign: "center" }}>You can also follow : </h5>
            </div>
            <br />
            <div className="card-body">
              {this.props.Users.map(User => (
                <div>
                  <br />
                  <div
                    className="row"
                    style={{
                      padding: "1%",
                      borderRadius: "50px",
                      border: "4px",
                      backgroundColor: "#e6e6e6aa"
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
                    {/* <div className="col">{User.user_data.id}</div> */}
                    <div
                      className="col-7"
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
                    <div
                      className="col-4"
                      style={{ marginTop: "auto", marginBottom: "auto" }}
                    >
                      <button
                        className="btn btn-info btn-sm"
                        onClick={this.OnFollow.bind(
                          this,
                          User.id,
                          User.user_data.username
                        )}
                        style={{
                          backgroundColor: "rgb(62, 190, 182)",
                          borderColor: "rgb(62, 190, 182)"
                        }}
                      >
                        <i className="fa fa-plus fa-sm" />
                        &nbsp; Follow
                      </button>
                    </div>
                  </div>

                  <br />
                </div>
              ))}
            </div>
          </div>
        </div>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  Followers: state.Followers.Followers,
  Following: state.Following.Following,
  Users: state.Users.Users,
  auth: state.auth
});

export default connect(
  mapStateToProps,
  {
    getFollowers,
    getFollowing,
    deleteFollowing,
    addFollowing,
    getUsers,
    createMessage
  }
)(Followers);
