import React, { Component } from "react";
import axios from "axios";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import Select from "@material-ui/core/Select";
import MenuItem from "@material-ui/core/MenuItem";
import Input from "@material-ui/core/Input";
import InputLabel from "@material-ui/core/InputLabel";
import FormControl from "@material-ui/core/FormControl";
import update from "react-addons-update"; // ES6
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogContentText from "@material-ui/core/DialogContentText";
import DialogTitle from "@material-ui/core/DialogTitle";
import Slide from "@material-ui/core/Slide";

const styles = theme => ({
  root: {
    width: "100%",
    backgroundColor: theme.palette.background.paper
  },
  textField: {
    marginLeft: theme.spacing.unit,
    marginRight: theme.spacing.unit,
    width: "50%"
  },
  title: {
    paddingTop: theme.spacing.unit * 2,
    marginLeft: theme.spacing.unit,
    marginRight: theme.spacing.unit,
    width: "25%"
  },
  textFieldAnswer: {
    marginLeft: theme.spacing.unit,
    marginRight: theme.spacing.unit,
    width: "30%"
  },
  button: { margin: theme.spacing.unit }
});


function Transition(props) {
  return <Slide direction="up" {...props} />;
};

class CreateQuiz extends Component {
  state = {
    title: null,
    quiz: [],
    answers: [],
    accesskey: "",
    starttime: null,
    endtime: null,
    open: false
  };

  handleClickOpen = () => {
    this.setState({ open: true });
  };

  handleClose = () => {
    this.setState({ open: false });
  };

  componentDidMount() {
    var pagetitle = document.getElementById("pagetitle");
    pagetitle.innerHTML = "Create Quiz";
  }

  quiz = () => {
    let questions = [];
    for (let i = 0; i < this.state.quiz.length; i++) {
      let answers = [];
      for (let j = 0; j < this.state.quiz[i].options.length; j++) {
        console.log(this.state.quiz[i].options[j]);
      }
    }
  };

  handleAddQuestion = e => {
    let questions = this.state.quiz;
    let totalQues = this.state.quiz.length;
    console.log(totalQues);
    let sampleQuestion = {
      id: totalQues, // change id when adding question
      questiontext: "SomeQuestion",
      options: ["A", "B"],
      answer: ""
    };
    this.setState(prevState => ({
      quiz: [...prevState.quiz, sampleQuestion]
    }));
  };

  handleAddOption = id => {
    console.log(
      id
    ); /*
    var options = [...this.state.quiz[id].options, 'Another Option'];
    // options.push("Another Option");
    console.log(options);
    this.state.quiz[id].options = options;
    this.forceUpdate(); */
    let quiz = this.state.quiz.slice();
    quiz[id].options.push("Another Option");
    this.setState({
      quiz: quiz
    });
  };

  handleAnswerChange = e => {
    console.log(e.target.value, e.target, e.target.id);
    let quiz = this.state.quiz.slice();
    quiz[e.target.name].answer = e.target.value;
    let answers = this.state.answers;
    answers[e.target.name] = this.state.quiz[e.target.name].options.findIndex(
      option => {
        return option == e.target.value;
      }
    );
    this.setState({
      quiz: quiz,
      answers: answers
    });
  };

  handleQuestionChange = e => {
    console.log(e.target.value, e.target.id);
    let quiz = this.state.quiz.slice();
    quiz[e.target.id].questiontext = e.target.value;
    this.setState({
      quiz: quiz
    });
  };

  handleOptionChange = (questionId, optionId, e) => {
    console.log(questionId, optionId, e.target.value);
    let quiz = this.state.quiz.slice();
    quiz[questionId].options[optionId] = e.target.value;
    this.setState(
      {
        quiz: quiz
      },
      () => {
        console.log(this.state.quiz);
      }
    );
  };

  handleTitleChange = e => {
    this.setState(
      {
        title: e.target.value
      },
      () => {
        console.log(this.state.title);
      }
    );
  };
  handleAccesskeyChange = e => {
    this.setState(
      {
        accesskey: e.target.value
      },
      () => {
        console.log(this.state.accesskey);
      }
    );
  };
  handleStartTimeChange = e => {
    this.setState(
      {
        starttime: e.target.value + "+05:30"
      },
      () => {
        console.log(this.state.starttime);
      }
    );
  };
  handleEndTimeChange = e => {
    this.setState(
      {
        endtime: e.target.value + "+05:30"
      },
      () => {
        console.log(this.state.endtime);
      }
    );
  };

