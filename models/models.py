# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
import time
# class rusia(models.Model):
#     _name = 'rusia.rusia'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


# Modelo Rusia.Ciudades

class Ciudades(models.Model):
   _name = 'rusia.ciudades'

   name = fields.Char()
   Image = fields.Binary()
   Code = fields.Char()
   Tel_Emergency = fields.Char()
   Map = fields.Binary()
   Punto_Encuentro = fields.Char()
   Image_Punto_Encuentro = fields.Binary()
   Url_Map = fields.Char()
   tour_id = fields.One2many('rusia.tours', 'ciudad_id', string="Tours relacionados")
   eventos_ids = fields.One2many('rusia.eventos', 'ciudad_id', string="Eventos relacionados")
   gastos_ids = fields.One2many('rusia.gastos.ciudad', 'name', string="Gastos relacionados")



# Modelo Rusia.Tours

class Tours(models.Model):
    _name = 'rusia.tours'

    name = fields.Char()
    Code = fields.Char()
    No_show = fields.Char()
    Pax_minimo = fields.Char()
    Salario_minimo = fields.Char()
    Is_Privado = fields.Boolean(default=True)
    Is_Museo = fields.Boolean(default=True)
    Salario_Extra = fields.Char()
    Is_Gratis = fields.Boolean(default=True)
    Hora_Inicio = fields.Datetime()
    Hora_Finalizar = fields.Datetime()
    Descripcion = fields.Char()
    ciudad_id = fields.Many2one('rusia.ciudades', ondelete="set null", string="Ciudad", index=True)
    Costo_Pax1 = fields.Float()
    Costo_Pax2 = fields.Float()
    Costo_Pax3 = fields.Float()
    Costo_Pax4 = fields.Float()
    Costo_Pax5 = fields.Float()
    Costo_Pax6 = fields.Float()
    Costo_Pax7 = fields.Float()
    Costo_Pax8 = fields.Float()
    Costo_Pax9 = fields.Float()
    Costo_Pax10 = fields.Float()
    Gasto_Pax1 = fields.Float()
    Gasto_Pax2 = fields.Float()
    Gasto_Pax3 = fields.Float()
    Gasto_Pax4 = fields.Float()
    Gasto_Pax5 = fields.Float()
    Gasto_Pax6 = fields.Float()
    Gasto_Pax7 = fields.Float()
    Gasto_Pax8 = fields.Float()
    Gasto_Pax9 = fields.Float()
    Gasto_Pax10 = fields.Float()





# Modelo Rusia.Eventos  

