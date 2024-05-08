import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { WorkspaceService } from '../../../../services/workspace.service';

@Component({
  selector: 'app-layout',
  templateUrl: './layout.component.html',
  // styleUrl: './layout.component.scss'
})
export class LayoutComponent {

  loggedUser: any;
  constructor(
    private router: Router,
    private workspaceService: WorkspaceService
  ) {
    const localUser = localStorage.getItem('loggedUser');
    if (localUser != null) {
      this.loggedUser = JSON.parse(localUser);
    }
  }

  onLogoff() {
    this.router.navigateByUrl('/login');
  }

  onScriptButtonAdd() {
    this.workspaceService.addButton();
  }
}
