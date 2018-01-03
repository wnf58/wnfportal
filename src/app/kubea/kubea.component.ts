import { Component, OnInit } from '@angular/core';
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

  constructor(private kubeaService: KubeaService) { }

  ngOnInit() {
    this.getKubEARecords();
  }

  onSelect(kubea: KubeaRecord): void {
    this.selectedKubEA = kubea;
  }

  getKubEARecords(): void {
    this.kubeaService.getKubEARecords()
        .subscribe(kubea => this.kubeaRecords = kubea);
  }

}