class Eventos(models.Model):
    _name = 'rusia.eventos'


    def a_padre(self):
        # return self.algo()
        print "pasa,poas :D"
        return "hola22"
        #Aquui buscamos siempre el primer evento hijo, si no existe pues no podemos nada

    name = fields.Char()
    Fecha_Inicio = fields.Date()
    Fecha_Fin = fields.Date()
    hora_inicio = fields.Char()
    hora_final = fields.Char()
    Pax_Pago = fields.Char()
    Pax_Terceros = fields.Char()
    Pax_All_Included = fields.Char()
    Total_Paxs = fields.Char()
    Total_Euros = fields.Float()
    Total_Usd = fields.Float()
    Total_Rub = fields.Float()
    Total_Paypal = fields.Float()
    Total_Tarjeta = fields.Float()
    Total_Representante = fields.Float()
    Total_Beneficios = fields.Float()
    Comentarios_Internos = fields.Text()
    Comentarios_Guia = fields.Text()
    Comentarios_Cliente = fields.Text()
    Comentarios_Chofer = fields.Text()
    Transporte = fields.Char()
    Numero_Reserva = fields.Char()
    Total_Pago_Clientes = fields.Float()
    Total_Pagado_Web = fields.Float()
    Servicio_Gastos = fields.Float()
    representante_id = fields.Many2one('res.users', 'Representantes')
    Datos_Cliente_id = fields.Many2one('res.users', 'Cliente')
    gastostour_ids = fields.One2many('rusia.gastostours', 'eventos_id', string="Gastos de los tours")
    servicio_id = fields.Many2one('rusia.tiposervicios', 'Tipo de servicio')
    chofer_id = fields.Many2one('res.users', 'Chofer')
    documentos_ids = fields.One2many('ir.attachment', 'eventos_id', 'Documentos del servicio')
    documentos_clientes_ids = fields.One2many('ir.attachment', 'eventos_cliente_id', 'Documentos del cliente')
    # documentos_id = fields.Many2one('ir.attachment', 'Documentos')
    descripcionitinerario_ids = fields.One2many('rusia.toursitinerario','eventos_id', 'Descripción Itinerario')
    guia_id = fields.Many2one('res.users', ondelete="set null", string="Guía", index=True)
    tour_id = fields.Many2one('rusia.tours', ondelete="set null", string="Tour", index=True)
    # pasajeros_id = fields.One2many('rusia.tourspasajeros', 'eventos_id', string="Datos del cliente")
    evento_id = fields.Many2one('rusia.eventos','Evento Padre')
    evento_ids = fields.One2many('rusia.eventos','evento_id','Evento Hijos')
    toursitinerario_ids = fields.One2many('rusia.toursitinerario', 'eventos_id', 'Itinerario del tour')
    gastostoursline_ids = fields.One2many('rusia.gastostoursline', 'eventos_id', 'Gastos Tours')
    message =  fields.Text('Descripcion del tipo de servicio')
    is_padre = fields.Boolean('Es un evento padre')
    ciudad_id = fields.Many2one('rusia.ciudades', 'Ciudad')
    gastos_ids = fields.One2many('rusia.gastos.ciudad', 'evento_id', string="Gastos relacionados")
    is_write = fields.Boolean('Es para escribir')
    hotel = fields.Char("Hotel")
    is_traslado = fields.Boolean("Transporte privado")
    numero_pax = fields.Char("Numero de personas")
    hotel_id = fields.Many2one('rusia.hoteles','Hotel')
    # generar_documentos = fields.Float(compute="get_documentos", store=True)
    tarjeta_usd = fields.Float("Gastos TC USD")
    tarjeta_rub = fields.Float("Gastos TC RUB")
    tarjeta_eur = fields.Float("Gastos TC EUR")
    gasto_rub = fields.Float("Gastos RUB") 
    gasto_usd = fields.Float("Gastos USD")
    gasto_eur = fields.Float("Gastos EUR")
    gasto_paypal = fields.Float("Gastos Paypal") 
    #mientras buscamos e eliminamos
    Total_Gastos = fields.Float("Gastos RUB")
    gastos_reps_ids = fields.One2many('rusia.reps.gastos', 'gasto_evento_id', string='Gastos Reps')
    fecha_padre = fields.Date("Fecha")
    tarjeta_usd_pos = fields.Float("Tarjeta USD")
    tarjeta_eur_pos = fields.Float("Tarjeta EUR")
    


    # @api.onchange('Fecha_Inicio')
    # def _onchange_fecha(self):

    #     print "hora inicio",self.hora_inicio
    #     print "fecha: ",self.Fecha_Inicio

    #     fecha = "12/12/2018 00:00:00"
    #     # formato_fecha = '%Y-%m-%d %H:%M:%S' 
    #     formato_fecha = '%d/%m/%Y %H:%M:%S' 
    #     f_date_b  = datetime.datetime.strptime(fecha, formato_fecha)
    #     self.Fecha_Inicio = f_date_b
    #     print "Fecha nueva: ",f_date_b



    @api.onchange('servicio_id')
    def _onchange_servicio(self):
         self.message = self.servicio_id.Descripcion
         self.hora_inicio = self.servicio_id.Hora_Inicio
         self.hora_final = self.servicio_id.Hora_Finalizar
         self.is_traslado = self.servicio_id.is_traslado
         self.ciudad_id = self.servicio_id.ciudad_id.id
        
        

    @api.model
    def create(self, vals):

        # print "Vals",vals

        if vals['is_padre']:
            print "Estamos en el padre"
            res = super(Eventos, self).create(vals)
            get_gastos_padre = self.get_gastos_padre(res)
        else:
            print "Estamos en hijo"
            res = super(Eventos, self).create(vals)
            campos = self.env['rusia.eventos'].browse(res)
            print "campos",campos.id.evento_id.id
            generamos = self.get_documentos(campos.id.evento_id.id)
            totales = self.get_gastos_hijo(res)
            # gastos_padre = self.get_gastos_padre(campos.id.evento_id)
            gasto_itineraio_padre = self.set_gastos_ciudad_padre(campos.id.evento_id,res,totales)
            sumar_todo_new = self.sumar_gastos_to_padre(campos.id.evento_id,res)
            obtener = self.actualizar_monto_padre(campos.id.evento_id)
            #mandamos la fecha del primer evento hijo al padre
            set_fecha = self.set_fecha(campos.id.evento_id)
        return res

    def set_fecha(self,id_padre):
        print "Entramos al ID padre"

        id_primero = self.env['rusia.eventos'].search([('evento_id', '=', id_padre.id)],order="id asc",limit=1,)
        if id_primero:
            print "Fecha: ",id_primero.Fecha_Inicio

            va = {
                'fecha_padre' : id_primero.Fecha_Inicio
            }
            id_padre.write(va)

        return True




    
    def write(self,vals):

        print "self",self.id
        print "Vals:",vals

        campos = self.env['rusia.eventos'].browse(self.id)

        if campos.is_padre:
            print "Ok, actualizamos todo el show"
            # generamos = self.get_documentos(campos.id)

            res = super(Eventos, self).write(vals)
            if "gastostoursline_ids" in vals:
                get_gastos_padre = self.get_gastos_padre(self)
            else:
                print "no hacemos nada"
            

        else:
            
            res = super(Eventos, self).write(vals)
            campos = self.env['rusia.eventos'].browse(self.id)
            generamos = self.get_documentos(campos.evento_id.id)
            
            #esta "is_write" bandera, es por que se hacia un bulce infinito al escribir a el mismo
            if 'is_write' in vals and vals['is_write']:
                print "no hacemos nada"
            else:
                print "si hacemos algo"
                #sumamos todos los gastos evento hijo, y se lo seteamos al campo 
                gastos_hijo = self.get_gastos_hijo(self)
                #Acutalizamos el gastos line, relacionado a este hijo, por medio de la ciudad y padre, esto solo de la linea invididual
                # actualizar = self.actualizar_gasto_line_padre(self,gastos_hijo)
                #buyscamos todos los hijos para meter la suma general en el padre
                sumar_todo = self.sumar_gastos_to_padre(campos.evento_id,self)
                get_gastos_padre = self.get_gastos_padre(campos.evento_id)
            
            # gastos_padre = self.get_gastos_padre(campos.evento_id)

        return res

    @api.multi
    def unlink(self):

        print "self: ",self.id
        print "self: ",self.is_padre
        hijos_id = self.id
        padre_id = self.evento_id.id
        id_ciudad = self.ciudad_id.id

        if self.is_padre:
            for x in self.env['rusia.eventos'].search([('evento_id', '=', self.id)]):
                x.unlink()
            for y in self.env['rusia.gastos.ciudad'].search([('evento_id', '=', self.id)]):
                for z in self.env['rusia.general'].search([('id_ciudad_gastos', '=', y.id)]):
                    z.unlink()    
                y.unlink()
            
            super(Eventos, self).unlink()
        else:
            print "paso por aqui?"
            super(Eventos, self).unlink()
            print "paso por aqui?2"
            self.sumar_gastos_to_padre_al_eliminar(padre_id,hijos_id,id_ciudad)
            print "paso por aqui?3"
        # return False
        #Si se elimina un evento hijo, igual eliminemos el gastos_line del padre
        # print "id_padre:",self.evento_id.id
        # print "id_ciudad:",self.ciudad_id.id
        #quitamos esto, asi si se limina uno que sea la misma ciudad no hacemos nada mas
        # id_linea_gasto = self.env['rusia.gastos.ciudad'].search([('evento_id', '=', self.evento_id.id),('name','=',self.ciudad_id.id)]).unlink()
        # super(Eventos, self).unlink()
        print "paso por aqui?4"

        
        
        return True

    @api.multi
    def actualizar_monto_padre(self,evento_id):

        #Del evento, padre, buscamos todos los hijos
        #sumamos todos los campos, y se lo insertamos a su costo
        #por itinerario por ciudad

        Total_Pago_Clientes = 0
        Total_Euros = 0
        Total_Usd = 0
        Total_Rub = 0
        Total_Paypal = 0
        Total_Tarjeta = 0
        Total_Representante = 0
        Total_Gastos = 0
        Total_Beneficios = 0
        Total_Pagado_Web = 0
        gasto_rub = 0
        gasto_usd = 0
        gasto_eur = 0
        tarjeta_usd = 0
        tarjeta_rub = 0
        tarjeta_eur = 0
        gasto_paypal = 0
        web_calculos = 0
        web_calculos2 = 0
        web_calculos3 = 0
        tarjeta_usd_pos = 0
        tarjeta_eur_pos = 0


        for x in self.env['rusia.gastos.ciudad'].search([('evento_id', '=', evento_id.id)]):
            # print "X gastos line",x.Total_Gastos
            Total_Pago_Clientes = Total_Pago_Clientes + float(x.Total_Pago_Clientes)
            Total_Euros = Total_Euros + float(x.Total_Euros)
            Total_Usd = Total_Usd + float(x.Total_Usd)
            Total_Rub = Total_Rub + float(x.Total_Rub)
            Total_Paypal = Total_Paypal + float(x.Total_Paypal)
            Total_Tarjeta = Total_Tarjeta + float(x.Total_Tarjeta)
            Total_Beneficios = Total_Beneficios + float(x.Total_Beneficios)
            Total_Pagado_Web = Total_Pagado_Web + float(x.Total_Pagado_Web)
            gasto_rub = gasto_rub + float(x.gasto_rub)
            gasto_usd = gasto_usd + float(x.gasto_usd)
            gasto_eur = gasto_eur + float(x.gasto_eur)
            tarjeta_usd = tarjeta_usd + float(x.tarjeta_usd)
            tarjeta_rub = tarjeta_rub + float(x.tarjeta_rub)
            tarjeta_eur = tarjeta_eur + float(x.tarjeta_eur)
            gasto_paypal = gasto_paypal + float(x.gasto_paypal)
            tarjeta_usd_pos = tarjeta_usd_pos + float(x.tarjeta_usd_pos)
            tarjeta_eur_pos = tarjeta_eur_pos + float(x.tarjeta_eur_pos)



            Total_Representante = Total_Representante + float(x.Total_Representante)
            Total_Gastos = Total_Gastos + float(x.Total_Gastos)
            
            # tarjeta_usd = tarjeta_usd + float(x.tarjeta_usd)
            # tarjeta_rub = tarjeta_rub + float(x.tarjeta_rub)
            # tarjeta_eur = tarjeta_eur + float(x.tarjeta_eur)

            # usd_calculos = float(x.Total_Usd) - float(x.tarjeta_usd)
            # Total_Usd = float(usd_calculos) + float(Total_Usd)

            # rub_calculos = float(x.Total_Rub) - float(x.tarjeta_rub)
            # Total_Rub = float(rub_calculos) + float(Total_Rub)

            # eur_calculos = float(x.Total_Euros) - float(x.tarjeta_eur)
            # Total_Euros = float(eur_calculos) + float(Total_Euros)

            # web_calculos = float(x.Total_Pagado_Web) + float(x.Total_Tarjeta)
            # web_calculos2 = float(web_calculos) - float(x.tarjeta_rub)
            # web_calculos3 = float(web_calculos3) + float(web_calculos2) 




        # paso1 = float(Total_Gastos) + float(Total_Representante)
        # paso2 = float(Total_Rub) - float(paso1)

        vals = {
            "Total_Pago_Clientes" : Total_Pago_Clientes,
            "Total_Euros" : Total_Euros,
            "Total_Usd" : Total_Usd,
            "Total_Rub" : Total_Rub,
            "Total_Paypal" : Total_Paypal,
            "Total_Tarjeta" : Total_Tarjeta,
            "Total_Representante" : Total_Representante,
            "Total_Gastos" : Total_Gastos,
            "Total_Beneficios" : Total_Beneficios,
            "Total_Pagado_Web" : Total_Pagado_Web,
            # "Total_Beneficios" : paso2,
            "gasto_rub" : gasto_rub,
            "gasto_usd" : gasto_usd,
            "gasto_eur" : gasto_eur,
            "tarjeta_usd" : tarjeta_usd,
            "tarjeta_rub" : tarjeta_rub,
            "tarjeta_eur" : tarjeta_eur,
            "gasto_paypal" : gasto_paypal,
            "tarjeta_usd_pos" : tarjeta_usd_pos,
            "tarjeta_eur_pos" : tarjeta_eur_pos,

        }

        evento_id.write(vals)

        return True

    def sumar_gastos_to_padre_al_eliminar(self,id_padre,id_hijo,id_ciudad):
        # print "Hacemos misma dinamica que en documentos, del padre obtenemos todos gastos line"
        #Solo que aqui, solo vamos afectar el campo Total_Gastos del padre

        # print "si llego aqui"


        # return True

        #Esta funcion, es para mandarle a rusia.gastos.ciudad,el monto de total_gastos, y como escribe,
        #igual pasa a su propio write, que es donde actualizo los valores para el costoitinerario genral
        # print "hijo: ",id_hijo
        # print "padrE: ",id_padre

        # return False

        # print "2ciudad del hijo: ",id_hijo.ciudad_id.id
        # print "2 ciudad id ",id_padre.id

        # total_gastos = 0

        # # print "pasamos aqui cuando escrivimos"

        # for x in self.env['rusia.eventos'].search([('evento_id', '=', id_padre),('ciudad_id','=',id_ciudad)]):
        #     print "X gastos line",x.Total_Gastos
        #     total_gastos = total_gastos + float(x.Servicio_Gastos)


        # var = self.env['rusia.gastos.ciudad'].search([('evento_id', '=', id_padre),('name','=',id_ciudad)])    
        # print "varrrrr ",var


        # vals = {
        #     'Total_Gastos' : total_gastos
        # }


        total_gastos = 0
        gasto_rub = 0
        gasto_usd = 0
        gasto_eur = 0
        tarjeta_usd = 0
        tarjeta_rub = 0
        tarjeta_eur = 0
        gasto_paypal = 0

        print "pasamos aqui cuando escribimos"

        for x in self.env['rusia.eventos'].search([('evento_id', '=', id_padre),('ciudad_id','=',id_ciudad)]):
            print "X gastos line",x.Total_Gastos
            total_gastos = total_gastos + float(x.Servicio_Gastos)
            gasto_rub = gasto_rub + float(x.gasto_rub)
            gasto_usd = gasto_usd + float(x.gasto_usd)
            gasto_eur = gasto_eur + float(x.gasto_eur)
            tarjeta_usd = tarjeta_usd + float(x.tarjeta_usd)
            tarjeta_rub = tarjeta_rub + float(x.tarjeta_rub)
            tarjeta_eur = tarjeta_eur + float(x.tarjeta_eur)
            gasto_paypal = gasto_paypal + float(x.gasto_paypal)


        var = self.env['rusia.gastos.ciudad'].search([('evento_id', '=', id_padre),('name','=',id_ciudad)])    
        print "varrrrr ",var


        vals = {
            'Total_Gastos' : total_gastos,
            'gasto_rub' : gasto_rub,
            'gasto_usd' : gasto_usd,
            'gasto_eur' : gasto_eur,
            'tarjeta_usd' : tarjeta_usd,
            'tarjeta_rub' : tarjeta_rub,
            'tarjeta_eur' : tarjeta_eur,
            'gasto_paypal' : gasto_paypal
        }
        
        var.write(vals)

        return True

    def sumar_gastos_to_padre(self,id_padre,id_hijo):   
        #Buscamos del evento padre y ciudad del hijop que coincidad, sumamos todos los campos
        #luego se lo enviamos a rusia.gastos.ciudad, en donde
        #id_padre sea padre y la ciudad, sea del hijo que viene
        

        print "2ciudad del hijo: ",id_hijo.ciudad_id.id
        print "2 ciudad id ",id_padre.id

        total_gastos = 0
        gasto_rub = 0
        gasto_usd = 0
        gasto_eur = 0
        tarjeta_usd = 0
        tarjeta_rub = 0
        tarjeta_eur = 0
        gasto_paypal = 0
        Total_Rub = 0

        total_rep = 0

        print "pasamos aqui cuando escribimos"

        #Este for, es para buscar costos de REPS, de la ciudad que actualmente estamos recorriendo
        #En teoria deberia pasar por todos
        for z in self.env['rusia.reps.gastos'].search([('gasto_evento_id', '=', id_padre.id),('name','=',id_hijo.ciudad_id.id)]):
            total_rep = total_rep + float(z.monto)


        for x in self.env['rusia.eventos'].search([('evento_id', '=', id_padre.id),('ciudad_id','=',id_hijo.ciudad_id.id)]):
            # print "X gastos line",x.Total_Gastos
            total_gastos = total_gastos + float(x.Servicio_Gastos)
            gasto_rub = gasto_rub + float(x.gasto_rub)
            gasto_usd = gasto_usd + float(x.gasto_usd)
            gasto_eur = gasto_eur + float(x.gasto_eur)
            tarjeta_usd = tarjeta_usd + float(x.tarjeta_usd)
            tarjeta_rub = tarjeta_rub + float(x.tarjeta_rub)
            tarjeta_eur = tarjeta_eur + float(x.tarjeta_eur)
            gasto_paypal = gasto_paypal + float(x.gasto_paypal)
            # Total_Rub = Total_Rub + float(x.Total_Rub)


        # print "Total: rep ",total_rep
        # print "gasto rub: ",gasto_rub
        # print "total rub: ",Total_Rub

        # paso1 = float(gasto_rub) + float(total_rep)
        # # paso1 = float(paso1) * -1
        # paso2 = float(Total_Rub) - float(paso1)
        # # self.Total_Beneficios = paso2


        var = self.env['rusia.gastos.ciudad'].search([('evento_id', '=', id_padre.id),('name','=',id_hijo.ciudad_id.id)])    
        print "varrrrr ",var

        paso1 = float(gasto_rub) + float(total_rep)
        # paso1 = float(paso1) * -1
        paso2 = float(var.Total_Rub) - float(paso1)
        # self.Total_Beneficios = paso2


        vals = {
            'Total_Gastos' : total_gastos,
            'gasto_rub' : gasto_rub,
            'gasto_usd' : gasto_usd,
            'gasto_eur' : gasto_eur,
            'tarjeta_usd' : tarjeta_usd,
            'tarjeta_rub' : tarjeta_rub,
            'tarjeta_eur' : tarjeta_eur,
            'gasto_paypal' : gasto_paypal,
            'Total_Representante' : total_rep,
            'Total_Beneficios' : paso2 
        }
        
        var.write(vals)

        return True

    def set_gastos_ciudad_padre(self,id_padre,id_hijo,totales):

        #Aqui validamos si la ciudad ya existe con el padre creado
        #Si no existe un registro, lo creamos y enviamos los valores
        #Si existe, no hacemos nada
        #Ya que en la siguiente funcion, buscamos el monto de todos y se lo seteamos al padre
        print "padre id",id_padre.id
        print "la ciudad",id_hijo.ciudad_id.id



        #para setear el concepto, por que es un servicios
        id_concepto_servicios = self.env['rusia.conceptos.gral'].search([('name', '=', 'Servicios')])
        
        id_linea_gasto = self.env['rusia.gastos.ciudad'].search([('evento_id', '=', id_padre.id),('name','=',id_hijo.ciudad_id.id)])

        if id_linea_gasto:

            print "aqui paso por que"

            return False
        else:
            #creamos el line en rusia.gastos.ciudad, ya que siempre que se haga un hijo, hay que pasar por aqui
            # totales = [gasto_rub,gasto_usd,gasto_eur,tarjeta_usd,tarjeta_rub,tarjeta_eur,gasto_paypal]
            vals = {
                'name' : id_hijo.ciudad_id.id,
                'evento_id' : id_padre.id,
                # 'Total_Gastos' : suma,
                'gasto_rub' : totales[0],
                'gasto_usd' : totales[1],
                'gasto_eur' : totales[2],
                'tarjeta_usd' : totales[3],
                'tarjeta_rub' : totales[4],
                'tarjeta_eur' : totales[5],
                'gasto_paypal' : totales[6],
                'dia' : id_hijo.Fecha_Inicio,
                'concepto_id' : id_concepto_servicios.id
            }
        
            new_line = self.env['rusia.gastos.ciudad'].create(vals)
            return True

    def actualizar_gasto_line_padre(self,id_hijo,suma):
        #Buscamos en rusia.gastos.ciudad, donde padre, ciudad hagan match con la info del hijo
        #y le escribimos la suma de lo que viene en evento hijo

        print "Padre:",id_hijo.evento_id.id
        print "ciudad:",id_hijo.ciudad_id.id

        id_linea_gasto = self.env['rusia.gastos.ciudad'].search([('evento_id', '=', id_hijo.evento_id.id),('name','=',id_hijo.ciudad_id.id)])

        if id_linea_gasto:
            print "linea: ",id_linea_gasto
            vals = {
                'Total_Gastos' : suma
            }
        
            id_linea_gasto.write(vals)
        
        return True     

    def get_gastos_padre(self,id_padre):

        #Como padre ya tiene sus propios gastos, busquemos

        print "***id padre:",id_padre.id

        
        
        #Obtenemos todos los relacionados a rusia.gastostoursline del padre
        #primero buscamos las ciudades

        for ciudades in self.env['rusia.ciudades'].search([]):
            print "Ciudades: ",ciudades.id
            print "Ciudades: ",ciudades.name

            gasto_rub = 0
            gasto_usd = 0
            gasto_eur = 0
            tarjeta_usd = 0
            tarjeta_rub = 0
            tarjeta_eur = 0
            gasto_paypal = 0
            si_hay = False

            #Esta solo es la cantidad del padre
            for x in self.env['rusia.gastostoursline'].search([('eventos_id', '=', id_padre.id),('ciudad_id','=',ciudades.id)]):
                #sumamos
                si_hay = True
                if x.tipo_moneda == "usd":
                    gasto_usd = float(gasto_usd) + float(x.Total)
                if x.tipo_moneda == "eur":
                    gasto_eur = float(gasto_eur) + float(x.Total)
                if x.tipo_moneda == "rub":
                    gasto_rub = float(gasto_rub) + float(x.Total)
                if x.tipo_moneda == "pp":
                    gasto_paypal = float(gasto_paypal) + float(x.Total)
                if x.tipo_moneda == "card":
                    tarjeta_rub = float(tarjeta_rub) + float(x.Total)
                if x.tipo_moneda == "cardusd":
                    tarjeta_usd = float(tarjeta_usd) + float(x.Total) 
                if x.tipo_moneda == "cardeu":
                    tarjeta_eur = float(tarjeta_eur) + float(x.Total) 

                # print "x: ",x.Total
                print "ciudad: ",x.ciudad_id.id
                print "ciudad: ",x.ciudad_id.name
                # suma = suma + float(x.Total)

            #Esta solo es la cantidad de los hijos del padre y donde la ciudad sea la misma
            

            total_gastos2 = 0
            gasto_rub2 = 0
            gasto_usd2 = 0
            gasto_eur2 = 0
            tarjeta_usd2 = 0
            tarjeta_rub2 = 0
            tarjeta_eur2 = 0
            gasto_paypal2 = 0


            for m in self.env['rusia.eventos'].search([('evento_id', '=', id_padre.id),('ciudad_id','=',ciudades.id)]):
                # print "X gastos line",x.Total_Gastos
                total_gastos2 = total_gastos2 + float(m.Servicio_Gastos)
                gasto_rub2 = gasto_rub2 + float(m.gasto_rub)
                gasto_usd2 = gasto_usd2 + float(m.gasto_usd)
                gasto_eur2 = gasto_eur2 + float(m.gasto_eur)
                tarjeta_usd2 = tarjeta_usd2 + float(m.tarjeta_usd)
                tarjeta_rub2 = tarjeta_rub2 + float(m.tarjeta_rub)
                tarjeta_eur2 = tarjeta_eur2 + float(m.tarjeta_eur)
                gasto_paypal2 = gasto_paypal2 + float(m.gasto_paypal)
                # Total_Rub = Total_Rub + float(x.Total_Rub)

            if si_hay:

                print "gasto_rub: ",gasto_rub
                print "gasto_usd: ",gasto_usd
                print "gasto_eur: ",gasto_eur
                print "tarjeta_usd: ",tarjeta_usd
                print "tarjeta_rub: ",tarjeta_rub
                print "tarjeta_eur: ",tarjeta_eur
                print "gasto_paypal: ",gasto_paypal

                #Ahora de aqui, obtenemos los campos de rusia.gastos.ciudad donde:
                #ciudad sea la misma y evento sea el padre evento_id 
                #Sumamos estas cantidades a lo que venga y le volvemos a escribir
                #name, evento_id
                gasto_ciudad = self.env['rusia.gastos.ciudad'].search([('evento_id', '=', id_padre.id),('name','=',ciudades.id)])
                print "***Gasto ciudad ",gasto_ciudad.id

                gasto_rub = float(gasto_rub2) + gasto_rub
                gasto_usd = float(gasto_usd2) + gasto_usd
                gasto_eur = float(gasto_eur2) + gasto_eur
                tarjeta_usd = float(tarjeta_usd2) + tarjeta_usd
                tarjeta_rub = float(tarjeta_rub2) + tarjeta_rub
                tarjeta_eur = float(tarjeta_eur2) + tarjeta_eur
                gasto_paypal = float(gasto_paypal2) + gasto_paypal

                vals2 = {
                    "gasto_rub" : gasto_rub,
                    "gasto_usd" : gasto_usd,
                    "gasto_eur" : gasto_eur,
                    "tarjeta_usd" : tarjeta_usd,
                    "tarjeta_rub" : tarjeta_rub,
                    "tarjeta_eur" : tarjeta_eur,
                    "gasto_paypal" : gasto_paypal,
                }

                print "valores 2",vals2

                gasto_ciudad.write(vals2)




        # print "Obtenemos todos los hijos del padre el campo Servicio_Gastos"
        # suma = 0
        # for x in self.env['rusia.eventos'].search([('evento_id', '=', id_padre.id)]):
        #     #sumamos
        #     print "x: ",x.Servicio_Gastos
        #     suma = suma + float(x.Servicio_Gastos)

        # vals_padre_write = {
        #     'Total_Gastos': suma
        # }

        # id_padre.write(vals_padre_write)


        return True



    def get_gastos_hijo(self,id_hijo):


        #Esta funcion sirve, para buscar todos los gastos_line,de hijo,y por cada tipo
        #de moneda, se le va sumando al campo correspondiente, y luego
        #el valor se le asigna al campo corrrespondiente

        print "Pasamos al hijo"
        print "Id hijo:",id_hijo

        totales = []

        gasto_rub = 0
        gasto_usd = 0
        gasto_eur = 0
        tarjeta_usd = 0
        tarjeta_rub = 0
        tarjeta_eur = 0
        gasto_paypal = 0
        
        #Obtenemos todos los relacionados a rusia.gastostoursline del hijo
        suma = 0
        for x in self.env['rusia.gastostoursline'].search([('eventos_id', '=', id_hijo.id)]):
            #sumamos
            if x.tipo_moneda == "usd":
                gasto_usd = float(gasto_usd) + float(x.Total)
            if x.tipo_moneda == "eur":
                gasto_eur = float(gasto_eur) + float(x.Total)
            if x.tipo_moneda == "rub":
                gasto_rub = float(gasto_rub) + float(x.Total)
            if x.tipo_moneda == "pp":
                gasto_paypal = float(gasto_paypal) + float(x.Total)
            if x.tipo_moneda == "card":
                tarjeta_rub = float(tarjeta_rub) + float(x.Total)
            if x.tipo_moneda == "cardusd":
                tarjeta_usd = float(tarjeta_usd) + float(x.Total) 
            if x.tipo_moneda == "cardeu":
                tarjeta_eur = float(tarjeta_eur) + float(x.Total) 

            print "x: ",x.Total
            suma = suma + float(x.Total)


        print "la suma:",suma

        #Escribimos en el hijo en el campo el valor Servicio_Gastos
        vals_hijo_write = {
            'Servicio_Gastos': suma,
            'gasto_rub' : gasto_rub,
            'gasto_usd' : gasto_usd,
            'gasto_eur' : gasto_eur,
            'tarjeta_usd' : tarjeta_usd,
            'tarjeta_rub' : tarjeta_rub,
            'tarjeta_eur' : tarjeta_eur,
            'gasto_paypal' : gasto_paypal,
            'is_write' : True
        }


        id_hijo.write(vals_hijo_write)
        totales = [gasto_rub,gasto_usd,gasto_eur,tarjeta_usd,tarjeta_rub,tarjeta_eur,gasto_paypal]
        return totales


    def get_documentos(self,id_padre):

       
        self.generar_documentos = True


        print "Obtener documentos"
        print "Yo el ID activo: ",id_padre
        #Eliminamos todos los registro del padre de ir.attachment, para que no se dupliquen
        self.env['ir.attachment'].search([('eventos_id', '=', id_padre)]).unlink()

        #1. obtenemos los hijos

        hijos_id = []

        for x in self.env['rusia.eventos'].search([('evento_id','=',id_padre)]):
            hijos_id.append(x.id)
        
        print "hijos:",hijos_id

        lista_nuevos = []

        # documentos_hijos = self.env['ir.attachment'].search([('eventos_id','in',hijos_id)])
        for y in self.env['ir.attachment'].search([('eventos_id','in',hijos_id)]):
            print "Y: ",y.id



            campos = self.env['ir.attachment'].browse(y.id)

            # print "campos: ",campos.db_datas
            # print "campos: ",campos.type
            # print "campos: ",campos.public
            # print "campos: ",campos.mimetype
            # print "campos: ",campos.name
            # print "campos: ",campos.eventos_i
            # print "campos: ",campos.Tipo_Documento

            valores_documentos = {
                'db_datas' : campos.db_datas,
                'type' : campos.type,
                'public' : campos.public,
                'mimetype' : campos.mimetype,
                'name' : campos.name,
                'Tipo_Documento' : campos.Tipo_Documento,
                'eventos_id' : id_padre
            }

            # print "valores_documentos",valores_documentos

            new_document = self.env['ir.attachment'].create(valores_documentos)

            # lista_nuevos.append(new_document)

            # vals_padre_write = {
            #     'documentos_ids': lista_nuevos
            # }


            # obtenemos_nuevamente_wtf = self.env['rusia.eventos'].search([('id', '=', self.id)])

            # obtenemos_nuevamente_wtf.write(vals_padre_write)


            # new_id = self.env['ir.attachment'].copy(y.id)

            # print "nuevo id de documento: ",new_id

        # print "documentos hijos: ",documentos_hijos
        return True


        



