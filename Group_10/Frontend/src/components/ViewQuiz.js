import React from "react";
import axios from "axios";
import FormControl from "@material-ui/core/FormControl";
import RadioGroup from "@material-ui/core/RadioGroup";
import Radio from "@material-ui/core/Radio";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import CssBaseline from "@material-ui/core/CssBaseline";
import Pagination from "material-ui-flat-pagination";
import { createMuiTheme, MuiThemeProvider } from "@material-ui/core/styles";
import { Typography, Button } from "@material-ui/core";
import Paper from "@material-ui/core/Paper";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItemText";

const theme = createMuiTheme({
  palette: {
    primary: {
      main: "#616161"
    },
    secondary: {
      main: "#212121"
    }
  },
  shadows: ["none"],
  overrides: {
    MuiButton: {
      // Name of the component ⚛️ / style sheet
      text: {
        // Name of the rule
        color: "white" // Some CSS
      }
    }
  }
});

const styles = theme => ({
  root: {
    textAlign: "center",
    color: "#fff",
    "&$checked": {
      color: "#fff"
    }
  },
  paper: {
    ...theme.mixins.gutters(),
    paddingTop: theme.spacing.unit * 1,
    paddingBottom: theme.spacing.unit * 1
  },
  outsidePaper: {
    display: "inline-block",
    width: "75%"
  },
  options: {
    paddingTop: theme.spacing.unit * 1,
    paddingBottom: theme.spacing.unit * 1
  },
  group: {
    marginLeft: "10px",
    margin: `${theme.spacing.unit}px 0`
  },
  option: {
    color: "#fff"
  },
  formControl: {
    margin: theme.spacing.unit * 3,
    color: "#fff"
  },
  label: {
    color: "#fff"
  },
  control: {
    color: "#fff"
  }
});

class QuizInfo extends React.Component {
  state = {
    quizdata: [],
    userinfo: [],
    selectedIndex: 1,
    offset: 0,
    limit: 0,
    quizname: "General Knowledge Quiz",
    qdata: [
      {
        id: "1",
        questiontext: "Which one is correct team name in NBA?",
        options: [
          "New York Bulls",
          "Los Angeles Kings",
          "Golden State Warriros",
          "Houston Rockets"
        ],
        answer: "Houston Rockets"
      },
      {
        id: "2",
        questiontext: "5 + 7 = ?",
        options: ["10", "11", "12", "13"],
        answer: "12"
      },
      {
        id: "3",
        questiontext: "12 - 8 = ?",
        options: ["1", "2", "3", "4"],
        answer: "4"
      }
    ]
  };

  handleClick = (e, offset) => {
    this.setState({
      offset: offset
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
        console.log(this.state.quizdata.qdata[0]);

        const quiz = this.state.quizdata.qdata.slice();
        this.setState(
          {
            qdata: quiz,
            quizname: this.state.quizdata.quizname,
            limit: this.state.qdata.length - 2
          },
          () => {
            console.log("limit", this.state.limit);
          }
        );
      });
  }
  render() {
    const { classes } = this.props;
    const questionNum = this.state.offset;
    console.log("quiz", this.state.quizdata.qdata);
    //const questiontext = this.state.qdata[this.state.offset].questiontext;
    const questiontext = this.state.qdata[this.state.offset].questiontext;
    console.log(questiontext);
    const options = this.state.qdata[this.state.offset].options;

    const optionList = (
      <MuiThemeProvider theme={theme}>
        <List component="nav">
          {options.map((op, opNum) => (
            <ListItem>
              <ListItemText primary={op} id={opNum} />
            </ListItem>
          ))}
        </List>
      </MuiThemeProvider>
    );

    return (
      <div
        className={classes.root}
        style={{
          backgroundColor: "#e0e0e0",
          position: "absolute",
          top: 0,
          width: "100%",
          height: "100%"
        }}
      >
        {JSON.stringify(this.state.quizdata, null, 2)}
        <Typography
          variant="caption"
          className="bounceIn"
          style={{
            textAlign: "center",
            paddingTop: "7%",
            paddingBottom: "2%",
            fontSize: "16px"
          }}
        >
          {this.state.quizname}
        </Typography>
        <div className={classes.outsidePaper}>
          <Paper
            className={classes.paper}
            elevation={1}
            style={{
              backgroundColor: "#212121"
            }}
          >
            <Typography
              variant="h4"
              style={{
                textAlign: "center",
                paddingTop: "5%",
                paddingBottom: "5%",
                color: "#fff"
              }}
            >
              {questiontext}
            </Typography>
          </Paper>
        </div>
        <div
          style={{
            width: "76%",
            position: "relative",
            height: "auto",
            margin: "0 auto",
            padding: "10px"
          }}
        >
          <Paper style={{ color: "#fff" }}>{optionList}</Paper>
        </div>
        <div
          style={{
            top: "10%",
            float: "center",
            marginLeft: "0%",
            paddingTop: "5%"
          }}
        >
          <MuiThemeProvider theme={theme}>
            <CssBaseline />
            <Pagination
              limit={1}
              offset={this.state.offset}
              total={this.state.qdata.length}
              onClick={(e, offset) => this.handleClick(e, offset)}
              style={{
                marginTop: "-65px",
                marginBottom: "20px"
              }}
            />
          </MuiThemeProvider>
        </div>
      </div>
    );

    /* return(
      <div>
      <h1>Quiz Details:{this.state.quizdata.quizname} </h1>
      <pre>{JSON.stringify(this.state.quizdata,null,2)}</pre>
      </div> 
    )*/
  }
}

QuizInfo.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(QuizInfo);
