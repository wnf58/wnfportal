import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Location } from '@angular/common';

import { KubeaRecord } from '../kubea_const';
import { KubeaService } from '../kubea.service';

@Component({
  selector: 'app-kubea',
  templateUrl: './kubea.component.html',
  styleUrls: ['./kubea.component.css']
})
export class KubeaComponent implements OnInit {

  selectedKubEA: KubeaRecord;

  kubeaRecords: KubeaRecord[];

  title = 'xxx';

  constructor(
    private kubeaService: KubeaService,
    private location: Location,
    private route: ActivatedRoute) { }

  ngOnInit() {
    this.title = 'yyy';
    this.route.params.subscribe((params: Params) => {
      console.log(params);
      });
    this.getKubEARecords();
  }

  onSelect(kubea: KubeaRecord): void {
    this.selectedKubEA = kubea;
  }

  getKubEARecords(): void {
    this.kubeaService.getKubEARecords()
        .subscribe(kubea => this.kubeaRecords = kubea);
  }

  goBack(): void {
    this.location.back();
  }

}
