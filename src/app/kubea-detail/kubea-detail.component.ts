import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { KubeaRecord } from '../kubea_const';
import { KubeaService } from '../kubea.service';

@Component({
  selector: 'app-kubea-detail',
  templateUrl: './kubea-detail.component.html',
  styleUrls: ['./kubea-detail.component.css']
})
export class KubeaDetailComponent implements OnInit {
  @Input() kubea: KubeaRecord;

  constructor(
    private route: ActivatedRoute,
    private kubeaService: KubeaService,
    private location: Location
  ) {}

  ngOnInit(): void {
    this.getKubEA();
  }

  getKubEA(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.kubeaService.getKubEA(id)
      .subscribe(kubea => this.kubea = kubea);
  }

  goBack(): void {
    this.location.back();
  }

 save(): void {
    this.kubeaService.updateKubEA(this.kubea)
      .subscribe(() => this.goBack());
  }
}


