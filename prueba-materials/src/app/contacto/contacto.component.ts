import { Component, OnInit } from '@angular/core';
import { ContactoService } from '../services/contacto.service';
import { Contacto } from '../models/contacto.model';

@Component({
  selector: 'app-contacto',
  templateUrl: './contacto.component.html',
  styleUrls: ['./contacto.component.css']
})
export class ContactoComponent implements OnInit {

  public contacto = new Contacto();
  public entregado = false;

  constructor(public contactoService: ContactoService) { }

  ngOnInit() {

  }



  sendEmail() {
    if (sessionStorage.getItem('id')) {
      this.contacto.id = parseInt(sessionStorage.getItem('id'), 0 );
    }
    console.log(this.contacto);
    this.contactoService.sendEmail(this.contacto)
    .subscribe(res => {
      console.log(res['ok']);

        this.entregado = true;

    });
  }

}