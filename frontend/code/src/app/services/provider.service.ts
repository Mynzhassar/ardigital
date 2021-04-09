import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {MainService} from "./main.service";
import {Profit, Service} from '../models/models';

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
}
