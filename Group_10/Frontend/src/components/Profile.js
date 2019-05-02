import React from "react";
import axios from "axios";
import JoinCourse from "./JoinCourse";
import CreateCourse from "./CreateCourse";
import Paper from "@material-ui/core/Paper";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import Typography from "@material-ui/core/Typography";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import CourseContainer from "./CourseContainer";

const styles = theme => ({
  close: {
    padding: theme.spacing.unit / 2
  },
  paper: {
    ...theme.mixins.gutters(),
    paddingTop: theme.spacing.unit * 1,
    paddingBottom: theme.spacing.unit * 1
  }
});

class Profile extends React.Component {
  state = {
    userinfo: [],
    courses: []
  };
  componentDidMount() {
    var pagetitle = document.getElementById("pagetitle");
    pagetitle.innerHTML = "Profile";
    var token = localStorage.getItem("auth-token");
    var config = {
      headers: { "x-access-token": token }
    };
    axios.get("http://10.0.36.104:8000/api/auth/me", config).then(res => {
      const userinfo = res.data[0];
      console.log(userinfo);
      this.setState({ userinfo });
    });
    axios.get("http://10.0.36.104:8000/course/listgroups", config).then(res => {
      const courses = res.data;
      this.setState({ courses });
    });
  }

  render() {
    const { classes } = this.props;

    var course_container_list = this.state.courses.map(course_object => (
      <a href={"/courses/" + course_object.cid}>
        <CourseContainer data={course_object} />
      </a>
    ));

    const courses = [
      { cid: 0, cname: "DBMS" },
      { cid: 1, cname: "Machine Learning" }
    ];
    const courseList = courses.map(course => (
      <a href={"/courses/" + course.cid}>
        <CourseContainer data={course} />
      </a>
    ));
    return (
      <div
        style={{
          backgroundColor: "#e0e0e0",
          position: 'absolute',
          width: "102%",
          minHeight: "100%",
          top: 0,
          marginLeft: "-10px",
          textAlign: "center"
        }}
      >
        <div
          style={{
            paddingTop: "7%",
            width: "75%",
            display: 'inline-block',
            textAlign: 'center'
          }}
        >
          <Paper className={classes.paper} elevation={1}>
            <Typography
              component="h2"
              variant="display3"
              gutterBottom
              style={{
                paddingTop: "40px"
              }}
            >
              Profile
            </Typography>
            <Typography
              component="h2"
              variant="display1"
              gutterBottom
              style={{
                fontSize: "18px",
                paddingRight: "80px"
              }}
              align="right"
            >
              {this.state.userinfo.username}
            </Typography>
            <Typography
              component="h2"
              variant="display1"
              gutterBottom
              style={{
                paddingTop: "0px",
                fontSize: "14px",
                paddingRight: "80px"
              }}
              align="right"
            >
              {this.state.userinfo.email}
            </Typography>
            {/* <div>
              {this.state.userinfo.username},{this.state.userinfo.email}
            </div> */}
            <Typography
              component="h2"
              variant="display1"
              gutterBottom
              style={{
                marginTop: "-50px",
                paddingTop: "-20px",
                fontWeight: "lighter",
                paddingLeft: "80px",
                paddingBottom: "20px"
              }}
              align="left"
            >
              Your Courses
            </Typography>
            <div>{course_container_list}</div>
            <p>
              {this.state.userinfo.isTeacher ? (
                <CreateCourse />
              ) : (
                <JoinCourse />
              )}
            </p>
          </Paper>
        </div>
      </div>
    );
  }
}

Profile.propTypes = {
  classes: PropTypes.object.isRequired
};

CourseContainer.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(Profile);
