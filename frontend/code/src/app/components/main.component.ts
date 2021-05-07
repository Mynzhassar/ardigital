import {ChangeDetectionStrategy, Component, OnDestroy, OnInit} from '@angular/core';
import {ProviderService} from '../services/provider.service';
import {Advertisement, Application, Consultation, Profit, Service, Site} from '../models/models';
import {Observable, Subject} from "rxjs";
import {takeUntil} from "rxjs/operators";
import {environment} from "../../environments/environment";

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})

export class MainComponent implements OnInit, OnDestroy {

  public apiUrl = environment.apiUrl;

  public profits: Observable<Profit[]> | undefined;
  public services: Observable<Service[]> | undefined;
  public sites: Observable<Site[]> | undefined;
  public advertisements: Observable<Advertisement[]> | undefined;
  public applications: Application[] = [];
  public consultations: Consultation[] = [];

  public consultationFullName: any = '';
  public consultationTelephoneNumber: any = '';
  public consultationEmail: any = '';

  public applicationFullName: any = '';
  public applicationTelephoneNumber: any = '';
  public applicationEmail: any = '';

  public showCase: any = 'sites';

  private destroy = new Subject<void>();

  constructor(private provider: ProviderService) {
  }

  ngOnInit() {
    this.getProfits();
    this.getServices();
    this.getCases(this.showCase);
  }

  public getProfits() {
    this.profits = this.provider.getProfits();
  }

  public getServices() {
    this.services = this.provider.getServices();
  }

  public addConsultation(service_id: number) {
    this.provider.addConsultation(service_id, this.consultationFullName, this.consultationTelephoneNumber, this.consultationEmail).pipe(takeUntil(this.destroy)).subscribe(res => {
      this.consultationFullName = '';
      this.consultationTelephoneNumber = '';
      this.consultationEmail = '';
      this.consultations.push(res);
    })
  }

  public getSites() {
    this.sites = this.provider.getSites();
  }

  public getAdvertisements() {
    this.advertisements = this.provider.getAdvertisements();
  }

  public getCases(current_case: string) {
    if (current_case == 'sites') {
      this.getSites();
    }
    if (current_case == 'advertisements') {
      this.getAdvertisements();
    }
  }

  public showSites() {
    this.showCase = 'sites';
    this.getCases(this.showCase);
  }

  public showAdvertisements() {
    this.showCase = 'advertisements';
    this.getCases(this.showCase);
  }

  public addApplication() {
    this.provider.addApplication(this.applicationFullName, this.applicationTelephoneNumber, this.applicationEmail).pipe(takeUntil(this.destroy)).subscribe(res => {
      this.applicationFullName = '';
      this.applicationTelephoneNumber = '';
      this.applicationEmail = '';
      this.applications.push(res)
    })
  }

  ngOnDestroy(): void {
    this.destroy.next();
    this.destroy.complete();
  }
}
