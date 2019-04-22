import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';


import { AuthenticationService } from '@/_services';
import * as customValidators from '@/custom-validators';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
    registerForm: FormGroup;
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
        this.registerForm = this.formBuilder.group({
            username: ['', [Validators.required,customValidators.usernameValidator()]],
            email: ['',[Validators.required,customValidators.emailValidator()]],
            password1: ['', [Validators.required,customValidators.passwordValidator()]],
            password2: ['', customValidators.matchOtherValidator('password1')],
        });
        
        // get return url from route parameters or default to '/'
        this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/home';
    }

    // convenience getter for easy access to form fields
    get f() { return this.registerForm.controls; }

    onSubmit() {
        this.submitted = true;
        var username = this.f.username.value;
        var email = this.f.email.value;
        if (this.registerForm.invalid) {
            return;
        }
        this.http.post(`http://localhost:3000/api/username`, {username})
        .pipe(first())
            .subscribe(
                data => {
                    if (data){
                        this.http.post(`http://localhost:3000/api/email`, {email})
                        .pipe(first())
                        .subscribe(
                            data2 => {
                                if (data2){
                                    this.loading = true;
                                    this.authenticationService.register(this.f.username.value, this.f.email.value, this.f.password1.value)
                                    .pipe(first())
                                    .subscribe(
                                        data => {
                                            this.router.navigate([this.returnUrl]);
                                        },
                                        error => {
                                            this.error = error;
                                            this.loading = false;
                                        });
                                } else {
                                    this.f.email.setErrors({'emailtakenValidator': true})
                                    return;
                                }
                            }
                        )

                    } else {
                        this.f.username.setErrors({'usernametakenValidator': true})
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
