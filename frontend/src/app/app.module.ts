import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { JwtModule } from '@auth0/angular-jwt';
import { HttpClientModule } from '@angular/common/http';

import { DndModule } from '@ng-dnd/core';
import { HTML5Backend } from 'react-dnd-html5-backend';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './pages/login/login.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { LayoutComponent } from './pages/dashboard/components/layout/layout.component';
import { WorkspaceComponent } from './pages/dashboard/components/workspace/workspace.component';
import { ScriptButtonComponent } from './pages/dashboard/components/workspace/components/script-button/script-button.component';
import { EditSidebarComponent } from './pages/dashboard/components/workspace/components/edit-sidebar/edit-sidebar.component';

import { API_HOST } from './constants/const';


export function tokenGetter() {
  return localStorage.getItem("access_token");
}

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
    JwtModule.forRoot({
      config: {
        tokenGetter: tokenGetter,
        allowedDomains: [API_HOST],
      },
    }),
    DndModule.forRoot({ backend: HTML5Backend }),
    NgbModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
