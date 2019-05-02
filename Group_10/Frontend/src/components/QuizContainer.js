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
import StartQuiz from './StartQuiz';

const styles = theme => ({
  card: {
    minWidth: 275,
    display: "inline-block",
    backgroundColor: "#82b1ff"
  },
  bullet: {
    display: "inline-block",
    margin: "0 2px",
    transform: "scale(0.8)"
  },
  title: {
    fontSize: 14
  },
  pos: {
    marginBottom: 12
  }
});

class QuizContainer extends React.Component {
  render() {
    const { classes } = this.props;
    return (
      <span
        style={{
          paddingTop: "15px",
          paddingBottom: "15px",
          paddingLeft: "15px",
          paddingRight: "15px",
          textAlign: "center"
        }}
      >
        <span style={{ display: "inline-block", paddingBottom: "30px" }}>
          <Card className={classes.card}>
            <CardContent>
              <Typography
                className={classes.title}
                color="textSecondary"
                gutterBottom
              />
              <Typography variant="h5" component="h2">
                {this.props.data.quizname}
              </Typography>
              <Typography className={classes.pos} color="textSecondary">
                {this.props.data.name}
              </Typography>
              <Typography
                className={classes.title}
                color="textSecondary"
                gutterBottom
              >
                Start Time:{this.props.data.starttime}
              </Typography>
              <Typography
                className={classes.title}
                color="textSecondary"
                gutterBottom
              >
                End time:
                {this.props.data.endtime}{" "}
              </Typography>
            </CardContent>
            <CardActions>
              <Button
                size="small"
                href={"/quizresults/" + this.props.data.quizid}
              >
                View Results
              </Button>
            </CardActions>
          </Card>
        </span>
      </span>
    );
  }
}

QuizContainer.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(QuizContainer);
