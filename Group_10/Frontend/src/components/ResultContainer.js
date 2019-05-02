import React from "react";
import Typography from "@material-ui/core/Typography";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";

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

class ResultContainer extends React.Component {
  getPercentile(markslist, current_mark) {
    var lessThanCurrent = 0;
    for (var mark in markslist) {
      if (current_mark > mark) lessThanCurrent += 1;
    }
    return (lessThanCurrent / markslist.length) * 100;
  }
  render() {
    const { classes } = this.props;
    return (
      <span
        style={{
          marginTop: "15px",
          marginBottom: "15px",
          marginLeft: "15px",
          marginRight: "15px",
          textAlign: "center"
        }}
      >
        <span style={{ display: "inline-block", marginBottom: "30px" }}>
          <Card className={classes.card}>
            <CardContent>
              <Typography
                className={classes.title}
                color="textSecondary"
                gutterBottom
              >
                Username: {this.props.data.username}
              </Typography>
              <Typography
                className={classes.title}
                color="textSecondary"
                gutterBottom
              >
                Email: {this.props.data.email}
              </Typography>
              <Typography className={classes.pos} color="textSecondary">
                {this.props.data.name}
              </Typography>
              <Typography className={classes.pos} color="textSecondary">
                Marks: {this.props.data.marks ? this.props.data.marks : 0}
              </Typography>
              <Typography className={classes.pos} color="textSecondary">
                Response: {this.props.data.response}
              </Typography>
              <Typography className={classes.pos} color="textSecondary">
                Percentile:{" "}
                {this.getPercentile(
                  this.props.markslist,
                  this.props.data.marks
                )}
              </Typography>
            </CardContent>
          </Card>
        </span>
        {/* Username : {this.props.data.username} <br />
        Marks: {this.props.data.marks ? this.props.data.marks : 0}
        <br /> */}
        <br />
      </span>
    );
  }
}

ResultContainer.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(ResultContainer);
