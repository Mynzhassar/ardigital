import {Component, OnInit} from '@angular/core';
import {ProviderService} from '../services/provider.service';
import {Advertisement, Application, Consultation, Profit, Service, Site} from '../models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})

export class MainComponent implements OnInit {

  public profits: Profit[] = []
  public services: Service[] = []
  public consultations: Consultation[] = []
  public sites: Site[] = []
  public advertisements: Advertisement[] = []
  public applications: Application[] = []

  public consultation_full_name: any = ''
  public consultation_telephone_number: any = ''
  public consultation_email: any = ''

  public application_full_name: any = ''
  public application_telephone_number: any = ''
  public application_email: any = ''

  constructor(private provider: ProviderService) {
  }

  ngOnInit() {
    this.getProfits()
    this.getServices()
    this.getSites()
    this.getAdvertisements()
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
    
    this.provider.addConsultation(service_id, this.consultation_full_name, this.consultation_telephone_number,
      this.consultation_email).then(res => {
      this.consultation_full_name = ''
      this.consultation_telephone_number = ''
      this.consultation_email = ''
      this.consultations.push(res)
    })
  }

  public getSites() {
    this.provider.getSites().then(res => {
      this.sites = res
    })
  }

  public getAdvertisements() {
    this.provider.getAdvertisements().then(res => {
      this.advertisements = res
    })
  }

  public addApplication() {
    this.provider.addApplication(this.application_full_name, this.application_telephone_number,
      this.application_email).then(res => {
      this.application_full_name = ''
      this.application_telephone_number = ''
      this.application_email = ''
      this.applications.push(res)
    })
  }
}
