import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { AuthenticationService } from '@/_services';

@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.css']
})
export class LandingComponent implements OnInit {
  constructor(
  private router: Router,
  private authenticationService: AuthenticationService
  ) { 
    var user = this.authenticationService.currentUserValue
    if (user) { 
      if(user.role === '1') this.router.navigate(['/home']);
      if(user.role === '2') this.router.navigate(['/admin']);
      if(user.role === '3') this.router.navigate(['/restaurant']);
    }
  }

  ngOnInit() {
  }

}
