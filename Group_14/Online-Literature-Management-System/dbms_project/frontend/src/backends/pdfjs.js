export class PDFJs {
  init = (source, element) => {
    const iframe = document.createElement('iframe');

    iframe.src = `../../public/pdfjs-mozilla/web/viewer.html?file=${source}`;
    iframe.width = '100%';
    iframe.height = '100%';

    element.appendChild(iframe);
  };
}

export default PDFJs;