# Modelo Rusia.Tours.Pasajeros

# class ToursPasajeros(models.Model):
#     _name = 'rusia.tourspasajeros'

#     name = fields.Char(string="Nombre Pax")
#     Email = fields.Char()
#     Telefono = fields.Char()
#     Nombre_Hotel = fields.Char()
#     No_Personas = fields.Float()
#     administrador_id = fields.Many2one('res.users', 'Administrador')
#     Observaciones = fields.Text()
#     eventos_id = fields.Many2one('rusia.eventos', ondelete="set null", string="Evento", index=True)
#     pasajeros_ids = fields.One2many('rusia.eventos', 'Datos_Cliente_id', string="Evento")

# Modelo Rusia.Tipo.Servicios

class TipoServicios(models.Model):
    _name = 'rusia.tiposervicios'

    name = fields.Char()
    Code = fields.Char()
    # Ciudad = fields.Char()
    Hora_Inicio = fields.Char()
    Hora_Finalizar = fields.Char()
    Descripcion = fields.Text()
    is_traslado = fields.Boolean("Transporte privado")
    ciudad_id = fields.Many2one('rusia.ciudades', 'Ciudad')



# Modelo Rusia.Tours.Itinerario


class ToursItinerario(models.Model):
    _name = 'rusia.toursitinerario'

    name = fields.Char()
    Descripcion_General = fields.Text()
    Regreso = fields.Char()
    toursitinerarioline_ids = fields.One2many('rusia.toursitinerarioline', 'itinerario_id', 'Puntos')
    eventos_id = fields.Many2one('rusia.eventos', ondelete="set null", string="Itinerario del tour", index=True)


