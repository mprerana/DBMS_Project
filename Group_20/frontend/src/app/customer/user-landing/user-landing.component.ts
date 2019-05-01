import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

import { UserService,AuthenticationService } from '@/_services';

import { RestaurantProfile } from '@/_models';

@Component({
  selector: 'app-landing',
  templateUrl: './user-landing.component.html',
  styleUrls: ['./user-landing.component.css',
              '../assets/css/open-iconic-bootstrap.min.css',
              "../assets/css/animate.css",
              // "./assets/css/owl.carousel.min.css",
              "../assets/css/owl.theme.default.min.css",
              "../assets/css/magnific-popup.css",
              "../assets/css/aos.css",
              "../assets/css/ionicons.min.css",
              "../assets/css/bootstrap-datepicker.css",
              "../assets/css/jquery.timepicker.css",
              "../assets/css/flaticon.css",
              "../assets/css/icomoon.css",
              "../assets/css/style.css"
]
})
export class UserLandingComponent implements OnInit {

  returnUrl: string;
  error = '';
  restaurants;
  slide1;
  slide2;
  slide3;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private userService: UserService,
    private authenticationService: AuthenticationService,
  ) { }

  ngOnInit() {
    this.getRestaurants();
    this.slide1 = setTimeout(this.slideshow1,3000)
    this.slide2 = setTimeout(this.slideshow2,6000)
    this.slide3 = setTimeout(this.slideshow3,9000)
  }
  ngOnDestroy() {
    clearTimeout(this.slide1)
    clearTimeout(this.slide2)
    clearTimeout(this.slide3)
  }

  getRestaurants(): void {
    this.userService.getRestaurantProfiles()
      .subscribe(restaurants => {
        this.restaurants = restaurants
        this.restaurants = this.restaurants.slice(0,3)
      });
  }
  slideshow1(){
    document.getElementById('slide1').style.display = 'none';
    document.getElementById('slide1').style.opacity = '0';
    document.getElementById('slide1').style.visibility = 'hidden';
    document.getElementById('slide2').style.display = 'block';
    document.getElementById('slide2').style.visibility = 'visible';
    document.getElementById('slide2').style.opacity = '1';
  }
  slideshow2(){
    document.getElementById('slide2').style.display = 'none';
    document.getElementById('slide2').style.opacity = '0';
    document.getElementById('slide2').style.visibility = 'hidden';
    document.getElementById('slide3').style.display = 'block';
    document.getElementById('slide3').style.visibility = 'visible';
    document.getElementById('slide3').style.opacity = '1';
  }
  slideshow3(){
    document.getElementById('slide3').style.display = 'none';
    document.getElementById('slide3').style.opacity = '0';
    document.getElementById('slide3').style.visibility = 'hidden';
    document.getElementById('slide1').style.display = 'block';
    document.getElementById('slide1').style.visibility = 'visible';
    document.getElementById('slide1').style.opacity = '1';
  }
  
  logout() {
    this.authenticationService.logout();
    this.router.navigate(['/login']);
  }
}
