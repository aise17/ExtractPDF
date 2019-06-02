import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import { ContenidoService } from '../services/contenido.service';
import { MatDialog } from '@angular/material';
import { Faqs } from '../models/faqs.model';
import { DialogErrorComponent } from '../dialog-error/dialog-error.component';
import { Norma } from '../models/norma.model';





@Component({
  selector: 'app-normas-ocr',
  templateUrl: './normas-ocr.component.html',
  styleUrls: ['./normas-ocr.component.css']
})
export class NormasOcrComponent implements OnInit {


  constructor(private _formBuilder: FormBuilder, private service: ContenidoService, public dialog: MatDialog) {}

  ngOnInit() {

    this.getNormaOcr();
  }

  public result: Norma[];


  getNormaOcr(): void {
    console.log('pulsado');

    this.service.getNormasOcr()
    .subscribe(res => {
      console.log('resultado - >' + res['ok'])
      if (res['ok'] === true){
        this.result = res['salida'];
        console.log(this.result)
        console.log('Las normas optenidos en la peticion son -> ' + this.result);
      }else if(res['ok'] === false){
        this.openDialogError(res['error'])
      }
    }); 
  }

   openDialogError(request): void {
    const dialogRef = this.dialog.open(DialogErrorComponent, {
      width: '250px',
      data: {error: request}
    });

    dialogRef.afterClosed().subscribe(result => {
     
        console.log('dialogo error cerrado')
      
    });
  
  }





}