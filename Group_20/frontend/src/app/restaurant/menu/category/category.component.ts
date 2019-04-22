import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';


import { AuthenticationService } from '@/_services';
import * as customValidators from '@/custom-validators';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css',
  '../../../admin/assets/css/bootstrap.min.css',
  '../../../admin/assets/css/now-ui-dashboard.css?v=1.3.0',
  '../../../admin/assets/demo/demo.css',                
]
})
export class CategoryComponent implements OnInit {
addCategoryForm: FormGroup;
  loading = false;
  submitted = false;
  returnUrl: string;
  error = '';

  constructor(
      private formBuilder: FormBuilder,
      private route: ActivatedRoute,
      private router: Router,
      private authenticationService: AuthenticationService,
      private http: HttpClient
  ) { 
  }

  ngOnInit() {
      this.addCategoryForm = this.formBuilder.group({
          name: ['', [Validators.required,customValidators.nameValidator()]],
      });
      
      // get return url from route parameters or default to '/'
      this.returnUrl = '/restaurant/menu';
  }

  // convenience getter for easy access to form fields
  get f() { return this.addCategoryForm.controls; }

  onSubmit() {
      this.submitted = true;
      if (this.addCategoryForm.invalid) {
          return;
      }
      var catName = this.f.name.value;
      this.http.post(`http://localhost:3000/restaurant/addCategory`, {catName})
      .pipe(first())
          .subscribe(
              data => {
                  if (data){
                    this.router.navigate([this.returnUrl]);
                    return;
                  } else { 
                    this.f.name.setErrors({'nametakenValidator': true})
                    return;
                  }
              },
              error => {
                  this.error = error;
                  this.loading = false;
                  return;
              }
          );
  }

}
