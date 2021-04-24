import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import type {Advertisement, Application, Consultation, Profit, Service, Site} from '../models/models';
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class ProviderService {
  API_URL = 'http://localhost:80/api'

  constructor(private http: HttpClient) {
  }

  public getProfits(): Observable<Profit[]> {
    return this.http.get<Profit[]>(`${this.API_URL}/profits`)
  }

  public getServices(): Observable<Service[]> {
    return this.http.get<Service[]>(`${this.API_URL}/services`)
  }

  public addConsultation(service_id: number, full_name: any, telephone_number: any, email: any): Observable<Consultation> {
    return this.http.post<Consultation>(`${this.API_URL}/${service_id}/add_consultation`, {
      full_name: full_name,
      telephone_number: telephone_number,
      email: email,
    })
  }

  public getSites(): Observable<Site[]> {
    return this.http.get<Site[]>(`${this.API_URL}/sites`, {})
  }

  public getAdvertisements(): Observable<Advertisement[]> {
    return this.http.get<Advertisement[]>(`${this.API_URL}/advertisements`, {})
  }

  public addApplication(full_name: any, telephone_number: any, email: any): Observable<Application> {
    return this.http.post<Application>(`${this.API_URL}/add_application`, {
      full_name: full_name,
      telephone_number: telephone_number,
      email: email,
    })
  }
}
