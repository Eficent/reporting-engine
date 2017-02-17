# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import openerp.tests.common as common
from openerp.exceptions import UserError


class TestBiViewEditor(common.TransactionCase):

    def setUp(self):
        super(TestBiViewEditor, self).setUp()
        self.bi_view = self.env['bve.view']

    def test_create_bve_view(self):
        """Tests the creation of a custom BI view."""
        custom_view = self.bi_view.create({
            'name': 'Test BI view',
        })
        with self.assertRaises(UserError):
            custom_view.action_create()
        custom_view.write({
            'data': """"[{"model_id":80,"name":"email","model_name":"Partner","model":"res.partner","custom":false,"type":"char","id":942,"description":"Email","table_alias":"t0","row":false,"column":false,"measure":false}]"""""
        })
        custom_view.action_create()
        self.assertEqual(custom_view.state, 'created',
                         'Custom view creation failed.')

    # def test_unique_names(self):
    #     """Test if error raises for duplicated name."""
    #     custom_view = self.bi_view.create({
    #         'name': 'Test BI view',
    #     })
    #     custom_view2 = self.bi_view.create({
    #         'name': 'Test BI view',
    #     })
    #     with self.assertRaises(UserError):
    #         custom_view.action_create()