# Modelo Rusia.Tours.Itinerario.Line


class ToursItinerarioLine(models.Model):
    _name = 'rusia.toursitinerarioline'

    name = fields.Char()
    itinerario_id = fields.Many2one('rusia.toursitinerario', ondelete="set null", string="Itinerario del tour", index=True)

class Documentos(models.Model):
    # _name = 'rusia.documentos'

    _inherit = 'ir.attachment'

    eventos_id = fields.Many2one('rusia.eventos','Tour')
    eventos_cliente_id = fields.Many2one('rusia.eventos','Tour')
    Tipo_Documento = fields.Char()
    Descargar = fields.Boolean(default=False)

class TipoPagos(models.Model):
    _name = 'rusia.tipopagos'

    name = fields.Char(string="Tipo de pago")

# Modelo Rusia.Gastos.Tours

class GastosTours(models.Model):
    _name = 'rusia.gastostours'

    name = fields.Char()
    # Dia = fields.Float()
    # Total = fields.Float()
    eventos_id = fields.Many2one('rusia.eventos', 'Tours')
    # tipopago_id = fields.Many2one('rusia.tipopagos', 'Tipo de pago')
    # tiposervicios_id = fields.Many2one('rusia.tiposervicios', 'Nombre del tour')
    gastos_tours_line_ids = fields.One2many('rusia.gastostoursline', 'concepto_gasto_id', 'Historial Gastos de Concepto')




