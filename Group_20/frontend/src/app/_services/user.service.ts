import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';

import { UserProfile } from '@/_models';

import { RestaurantProfile } from '@/_models';
import { MenuItems } from '@/_models';
import { OrderItems, Order } from '@/_models';

@Injectable({ providedIn: 'root' })
export class UserService {
    constructor(private http: HttpClient) { }

    getAll() {
        return this.http.get<UserProfile[]>(`http://localhost:3000/admin/users`);
    }

    getUserProfile() {
        return this.http.get<UserProfile>(`http://localhost:3000/user`);
    }
    updateUserProfile(username,options){
        return this.http.post<UserProfile>(`http://localhost:3000/user`,{username,options});
    }

    getRestaurantProfiles() {
        return this.http.get<RestaurantProfile>(`http://localhost:3000/user/landing`);
    }

    getRestaurantItems(id) {
        //let params = new HttpParams().set("id", id); //Create new HttpParams
        return this.http.get<MenuItems>(`http://localhost:3000/user/restaurant/${id}`,);
    }

    addOrderItems(orderid, itemid, quantity) {
        return this.http.post<OrderItems>(`http://localhost:3000/user/order`, {orderid, itemid, quantity});
    }

    createOrder(orderid, username, restname, lat, lon, deliveryname) {
        return this.http.post<Order>(`http://localhost:3000/user/createorder`, {orderid, username, restname, lat, lon, deliveryname});
    }

    getLastOrder() {
        return this.http.get<Order>(`http://localhost:3000/user/lastorder`);
    }
}