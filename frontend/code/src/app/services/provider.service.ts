import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Profit, Service} from '../models/models';


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
}
