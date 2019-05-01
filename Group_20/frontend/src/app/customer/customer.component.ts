import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { AuthenticationService } from '@/_services';

@Component({
  selector: 'app-home',
  templateUrl: './customer.component.html',
  styleUrls: ['./customer.component.css',
              './assets/css/open-iconic-bootstrap.min.css',
              "./assets/css/animate.css",
              // "./assets/css/owl.carousel.min.css",
              "./assets/css/owl.theme.default.min.css",
              "./assets/css/magnific-popup.css",
              "./assets/css/aos.css",
              "./assets/css/ionicons.min.css",
              "./assets/css/bootstrap-datepicker.css",
              "./assets/css/jquery.timepicker.css",
              "./assets/css/flaticon.css",
              "./assets/css/icomoon.css",
              "./assets/css/style.css"
]
})
export class CustomerComponent implements OnInit {

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
  public loadScript(url: string) {
    const body = <HTMLDivElement> document.body;
    const script = document.createElement('script');
    script.innerHTML = '';
    script.src = url;
    script.type = 'text/javascript';
    script.async = false;
    script.defer = true;
    body.appendChild(script);
  }
}
