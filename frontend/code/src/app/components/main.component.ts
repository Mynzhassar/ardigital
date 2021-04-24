import {ChangeDetectionStrategy, Component, OnDestroy, OnInit} from '@angular/core';
import {ProviderService} from '../services/provider.service';
import {Advertisement, Application, Consultation, Profit, Service, Site} from '../models/models';
import {Observable, Subject} from "rxjs";
import {takeUntil} from "rxjs/operators";

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})

export class MainComponent implements OnInit, OnDestroy {

  public profits: Observable<Profit[]> | undefined;
  public services: Observable<Service[]> | undefined;
  public sites: Observable<Site[]> | undefined
  public advertisements: Observable<Advertisement[]> | undefined;
  public applications: Application[] = []
  public consultations: Consultation[] = []

  public consultation_full_name: any = ''
  public consultation_telephone_number: any = ''
  public consultation_email: any = ''

  public application_full_name: any = ''
  public application_telephone_number: any = ''
  public application_email: any = ''

  private destroy = new Subject<void>();
  constructor(private provider: ProviderService) {
  }

  ngOnInit() {
    this.getProfits()
    this.getServices()
    this.getSites()
    this.getAdvertisements()
  }

  public getProfits() {
    this.profits = this.provider.getProfits();
  }

  public getServices() {
    this.services = this.provider.getServices();
  }

  public addConsultation(service_id: number) {
    this.provider.addConsultation(service_id, this.consultation_full_name, this.consultation_telephone_number, this.consultation_email).pipe(takeUntil(this.destroy)).subscribe(res => {
      this.consultation_full_name = ''
      this.consultation_telephone_number = ''
      this.consultation_email = ''
      this.consultations.push(res)
    })
  }

  public getSites() {
    this.sites = this.provider.getSites();
  }

  public getAdvertisements() {
    this.advertisements = this.provider.getAdvertisements();
  }

  public addApplication() {
    this.provider.addApplication(this.application_full_name, this.application_telephone_number, this.application_email).pipe(takeUntil(this.destroy)).subscribe(res => {
      this.application_full_name = ''
      this.application_telephone_number = ''
      this.application_email = ''
      this.applications.push(res)
    })
  }

  ngOnDestroy(): void {
    this.destroy.next();
    this.destroy.complete();
  }
}
