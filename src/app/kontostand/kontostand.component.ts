import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { KontoRecord,KONTOSTANDDEMO } from '../kubea_const';
import { KubeaService } from '../kubea.service';

@Component({
  selector: 'app-kontostand',
  templateUrl: './kontostand.component.html',
  styleUrls: ['./kontostand.component.css']
})
export class KontostandComponent implements OnInit {

  selectedKonto: KontoRecord;

  kontenRecords: KontoRecord[];

  constructor(
    private kubeaService: KubeaService,
    private location: Location,
    private route: ActivatedRoute) { }

  ngOnInit() {
    this.kontenRecords = KONTOSTANDDEMO;
    // this.getKontostand();
  }

  onSelect(konto: KontoRecord): void {
    this.selectedKonto = konto;
  }

  getKontostand(): void {
    this.kubeaService.getKontostand()
        .subscribe(konto => this.kontenRecords = konto);

  }

  goBack(): void {
    this.location.back();
  }

}
