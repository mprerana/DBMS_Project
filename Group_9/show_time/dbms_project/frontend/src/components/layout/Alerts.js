import React, { Component, Fragment } from "react";
import { withAlert } from "react-alert";
import { connect } from "react-redux";
import PropTypes from "prop-types";

export class Alerts extends Component {
  static propTypes = {
    error: PropTypes.object.isRequired,
    message: PropTypes.object.isRequired
  };
  componentDidUpdate(prevProps) {
    const { error, alert, message } = this.props;
    if (error !== prevProps.error) {
      if (error.msg.msg.username) {
        alert.error(`Username:${error.msg.msg.username}`);
      }
      if (error.msg.msg.password) {
        alert.error(`Password:${error.msg.msg.password}`);
      }
      if (error.msg.msg.non_field_errors) {
        //const JSONerror = JSON.stringify(error.msg);
        console.log(error.msg.msg.non_field_errors);
        alert.error(`Error:${error.msg.msg.non_field_errors}`);
      }
    }
    if (message !== prevProps.message) {
      // if (message.movieLoad) {
      //   alert.success(message.movieLoad);
      // }

      if (message.passwordNotMatch) {
        alert.error(message.passwordNotMatch);
      }
      if (message.dobEmpty) {
        alert.error(message.dobEmpty);
      }
      if (message.cityEmpty) {
        alert.error(message.cityEmpty);
      }
      if (message.phoneEmpty) {
        alert.error(message.phoneEmpty);
      }
      if (message.notloggedin) {
        alert.info(message.notloggedin);
      }
      if (message.alreadyReviewed) {
        alert.info(message.alreadyReviewed);
      } else if (message.movieReview) {
        alert.info(message.movieReview);
      }
      if (message.noseatselected) {
        alert.error(message.noseatselected);
      }
    }
  }

  //   componentDidMount() {
  //     this.props.alert.show("it works");
  //   }

  render() {
    return <Fragment />;
  }
}

const mapStateToProps = state => ({
  error: state.errors,
  message: state.messages
});

export default connect(mapStateToProps)(withAlert()(Alerts));
