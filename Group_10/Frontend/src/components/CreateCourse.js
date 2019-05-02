import React from "react";
import axios from "axios";
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Snackbar from '@material-ui/core/Snackbar';
import IconButton from '@material-ui/core/IconButton';
import CloseIcon from '@material-ui/icons/Close';
import { visitLexicalEnvironment } from "typescript";

const styles = theme => ({
  close: {
    padding: theme.spacing.unit / 2,
  },
});


class CreateCourse extends React.Component{
  state={
    status_box_text:"",
    open: false,
    snackbarOpen: false
  }
  
  handleSnackbarClick = () => {
    this.setState({ snackbarOpen: true });
  };

  handleSnackbarClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }

    this.setState({ snackbarOpen: false });
  };

  handleChange =(e)=> {
    this.setState({
      status_box_text: e.target.value
    })
  }

  sendData = (event)=>{
    var token = localStorage.getItem("auth-token");
    var config = {
      headers:{'x-access-token':token}
    }
    var data ={
      cname:this.refs.cname.value
    }
    this.setState({
      snackbarOpen: true
    })
    axios.post("http://10.0.36.104:8000/course/createcourse",data,config).then(res=>{
      const status_box_text = "Course has been created JoinKey : " + res.data.joinKey
      this.setState({status_box_text, snackbarOpen: true})
    })
  }

  handleClickOpen = () => {
    this.setState({ open: true });
  };

  handleClose = () => {
    this.setState({ open: false });
  };


  render(){
    const { classes } = this.props;

    const status = (<Snackbar
      anchorOrigin={{
        vertical: 'bottom',
        horizontal: 'left',
      }}
      open={this.state.snackbarOpen}
      autoHideDuration={60000}
      onClose={this.handleSnackbarClose}
      ContentProps={{
        'aria-describedby': 'message-id',
      }}
      message={<span id='message-id'>{this.state.status_box_text}</span>}
      action={[
        <IconButton
          key="close"
          aria-label="Close"
          color="inherit"
          className={classes.close}
          onClick={this.handleSnackbarClose}
        >
          <CloseIcon />
        </IconButton>,
      ]}
    />)

    return(
      <div>
        <Button variant="contained" color="primary" onClick={this.handleClickOpen}>
          Create Course
        </Button>
        <Dialog
          open={this.state.open}
          onClose={this.handleClose}
          aria-labelledby="form-dialog-title"
        >
          <DialogTitle id="form-dialog-title">Create Course</DialogTitle>
          <DialogContent>
            <DialogContentText>
              Enter course name below to create course
            </DialogContentText>
            <TextField
              autoFocus
              margin="dense"
              id='cname'
              ref= 'cname'
              label="Course Name"
              type="text"
              fullWidth
              onChange={this.handleChange}
            />
          </DialogContent>
          <DialogActions>
            <Button onClick={this.handleClose} color="primary">
              Cancel
            </Button>
            <Button onClick={(event)=>{
              this.sendData(event)
              this.handleClose()
              }} color="primary">
              Create Course
            </Button>
          </DialogActions>
        </Dialog>
        {status}
      {/* <h1>Create Course</h1>
      <p>Please Enter Name of New Course</p>
      <input ref="cname" type="text"  />
      <button onClick={this.sendData} >Create Course</button>
      <p>{this.state.status_box_text}</p> */}
      </div>
    )
  }
}


CreateCourse.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(CreateCourse);