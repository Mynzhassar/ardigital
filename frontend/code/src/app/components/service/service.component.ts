import {Component, OnInit} from '@angular/core';
import {Observable} from 'rxjs';

import {ServiceService} from '../../services/service/service.service';
import {Service} from '../../models/models';

@Component({
  selector: 'app-service',
  templateUrl: './service.component.html',
  styleUrls: ['./service.component.css']
})

export class ServiceComponent implements OnInit {
  services$ !: Observable<Service[]>;

  constructor(private serviceService: ServiceService) {
  }

  ngOnInit() {
    this.getServices();
  }

  public getServices() {
    this.services$ = this.serviceService.getServices();
  }

}
