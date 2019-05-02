import React, { Component, Fragment } from "react";
import { Link, Redirect } from "react-router-dom";
import { connect } from "react-redux";
import "./Profile_page.css";
import Header_1 from "../home_page/Header_1";
import Uploads from "../Upload/uploads";
import Myreadlists from "../Literature/myreadingliststable";
import Blog from "../Blog/Blog";
import { getProfile } from "../../actions/Profile";
import { getFollowers } from "../../actions/Followers";
import {
  getFollowing,
} from "../../actions/Following";


export class Profile_page extends Component {

  componentDidMount() {
    const { user } = this.props.auth;
    this.props.getProfile(user.id);
    this.props.getFollowers(user.id);
    this.props.getFollowing(user.id);
  }



  render() {
    let nooffollowers = 0;
    
    {
        this.props.Followers.followers
            ? this.props.Followers.followers.forEach((followers) => {
    
                nooffollowers = nooffollowers + 1;
            })
            : null;
    }
        
    let nooffollowing = 0;
    
    {
        this.props.Following.following
            ? this.props.Following.following.forEach((following) => {
    
                nooffollowing = nooffollowing + 1;
            })
            : null;
    }
          


    return (
      <Fragment>
        <Header_1 />
        <div className="container animated fadeInDown" id="pp">
          <div className="row align-items-start justify-content-end pph">
            <Link className="col-2" to="/profile_edit">
              Edit Profile &nbsp;
              <i className="fa fa-user-edit" />
            </Link>
          </div>
          <div className="card" style={{ padding: "4%" }}>
            <div className="row">
              <div
                className="col-2"
                style={{ borderRight: "2px solid #3ebeb6" }}
              >
                <img
                  src="https://i.ibb.co/3kkXHWH/profile-img.jpg"
                  alt="profile_photo"
                  id="profile_photo"
                  height="120"
                  width="120"
                />
              </div>
              <div
                className="col-6"
                style={{ borderRight: "2px solid #3ebeb6" }}
              >
                {/* make this dynamic */}
                {/* fullname */}
                <div id="pname">{this.props.Profile.first_name} {this.props.Profile.last_name} </div>
                {/* username */}
                <div id="pusername">@{this.props.Profile.username}</div>
                <br />
                {/* bio */}
                <div id="pbio">{this.props.Profile.bio}</div>
              </div>
              <div
                className="col-2"
                style={{ borderRight: "2px solid #3ebeb6" }}
              >
                
                <div id="pnumbers">{nooffollowers} </div>
                <div id="pft">Followers</div>
              </div>
              <div className="col-2">
                {/* code for no.of following */}
                <div id="pnumbers">{nooffollowing}</div>
                <div id="pft">Following</div>
              </div>
            </div>
          </div>
          <br />
        </div>
        <br />
        <div
          className="container-fluid"
          style={{ paddingLeft: "5%", paddingRight: "5%" }}
        >
          <ul
            class="nav nav-pills nav-fill"
            id="myTab"
            role="tablist"
            style={{ fontFamily: "Quicksand" }}
          >
            <li class="nav-item">
              <a
                class="nav-link active"
                id="books-tab"
                data-toggle="pill"
                href="#books"
                role="tab"
                aria-controls="books"
                aria-selected="true"
              >
                My Books
              </a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link"
                id="blogs-tab"
                data-toggle="pill"
                href="#blogs"
                role="tab"
                aria-controls="blogs"
                aria-selected="false"
              >
                My Blogs
              </a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link"
                id="lists-tab"
                data-toggle="pill"
                href="#lists"
                role="tab"
                aria-controls="lists"
                aria-selected="false"
              >
                My Reading-lists
              </a>
            </li>
          </ul>
          <br />
          <br />
          <div class="tab-content" id="myTabContent">
            <div
              class="tab-pane fade show active"
              id="books"
              role="tabpanel"
              aria-labelledby="books-tab"
            >
              <Uploads />
            </div>
            <div
              class="tab-pane fade"
              id="blogs"
              role="tabpanel"
              aria-labelledby="blogs-tab"
            >
              <Blog />
            </div>
            <div
              class="tab-pane fade"
              id="lists"
              role="tabpanel"
              aria-labelledby="lists-tab"
              style={{ backgroundColor: "white" }}
            >
              <Myreadlists />
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
  auth: state.auth,
  Profile: state.Profile.Profile
});

export default connect(
  mapStateToProps,
  { getProfile,
    getFollowers,
    getFollowing,}
)(Profile_page);

