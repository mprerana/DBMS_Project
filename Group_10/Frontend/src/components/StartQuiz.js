import React from "react";
import axios from "axios";
import Paper from "@material-ui/core/Paper";
import Typography from "@material-ui/core/Typography";
import { withStyles } from "@material-ui/core/styles";
import PropTypes from "prop-types";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";

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
class StartQuizPage extends React.Component {
  state = {
    status_box_text: "",
    userinfo: [],
    quizdata: [],
    quizstarted: false,
    accessKey: ""
  };
  setData = e => {
    this.setState(
      {
        accessKey: e.target.value
      },
      () => {
        console.log(this.state.accessKey);
      }
    );
  };
  sendData = event => {
    console.log(this.state.accessKey);
    var token = localStorage.getItem("auth-token");
    var config = {
      headers: { "x-access-token": token }
    };
    var data = {
      accesskey: this.state.accessKey,
      quizid: this.props.match.params.quizid
    };
    console.log(data.accesskey);
    axios
      .post("http://10.0.36.104:8000/quiz/startquiz", data, config)
      .then(res => {
        const status_box_text = "Quiz Started.You may take the quiz";
        const quizstarted = true;
        this.setState({ status_box_text });
        this.setState({ quizstarted });
      })
      .catch(err => {
        const status_box_text = "Invalid AccessKey";
        this.setState({ status_box_text });
      });
  };
  componentDidMount() {
    var token = localStorage.getItem("auth-token");
    var config = {
      headers: { "x-access-token": token }
    };
    axios.get("http://10.0.36.104:8000/api/auth/me", config).then(res => {
      const userinfo = res.data[0];
      this.setState({ userinfo });
    });
    axios
      .get(
        "http://10.0.36.104:8000/quiz/getquiz/" +
          this.props.match.params.quizid,
        config
      )
      .then(res => {
        const quizdata = res.data[0];
        this.setState({ quizdata });
      });
  }
  render() {
    const { classes } = this.props;
    return (
      <div
        style={{
          backgroundColor: "#e0e0e0",
          position: "absolute",
          top: 0,
          width: "100%",
          height: "100%",
          marginLeft: "-20px"
        }}
      >
        <div
          style={{
            paddingTop: "10%",
            width: "75%",
            display: "inline-block"
          }}
        >
          <Paper
            className={classes.paper}
            elevation={1}
            style={{
              backgroundColor: "#82b1ff",
              color: "#212121"
            }}
          >
            <Typography
              component="h2"
              variant="display1"
              gutterBottom
              ref="accesskey"
              style={{
                paddingTop: "40px",
                fontWeight: "light",
                fontSize: "20px",
                color: "#212121"
              }}
            >
              You are about to start quiz
            </Typography>
            <Typography
              component="h2"
              variant="display1"
              gutterBottom
              ref="accesskey"
              style={{
                paddingTop: "10px",
                fontWeight: "regular",
                color: "#212121"
              }}
            >
              {console.log(this.state.quizdata.quizname)}
              {this.state.quizdata.quizname}
            </Typography>
            <TextField
              id="accesskey"
              onChange={this.setData}
              label="Access Key"
              placeholder="YOLO"
              className={classes.textField}
              margin="normal"
              style={{
                color: "#fff"
              }}
            />
            <br />
            <br />
            <Button
              variant="contained"
              color="secondary"
              onClick={this.sendData}
            >
              Start Quiz
            </Button>
            {/* <p>Enter the Access Key </p>
            <input type="text" ref="accesskey" />
            <button onClick={this.sendData}>Start Quiz</button>
             */}
            <Typography
              component="h2"
              variant="display1"
              gutterBottom
              ref="accesskey"
              style={{
                marginTop: "20px",
                fontWeight: "light",
                fontSize: "14px",
                marginBottom: "20px"
              }}
            >
              {this.state.status_box_text}
            </Typography>
            {/* <p>{this.state.status_box_text}</p> */}
            <div>
              {this.state.quizstarted ? (
                <Button
                  variant="contained"
                  href={"/quiz/" + this.props.match.params.quizid}
                  style={{
                    backgroundColor: "#212121",
                    color: "#ffff",
                    float: "center",
                    marginBottom: "30px"
                  }}
                >
                  Quiz Link
                </Button>
              ) : (
                ""
              )}
            </div>
          </Paper>
        </div>
      </div>
    );
  }
}

StartQuizPage.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(StartQuizPage);
