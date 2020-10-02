from odoo import fields, models, _
import sys

'''
To use this popup you need:
1. Create an instance of this model
2. Return an action to show the view with the created instance

Example:
1. 
    wizard = self.env['magic_popup.confirm_cancel_popup'].create({
        'title': 'Your title!', 
        'message': 'Your message!',
        'onConfirm': 'confirm_continue'  <-- the name of the method of your model to be invoked on confirm
    })

2.
    return {
                'name': 'Name of view!',
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'magic_popup.confirm_cancel_popup',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'res_id': wizard.id,
                'context': self.env.context,
            }
'''

class ConfirmCancelPopup(models.TransientModel):
    _name = 'magic_popup.confirm_cancel_popup'
    _description = 'Popup message window with Confirm and Cancel button.'

    title = fields.Char(string="Title", required=True)
    message = fields.Char(string="Message", required=True)
    onConfirm = fields.Char(help="Method to execute when Confirm button is clicked")

    def continue_(self) :
        if self.onConfirm :
            _id = self.env.context['active_id']
            _model = self.env.context['active_model']
            _record = self.env[_model].browse(_id)
            return getattr(_record, self.onConfirm)()
        return
