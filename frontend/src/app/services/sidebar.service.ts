import { Injectable, inject } from '@angular/core';
import { Observable, Subject, timer } from 'rxjs';
import { NgbOffcanvas } from '@ng-bootstrap/ng-bootstrap';

import { ScriptButton } from '../interfaces/script-button.interface';
import { EditSidebarComponent } from '../pages/dashboard/components/workspace/components/edit-sidebar/edit-sidebar.component';

@Injectable({
  providedIn: 'root'
})
export class SidebarService {
  
  private currentScriptButton$ = new Subject<ScriptButton>();
  private currentScriptText$ = new Subject<string>();
  private offcanvasService = inject(NgbOffcanvas);

  openSidebarForScript(scriptButton: ScriptButton) {
    const offcanvasRef = this.offcanvasService.open(
      EditSidebarComponent,
      { position: 'end' });

    offcanvasRef.shown.subscribe(_ => {
      this.currentScriptButton$.next(scriptButton);
      this.currentScriptText$.next('Loading...');
      timer(2000).subscribe(_ => this.currentScriptText$.next('Dummy text'));
    });
  }

  getScriptButtonAsObservable(): Observable<ScriptButton> {
    return this.currentScriptButton$.asObservable();
  }

  getScriptTextAsObservable(): Observable<string> {
    return this.currentScriptText$.asObservable();
  }
}
