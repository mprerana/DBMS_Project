import React from "react";
import axios from "axios";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import CssBaseline from "@material-ui/core/CssBaseline";
import Pagination from "material-ui-flat-pagination";
import { createMuiTheme, MuiThemeProvider } from "@material-ui/core/styles";
import { Typography, Button } from "@material-ui/core";
import Paper from "@material-ui/core/Paper";
import RadioGroup from "@material-ui/core/RadioGroup";
import Radio from "@material-ui/core/Radio";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import Navbar from "./Navbar";
import "./QuizPage.css";
import "../animate.css";
import FormControl from "@material-ui/core/FormControl";
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogContentText from "@material-ui/core/DialogContentText";
import DialogTitle from "@material-ui/core/DialogTitle";
import Slide from "@material-ui/core/Slide";

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

function Transition(props) {
  return <Slide direction="up" {...props} />;
}

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

class SelectedListItem extends React.Component {
  state = {
    selectedIndex: 1,
    offset: 0,
    limit: 2,
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
    ],
    answers: [],
    endtime: null,
    open: false
  };

  handleClickOpen = () => {
    this.setState({ open: true });
  };

  handleClose = () => {
    this.setState({ open: false });
  };

  componentDidMount = () => {
    var answers = this.state.answers;
    answers = Array(this.state.qdata.length).map((value, index) => {
      return "";
    });
    console.log(answers);
    this.setState({
      answers: answers
    });
    var token = localStorage.getItem("auth-token");
    var config = {
      headers: { "x-access-token": token }
    };
    axios
      .get(
        "http://10.0.36.104:8000/quiz/getquiz/" +
          this.props.match.params.quizid,
        config
      )
      .then(res => {
        const quizname = res.data[0].quizname;
        const qdata = res.data[0].qdata;
        this.setState({ quizname });
        this.setState({ qdata });
        this.setState({
          limit: this.state.qdata.length - 2
        });
      });
  };

  handleListItemClick = (event, index) => {
    this.setState({ selectedIndex: index });
  };

  handlePageChange = e => {
    console.log(e.target.value);
  };

  handleClick(e, offset) {
    console.log(offset);
    this.setState({ offset });
  }

  handleChange = e => {
    const options = this.state.qdata[this.state.offset].options;
    //answer number
    //SendAnswer
    var token = localStorage.getItem("auth-token");
    var config = {
      headers: { "x-access-token": token }
    };
    var data = {
      quizid: parseInt(this.props.match.params.quizid),
      question: this.state.offset,
      answer: options.findIndex(option => {
        return option == e.target.value;
      })
    };
    console.log(data);
    axios
      .post("http://10.0.36.104:8000/quiz/sendAnswer", data, config)
      .then(res => {
        console.log(res);
      });

    var answer = e.target.value;
    var ansNo = options.findIndex(option => {
      return option == e.target.value;
    });
    var answers = this.state.answers.slice();
    answers[this.state.offset] = answer;
    this.setState(
      {
        answers: answers
      },
      () => {
        console.log(this.state.answers);
      }
    );
  };

  render() {
    const { classes } = this.props;
    const messagebox = (
      <div>
        <Button
          variant="contained"
          onClick={() => {
            this.handleClickOpen();
          }}
          style={{
            backgroundColor: "#212121",
            color: "#ffff",
            float: "right",
            marginRight: "12.5%"
          }}
        >
          Submit Quiz
        </Button>
        <Dialog
          open={this.state.open}
          TransitionComponent={Transition}
          keepMounted
          onClose={this.handleClose}
          aria-labelledby="alert-dialog-slide-title"
          aria-describedby="alert-dialog-slide-description"
        >
          <DialogTitle id="alert-dialog-slide-title">{"Exit"}</DialogTitle>
          <DialogContent>
            <DialogContentText id="alert-dialog-slide-description">
              Are you sure you want to exit this quiz?
            </DialogContentText>
          </DialogContent>
          <DialogActions>
            <Button onClick={this.handleClose} color="primary">
              No
            </Button>
            <Button onClick={this.handleClose} href="/profile" color="primary">
              Yes
            </Button>
          </DialogActions>
        </Dialog>
      </div>
    );
    const questionNum = this.state.offset;
    const questiontext = this.state.qdata[this.state.offset].questiontext;
    console.log(questiontext);
    const options = this.state.qdata[this.state.offset].options;
    console.log(options);
    var id = 0;
    const answer = this.state.answers[this.state.offset];
    console.log(
      "offset",
      this.state.offset,
      "asnwer",
      this.state.answers[this.state.offset]
    );
    const optionList = (
      <MuiThemeProvider theme={theme}>
        <FormControl
          component="fieldset"
          color="primary"
          className={classes.formControl}
        >
          <RadioGroup
            aria-label="Gender"
            name="gender1"
            // value='Golden State Warriros'
            value={answer}
            onChange={this.handleChange}
          >
            {options.map((op, opNum) => (
              <FormControlLabel
                value={op}
                id={opNum}
                control={<Radio />}
                label={op}
              />
            ))}
          </RadioGroup>
        </FormControl>
      </MuiThemeProvider>
    );
    const OptionList = options.map((option, id) => (
      <span
        id={id}
        onClick={event => {
          console.log(questionNum, event.target.id);
        }}
      >
        {/*
        <ListItem
          id={id}
          button
          selected={false}
          key={option.toString()}
          //onClick={event => this.handleListItemClick(event, 2)}
        >
          <ListItemText primary={option} />
        </ListItem> */}
      </span>
    ));
    console.log(this.state.offset);
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
          <Button
            variant="contained"
            style={{
              backgroundColor: "#212121",
              color: "#ffff",
              marginTop: "20px",
              float: "left"
            }}
            onClick={() => {
              if(this.state.offset==0){
                return 0
              }
              this.setState({
                offset: this.state.offset - 1
              },()=>{
                console.log(this.state.offset, this.state.limit)
              });
            }}
          >
            Previos Question
          </Button>

          <Button
            variant="contained"
            style={{
              backgroundColor: "#212121",
              color: "#ffff",
              marginTop: "20px",
              float: "right"
            }}
            onClick={() => {
              console.log(this.state.offset, this.state.limit);
              /* if(this.state.offset==this.state.limit){
                return 0
              } */
              if (this.state.offset==this.state.limit)
                return 0;
              this.setState({
                offset: this.state.offset + 1
              },()=>{
                console.log('wow', this.state.offset, this.state.limit)
              });
            }}
          >
            Next Question
          </Button>
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
          {messagebox}
        </div>
      </div>
    );
  }
}

SelectedListItem.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(SelectedListItem);