  SendData = e => {
    console.log("Sending Data");
    var token = localStorage.getItem("auth-token");
    var config = {
      headers: { "x-access-token": token }
    };
    var data = {
      accesskey: this.state.accesskey,
      quizname: this.state.title,
      qdata: this.state.quiz,
      answers: this.state.answers,
      starttime: this.state.starttime,
      endtime: this.state.endtime,
      coursecid: this.props.match.params.courseid
    };
    axios
      .post("http://10.0.36.104:8000/quiz/createquiz", data, config)
      .then(res => {
        console.log("Created Sccesfuly");
      })
      .catch(err => {
        console.log(err);
      });
  };
  render() {
    const { classes } = this.props;
    let num = 0;
    const data = this.state.quiz;
    const messagebox = (
      <div>
        <Button
          variant="contained"
          color="secondary"
          className={classes.button}
          onClick={()=>{
            this.handleClickOpen();
            this.SendData()
          }}
        >
          Create Quiz
        </Button>
        <Dialog
          open={this.state.open}
          TransitionComponent={Transition}
          keepMounted
          onClose={this.handleClose}
          aria-labelledby="alert-dialog-slide-title"
          aria-describedby="alert-dialog-slide-description"
        >
          <DialogTitle id="alert-dialog-slide-title">
            {"Confirmation"}
          </DialogTitle>
          <DialogContent>
            <DialogContentText id="alert-dialog-slide-description">
              The quiz with title: {this.state.title} is created, click "Ok" to continue.
            </DialogContentText>
          </DialogContent>
          <DialogActions>
            <Button onClick={this.handleClose} href='/profile' color="primary">
              Ok
            </Button>
          </DialogActions>
        </Dialog>
      </div>
    );
    const questiontext = data.map((dataElement, num) => (
      <div>
        <TextField
          id={num}
          onChange={this.handleQuestionChange}
          label={["Question", num + 1].join(" ")}
          multiline
          defaultValue={dataElement.questiontext}
          rows="2"
          placeholder="What's an orange?"
          className={classes.textField}
          margin="normal"
        />
        {dataElement.options.map((op, opNum) => (
          <div>
            <TextField
              id={opNum}
              onChange={e => {
                this.handleOptionChange(num, opNum, e);
              }}
              label={["Option", opNum + 1].join(" ")}
              defaultValue={op}
              placeholder="What's an orange?"
              className={classes.textFieldAnswer}
              margin="normal"
            />
          </div>
        ))}
        <FormControl className={classes.formControl}>
          <InputLabel htmlFor="answer">Answer</InputLabel>
          <Select
            id={num}
            name={num}
            value={dataElement.answer}
            onChange={this.handleAnswerChange}
          >
            <MenuItem value="">
              <em>None</em>
            </MenuItem>
            {dataElement.options.map((op, opNum) => (
              <MenuItem value={op} className={classes.textFieldAnswer}>
                {op}
              </MenuItem>
            ))}
            {/*
          <MenuItem value={10}>Ten</MenuItem>
          <MenuItem value={20}>Twenty</MenuItem>
          <MenuItem value={30}>Thirty</MenuItem> */}
          </Select>
        </FormControl>
        <br />
        <Button
          id={dataElement.id}
          variant="contained"
          color="secondary"
          className={classes.button}
          onClick={() => this.handleAddOption(dataElement.id)}
        >
          Add Option
        </Button>
      </div>
    ));

    {
      /*
        <li id={num}>
        {dataElement.questiontext}
        <li>{dataElement.options}</li>
        </li> */
    }
    console.log(data);
    return (
      <div
        style={{
          backgroundColor: "#e0e0e0",
          position: "absolute",
          width: "100.5%",
          marginTop: "-15px",
          marginLeft: "-15px",
          minHeight: '100%'
        }}
      >
        <TextField
          id="title"
          onChange={this.handleTitleChange}
          label="Quiz Title"
          placeholder=""
          className={classes.title}
          margin="normal"
        />
        <TextField
          id="accesskey"
          onChange={this.handleAccesskeyChange}
          label="Accesskey"
          placeholder=""
          className={classes.title}
          margin="normal"
        />
        <br />
        <TextField
          id="Start Time"
          label="Start Time"
          type="datetime-local"
          onChange={this.handleStartTimeChange}
          defaultValue={null}
          className={classes.title}
          InputLabelProps={{
            shrink: true
          }}
        />
        <TextField
          id="End Time"
          label="End Time"
          type="datetime-local"
          onChange={this.handleEndTimeChange}
          defaultValue={null}
          className={classes.title}
          InputLabelProps={{
            shrink: true
          }}
        />
        {questiontext}
        {/* {this.quiz} */}
        {/* <TextField
          id="outlined-multiline-static"
          label="Multiline"
          multiline
          rows="2"
          placeholder="What's an orange?"
          className={classes.textField}
          margin="normal"
        /> */}
        <br />
        <Button
          variant="contained"
          color="secondary"
          className={classes.button}
          onClick={this.handleAddQuestion}
          style={{
            marginBottom: '25px'
          }}
        >
          Add Question
        </Button>
        <br />
        {messagebox}
      </div>
    );
  }
}

CreateQuiz.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(CreateQuiz);
