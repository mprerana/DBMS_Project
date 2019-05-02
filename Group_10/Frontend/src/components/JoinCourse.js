import React from "react"
import axios from "axios"
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


const styles = theme => ({
  close: {
    padding: theme.spacing.unit / 2,
  },
});

class JoinCourse extends React.Component{
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

  sendData = (event)=>{
    var token = localStorage.getItem("auth-token");
    var config = {
      headers:{'x-access-token':token}
    }
    var data ={
      joinKey:this.refs.joinKey.value
    }
    axios.post("http://10.0.36.104:8000/course/joincourse",data,config).then(res=>{
      const status_box_text = "Course has been added"
      console.log(res)
      this.setState({status_box_text,
      snackbarOpen: true})
    }).catch(err=>{
      const status_box_text = "Invalid Joinkey"
      console.log(err)
      this.setState({status_box_text,
      snackbarOpen: true})
    })
  }

  handleClickOpen = () => {
    this.setState({ open: true });
  };

  handleClose = () => {
    this.setState({ open: false });
  };


  render() {

    const { classes } = this.props;

    const status = (<Snackbar
      anchorOrigin={{
        vertical: 'bottom',
        horizontal: 'left',
      }}
      open={this.state.snackbarOpen}
      autoHideDuration={6000}
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

    return (
      <div>
        <Button variant="contained" color="secondary" onClick={this.handleClickOpen}>
          Join a course
        </Button>
        <Dialog
          open={this.state.open}
          onClose={this.handleClose}
          aria-labelledby="form-dialog-title"
        >
          <DialogTitle id="form-dialog-title">Join Course</DialogTitle>
          <DialogContent>
            <DialogContentText>
              To join a course enter its key below.
            </DialogContentText>
            <TextField
              autoFocus
              margin="dense"
              id='joinkey'
              ref= 'joinKey'
              label="Join Key"
              type="text"
              fullWidth
            />
          </DialogContent>
          <DialogActions>
            <Button onClick={this.handleClose} color="primary">
              Cancel
            </Button>
            <Button onClick={()=>{
              this.sendData()
              this.handleClose()
              }} color="primary">
              Join
            </Button>
          </DialogActions>
        </Dialog>
        {status}
      </div>
    );
  }

  /* render(){
    return(
      <div>
      <h1>Join Course</h1>
      <p>Please Enter JoinKey of New Course</p>
      <input ref="joinKey" type="text"  />
      <button onClick={this.sendData} >Join Course</button>
      <p>{this.state.status_box_text}</p>
      </div>
    )
  } */
}

JoinCourse.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(JoinCourse);
