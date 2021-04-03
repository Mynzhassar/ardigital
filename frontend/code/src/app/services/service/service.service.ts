import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Service} from "../../models/models";


@Injectable({
  providedIn: 'root'
})
export class ServiceService {
  API_URL = 'http://localhost:80/api'

  constructor(private http: HttpClient) {
  }

  public getServices(): Observable<Service[]> {
    return this.http.get<Service[]>(`${this.API_URL}/services`)
  }
}
