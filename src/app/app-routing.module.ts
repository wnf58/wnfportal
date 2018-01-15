import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { DashboardComponent }   from './dashboard/dashboard.component';
import { KubeaComponent }      from './kubea/kubea.component';
import { KubeaDetailComponent }  from './kubea-detail/kubea-detail.component';

const routes: Routes = [
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'detail/:id', component: KubeaDetailComponent },
  { path: 'kubea', component: KubeaComponent }
  { path: 'kubea/kontostand', component: KubeaComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
