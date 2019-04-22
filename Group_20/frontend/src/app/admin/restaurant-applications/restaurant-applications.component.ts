import { Component, OnInit } from '@angular/core';
import { first } from 'rxjs/operators';
import { Router } from '@angular/router';


import { AdminService,AuthenticationService } from '@/_services';
import { defineBase } from '@angular/core/src/render3';

@Component({
  selector: 'app-restaurant-applications',
  templateUrl: './restaurant-applications.component.html',
  styleUrls: ['../assets/css/bootstrap.min.css',
              '../assets/css/now-ui-dashboard.css?v=1.3.0',
              '../assets/demo/demo.css',
              './restaurant-applications.component.css',
            ],
})
export class RestaurantApplicationsComponent implements OnInit {
  restaurants: any;
  constructor(
    private adminService: AdminService,
    private router: Router,
    private authenticationService: AuthenticationService
  ) {
   }

  ngOnInit() {
    this.adminService.getRestaurantApplications().pipe(first()).subscribe(restaurants => {
      this.restaurants = restaurants;
    })

  }
  verifyAppl(email){
    this.adminService.updateRestaurantApplication(email, 'A').pipe(first()).subscribe(done => {
    });
    this.adminService.getRestaurantApplications().pipe(first()).subscribe(restaurants => {
      this.restaurants = restaurants;
    })
  }
  rejectAppl(email){
    this.adminService.updateRestaurantApplication(email, 'R').pipe(first()).subscribe(done => {
    });
    this.adminService.getRestaurantApplications().pipe(first()).subscribe(restaurants => {
      this.restaurants = restaurants;
    })
  }
  logout() {
    this.authenticationService.logout();
    this.router.navigate(['/login']);
    
  }

}
