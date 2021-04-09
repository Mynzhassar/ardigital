import {Component, OnInit} from '@angular/core';
import {ProviderService} from '../services/provider.service';
import {Consultation, Profit, Service} from '../models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})

export class MainComponent implements OnInit {

  public profits: Profit[] = [];
  public services: Service[] = [];
  public consultations: Consultation[] = [];

  public full_name: any = '';
  public telephone_number: any = '';
  public email: any = '';

  constructor(private provider: ProviderService) {
  }

  ngOnInit() {
    this.getProfits();
    this.getServices();
  }

  public getProfits() {
    this.provider.getProfits().then(res => {
      this.profits = res
    })
  }

  public getServices() {
    this.provider.getServices().then(res => {
      this.services = res
    })
  }

  public addConsultation(service_id: number) {
    this.provider.addConsultation(service_id, this.full_name, this.telephone_number, this.email).then(res => {
        this.full_name = '';
        this.telephone_number = '';
        this.email = '';
        this.consultations.push(res)
    })
  }

}
