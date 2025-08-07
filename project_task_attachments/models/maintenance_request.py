from odoo import models, fields, api, _
from odoo.exceptions import UserError


class FileAttachment(models.Model):
    _inherit = 'ir.attachment'

    attach_to = fields.Selection([('project', 'Project'), ('task', 'Task')], required=True, string="Attach To",
                                 default='project')
    project_id = fields.Many2one('project.project', string='Project', readonly="True")
    task_id = fields.Many2one('project.task', string='Task', readonly="True")

    @api.model_create_multi
    def create(self, vals_list):

        for vals in vals_list:
            if 'project_id' in vals.keys() and not vals['task_id']:
                vals['res_id'] = vals['project_id']
                vals['res_model'] = 'project.project'
            elif 'project_id' in vals.keys() and vals['task_id']:
                vals['res_id'] = vals['task_id']
                vals['res_model'] = 'project.task'
            elif ('project_id' not in vals.keys() and vals['res_model'] ==
                  'project.project'):
                vals['project_id'] = vals['res_id']
                vals['attach_to'] = 'project'
            elif 'task_id' not in vals.keys() and vals[
                'res_model'] == 'project.task':
                vals['task_id'] = vals['res_id']
                vals['attach_to'] = 'task'
        return super().create(vals_list)
