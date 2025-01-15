import { Component } from '@angular/core';
import {HeaderComponent} from "../../common-ui/header/header.component";

@Component({
  selector: 'app-home-page',
  imports: [
    HeaderComponent
  ],
  templateUrl: './home-page.component.html',
  standalone: true,
  styleUrl: './home-page.component.scss'
})
export class HomePageComponent {
}
