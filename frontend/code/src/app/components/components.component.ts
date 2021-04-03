import {Component, OnInit} from '@angular/core';
import {Observable} from 'rxjs';

import {ServicesService} from '../services.service';
import {Profit} from '../models';

@Component({
  selector: 'app-components',
  templateUrl: './components.component.html',
  styleUrls: ['./components.component.css']
})

export class ComponentsComponent implements OnInit {
  profits$ !: Observable<Profit[]>;

  constructor(private serviceService: ServicesService) { }

  ngOnInit() {
    this.getProfits();
  }

  public getProfits() {
    this.profits$ = this.serviceService.getProfits();
  }

}
