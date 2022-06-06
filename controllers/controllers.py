from odoo import http
from odoo.http import request


class CreateCrudIndex(http.Controller):
    @http.route('/', website=True, auth='public')
    def index(self, **kw):
        return request.render("curd_project.create_view", {})

    @http.route('/all-data', website=True, auth='public')
    def all_data(self, **kw):
        records = request.env['crud.create'].sudo().search([])
        return request.render("curd_project.all_data", {
            "records" : records,
        })

    @http.route('/create_curd',
                auth='user',
                website=True,
                type='http',
                csrf=False,
                cors='*',
                methods=['POST'])
    def create_curd(self, **kw):
        request.env['crud.create'].sudo().create(kw)
        return request.redirect('/all-data')

    @http.route('/delete/<int:id>',
                auth='user',
                website=True,
                type='http',
                methods=['GET'])
    def delete_data(self, id=False, **kw):

        if id:
            delete_data = request.env['crud.create'].sudo().search([('id', '=', id)])
            if delete_data:
                delete_data.unlink()

        return request.redirect("/all-data")

    @http.route('/edit/<int:id>',
                auth='user',
                website=True,
                type='http',
                methods=['GET'])
    def edit_data(self, id=False, **kw):

        if id:
            edit_data = request.env['crud.create'].sudo().search([('id', '=', id)])
            if edit_data:
                return request.render('curd_project.edit_data', {
                    "edit_data": edit_data,

                })

    @http.route('/update_crud/<int:id>',
                auth='user',
                website=True,
                type='http',
                csrf=False,
                methods=['POST'])
    def update_data(self, id=False, **kw):

        if id:
            data = request.env['crud.create'].sudo().search([('id', '=', id)])
            if data:
                data.write(kw)
        return request.redirect("/all-data")




