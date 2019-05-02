import React from "react";
import axios from "axios";
import { FilePond } from "react-filepond";
import "filepond/dist/filepond.min.css";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogContentText from "@material-ui/core/DialogContentText";
import DialogTitle from "@material-ui/core/DialogTitle";
import Slide from "@material-ui/core/Slide";
function Transition(props) {
  return <Slide direction="up" {...props} />;
}
class PdfUpload extends React.Component {
  state = {
    open:false,
    files: [
      {
        source: "index.html",
        options: {
          type: "local"
        }
      }
    ]
  };
  handleUploadFile = event => {
    var token = localStorage.getItem("auth-token");
    var config = {
      headers: { "x-access-token": token }
    };
    console.log(event.target.files[0]);
    const data = new FormData();
    data.append("document", event.target.files[0]);
    axios.post("http://10.0.36.104:8000/quiz/pdfupload", data, {}).then(res => {
      res.data.coursecid = this.props.match.params.courseid;
      axios
        .post("http://10.0.36.104:8000/quiz/createquiz", res.data, config)
        .then(res => {
          console.log("Quiz Created");
          this.setState({open:true})
        });
    });
  };

  handleInit() {
    console.log("FilePond instance has initialised", this.pond);
  }

  render() {
    var messagebox = (
      <Dialog
        open={this.state.open}
        TransitionComponent={Transition}
        keepMounted
        onClose={this.handleClose}
        aria-labelledby="alert-dialog-slide-title"
        aria-describedby="alert-dialog-slide-description"
      >
        <DialogTitle id="alert-dialog-slide-title">{"Success"}</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-slide-description">
            Quiz has been created
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={this.handleClose} href="/profile" color="primary">
            OK
          </Button>
        </DialogActions>
      </Dialog>
    )
    return (
      <div
        style={{
          backgroundColor: "#e0e0e0",
          position: "absolute",
          top: 0,
          width: "102%",
          minHeight: "100%",
          marginLeft: "-20px"
        }}
      >
        <Typography
          component="h2"
          variant="display2"
          gutterBottom
          style={{
            paddingTop: "8%",
            paddingBottom: "3%"
          }}
        >
          PDF File Upload
        </Typography>
        <Typography
          component="h2"
          variant="display1"
          gutterBottom
          style={{
            paddingBottom: "3%",
            fontSize: "20px",
            fontWeight: "normal"
          }}
        >
        Upload a pdf file to automatically generate a quiz!
        </Typography>
        <Button variant="contained" color="primary" component="label" style={{
          backgroundColor: '#212121',
          color: '#fff'
        }}>
          Upload File
          <input
            type="file"
            onChange={this.handleUploadFile}
            style={{ display: "none" }}
          />
        </Button>
        {/* <input type="file"  /> */}
        {messagebox}
      </div>
    );
  }
}

export default PdfUpload;
