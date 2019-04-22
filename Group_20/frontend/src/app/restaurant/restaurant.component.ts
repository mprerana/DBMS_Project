import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { AuthenticationService } from '@/_services';

@Component({
  selector: 'app-restaurant',
  templateUrl: './restaurant.component.html',
  styleUrls: ['./restaurant.component.css',
              '../admin/assets/css/bootstrap.min.css',
              '../admin/assets/css/now-ui-dashboard.css?v=1.3.0',
              '../admin/assets/demo/demo.css',
  ],
})
export class RestaurantComponent implements OnInit {

  constructor(
    private router: Router,
    private authenticationService: AuthenticationService
  ) { }

  ngOnInit() {
  }
  logout() {
    this.authenticationService.logout();
    this.router.navigate(['/login']);
  }

}