import React from "react";
import ReactDOM from "react-dom";

import Signup from "./components/Signup";
import Navbar from "./components/Navbar";
import Drawer from "./components/Drawer";
import InputField from "./components/InputField";
import LandingPage from "./components/LandingPage";
import LoginPage from "./components/LoginPage";
import QuizPage from "./components/QuizPage";
import CreateQuiz from './components/CreateQuiz';
import QuizResults from './components/QuizResults';
import CourseResults from './components/CourseResults';
import Profile from './components/Profile';
import CoursePage from './components/CoursePage';
import CreateCourse from './components/CreateCourse';
import JoinCourse from './components/JoinCourse';
import ViewQuiz from './components/ViewQuiz';
import StartQuiz from './components/StartQuiz';
import PdfUpload from './components/PdfUpload';
import "./styles.css";
import Helmet from "react-helmet";
import { BrowserRouter, Route } from "react-router-dom";
import "./components/LandingPage.css";
class App extends React.Component {
  componentDidMount() {
    const root = document.getElementById("root");
    root.classList.add("bg");
  }
  //10.0.36.104
  render() {
    return (
      <div className="App">
        <Helmet bodyAttributes={{ style: "background-color : #fff" }} />
        <BrowserRouter>
          <div className="Navbar">
            <Navbar />
          </div>
          <Route exact path="/" component={LandingPage} />
          <Route exact path="/login" component={LoginPage} />
          <Route exact path="/quiz/:quizid" component={QuizPage} />
          <Route exact path="/createquiz/:courseid" component={CreateQuiz} />
          <Route path="/quizresults/:quizid" component={QuizResults} />
          <Route exact path="/profile/" component={Profile} />
          <Route path="/courses/:cid" component={CoursePage} />
          <Route exact path="/createcourse" component={CreateCourse} />
          <Route path="/viewquiz/:quizid" component={ViewQuiz} />
          <Route path="/startquiz/:quizid" component={StartQuiz} />
          <Route path="/courseresults/:courseid" component={CourseResults} />
          <Route path="/pdfupload/:courseid" component={PdfUpload} />

          {/* <LandingPage /> */}
        </BrowserRouter>

        {/* <Drawer /> */}
        {/* <Signup /> */}

        {/* <InputField /> */}
      </div>
    );
  }
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
