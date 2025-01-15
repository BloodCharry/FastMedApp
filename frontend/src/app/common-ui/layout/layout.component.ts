import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import {SidebarComponent} from "../sidebar/sidebar.component";

@Component({
  selector: 'app-layout',
  imports: [RouterModule, SidebarComponent],
  templateUrl: './layout.component.html',
  standalone: true,
  styleUrl: './layout.component.scss'
})
export class LayoutComponent {

}
