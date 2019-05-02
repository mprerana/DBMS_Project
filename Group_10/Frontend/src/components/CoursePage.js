import React from "react";
import axios from "axios";
import Paper from "@material-ui/core/Paper";
import { withStyles } from "@material-ui/core/styles";
import PropTypes from "prop-types";
import Typography from "@material-ui/core/Typography";
import QuizContainer from "./QuizContainer";
import { Button } from "@material-ui/core";

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
/* class QuizContainer extends React.Component {
  render() {
    return (
      <div>
        Quiz Name:{this.props.data.quizname}
        <br />
        Start Time:{this.props.data.starttime} | End time:
        {this.props.data.endtime}
      </div>
    );
  }
}
 */
class Course extends React.Component {
  state = {
    quizlist: [],
    courseinfo: [],
    userinfo: []
  };
  componentDidMount() {
    var token = localStorage.getItem("auth-token");
    var pagetitle = document.getElementById("pagetitle");
    pagetitle.innerHTML = "Course";
    var config = {
      headers: { "x-access-token": token }
    };
    axios.get("http://10.0.36.104:8000/api/auth/me", config).then(res => {
      const userinfo = res.data[0];
      console.log(userinfo);
      this.setState({ userinfo });
    });
    axios
      .get(
        "http://10.0.36.104:8000/quiz/listquizzes/" +
          this.props.match.params.cid,
        config
      )
      .then(res => {
        const quizlist = res.data;
        this.setState({ quizlist });
      });
    axios
      .get(
        "http://10.0.36.104:8000/course/courseinfo/" +
          this.props.match.params.cid,
        config
      )
      .then(res => {
        const courseinfo = res.data[0];
        this.setState({ courseinfo });
      });
  }
  render() {
    const { classes } = this.props;

    var quiz_container_list = this.state.quizlist.map(quiz_object => (
      <span>
        <a
          href={
            this.state.userinfo.isTeacher
              ? "/viewquiz/" + quiz_object.quizid
              : "/startquiz/" + quiz_object.quizid
          }
        >
          <QuizContainer data={quiz_object} />
        </a>
        {/* <a href={"/quizresults/" + quiz_object.quizid}>
          <p>View Results</p>
        </a> */}
      </span>
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
            marginTop: "7%",
            width: "75%",
            display: "inline-block",
            textAlign: "center"
          }}
        >
          <Paper className={classes.paper} elevation={1} style={{
            paddingBottom: '10%'
          }}>
            <Typography
              component="h2"
              variant="display3"
              gutterBottom
              style={{
                paddingTop: "40px",
              }}
            >
              {this.state.courseinfo.cname}
            </Typography>
            <Typography
              component="h2"
              variant="display1"
              gutterBottom
              style={{
                fontSize: "18px",
                paddingRight: "80px",
                paddingTop: "20px"
              }}
              align="right"
            >
              Instructor: {this.state.courseinfo.name}
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
              {this.state.courseinfo.email}
            </Typography>
            <Typography
              variant="caption"
              gutterBottom
              style={{
                marginTop: "-40px",
                paddingTop: "10px",
                fontSize: "14px",
                paddingLeft: "80px"
              }}
              align="left"
            >
              JoinKey: {this.state.courseinfo.joinKey}
            </Typography>
            <Typography
              component="h2"
              variant="display1"
              gutterBottom
              style={{
                paddingTop: "40px",
                fontWeight: "lighter"
              }}
            >
              Quizzes
            </Typography>
            <div>{quiz_container_list}</div>
            {this.state.userinfo.isTeacher ? (
              <Button
                variant="contained"
                color="secondary"
                href={"/createquiz/" + this.state.courseinfo.cid}
                style={{
                  float:'left',
                  marginLeft: '10%'
                }}
              >
                Create New Quiz
              </Button>
            ) : null}
            {this.state.userinfo.isTeacher ? (
              <Button
                variant="contained"
                color="secondary"
                href={"/PdfUpload/" + this.state.courseinfo.cid}
                style={{
                  float:'center',
                }}
              >
                Add Quiz from PDF
              </Button>
            ) : null}
            <Button
                variant="contained"
                color="secondary"
                href={"/courseresults/" + this.state.courseinfo.cid}
                style={{
                  float:'right',
                  marginRight: '10%'
                }}
              >
                View Course Results
              </Button>
          </Paper>
        </div>
      </div>
    );
  }
}

Course.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(Course);
