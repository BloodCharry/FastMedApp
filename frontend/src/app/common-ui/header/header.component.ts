import { Component } from '@angular/core';
import { SvgIconComponent } from "../svg-icons/svg-icons.component";


@Component({
  selector: 'app-header',
  imports: [SvgIconComponent],
  templateUrl: './header.component.html',
  standalone: true,
  styleUrl: './header.component.scss'
})

export class HeaderComponent {}
