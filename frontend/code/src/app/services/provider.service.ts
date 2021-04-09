import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {MainService} from "./main.service";
import {Advertisement, Application, Consultation, Profit, Service, Site} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService{
  API_URL = 'http://localhost:80/api'

  constructor(http: HttpClient) {
    super(http)
  }

  public getProfits(): Promise<Profit[]> {
    return this.get(`${this.API_URL}/profits`, {})
  }

  public getServices(): Promise<Service[]> {
    return this.get(`${this.API_URL}/services`, {})
  }

  public addConsultation(service_id: number, full_name: any, telephone_number: any, email: any): Promise<Consultation> {
    return this.post(`${this.API_URL}/${service_id}/add_consultation`, {
      full_name: full_name,
      telephone_number: telephone_number,
      email: email,
    })
  }

  public getSites(): Promise<Site[]> {
    return this.get(`${this.API_URL}/sites`, {})
  }

  public getAdvertisements(): Promise<Advertisement[]> {
    return this.get(`${this.API_URL}/advertisements`, {})
  }

  public addApplication(full_name: any, telephone_number: any, email: any): Promise<Application> {
    return this.post(`${this.API_URL}/add_application`, {
      full_name: full_name,
      telephone_number: telephone_number,
      email: email,
    })
  }
}
