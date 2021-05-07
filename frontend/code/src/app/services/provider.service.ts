import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import type {Advertisement, Application, Consultation, Profit, Service, Site} from '../models/models';
import {Observable} from "rxjs";
import {environment} from "../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class ProviderService {
  apiUrl = environment.apiUrl + '/api';

  constructor(private http: HttpClient) {
  }

  public getProfits(): Observable<Profit[]> {
    return this.http.get<Profit[]>(`${this.apiUrl}/profits`);
  }

  public getServices(): Observable<Service[]> {
    return this.http.get<Service[]>(`${this.apiUrl}/services`);
  }

  public addConsultation(serviceId: number, fullName: any, telephoneNumber: any, email: any): Observable<Consultation> {
    return this.http.post<Consultation>(`${this.apiUrl}/${serviceId}/add_consultation`, {
      fullName: fullName,
      telephoneNumber: telephoneNumber,
      email: email,
    });
  }

  public getSites(): Observable<Site[]> {
    return this.http.get<Site[]>(`${this.apiUrl}/sites`, {});
  }

  public getAdvertisements(): Observable<Advertisement[]> {
    return this.http.get<Advertisement[]>(`${this.apiUrl}/advertisements`, {});
  }

  public addApplication(fullName: any, telephoneNumber: any, email: any): Observable<Application> {
    return this.http.post<Application>(`${this.apiUrl}/add_application`, {
      full_name: fullName,
      telephone_number: telephoneNumber,
      email: email,
    });
  }
}