class GastosToursLine(models.Model):
    _name = 'rusia.gastostoursline'

    name = fields.Many2one('rusia.gastostours', 'Nombre')
    concepto_gasto_id = fields.Many2one('rusia.gastostours', 'Concepto de Gasto',required = True)
    Tipo_Pago = fields.Many2one('rusia.tipopagos', 'Tipo de pago')
    Total = fields.Float('Total',required = True)
    eventos_id = fields.Many2one('rusia.eventos', 'Gastos Tours')
    usuario_id = fields.Many2one('res.users', 'Usuario')
    evento_padre = fields.Char("Evento Padre")
    fecha = fields.Date('Fecha')
    tipo_moneda = fields.Selection([('usd','USD'),('eur','EUR'),('rub','RUB'),('pp','PayPal'),('card','Tarjeta RUB'),('cardeu','Tarjeta EUR'),('cardusd','Tarjeta USD')],'Moneda',required = True)
    observaciones = fields.Text('Observaciones')
    ciudad_id = fields.Many2one('rusia.ciudades', 'Ciudad')
    pagado = fields.Boolean('Pagado')

class RusiaUsuarios(models.Model):
    _inherit = 'res.users'

    gastos_users_ids = fields.One2many('rusia.gastostoursline', 'usuario_id', 'Historial Salarios')  
    is_chofer = fields.Boolean("Chofer")
    is_guia = fields.Boolean("Guia")
    is_rep = fields.Boolean("REP")
    is_client = fields.Boolean("Cliente")
    eventos_ids = fields.One2many('rusia.eventos', 'Datos_Cliente_id', string="Historial de Evento")
    tipo_usuario = fields.Char('Es Cliente')
    reps_gastos_ids = fields.One2many('rusia.reps.gastos','usuario_id','Historial Nomina REP')



    @api.model
    def create(self,vals):


        model_data = self.buscar_res_data_grupos()
        print "model data",model_data

        is_chofer =  False
        is_guia =  False
        is_rep =  False
        is_client =  False

        tipo_usuario = ""
        
        if vals.has_key('groups_id'):
            print "entro"
            if model_data[0] in vals['groups_id'][0][2]:
                is_chofer = True
                print "Chofer"
            if model_data[1] in vals['groups_id'][0][2]:
                is_guia = True
                print "Guia"
            if model_data[2] in vals['groups_id'][0][2]:
                is_rep = True
                print "rep"
            if model_data[3] in vals['groups_id'][0][2]:
                is_client = True  
                tipo_usuario = "Cliente"  
                print "Cliente"
        else:
            print "no entro"

        vals['is_chofer'] = is_chofer
        vals['is_guia'] = is_guia
        vals['is_rep'] = is_rep
        vals['is_client'] = is_client
        vals['tipo_usuario'] = tipo_usuario
        
        print "Valores: ",vals

        res = super(RusiaUsuarios, self).create(vals)

        return res

    def write(self,vals):
       
        model_data = self.buscar_res_data_grupos()
        print "model data",model_data

        
        is_chofer =  False
        is_guia =  False
        is_rep =  False
        is_client =  False
        tipo_usuario = ""

        
        if vals.has_key('groups_id'):
            print "entro"
            if model_data[0] in vals['groups_id'][0][2]:
                is_chofer = True
            else:
                is_chofer = False
                print "Chofer"

            if model_data[1] in vals['groups_id'][0][2]:
                is_guia = True
            else:
                is_guia = False
                print "Guia"

            if model_data[2] in vals['groups_id'][0][2]:
                is_rep = True
            else:
                is_rep = False
                print "rep"

            if model_data[3] in vals['groups_id'][0][2]:
                is_client = True
                tipo_usuario = "Cliente"

            else:
                is_client = False
                tipo_usuario = ""
                print "Cliente"
        else:
            print "no entro"

        vals['is_chofer'] = is_chofer
        vals['is_guia'] = is_guia
        vals['is_rep'] = is_rep
        vals['is_client'] = is_client
        vals['tipo_usuario'] = tipo_usuario

        
        res = super(RusiaUsuarios, self).write(vals)
        return res
        

        #Buscamos en ir.model.data el valor de los permisos
        #guia,chofer,cliente,representantes,

    def buscar_res_data_grupos(self):

        chofer = self.env['ir.model.data'].search([('model', '=','res.groups'),('module','=','rusia'),('name','=','group_check_chofer')])
        print "Res chofer: ",chofer.res_id

        guia = self.env['ir.model.data'].search([('model', '=','res.groups'),('module','=','rusia'),('name','=','group_check_guia')])
        print "Res guia: ",guia.res_id

        rep = self.env['ir.model.data'].search([('model', '=','res.groups'),('module','=','rusia'),('name','=','group_check_representante')])
        print "Res REP: ",rep.res_id

        cliente = self.env['ir.model.data'].search([('model', '=','res.groups'),('module','=','rusia'),('name','=','group_check_Cliente')])
        print "Res Cliente: ",cliente.res_id

        lista_res = [chofer.res_id,guia.res_id,rep.res_id,cliente.res_id]

        return lista_res




