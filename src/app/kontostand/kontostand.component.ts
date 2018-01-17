import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { KontoRecord } from '../kubea_const';
import { KubeaService } from '../kubea.service';

@Component({
  selector: 'app-kontostand',
  templateUrl: './kontostand.component.html',
  styleUrls: ['./kontostand.component.css']
})

export class KontostandComponent implements OnInit {

  selectedKonto: KontoRecord;

  kontostandRecords: KontoRecord[];

  kontostandSumme: KontostandSummeRecord;

  constructor(
    private kubeaService: KubeaService,
    private location: Location,
    private route: ActivatedRoute) { }

  ngOnInit() {
    this.getKontostand();
  }

  onSelect(konto: KontoRecord): void {
    this.selectedKonto = konto;
  }

  getKontostand(): void {
    this.kubeaService.getKontostandSumme()
        .subscribe(summe => this.kontostandSumme = summe);
    this.kubeaService.getKontostand()
        .subscribe(konto => this.kontostandRecords = konto);
  }

  goBack(): void {
    this.location.back();
  }

}
