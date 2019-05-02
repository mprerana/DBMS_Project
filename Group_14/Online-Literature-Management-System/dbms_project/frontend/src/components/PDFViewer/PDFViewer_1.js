import React, { Component } from 'react'

export class PDFViewer_1 extends Component {
  render() {

    const {bookLink} = this.props.match.params;
    return (
      <div>
        <iframe src={bookLink} width='100%' height='100%'/>
      </div>
    )
  }
}

export default PDFViewer_1
