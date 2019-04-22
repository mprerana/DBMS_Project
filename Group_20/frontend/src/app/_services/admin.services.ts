import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { UserProfile } from '@/_models';

@Injectable({ providedIn: 'root' })
export class AdminService {
    constructor(private http: HttpClient) { }

    getAll() {
        return this.http.get<UserProfile[]>(`http://localhost:3000/admin/users`);
    }

    getRestaurantApplications() {
        return this.http.get(`http://localhost:3000/admin/restaurant-applications`);
    }
    getRestaurantApplicationByID(id) {
        return this.http.get(`http://localhost:3000/admin/restaurant-application/` + id);
    }
    updateUserProfile(username,options){
        return this.http.post<UserProfile>(`http://localhost:3000/user`,{username,options});
    }
    updateRestaurantApplication(email, status){
        return this.http.post(`http://localhost:3000/admin/restaurantApplication`,{email, status});
    }
}