import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { DndModule } from '@ng-dnd/core';
import { HTML5Backend } from 'react-dnd-html5-backend';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './pages/login/login.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { LayoutComponent } from './pages/dashboard/components/layout/layout.component';
import { WorkspaceComponent } from './pages/dashboard/components/workspace/workspace.component';
import { ScriptButtonComponent } from './pages/dashboard/components/workspace/components/script-button/script-button.component';
import { EditSidebarComponent } from './pages/dashboard/components/workspace/components/edit-sidebar/edit-sidebar.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    DashboardComponent,
    LayoutComponent,
    WorkspaceComponent,
    ScriptButtonComponent,
    EditSidebarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    DndModule.forRoot({ backend: HTML5Backend }),
    NgbModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