class RusiaGastosExtras(models.Model):
    _name = 'rusia.gastos.extras'

    name = fields.Many2one('rusia.conceptos.gral','Concepto')
    # name = fields.Char('Concepto')
    fecha = fields.Date('Fecha')
    # tipo_moneda = fields.Many2one('rusia.tipopagos', 'Moneda')
    tipo_moneda = fields.Selection([('usd','USD'),('eur','EUR'),('rub','RUB'),('pp','PayPal'),('card','Tarjeta RUB'),('cardeu','Tarjeta EUR'),('cardusd','Tarjeta USD')],'Moneda')
    monto = fields.Float('Monto')
    observaciones = fields.Text('Observaciones')
    Tipo_Pago = fields.Many2one('rusia.tipopagos', 'Tipo de pago')
    ciudad_id = fields.Many2one('rusia.ciudades','Ciudad')

    @api.model
    def create(self,vals):
        print "Pasamos al crear un gasto extra"


        tarjeta_usd = 0
        tarjeta_rub = 0
        tarjeta_eur = 0
        gasto_rub = 0
        gasto_usd = 0
        gasto_eur = 0
        gasto_paypal = 0

        if vals['tipo_moneda'] == 'usd':
            tarjeta_usd = float(vals['monto'])
        if vals['tipo_moneda'] == 'eur':
            gasto_eur = float(vals['monto'])
        if vals['tipo_moneda'] == 'rub':
            gasto_rub = float(vals['monto'])
        if vals['tipo_moneda'] == 'pp':
            gasto_paypal = float(vals['monto'])
        if vals['tipo_moneda'] == 'pp':
            gasto_paypal = float(vals['monto'])
        if vals['tipo_moneda'] == 'card':
            tarjeta_rub = float(vals['monto'])
        if vals['tipo_moneda'] == 'cardeu':
            tarjeta_eur = float(vals['monto'])
        if vals['tipo_moneda'] == 'cardusd':
            tarjeta_usd = float(vals['monto'])

        res = super(RusiaGastosExtras, self).create(vals)

        vals2 = {
            'tarjeta_usd' : tarjeta_usd,
            'tarjeta_rub' : tarjeta_rub,
            'tarjeta_eur' : tarjeta_eur,
            'gasto_rub' : gasto_rub,
            'gasto_usd' : gasto_usd,
            'gasto_eur' : gasto_eur,
            'gasto_paypal' : gasto_paypal,
            'gastos_id' : res,
            'dia' : vals['fecha'],
            'name' : vals['ciudad_id'],
            'concepto_id' : vals['name'],
        }

        print "Vals2: ",vals2

        self.env['rusia.gastos.ciudad'].create(vals2)


        return res


class RusiaGastosExtras(models.Model):
    _name = 'rusia.ganancias.totales'

    def a_fun(self):
        id_concepto_servicios = self.env['rusia.conceptos.gral'].search([('name', '=', 'Ganancia')])
        return id_concepto_servicios.id


    # name = fields.Many2one('rusia.conceptos.gral','Concepto')
    name = fields.Many2one('rusia.conceptos.gral',default=a_fun)
    # name = fields.Char('Concepto')
    fecha = fields.Date('Fecha')
    # tipo_moneda = fields.Many2one('rusia.tipopagos', 'Moneda')
    tipo_moneda = fields.Selection([('usd','USD'),('eur','EUR'),('rub','RUB'),('pp','PayPal'),('card','Tarjeta RUB'),('cardeu','Tarjeta EUR'),('cardusd','Tarjeta USD')],'Moneda')
    monto = fields.Float('Monto')
    observaciones = fields.Text('Observaciones')
    Tipo_Pago = fields.Many2one('rusia.tipopagos', 'Tipo de pago')
    ciudad_id = fields.Many2one('rusia.ciudades','Ciudad')

    @api.model
    def create(self,vals):
        print "Pasamos al crear un gasto extra"


        tarjeta_usd = 0
        tarjeta_rub = 0
        tarjeta_eur = 0
        gasto_rub = 0
        gasto_usd = 0
        gasto_eur = 0
        gasto_paypal = 0

        if vals['tipo_moneda'] == 'usd':
            tarjeta_usd = float(vals['monto'])
        if vals['tipo_moneda'] == 'eur':
            gasto_eur = float(vals['monto'])
        if vals['tipo_moneda'] == 'rub':
            gasto_rub = float(vals['monto'])
        if vals['tipo_moneda'] == 'pp':
            gasto_paypal = float(vals['monto'])
        if vals['tipo_moneda'] == 'pp':
            gasto_paypal = float(vals['monto'])
        if vals['tipo_moneda'] == 'card':
            tarjeta_rub = float(vals['monto'])
        if vals['tipo_moneda'] == 'cardeu':
            tarjeta_eur = float(vals['monto'])
        if vals['tipo_moneda'] == 'cardusd':
            tarjeta_usd = float(vals['monto'])

        res = super(RusiaGastosExtras, self).create(vals)

        vals2 = {
            'tarjeta_usd' : tarjeta_usd,
            'tarjeta_rub' : tarjeta_rub,
            'tarjeta_eur' : tarjeta_eur,
            'gasto_rub' : gasto_rub,
            'gasto_usd' : gasto_usd,
            'gasto_eur' : gasto_eur,
            'gasto_paypal' : gasto_paypal,
            'gastos_id' : res,
            'dia' : vals['fecha'],
            'name' : vals['ciudad_id'],
            'concepto_id' : vals['name'],
        }

        print "Vals2: ",vals2

        self.env['rusia.gastos.ciudad'].create(vals2)


        return res



class RusiaGastosConceptos(models.Model):
    _name = 'rusia.gastos.concepto'

    name = fields.Char('Nombre Concepto')
    # conceptos_beneficios_ids = One2many('rusia.beneficios','name',string="Historial")
    gastos_ids = fields.One2many('rusia.gastos.extras', 'name', string="Gastos relacionados")


class RusiaConceptosGral(models.Model):
    _name = 'rusia.conceptos.gral'

    name = fields.Char('Nombre Concepto')
    # conceptos_beneficios_ids = One2many('rusia.beneficios','name',string="Historial")
    # gastos_ids = fields.One2many('rusia.gastos.extras', 'name', string="Gastos relacionados")




class RusiaBeneficios(models.Model):
    _name = 'rusia.beneficios'

    name = fields.Many2one('rusia.conceptos.gral','Concepto')
    # name = fields.Char('Concepto')
    fecha = fields.Date('Fecha')
    # tipo_moneda = fields.Many2one('rusia.tipopagos', 'Moneda')
    tipo_moneda = fields.Selection([('usd','USD'),('eur','EUR'),('rub','RUB'),('pp','PayPal'),('card','Tarjeta RUB'),('cardeu','Tarjeta EUR'),('cardusd','Tarjeta USD')],'Moneda')
    monto = fields.Float('Monto')
    observaciones = fields.Text('Observaciones')
    Tipo_Pago = fields.Many2one('rusia.tipopagos', 'Tipo de pago')
    ciudad_id = fields.Many2one('rusia.ciudades','Ciudad')

    @api.model
    def create(self,vals):
        print "Pasamos al crear un gasto extra"


        tarjeta_usd = 0
        tarjeta_rub = 0
        tarjeta_eur = 0
        gasto_rub = 0
        gasto_usd = 0
        gasto_eur = 0
        gasto_paypal = 0

        if vals['tipo_moneda'] == 'usd':
            tarjeta_usd = float(vals['monto'])
        if vals['tipo_moneda'] == 'eur':
            gasto_eur = float(vals['monto'])
        if vals['tipo_moneda'] == 'rub':
            gasto_rub = float(vals['monto'])
        if vals['tipo_moneda'] == 'pp':
            gasto_paypal = float(vals['monto'])
        if vals['tipo_moneda'] == 'pp':
            gasto_paypal = float(vals['monto'])
        if vals['tipo_moneda'] == 'card':
            tarjeta_rub = float(vals['monto'])
        if vals['tipo_moneda'] == 'cardeu':
            tarjeta_eur = float(vals['monto'])
        if vals['tipo_moneda'] == 'cardusd':
            tarjeta_usd = float(vals['monto'])

        res = super(RusiaBeneficios, self).create(vals)

        vals2 = {
            'tarjeta_usd_pos' : tarjeta_usd,
            'Total_Tarjeta' : tarjeta_rub,
            'tarjeta_eur_pos' : tarjeta_eur,
            'Total_Rub' : gasto_rub,
            'Total_Euros' : gasto_usd,
            'Total_Euros' : gasto_eur,
            'Total_Paypal' : gasto_paypal,
            'beneficios_id' : res,
            'dia' : vals['fecha'],
            'name' : vals['ciudad_id']
        }

        print "Vals2: ",vals2

        self.env['rusia.gastos.ciudad'].create(vals2)


        return res

