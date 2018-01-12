import { Component, OnInit, Input } from '@angular/core';
import { KubeaRecord } from '../kubea_const';
import { KubeaService } from '../kubea.service';

@Component({
  selector: 'app-kubea-detail',
  templateUrl: './kubea-detail.component.html',
  styleUrls: ['./kubea-detail.component.css']
})
export class KubeaDetailComponent implements OnInit {
  @Input() kubea: KubeaRecord;

  constructor() { }

  ngOnInit() {
  }

}
