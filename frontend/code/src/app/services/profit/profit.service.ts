import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Profit} from '../../models/models';


@Injectable({
  providedIn: 'root'
})
export class ProfitService {
  API_URL = 'http://localhost:80/api'

  constructor(private http: HttpClient) {
  }

  public getProfits(): Observable<Profit[]> {
    return this.http.get<Profit[]>(`${this.API_URL}/profits`)
  }
}