class RusiaBeneficiosConceptos(models.Model):
    _name = 'rusia.beneficios.concepto'

    name = fields.Char('Nombre Concepto')
    # conceptos_beneficios_ids = One2many('rusia.beneficios','name',string="Historial")
    beneficios_ids = fields.One2many('rusia.beneficios', 'name', string="Beneficios relacionados")



class RusiaGananciasGenerales(models.Model):
    _name = 'rusia.gananciasgenerales'

    name = fields.Char('Nombre')
    Total_Paypal = fields.Float('Total PayPal')
    Total_Pax = fields.Char('Total Pax')
    Total_Tarjeta = fields.Float('Total Tarjeta')
    Total_Usd = fields.Float('Total USD')
    Total_Rub = fields.Float('Total RUB')
    Total_Euros = fields.Float('Total EUR')
    Dia = fields.Date('Día')
    ciudad_id = fields.Many2one('rusia.ciudades', 'Ciudad')

class RusiaGeneral(models.Model):
    _name = 'rusia.general'

    name = fields.Char('Nombre')
    concepto_id = fields.Many2one('rusia.conceptos.gral','Concepto')
    fecha = fields.Date('Fecha')
    ciudad_id = fields.Many2one('rusia.ciudades','Ciudad')
    rublos = fields.Float("Rublos")
    euros = fields.Float("Euros")
    usd = fields.Float("USD")
    tc_rub = fields.Float("Tarjeta RUB")
    tc_eur = fields.Float("Tarjeta Euro")
    tc_usd = fields.Float("Tarjeta USD")
    tarjeta_pp = fields.Float("Paypal")
    id_ciudad_gastos = fields.Float()
    
    # Paxs_Pago = fields.Float('Paxs pago')
    # Paxs_Terceros = fields.Float('Paxs terceros')
    # Paxs_All_Included = fields.Float('Paxs todo incluido')
    # Paypal = fields.Float('PayPal')
    # Total_Paxs = fields.Char('Total Paxs')
    # Total_Tarjeta = fields.Float('Total Tarjeta')
    # Usd = fields.Float('USD')
    # Rub = fields.Float('RUB')
    # Euros = fields.Float('EUR')
    # Usd_Reserva = fields.Float('USD Reserva')
    # Rub_Reserva = fields.Float('RUB Reserva')
    # Euros_Reserva = fields.Float('EUR Reserva')
    # Dia = fields.Date('Día')
    # ciudad_id = fields.Many2one('rusia.ciudades', 'Ciudad')
    # tour_id = fields.Many2one('rusia.eventos', 'Tour')

