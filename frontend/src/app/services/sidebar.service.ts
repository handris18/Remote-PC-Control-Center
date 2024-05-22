import { Injectable, inject } from '@angular/core';
import { Observable, Subject, timer } from 'rxjs';
import { NgbOffcanvas } from '@ng-bootstrap/ng-bootstrap';

import { APIService } from './api.service';
import { EditSidebarComponent } from '../pages/dashboard/components/workspace/components/edit-sidebar/edit-sidebar.component';
import { ScriptButton, ScriptObject } from '../interfaces/script-button.interface';
import { UpdateResponse } from '../interfaces/api-interfaces.interface';

@Injectable({
  providedIn: 'root'
})
export class SidebarService {
  
  private currentScriptButton$ = new Subject<ScriptButton>();
  private currentScriptText$ = new Subject<string>();
  private offcanvasService = inject(NgbOffcanvas);

  constructor(private apiService: APIService) {}

  openSidebarForScript(scriptButton: ScriptButton) {
    const offcanvasRef = this.offcanvasService.open(
      EditSidebarComponent,
      { position: 'end', panelClass: "w-50" });

    offcanvasRef.shown.subscribe(_ => {
      this.currentScriptButton$.next(scriptButton);
      this.currentScriptText$.next('Loading...');

      this.apiService.fetchScript(parseInt(scriptButton.id)).subscribe(
        scriptObj => {
          if (scriptObj !== null) {
            const {id, name, content} = scriptObj;
            this.currentScriptButton$.next({id, name});
            this.currentScriptText$.next(content);
          } else {
            this.currentScriptText$.next("Couldn't load script text");
          }
        }
      )
    });
  }

  getScriptButtonAsObservable(): Observable<ScriptButton> {
    return this.currentScriptButton$.asObservable();
  }

  saveScript(scriptObj: ScriptObject): Observable<UpdateResponse> {
    return this.apiService.updateScript(scriptObj);
  }

  getScriptTextAsObservable(): Observable<string> {
    return this.currentScriptText$.asObservable();
  }
}
