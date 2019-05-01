import React from "react";
import { enquireScreen } from "enquire-js";
// import Header from "../component/Header/Header";
import Header from "../../components/Header/Header";

// import Header from "../../components/Header/Header";
let isMobile = false;
enquireScreen(b => {
  isMobile = b;
});

class Home extends React.PureComponent {
  state = {
    isFirstScreen: true,
    isMobile
  };

  componentDidMount() {
    enquireScreen(b => {
      this.setState({
        isMobile: !!b
      });
    });
  }

  onEnterChange = mode => {
    this.setState({
      isFirstScreen: mode === "enter"
    });
  };
  render() {
    return [
      <Header isMobile={this.state.isMobile} />

      // <Banner key="banner" onEnterChange={this.onEnterChange} />,
      // <Page1 key="page1" isMobile={this.state.isMobile} />,
      // <Page2 key="page2" />,
      // <Page3 key="page3" isMobile={this.state.isMobile} />,
      // <Page4 key="page4" />,
      // <Footer key="footer" />,
      // <DocumentTitle title="Ant Design - 一个 UI 设计语言" key="title" />
    ];
  }
}
export default Home;