class GastosporCiudad(models.Model):
    _name = 'rusia.gastos.ciudad'


    # @api.multi
    # def unlink(self):
    #     print "unlink de gastos line"
    #     print "Padre: ",self.evento_id
    #     id_padre = self.evento_id

    #     for x in self:
    #         print "X",x.id_padre

    #         super(GastosporCiudad, self).unlink()

    #         actualizar = self.actualizar_monto_padre(id_padre)

        # return True
    @api.model
    def create(self,vals):

        print "Valores: ",vals

        res = super(GastosporCiudad, self).create(vals)

        tipo = True
        crear = self.crear_actualizar_gral(res,tipo)
        
        return res

    def crear_actualizar_gral(self,res,tipo):
        print "Nuevo id:",res.id
        print "concepto id:",res.concepto_id.id
        print "Fecha: ",res.dia
        print "Ciudad: ",res.name.id

        rublos = 0
        rublos1 = 0
        total_rublos = res.Total_Rub
        total_rep = res.Total_Representante
        total_gasto_rub = res.gasto_rub
        rublos = float(total_rep) + float(total_gasto_rub)
        rublos1 = float(total_rublos) - float(rublos)
        print "Total rublos generl: ",rublos1

        euros = 0
        total_euros = res.Total_Euros
        gastos_euros = res.gasto_eur
        euro = float(total_euros) - float(gastos_euros)
        print "Total euros general: ",euro

        usd = 0
        usd = float(res.Total_Usd) - float(res.gasto_usd)
        print "usd general: ",usd

        tarjeta_rub = 0
        tarjeta_rub1 = 0
        tarjeta_rub = float(res.Total_Pagado_Web) + float(res.Total_Tarjeta)
        tarjeta_rub1 = tarjeta_rub - float(res.tarjeta_rub)
        print "Tarjeta rub general: ",tarjeta_rub1

        tarjeta_euros = float(res.tarjeta_eur_pos) - float(res.tarjeta_eur)
        print "tc eur gral: ",tarjeta_euros

        tarjeta_usd = float(res.tarjeta_usd_pos) - float(res.tarjeta_usd)
        print "tc usd: ",tarjeta_usd

        paypal = float(res.Total_Paypal) - float(res.gasto_paypal)
        print "total paypal gral: ",paypal

        #De todos estos valores, creamos el registro

        vals_gral = {

            'concepto_id' : res.concepto_id.id,
            'fecha' : res.dia,
            'ciudad_id' : res.name.id,
            'rublos' : rublos1,
            'euros' : euro,
            'usd' : usd,
            'tc_rub' : tarjeta_rub1,
            'tc_eur' : tarjeta_euros,
            'tc_usd' : tarjeta_usd,
            'tarjeta_pp' : paypal,
            'id_ciudad_gastos' : res.id,

        }

        if tipo:
            self.env['rusia.general'].create(vals_gral)
        else:
            #buscamos elid, de este registro en rusia.general
            #y escribimos
            id_busqueda = self.env['rusia.general'].search([('id_ciudad_gastos', '=',res.id)])

            a = id_busqueda.write(vals_gral)

        return True
        #buscamos de este nuevo id, todos los campos, y hacemos los calculos para escribir en rusia.general


    def write(self,vals):
        print "Entramos al write de lkos gastos line"
        print "Vals:",vals
        print "Padre: ",self.evento_id

        #primero dejamos que se actualice
        res = super(GastosporCiudad, self).write(vals)

        print "****self id: ",self.id

        tipo = False
        id_yo = self.env['rusia.gastos.ciudad'].search([('id', '=',self.id)])
        actualizar = self.crear_actualizar_gral(id_yo,tipo)

        #misma dinamica, del id padre buscamos todos los campos, sumamos y escribimos en padre
        actualizar = self.actualizar_monto_padre(self.evento_id)

    @api.onchange('Total_Representante','gasto_rub','Total_Rub')
    def _calcular_beneficio_ciudad(self):
        paso1 = float(self.gasto_rub) + float(self.Total_Representante)
        paso2 = float(self.Total_Rub) - float(paso1)
        self.Total_Beneficios = paso2

    @api.multi
    def actualizar_monto_padre(self,evento_id):
        #Del evento, padre, buscamos todos los hijos
        #sumamos todos los campos, y se lo insertamos a su costo
        #por itinerario por ciudad

        Total_Pago_Clientes = 0
        Total_Euros = 0
        Total_Usd = 0
        Total_Rub = 0
        Total_Paypal = 0
        Total_Tarjeta = 0
        Total_Representante = 0
        Total_Gastos = 0
        Total_Beneficios = 0
        Total_Pagado_Web = 0
        gasto_rub = 0
        gasto_usd = 0
        gasto_eur = 0
        tarjeta_usd = 0
        tarjeta_rub = 0
        tarjeta_eur = 0
        gasto_paypal = 0
        web_calculos = 0
        web_calculos2 = 0
        web_calculos3 = 0
        tarjeta_usd_pos = 0
        tarjeta_eur_pos = 0


        for x in self.env['rusia.gastos.ciudad'].search([('evento_id', '=', evento_id.id)]):
            # print "X gastos line",x.Total_Gastos
            Total_Pago_Clientes = Total_Pago_Clientes + float(x.Total_Pago_Clientes)
            Total_Euros = Total_Euros + float(x.Total_Euros)
            Total_Usd = Total_Usd + float(x.Total_Usd)
            Total_Rub = Total_Rub + float(x.Total_Rub)
            Total_Paypal = Total_Paypal + float(x.Total_Paypal)
            Total_Tarjeta = Total_Tarjeta + float(x.Total_Tarjeta)
            Total_Beneficios = Total_Beneficios + float(x.Total_Beneficios)
            Total_Pagado_Web = Total_Pagado_Web + float(x.Total_Pagado_Web)
            gasto_rub = gasto_rub + float(x.gasto_rub)
            gasto_usd = gasto_usd + float(x.gasto_usd)
            gasto_eur = gasto_eur + float(x.gasto_eur)
            tarjeta_usd = tarjeta_usd + float(x.tarjeta_usd)
            tarjeta_rub = tarjeta_rub + float(x.tarjeta_rub)
            tarjeta_eur = tarjeta_eur + float(x.tarjeta_eur)
            gasto_paypal = gasto_paypal + float(x.gasto_paypal)
            tarjeta_usd_pos = tarjeta_usd_pos + float(x.tarjeta_usd_pos)
            tarjeta_eur_pos = tarjeta_eur_pos + float(x.tarjeta_eur_pos)



            Total_Representante = Total_Representante + float(x.Total_Representante)
            Total_Gastos = Total_Gastos + float(x.Total_Gastos)
            
            # tarjeta_usd = tarjeta_usd + float(x.tarjeta_usd)
            # tarjeta_rub = tarjeta_rub + float(x.tarjeta_rub)
            # tarjeta_eur = tarjeta_eur + float(x.tarjeta_eur)

            # usd_calculos = float(x.Total_Usd) - float(x.tarjeta_usd)
            # Total_Usd = float(usd_calculos) + float(Total_Usd)

            # rub_calculos = float(x.Total_Rub) - float(x.tarjeta_rub)
            # Total_Rub = float(rub_calculos) + float(Total_Rub)

            # eur_calculos = float(x.Total_Euros) - float(x.tarjeta_eur)
            # Total_Euros = float(eur_calculos) + float(Total_Euros)

            # web_calculos = float(x.Total_Pagado_Web) + float(x.Total_Tarjeta)
            # web_calculos2 = float(web_calculos) - float(x.tarjeta_rub)
            # web_calculos3 = float(web_calculos3) + float(web_calculos2) 




        # paso1 = float(Total_Gastos) + float(Total_Representante)
        # paso2 = float(Total_Rub) - float(paso1)

        vals = {
            "Total_Pago_Clientes" : Total_Pago_Clientes,
            "Total_Euros" : Total_Euros,
            "Total_Usd" : Total_Usd,
            "Total_Rub" : Total_Rub,
            "Total_Paypal" : Total_Paypal,
            "Total_Tarjeta" : Total_Tarjeta,
            "Total_Representante" : Total_Representante,
            "Total_Gastos" : Total_Gastos,
            "Total_Beneficios" : Total_Beneficios,
            "Total_Pagado_Web" : Total_Pagado_Web,
            # "Total_Beneficios" : paso2,
            "gasto_rub" : gasto_rub,
            "gasto_usd" : gasto_usd,
            "gasto_eur" : gasto_eur,
            "tarjeta_usd" : tarjeta_usd,
            "tarjeta_rub" : tarjeta_rub,
            "tarjeta_eur" : tarjeta_eur,
            "gasto_paypal" : gasto_paypal,
            "tarjeta_usd_pos" : tarjeta_usd_pos,
            "tarjeta_eur_pos" : tarjeta_eur_pos,

        }

        evento_id.write(vals)

        return True



    Total_Pago_Clientes = fields.Float("Total pago clientes")
    Total_Pagado_Web = fields.Float("Total pagado en web")
    Total_Euros = fields.Float("Total EUR")
    Total_Usd = fields.Float("Total USD")
    Total_Rub = fields.Float("Total RUB")
    Total_Paypal = fields.Float("Total PayPal")
    Total_Tarjeta = fields.Float("Total Tarjeta RUB")
    Total_Representante = fields.Float("Total representante")
    Total_Gastos = fields.Float("Total Gastos")
    Total_Beneficios = fields.Float("Restante RUB")
    name = fields.Many2one('rusia.ciudades', 'Ciudad')
    evento_id = fields.Many2one('rusia.eventos', 'Evento')
    dia = fields.Date("Dia")
    tarjeta_usd = fields.Float("Gastos TC USD")
    tarjeta_rub = fields.Float("Gastos TC RUB")
    tarjeta_eur = fields.Float("Gastos TC EUR")
    gasto_rub = fields.Float("Gastos RUB") 
    gasto_usd = fields.Float("Gastos USD")
    gasto_eur = fields.Float("Gastos EUR")
    gasto_paypal = fields.Float("Gastos Paypal") 
    gastos_id = fields.Char()
    beneficios_id = fields.Char()
    tarjeta_usd_pos = fields.Float("Tarjeta USD")
    tarjeta_eur_pos = fields.Float("Tarjeta EUR")
    concepto_id = fields.Many2one('rusia.conceptos.gral','Concepto')



class RusiaHoteles(models.Model):
    _name = 'rusia.hoteles'

    name = fields.Char("Nombre Hotel")
    direccion = fields.Text("Direccion")
    ciudad_id = fields.Many2one('rusia.ciudades','Ciudad')

class GastosReps(models.Model):
    _name = 'rusia.reps.gastos'

    name = fields.Many2one('rusia.ciudades','Ciudad',required=True)
    # tipo_moneda = fields.Selection([('rub','RUB')],'Moneda')
    fecha = fields.Date("Fecha",required=True)
    monto = fields.Char("Monto",required=True)
    gasto_evento_id = fields.Many2one('rusia.eventos','Evento')
    usuario_id = fields.Many2one('res.users','Rep')
    pagado = fields.Boolean('Pagado')

    @api.model
    def create(self, vals):

        print "evento padre",vals['gasto_evento_id']
        print "ciudad:",vals['name']
        print "monto:",vals['monto']

        



        ciudad_gasto = self.env['rusia.gastos.ciudad'].search([('evento_id', '=', vals['gasto_evento_id']),('name','=',vals['name'])])

        if ciudad_gasto:
            vals2 = {
                'Total_Representante' : float(vals['monto'])
            }

            ciudad_gasto.write(vals2)
        else:
            vals2 = {
                'Total_Representante' : float(vals['monto']),
                'name' : vals['name'],
                'evento_id' : vals['gasto_evento_id'],
                'dia' : vals['fecha']
            }
            
            res = self.env['rusia.gastos.ciudad'].create(vals2)

        res = super(GastosReps, self).create(vals)
        return res


    def write(self,vals):

        # print "evento padre",self.gasto_evento_id.id
        # print "ciudad:",self.name.id
        # print "monto:",vals['monto']
        antiguo = 0
        borramos = False

        if 'monto' in vals:
            monto = vals['monto']
        else:
            monto = self.monto

        if 'gasto_evento_id' in vals:
            evento = vals['gasto_evento_id']
        else:
            evento = self.gasto_evento_id.id

        if 'name' in vals:
            ciudad = vals['name']
            antiguo = self.name.id
            borramos = True
        else:
            ciudad = self.name.id

        #Si cambiamos de ciudad, a la que venia antes, dejamos a cero   
        if borramos:
            ciudad_gasto2 = self.env['rusia.gastos.ciudad'].search([('evento_id', '=', evento),('name','=',antiguo)])
            if ciudad_gasto2:
                vals2 = {
                    'Total_Representante' : 0
                }

                ciudad_gasto2.write(vals2)





        ciudad_gasto = self.env['rusia.gastos.ciudad'].search([('evento_id', '=', evento),('name','=',ciudad)])

        if ciudad_gasto:
            vals2 = {
                'Total_Representante' : float(monto)
            }

            ciudad_gasto.write(vals2)

        res = super(GastosReps, self).write(vals)
        return res
        









    
        

    

    
        
