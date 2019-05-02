const backdrop = document.querySelector('.backdrop');
const sideDrawer = document.querySelector('.mobile-nav');
const menuToggle = document.querySelector('#side-menu-toggle');

function backdropClickHandler() {
  backdrop.style.display = 'none';
  sideDrawer.classList.remove('open');
}

function menuToggleClickHandler() {
  backdrop.style.display = 'block';
  sideDrawer.classList.add('open');
}

backdrop.addEventListener('click', backdropClickHandler);
menuToggle.addEventListener('click', menuToggleClickHandler);

// document.querySelectorAll('.rateStar').addEventListener('click',() => console.log('hi') )

const starList = document.querySelectorAll('.rateStar');
for (let i = 0; i < starList.length; i++) {
    starList[i].addEventListener('click', (e) => console.log(starList[i].getAttribute('data-value')));

    starList[i].addEventListener('mouseover', (e) => {
        for (let j = 0; j < parseInt(starList[i].getAttribute('data-value')); j++) {
            starList[j].className = "fas fas-custom fa-star rateStar"
        }
    });

    starList[i].addEventListener('mouseout', (e) => {
      for (let j = 0; j < starList.length; j++) {
        starList[j].className = "far fas-custom fa-star rateStar"
      }
   })
}