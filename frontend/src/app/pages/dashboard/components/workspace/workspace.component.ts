import { Component, OnInit, inject } from '@angular/core';
import { Observable, of } from 'rxjs';

import { ScriptButton } from '../../../../interfaces/script-button.interface';
import { WorkspaceService } from '../../../../services/workspace.service';
import { SidebarService } from '../../../../services/sidebar.service';

@Component({
  selector: 'app-workspace',
  templateUrl: './workspace.component.html',
  // styleUrl: './workspace.component.scss'
})
export class WorkspaceComponent implements OnInit {

  buttons$: Observable<ScriptButton[]> = of();

  constructor(
    private workspaceService: WorkspaceService,
    private sidebarService: SidebarService,
  ) {}

  ngOnInit(): void {
    this.buttons$ = this.workspaceService.getButtonsAsObservable();
  }

  openSidebar(scriptButton: ScriptButton) {
    this.sidebarService.openSidebarForScript(scriptButton);
	}

  launchScript(scriptButton: ScriptButton) {
    alert(`The script ${scriptButton.id} has been laucnhed`);
  }
}
