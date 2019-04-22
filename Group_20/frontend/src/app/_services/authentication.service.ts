import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { User } from '@/_models';

@Injectable({ providedIn: 'root' })
export class AuthenticationService {
    private currentUserSubject: BehaviorSubject<User>;
    public currentUser: Observable<User>;

    constructor(private http: HttpClient) {
        this.currentUserSubject = new BehaviorSubject<User>(JSON.parse(localStorage.getItem('currentUser')));
        this.currentUser = this.currentUserSubject.asObservable();
    }

    public get currentUserValue(): User {
        return this.currentUserSubject.value;
    }

    login(username: string, password: string) {
        return this.http.post<any>(`http://localhost:3000/api/signin`, { username, password })
            .pipe(map(user => {
                // login successful if there's a jwt token in the response
                if (user && user.token) {
                    // store user details and jwt token in local storage to keep user logged in between page refreshes
                    localStorage.setItem('currentUser', JSON.stringify(user));
                    this.currentUserSubject.next(user);
                }

                return user;
            }));
    }

    verify(token: string) {
        return this.http.post<any>(`http://localhost:3000/api/confirm`, { token })
            .pipe(map(user => {
                // login successful if there's a jwt token in the response
                if (user && user.token) {
                    // store user details and jwt token in local storage to keep user logged in between page refreshes
                    localStorage.setItem('currentUser', JSON.stringify(user));
                    this.currentUserSubject.next(user);
                }

                return user;
            }));
    }

    iforgot(email: string) {
        return this.http.post<any>(`http://localhost:3000/api/iforgot`, { email })
        .pipe();
    }

    logout() {
        // remove user from local storage to log user out
        localStorage.removeItem('currentUser');
        this.currentUserSubject.next(null);
    }

    register(username: string, email: string, password: string) {
        return this.http.post<any>(`http://localhost:3000/api/signup`, { username, email, password })
            .pipe();
    }
    restaurantRegister(name: string, email: string, lon: string, lat:string, address, zipcode, phone, openingHrs, closingHrs, logo) {
        return this.http.post<any>(`http://localhost:3000/api/restaurant/signup`, { name, email, lon, lat, address, zipcode, phone, openingHrs, closingHrs, logo })
            .pipe();
    }
}