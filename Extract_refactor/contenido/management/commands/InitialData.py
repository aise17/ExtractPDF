from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from django.utils import timezone
from oauth2_provider.models import Application

import  sys



sys.path.append("../..")
#from Extract_refactor.ocr_api.models import Explicacion
#from Extract_refactor.ocr_api.serializers import ExplicaionSerializer


from ocr_api.models import MinSizeDocumento
from contenido.models import Explicacion, Bono, QuienSomos, ExplicacionScrapy, NormasOcr, NormasScrapy, Faqs
from usuarios.models import BonoUsuario


class Command(BaseCommand):
    help = 'Crea superadministrador'

    def handle(self, *args, **options):
        self.crearSuperuser()
        self.crearExplicacion1Inicial()
        self.crearExplicacion2Inicial()
        self.crearExplicacion3Inicial()
        self.crearApilicationOauthAngular()
        self.crearApilicationOauthAndroid()
        self.crearBonoSmallCard()
        self.crearBonoMediumCard()
        self.crearBonoGrantCard()
        self.crearMinSizeDocumentoDefault()
        self.crearQuienSomos()
        self.createSuperbono()
        self.crearExplicacion1Scrapy()
        self.crearExplicacion2Scrapy()
        self.crearExplicacion3Scrapy()
        self.crearNormaOcr1()
        self.crearNormaOcr2()
        self.crearNormaOcr3()
        self.crearNormaScrapy1()
        self.crearNormaScrapy2()
        self.crearFaqs1()
        self.crearFaqs2()

    def crearSuperuser(self):
        if (User.objects.filter(username='admin')):
            print('[+] El usuario superadministrador ya existe')

        else:

            user = User()
            user.username = 'admin'
            user.set_password('admin')
            user.is_superuser = True
            user.is_staff = True

            user.save()

            print('[+] superadministrador creado')

    def crearExplicacion1Inicial(self):
        if (Explicacion.objects.filter(titulo='Utilice el software OCR')):
            print('[+] Primera explicacion ya existe')

        else:
            explicacion = Explicacion()
            explicacion.titulo = 'Utilice el software OCR'
            explicacion.contenido = 'sin instalación en su computadora. Reconocer texto y caracteres de documentos escaneados en PDF (incluidos archivos de varias páginas), fotografías e imágenes captadas por cámaras digitales.'
            explicacion.publicado = True
            explicacion.titulo_imagen = 'imagen1'
            explicacion.imagen = 'http://innovagroupbcn.com/wp-content/uploads/2017/02/ocr.jpg'

            try:

                explicacion.save()

                print('[+] Primera explicacion creada')
            except:
                print('[+][+] Primera Explicacion no es valida')
                print('[+][+] Error producido -> ' + explicacion.contenido.__repr__())

    def crearExplicacion2Inicial(self):
        if (Explicacion.objects.filter(titulo='Convertir PDF a Word')):
            print('[+] Segunda explicacion ya existe')

        else:
            explicacion = Explicacion()
            explicacion.titulo = 'Convertir PDF a Word'
            explicacion.contenido = 'Convierta texto e imágenes de su documento PDF escaneado al formato DOC editable. Los documentos convertidos se ven exactamente como el original: tablas, columnas y gráficos.'
            explicacion.fecha_publicacion = timezone.now()
            explicacion.fecha_creacion = timezone.now()
            explicacion.publicado = True
            explicacion.titulo_imagen = 'imagen2'
            explicacion.imagen = 'https://sitejerk.com/images/convertir-png-en-pdf-11.png'

            try:

                explicacion.save()

                print('[+] Segunda explicacion creada')
            except:
                print('[+][+] Segunda Explicacion no es valida')
                print('[+][+] Error producido -> ' + explicacion.contenido.__repr__())

    def crearExplicacion3Inicial(self):
        if (Explicacion.objects.filter(titulo='Servicio gratuito')):
            print('[+] Tercera explicacion ya existe')

        else:
            explicacion = Explicacion()
            explicacion.titulo = 'Servicio gratuito'
            explicacion.contenido = 'OnlineOCR.net es un servicio de OCR gratuito en un "modo de invitado" (sin registro) que le permite convertir 15 archivos por hora (y 15 páginas en archivos de varias páginas). El registro le dará la capacidad de convertir documentos PDF de varias páginas y otras características.'
            explicacion.fecha_publicacion = timezone.now()
            explicacion.publicado = True
            explicacion.titulo_imagen = 'imagen3'
            explicacion.imagen = 'https://st.depositphotos.com/1031343/3971/v/950/depositphotos_39717745-stock-illustration-gratis-stamp.jpg'

            try:

                explicacion.save()

                print('[+] Tercera explicacion creada')
            except:
                print('[+][+] Tercera Explicacion no es valida')
                print('[+][+] Error producido -> ' + explicacion.contenido.__repr__())

    def crearApilicationOauthAngular(self):
        if (Application.objects.filter(name='Angular')):
            print('[+] Aplicacion Angular ya existe')
        else:
            aplication = Application()
            aplication.name = 'Angular'
            aplication.client_id = 'xIlTUtu3pv3YCN0NZxioinzAIvnqhaUPB3j6C9m1'
            aplication.client_secret = '15VmSMITKwQTOdDxSfUtFa6SGhvSkhRbtumDSJssPaOvhL1BJAoql5SCM6EVGdEPEubougfrpR3f29GoPDhgeez3o9kWlSQFRsd03wiJiHz9Wlgp9V61y8tdom0XyZoj'
            aplication.client_type = 'confidential'
            aplication.redirect_uris = ''
            aplication.authorization_grant_type = 'password'

            try:

                aplication.save()

                print('[+] Registro de Aplicacion creado')
            except:
                print('[+][+] Registro de Aplicacion no es valida')
                print('[+][+] Error en registro de Aplicacion -> ' + aplication.__repr__())

    def crearApilicationOauthAndroid(self):
        if (Application.objects.filter(name='Android')):
            print('[+] Aplicacion Android ya existe')
        else:
            aplication = Application()
            aplication.name = 'Android'
            aplication.client_id = 'NxZCC1cyEC4EaKWTp0WOKI8AcfxoLympY6ESrQFi'
            aplication.client_secret = 'gcogobaJ4lYihODys8U9ij7BUQBbx8Uta3GVo3AVpnFcSNtDi9rg1LElTOfttDMSqh3hyjEIHFyTzrD9J48yl5lEKOXShf13vPUrGQFLr7gRAZqu8264KWd5YrShqIby'
            aplication.client_type = 'confidential'
            aplication.redirect_uris = ''
            aplication.authorization_grant_type = 'password'

            try:

                aplication.save()

                print('[+] Registro de Aplicacion creado')
            except:
                print('[+][+] Registro de Aplicacion no es valida')
                print('[+][+] Error en registro de Aplicacion -> ' + aplication.__repr__())

    def crearBonoGrantCard(self):
        if Bono.objects.filter(titulo='Great Card'):
            print('[+] Bono Great Card ya existe')
        else:
            bono = Bono()
            bono.titulo = 'Great Card'
            bono.peticiones = '200'
            bono.descripcion = 'consige el este pak de 200 peticiones a nuestro servicios a un coste reducido'
            bono.precio = '10'
            bono.activado = True

            try:
                bono.save()
                print('[+] Registro de Bono Great Card creado')
            except:

                print('[+][+] Registro de Bono no es valido')
                print('[+][+] Error en registro de Aplicacion -> ' + bono.__repr__())

    def crearBonoMediumCard(self):
        if Bono.objects.filter(titulo='Medium Card'):
            print('[+] Bono Medium Card ya existe')
        else:
            bono = Bono()
            bono.titulo = 'Medium Card'
            bono.peticiones = '80'
            bono.descripcion = 'amplia tus peticiones con este pak de 80 peticiones por solo 8 euros'
            bono.precio = '8'
            bono.activado = True

            try:
                bono.save()
                print('[+] Registro de Bono Great Card creado')
            except:

                print('[+][+] Registro de Bono no es valida')
                print('[+][+] Error en registro de Aplicacion -> ' + bono.__repr__())

    def crearBonoSmallCard(self):
        if Bono.objects.filter(titulo='Small Card'):
            print('[+] Bono Small Card ya existe')
        else:
            bono = Bono()
            bono.titulo = 'Small Card'
            bono.peticiones = '20'
            bono.descripcion = 'este bono te permitirá adquirir 20 peticiones a nuestros servicios'
            bono.precio = '5'
            bono.activado = True

            try:
                bono.save()
                print('[+] Registro de Bono Great Card creado')
            except:

                print('[+][+] Registro de Bono no es valida')
                print('[+][+] Error en registro de Aplicacion -> ' + bono.__repr__())

    def crearMinSizeDocumentoDefault(self):
        if MinSizeDocumento.objects.filter(titulo='defecto'):
            print('[+] MinSizeDocumento defecto ya existe')
        else:
            min_size_documento = MinSizeDocumento()
            min_size_documento.titulo = 'defecto'
            min_size_documento.tam_min = 40000
            min_size_documento.activo = True

            try:
                min_size_documento.save()
                print('[+] Registro de MinSizeDocumento defecto creado')
            except:

                print('[+][+] Registro de MinSizeDocumento no es valida')
                print(
                    '[+][+] Error en registro de MinSizeDocumento defecto -> ' + min_size_documento.__repr__())

    def crearQuienSomos(self):
        if QuienSomos.objects.filter(titulo='defecto'):
            print('[+] QuienSomos defecto ya existe')
        else:
            quien_somos = QuienSomos()
            quien_somos.titulo = 'defecto'
            quien_somos.contenido = '<p>Jovenes estudiantes de programador interesados en tecnologias bakend y frontend con buen manejo en leguajes python, javascript y c# utilizando&nbsp; frameworks como django, .net, angular 5,&nbsp;sql, android y&nbsp;&nbsp;java</p>' \
                                    '<p>Especializado en tecnologias python y Django utilizando el stak django, celery redis, nginx sonbre docker(AISE)</p' \
                                    '><p>Especializado en tecnologias java, android, sapui5, abap, kotlin(MELEBA)</p><p>aficionado a la escalada, los viajes las buenas conversaciones(AISE)</p><p>aficionado a los videojuegos, los airsoft, los viajes en pareja,' \
                                    '&nbsp;las buenas conversaciones(AISE)</p><p>&nbsp;</p>'

            quien_somos.publicado = True

            try:
                quien_somos.save()
                print('[+] Registro de QuienSomos defecto creado')
            except:

                print('[+][+] Registro de QuienSomos no es valida')
                print(
                    '[+][+] Error en registro de QuienSomos defecto -> ' + quien_somos.__repr__())

    def createSuperbono(self):
        if BonoUsuario.objects.filter(usuario='1'):
            print('[+] createUserBonus defecto ya existe')
        else:
            user_bonus = BonoUsuario()
            user = User.objects.filter(username='admin').get()
            bono = Bono.objects.filter(titulo='Great Card').get()
            user_bonus.usuario = user
            user_bonus.bono = bono
            user_bonus.activado = True
            user_bonus.peticiones_restantes = 2000000

            try:
                user_bonus.save()
                print('[+] Registro de UsuarioBono para admin creado')
            except:

                print('[+][+] Registro de UsuarioBono no es valida')
                print(
                    '[+][+] Error en registro de UsuarioBono defecto -> ' + user_bonus.__repr__())


    def crearExplicacion1Scrapy(self):
        if (ExplicacionScrapy.objects.filter(titulo='Análisis de una tienda online o e-commerce')):
            print('[+] Primera explicacion Scrapy ya existe')

        else:
            explicacion = ExplicacionScrapy()
            explicacion.titulo = 'Análisis de una tienda online o e-commerce'
            explicacion.contenido = 'Consige informacion de ESTADO de la web, RANKING ALEXA, IDIOMA, EMAIL, PLATAFORMA utilizadas de fomra automatizada de paginas e-commerce con solo aportar un csv con las urls a analizar'
            explicacion.publicado = True
            explicacion.titulo_imagen = 'imagen1'
            explicacion.imagen = 'https://sell.emprendepyme.net/wp-content/uploads/2017/12/analitica-de-ventas.jpg'

            try:

                explicacion.save()

                print('[+] Primera explicacion Scrapy creada')
            except:
                print('[+][+] Primera Explicacion Scrapy no es valida')
                print('[+][+] Error producido -> ' + explicacion.contenido.__repr__())

    def crearExplicacion2Scrapy(self):
        if (ExplicacionScrapy.objects.filter(titulo='Aumenta tu eficiencia')):
            print('[+] Segunda explicacion Scrapy ya existe')

        else:
            explicacion = ExplicacionScrapy()
            explicacion.titulo = 'Aumenta tu eficiencia'
            explicacion.contenido = 'Ahorra destinar recursos o timpo en buscar informacion de contacto de sitios e-commerce. Automatiza tiodas estas tediosas tareas utilizando nuestro servicio Scrapy '
            explicacion.fecha_publicacion = timezone.now()
            explicacion.fecha_creacion = timezone.now()
            explicacion.publicado = True
            explicacion.titulo_imagen = 'imagen2'
            explicacion.imagen = 'https://telematics.tomtom.com/es_es/webfleet/blog/wp-content/uploads/sites/21/2018/01/flota-comercial.jpg'

            try:

                explicacion.save()

                print('[+] Segunda explicacion Scrapy creada')
            except:
                print('[+][+] Segunda Explicacion Scrapy no es valida')
                print('[+][+] Error producido -> ' + explicacion.contenido.__repr__())

    def crearExplicacion3Scrapy(self):
        if (ExplicacionScrapy.objects.filter(titulo='Tarifas Competitivas')):
            print('[+] Tercera explicacion Scrapy ya existe')

        else:
            explicacion = ExplicacionScrapy()
            explicacion.titulo = 'Tarifas Competitivas'
            explicacion.contenido = 'Servicio de Analisis gratuito en un "modo de invitado" (sin registro) que le permite procesar archivos csv de hasta 40 Kb. El registro y la posterior comra de bonos le daran acceso a nuestos servicios. Si tiene alguna necesidad de sistema de tarifa plana, por fabor contacte con nosotros'
            explicacion.fecha_publicacion = timezone.now()
            explicacion.publicado = True
            explicacion.titulo_imagen = 'imagen3'
            explicacion.imagen = 'https://img-aws.ehowcdn.com/877x500p/photos.demandstudios.com/getty/article/142/136/89684413.jpg'

            try:

                explicacion.save()

                print('[+] Tercera explicacion Scrapy creada')
            except:
                print('[+][+] Tercera Explicacion Scrapy no es valida')
                print('[+][+] Error producido -> ' + explicacion.contenido.__repr__())


    def crearNormaOcr1(self):
        if (NormasOcr.objects.filter(titulo='Extension de ficheros')):
            print('[-] Primera Norma Ocr ya existe')

        else:
            norma = NormasOcr()
            norma.titulo = 'Extension de ficheros'
            norma.contenido = 'Los archivos que se suban solo podran ser PDF '
            norma.fecha_publicacion = timezone.now()
            norma.publicado = True
            norma.titulo_imagen = 'imagen3'
            norma.imagen = 'https://img-aws.ehowcdn.com/877x500p/photos.demandstudios.com/getty/article/142/136/89684413.jpg'

            try:

                norma.save()

                print('[+] Primera Norma Ocr creada')
            except:
                print('[-][-] Primera Norma Ocr no es valida')
                print('[-][-] Error al insertar norma -> ' + norma.contenido.__repr__())


    def crearNormaOcr2(self):
        if (NormasOcr.objects.filter(titulo='Tipo de proceso')):
            print('[-] Segunda Norma Ocr ya existe')

        else:
            norma = NormasOcr()
            norma.titulo = 'Tipo de proceso'
            norma.contenido = 'En el despeglabe con el dibujo de engranaje se seleccionara el proceso por el que se pasara el documento para su mejor comprension. Se aconseja probar entre los tres ya que esta herramienta todavía eseta en proceso de desarroyo y dependera del tipo de imagen que se quiera procesar'
            norma.fecha_publicacion = timezone.now()
            norma.publicado = True
            norma.titulo_imagen = 'imagen3'
            norma.imagen = 'https://img-aws.ehowcdn.com/877x500p/photos.demandstudios.com/getty/article/142/136/89684413.jpg'

            try:

                norma.save()

                print('[+] Segundo Norma Ocr creada')
            except:
                print('[-][-] Segunda Norma Ocr no es valida')
                print('[-][-] Error al insertar norma -> ' + norma.contenido.__repr__())


    def crearNormaOcr3(self):
        if (NormasOcr.objects.filter(titulo='Acceso al servicio')):
            print('[-] Tercera Norma Ocr ya existe')

        else:
            norma = NormasOcr()
            norma.titulo = 'Acceso al servicio'
            norma.contenido = 'los usuarios anonimos, o sin bonos podran subir ficheros de hasta 40kb gratuitamente, para acceder a este servicio ilimitadamente solo tiene que registrarse y adquirir uno de nuestros bonos con un bajo conste '
            norma.fecha_publicacion = timezone.now()
            norma.publicado = True
            norma.titulo_imagen = 'imagen3'
            norma.imagen = 'https://img-aws.ehowcdn.com/877x500p/photos.demandstudios.com/getty/article/142/136/89684413.jpg'

            try:

                norma.save()

                print('[+] Tercera norma Ocr creada')
            except:
                print('[-][-] Tercera Norma Ocr no es valida')
                print('[-][-] Error al insertar norma -> ' + norma.contenido.__repr__())



    def crearNormaScrapy1(self):
        if (NormasScrapy.objects.filter(titulo='Extension de ficheros')):
            print('[-] Primera Norma Ocr ya existe')

        else:
            norma = NormasScrapy()
            norma.titulo = 'Extension de ficheros'
            norma.contenido = 'Los archivos que se suban solo podran ser Csv y contendras en la primera columna las urls que se van ha analizar '
            norma.fecha_publicacion = timezone.now()
            norma.publicado = True
            norma.titulo_imagen = 'imagen3'
            norma.imagen = 'https://img-aws.ehowcdn.com/877x500p/photos.demandstudios.com/getty/article/142/136/89684413.jpg'

            try:

                norma.save()

                print('[+] Primera Norma Scrapy creada')
            except:
                print('[-][-] Primera Norma Scrapy no es valida')
                print('[-][-] Error al insertar norma' + norma.contenido.__repr__())




    def crearNormaScrapy2(self):
        if (NormasScrapy.objects.filter(titulo='Acceso al servicio')):
            print('[-] Segunda Norma Scrapy ya existe')

        else:
            norma = NormasScrapy()
            norma.titulo = 'Acceso al servicio'
            norma.contenido = 'los usuarios anonimos, o sin bonos podran subir ficheros de hasta 40kb gratuitamente, para acceder a este servicio ilimitadamente solo tiene que registrarse y adquirir uno de nuestros bonos con un bajo conste '
            norma.fecha_publicacion = timezone.now()
            norma.publicado = True
            norma.titulo_imagen = 'imagen3'
            norma.imagen = 'https://img-aws.ehowcdn.com/877x500p/photos.demandstudios.com/getty/article/142/136/89684413.jpg'

            try:

                norma.save()

                print('[+] Segunda Norma Scrapy creada')
            except:
                print('[-][-] Segunda Noroma Scrapy no es valida')
                print('[-][-] Error al insertar norma -> ' + norma.contenido.__repr__())



    def crearFaqs1(self):
        if (Faqs.objects.filter(titulo='Como usar nuestros servicios desde aplicaciones propias')):
            print('[-] Primera Faq ya existe')

        else:
            faq = Faqs()
            faq.titulo = 'Como usar nuestros servicios desde aplicaciones propias'
            faq.contenido = 'Para usar nuestros servicios desde aplicacioines propias, hemos puesto a disposicion de los desarolladores una web swagger para facilitar la documetacion de nuestros servicios, en caso de dudas no dudes en contactar con nosotros atraves del apartado contacto de nuestra web'
            faq.fecha_publicacion = timezone.now()
            faq.publicado = True
            faq.titulo_imagen = 'imagen3'
            faq.imagen = 'https://img-aws.ehowcdn.com/877x500p/photos.demandstudios.com/getty/article/142/136/89684413.jpg'

            try:

                faq.save()

                print('[+] Primera Faq creada')
            except:
                print('[-][-] Primera Faq no es valida')
                print('[-][-] Error al insertar Faq' + faq.contenido.__repr__())




    def crearFaqs2(self):
        if (Faqs.objects.filter(titulo='Como contactar')):
            print('[-] Segunda Faq ya existe')

        else:
            faq = Faqs()
            faq.titulo = 'Como contactar'
            faq.contenido = 'En el menu desplegable izquierdo podremos encontrar el apartado Contacto. No dude en contactar con nosotros para cualquier duda, no tardaremos en atender su mensaje'
            faq.fecha_publicacion = timezone.now()
            faq.publicado = True
            faq.titulo_imagen = 'imagen3'
            faq.imagen = 'https://img-aws.ehowcdn.com/877x500p/photos.demandstudios.com/getty/article/142/136/89684413.jpg'

            try:

                faq.save()

                print('[+] Segunda Faq creada')
            except:
                print('[-][-] Segunda faq no es valida')
                print('[-][-] Error al insertar Faq -> ' + faq.contenido.__repr__())